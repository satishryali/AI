# Roadmap: small language model to fine-tuning and RAG

Use completion checks rather than calendar deadlines. Training duration and learning duration are different: an experiment may run quickly while understanding it takes several sessions.

## Stage 1: character counts

Follow [the first exercise](01_first_exercise.md).

Deliverable: a next-character sampler and a short explanation of its limitations.

Exit check: explain a conditional probability and show that your sampler follows the learned distribution.

## Stage 2: neural character prediction

Learn tensors, shapes, matrix multiplication, logits, softmax, cross-entropy, gradients, and an optimizer. Use PyTorch after [setup](02_setup.md).

Build a neural bigram model: a vocabulary-by-vocabulary table of learnable logits. Input a character ID; predict the next character ID. Then extend it to use several previous characters through embeddings and a small feed-forward network.

Experiments:

- Print input, output, and target shapes.
- Compare loss before and after training.
- Intentionally overfit a tiny batch as a debugging exercise.
- Compare neural and count-based bigram predictions on the same corpus.

Exit check: explain why `backward()` computes gradients and why the optimizer step changes parameters. Explain why a low training loss alone is insufficient.

## Stage 3: tiny GPT from random weights

Use a character tokenizer first. Learn embeddings, positions, causal attention, attention heads, feed-forward layers, residual connections, and normalization.

Implement progressively: one attention head, multiple heads, one Transformer block, then several blocks. Start around 1–5M parameters, short context, and a small batch. This is a starting design, not a guaranteed memory fit.

Keep a raw-text corpus split into train and validation before forming training windows. Save the tokenizer mapping with the model. During validation, disable gradient tracking and use evaluation mode; return to training mode afterward.

Exit checks:

- [ ] A causal mask prevents access to future tokens.
- [ ] Training starts from random weights, not a downloaded checkpoint.
- [ ] Validation uses held-out text and the same tokenizer.
- [ ] I can save/reload and generate text from a checkpoint.
- [ ] I can explain why next-token training produces a text-completion model, not automatically a chat assistant.

## Stage 4: investigate learning

Keep a baseline and vary one factor: context length, width, number of layers, amount of text, or sampling temperature. Log loss, throughput, peak memory, and fixed-prompt samples.

For unknown characters, define a tokenizer policy. For larger text, learn subword tokenization and compare it with characters. Token counts and losses across different tokenizers are not directly interchangeable.

Exit check: identify an example of overfitting or a failed hypothesis using actual results.

## Stage 5: fine-tune your checkpoint

Start with a narrow formatting task. Make input/output examples and serialize them consistently, for example:

```text
Input: remind me to drink water at 9 AM every day
Output: {"task":"drink water","time":"09:00","recurrence":"daily"}
```

These delimiters are ordinary text unless you deliberately add special tokens. Keep training and generation formatting consistent. Include a defined end-of-answer convention.

Keep unseen phrasings and tasks in evaluation. Include missing times and ambiguous requests; define a clarification response rather than inventing details. Avoid splitting near-duplicate examples between train and evaluation.

On a tiny model, full fine-tuning may fit. Learn LoRA/QLoRA later by adapting an existing pretrained model and comparing the methods. For supervised instruction tuning, learn how to mask prompt and padding positions so the loss targets the intended answer tokens.

Evaluate before and after: valid JSON, correct fields, unseen wording, and behavior on ambiguous inputs. A small validation set is an experiment, not proof of reliability. Fine-tuning cannot compensate for every weakness in the original model.

Exit check: show one improved behavior and one remaining failure. Keep an untouched copy of the base checkpoint.

## Stage 6: retrieval, then RAG

Begin with five short notes you wrote. Make ten questions with known supporting passages.

1. Split notes into labeled chunks with source IDs.
2. Build a simple keyword retriever first.
3. Check whether the correct passage appears in the top results.
4. Later compare embedding similarity search. A small corpus does not require a vector database.
5. Put retrieved passages and the question into the model input, within its context limit.
6. Compare answers without retrieval and with retrieval.

Record retrieval success separately from answer correctness. Ask for source IDs, inspect whether claims are supported, and include questions the notes cannot answer.

Your tiny model may not follow the context. Compare with an existing instruction model to distinguish a generation limitation from a retrieval failure. You can still learn and test retrieval independently.

Exit check: explain why RAG can update available information without retraining the generation model, and why retrieved text does not guarantee a correct answer.
