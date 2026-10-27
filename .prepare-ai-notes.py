from pathlib import Path
import json, csv, hashlib, sys
from datetime import date, timedelta
root = Path('C:/GIT/data-engineering-journey')
sys.path.insert(0, str(root / 'tracking'))
import note_revision

def write(rel, text):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')

write('Notes/AI/Index.md', '''# AI notes

- [Reminder model basics](reminder-model-basics.md): prompting, fine-tuning, checking model answers and example pairs.
- [Reminder input practice](reminder-input-practice.md): input cleanup and returned strings from today's code.
- [Recall questions](recall-questions.md): try these without opening the answers.
- [Session evidence and next task](../../progress/ai-reminder/2026-10-28-session.md).

Prepared from the saved 28 October 2026 session and inspected project files. Notes describe explored material; they do not imply independent mastery or completed training.
''')
old = root / 'Notes/revision/ai-reminder-questions.md'
write('Notes/AI/recall-questions.md', old.read_text(encoding='utf-8') + '\n- In the notebook, why does upper() display SATISH while print(s) still displays satish?\n- Does asking for HH:MM input check that a real time was entered?\n')
write('Notes/revision/ai-reminder-questions.md', '# AI reminder recall questions\n\nThe answer-free prompts are now in [the AI folder](../AI/recall-questions.md).\n')
p = root / 'Notes/AI/reminder-model-basics.md'
s = p.read_text(encoding='utf-8').replace('../revision/ai-reminder-questions.md', 'recall-questions.md')
p.write_text(s, encoding='utf-8')
write('Notes/AI/reminder-input-practice.md', '''# Collecting reminder inputs

Before building training examples, we need the task, time and repeat answer in a consistent form. The current collector asks for these three values.

## Read and clean text

The supplied script uses input() to read text and strip() to remove spaces at the beginning and end. Asking for a time in HH:MM format does not check that the entered value is a real time. Validation and saving examples are still future tasks.

The script currently prints task and time. It calls recurrence.upper() without saving or printing the returned text. No collector execution output was supplied.

## A string method returns new text

The practice notebook contains this small example:

```python
s = "satish"
s.upper()
```

Saved notebook result:

```text
'SATISH'
```

The next cell contains:

```python
print(s)
```

Saved notebook output:

```text
satish
```

upper() returns uppercase text. It does not replace the value held by s. A notebook can display the last expression's result; a script does not automatically print that expression. The shown output was read from saved notebook cells, not rerun during this note save.

## Sources and next step

- Project source: C:/GIT/AI/FineTuning/reminder_assistant/collect_example.py.
- Saved notebook: C:/GIT/AI/FineTuning/Test/reminder_assistant/collect_example_t.ipynb.
- [Exact pending task and session evidence](../../progress/ai-reminder/2026-10-28-session.md#exact-next-task).
- [Recall questions](recall-questions.md).

The learner writes the next change. No corrected collector, execution result or independent assessment is claimed here.
''')
p = root / 'Notes/README.md'
s = p.read_text(encoding='utf-8')
if '[AI notes]' not in s:
    s = s.replace('- [Python notes]', '- [AI notes](AI/Index.md)\n- [Python notes]', 1)
p.write_text(s, encoding='utf-8')
p = root / 'progress/ai-reminder/2026-10-28-session.md'
s = p.read_text(encoding='utf-8').replace('See canonical mistake M-PY-REM-001.', 'No canonical mistake entry was found during this save; the observation remains in this evidence record.')
s = s.replace('An exact byte snapshot is saved alongside this record as collect_example-2026-10-28.py.', 'An exact byte snapshot of the source inspected during the notes save is saved alongside this record as collect_example-2026-10-28.py.')
s += '\n## Notes-save verification\n\nThe notes save inspected the project source and notebook. Saved cells show upper() returning SATISH and print(s) showing satish; no rerun or independent diagnosis was assessed. Earlier model and hardware details above come from the pre-existing session record and were not rechecked in this save. AI notes and answer-free questions are grouped in Notes/AI.\n'
p.write_text(s, encoding='utf-8')
(root / 'progress/ai-reminder/collect_example-2026-10-28.py').write_bytes(Path('C:/GIT/AI/FineTuning/reminder_assistant/collect_example.py').read_bytes())
registry = json.loads((root / 'tracking/topic-map.json').read_text(encoding='utf-8'))
registry = note_revision.sync(root, registry, '2026-10-28')
concepts = [
 ('ai.reminder.model', 'Reminder models: inference prompting and fine-tuning', 'Notes/AI/reminder-model-basics.md', [], '2026-10-29'),
 ('ai.reminder.evaluation', 'Checking reminder model fields against a baseline', 'Notes/AI/reminder-model-basics.md', ['ai.reminder.model'], '2026-10-30'),
 ('ai.reminder.examples', 'Reminder input and target example pairs', 'Notes/AI/reminder-model-basics.md', ['ai.reminder.evaluation'], '2026-10-31'),
 ('py.strings.returned-text', 'String cleanup and returned case conversions', 'Notes/AI/reminder-input-practice.md', [], '2026-11-01')]
used = {t.get('initial_assessment_date_ist') for t in registry['topics']}
for ident, name, path, prereq, slot in concepts:
    if any(t['id'] == ident for t in registry['topics']):
        continue
    day = date.fromisoformat(slot)
    while day.isoformat() in used:
        day += timedelta(days=1)
    used.add(day.isoformat())
    registry['topics'].append(dict(id=ident, name=name, sources=[dict(path=path, sha256=hashlib.sha256((root/path).read_bytes()).hexdigest())], source_history=[], coverage='queued', prerequisites=prereq, exercise_ids=[], note_sections=[], initial_assessment_date_ist=day.isoformat()))
by_id = {t['id']:t for t in registry['topics']}
for item in registry['note_inventory']:
    path = item['path']
    if path == 'Notes/AI/recall-questions.md':
        item.pop('sections', None)
        item['exclusion_reason'] = 'Answer-free retrieval prompts; explanations mapped from AI notes.'
    elif path in ('Notes/AI/reminder-model-basics.md', 'Notes/AI/reminder-input-practice.md'):
        for sec in item.get('sections', []):
            heading = sec['key']
            if heading.endswith('Sources and session evidence') or heading.endswith('Sources and next step'):
                sec['exclusion_reason'] = 'Sources, provenance and pending task links; no extra concept.'
                continue
            ident = 'py.strings.returned-text' if path.endswith('reminder-input-practice.md') else 'ai.reminder.evaluation' if heading.endswith('Check the answer before training') else 'ai.reminder.examples' if heading.endswith('Create input and answer pairs') else 'ai.reminder.model'
            sec['topic_ids'] = [ident]
            ref = dict(path=path, key=heading)
            if ref not in by_id[ident]['note_sections']:
                by_id[ident]['note_sections'].append(ref)
write('tracking/topic-map.json', json.dumps(registry, indent=2, ensure_ascii=False) + '\n')
p = root/'tracking/revision-queue.csv'
with p.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
for ident, name, path, prereq, slot in concepts:
    if not any(row['item_id'] == ident for row in rows):
        row = {k:'' for k in fields}
        row.update(item_id=ident, skill=name, retrieval_task='One bounded question from Notes/AI/recall-questions.md; state help used.', last_result='not_attempted', status='unassessed', evidence=path, notes='Initial diagnostic slot is planning only; no score or retention due date.')
        rows.append(row)
with p.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(rows)
next_task = 'Update the recurrence input to retain a lowercase answer and display task, time and recurrence; run with YES and share the actual output.'
summary = 'Organized requested AI notes from the saved 28 October session under Notes/AI, with model basics, input practice, index and separate recall prompts. Source and saved notebook inspected; upper() result versus unchanged original documented. Existing session model/hardware observations were not rerun. Four concepts receive unassessed diagnostic planning slots only. No scored review, training, timer change or project acceptance. Learner source preserved. Next: ' + next_task
intro = '\n## AI notes saved, 28 October 2026\n\n[AI notes](%s) and [session evidence](%s) capture today\'s reminder-model exploration and collector practice. No independent assessment or training completed.\n\nNext AI task: ' + next_task + '\n\nEarlier Python follow-ups and RDS-001 remain pending.\n'
checkpoint = (root/'progress/current.md').read_text(encoding='utf-8')
handoff = (root/'START-HERE.md').read_text(encoding='utf-8')
checkpoint += intro % ('../Notes/AI/Index.md', 'ai-reminder/2026-10-28-session.md')
handoff += intro % ('Notes/AI/Index.md', 'progress/ai-reminder/2026-10-28-session.md')
event = dict(checkpoint_id='CP-20261028-ai-notes-organized', date_ist='2026-10-28', kind='setup', summary=summary, evidence_ids=['Notes/AI/Index.md', 'Notes/AI/reminder-model-basics.md', 'Notes/AI/reminder-input-practice.md', 'progress/ai-reminder/2026-10-28-session.md'], reviews=[], mistakes=[], skill_updates=[], checkpoint_text=checkpoint, handoff_text=handoff, next_task=next_task)
Path('C:/GIT/AI/.ai-notes-event.json').write_text(json.dumps(event, indent=2), encoding='utf-8')
print('AI notes organized; inventory mappings and checkpoint event prepared.')
