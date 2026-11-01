# First exercise: predict the next character

Goal: understand examples, probabilities, generation, and evaluation before adding neural networks. Allow as many sessions as you need.

## 1. Understand the data by hand

Use this tiny training string:

```text
hello hello
```

Treat the space as a character. Consecutive pairs are:

```text
he el ll lo o[space] [space]h he el ll lo
```

Answer before coding:

1. How many characters are there, including the space?
2. How many consecutive pairs are there?
3. Which characters follow `l`, and how often?
4. What next character would you predict after `h`?

Self-check: 11 characters, 10 pairs; `l` is followed by `l` twice and `o` twice. After `h`, this dataset always has `e`.

## 2. Build a count-based model

Create your own Python script alongside this guide, named `bigram_counts.py`.

Implement these steps using strings, dictionaries, loops, and Python's standard `random` module:

1. Read the training text.
2. Count each pair of neighboring characters.
3. For each current character, divide each following-character count by the total outgoing count.
4. Print the possible next characters and their probabilities.
5. Starting from `h`, repeatedly sample the next character and append it.
6. Stop after a fixed number of characters, such as 100.

Pseudocode:

```text
for every adjacent pair (current, next):
    increase counts[current][next]

repeat until output is long enough:
    sample next character using counts[current] as weights
    append it to output
    current = next character
```

If a character has no outgoing transitions, stop generation or restart from a known character. State which rule you chose. Set a random seed so you can repeat an experiment.

Completion checks:

- [ ] The outgoing probabilities for each character sum to approximately 1.
- [ ] After `l`, both `l` and `o` have probability 0.5.
- [ ] Sampling can produce repetitions that were not present as complete sentences.
- [ ] I can explain why this model remembers only one previous character.

## 3. Try a larger corpus

Write a few paragraphs yourself, or choose text whose license permits your use. Record its source and license. Use a small local text file initially.

Keep an initial portion for training and a later portion for validation. For example, split 90%/10% before extracting pairs and never create a pair across the split boundary. With a tiny corpus, results will be noisy.

Questions:

- What happens to capitalization and punctuation?
- What happens if you always choose the most probable next character instead of sampling?
- Can the model generate readable words? Can it maintain a topic?
- What should happen when validation contains a character absent from training?

Optional evaluation: compute average negative log probability of the true next characters on validation data. Zero probabilities require an explicit policy, such as add-one smoothing over a defined vocabulary and an unknown-character token. Do not silently discard hard examples.

## 4. Record the result

Copy one entry from [the experiment log](05_experiment_log.md). Save your prediction, one generated sample, and one limitation.

Move on when you can explain: “This model learns transition probabilities from counts. A neural model will learn probabilities by adjusting parameters to reduce prediction loss.”
