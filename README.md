# AI Agents & Projects

My central workspace for AI agents, AI-related tasks, experiments, and learning projects. This repository brings together practical implementations, reusable tools, and notes as I explore and build with artificial intelligence.

## What belongs here

- **AI agents:** Agents that reason, use tools, and complete tasks.
- **AI workflows and automation:** Scripts and workflows for everyday or project-specific tasks.
- **LLM experiments:** Prompting, model integrations, structured outputs, and evaluation.
- **Knowledge and retrieval:** Experiments with RAG, embeddings, memory, and search.
- **Learning and research:** Examples, notebooks, notes, and proofs of concept.
- **Reusable utilities:** Shared helpers that support multiple AI projects.

These are the areas this repository is intended to grow into. Each project may use its own language, framework, model provider, and dependencies.

## Current projects

| Project | Description |
| --- | --- |
| [Text-to-SQL agent](text_to_sql_agent/) | A Python agent built with `smolagents` that uses a DeepSeek model and a SQL tool to answer questions about a SQLite receipts database. |

## Repository layout

```text
AI/
├── text_to_sql_agent/    # Text-to-SQL agent and database connection code
├── receipts.db          # SQLite database used by the current agent
├── .gitignore
└── README.md
```

## Getting started

Choose a project and review its code and any project-specific instructions. There is no single setup or run command for the entire repository.

### Run the Text-to-SQL agent

Run the following commands from the repository root with Python installed:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install smolagents openai sqlalchemy python-dotenv
```

Create a `.env` file in the repository root containing your API key:

```dotenv
DEEPSEEK_API_KEY=your_api_key_here
```

Then run:

```powershell
python text_to_sql_agent/text_to_sql.py
```

The script uses the model configured in `text_to_sql.py` and asks: “What is the difference between the highest and lowest receipt?” Edit the `agent.run(...)` prompt to try another question about the receipts table.

Keep your working directory at the repository root so the script uses the included `receipts.db`. The database must contain the `receipts` table; the table creation and sample inserts in `sql_statements.py` are currently commented out. Running the agent sends requests to the configured model provider and may incur API charges.

## Adding a new project

1. Create a separate folder with a descriptive name, such as `research_agent/` or `document_search/`.
2. Keep the project's code, examples, and dependency files together.
3. Add a project README explaining its purpose, setup, required environment variables, and how to run it.
4. Include an `.env.example` with placeholder values when configuration is needed.
5. Add the project to the **Current projects** table above.

Keep credentials out of version control. The root `.env` file is already ignored; add ignore rules for any additional secret files, local environments, or generated artifacts your projects introduce.

## Project status

This is an evolving personal workspace. Projects may be exploratory or incomplete, and their setup and capabilities will vary. Document assumptions, limitations, and useful findings alongside each project as it develops.
