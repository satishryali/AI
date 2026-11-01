# Build a language model to understand it

This is a curiosity-driven learning project: build a small language model, train it from random weights, fine-tune it, and experiment with retrieval. Progress means being able to explain and change what you built.

Your detected GPU is an NVIDIA RTX 3050 with 6 GB VRAM. RAM and training throughput have not been measured. Start small; there is no reliable training-time estimate until you benchmark a working model.

## Start here

1. Work through [the first exercise](01_first_exercise.md). It needs only basic Python and can run on the CPU.
2. Follow [the setup guide](02_setup.md) before neural-network work.
3. Continue through [the roadmap](03_roadmap.md), using its completion checks.
4. Keep results in [the experiment log](05_experiment_log.md).
5. Use [the resource guide](04_resources.md) when you need an explanation.

Your first outcome: given a character, predict a likely next character and generate a short sequence. A count-based baseline comes before a neural network so you can understand what training is trying to improve.

## What “from scratch” means here

Write the model and training loop yourself, initialize random weights, and use PyTorch for tensor operations and automatic differentiation. Later, optionally implement a tiny automatic-differentiation engine to understand that layer too. You do not need to write GPU kernels.

A tiny GPT uses the same central ideas as much larger language models, but its language quality and knowledge will be limited. Begin around 1–5 million parameters when you reach the Transformer stage; fit and speed still depend on sequence length, batch size, and implementation.

## The three experiments

| Experiment | What changes? | Evidence to collect |
| --- | --- | --- |
| Pretraining | Model weights learn next-token patterns from raw text | Held-out loss and generated samples |
| Fine-tuning | Existing weights or adapters learn from task examples | Performance on unseen task examples |
| RAG | Retrieved text is added to the input; generation-model weights need not change | Retrieval accuracy and answers with/without context |

Fine-tuning and RAG are independent techniques. You can use either or both. A tiny model may fail to use retrieved context; compare with an existing instruction model later.

## Working habits

- Predict what an experiment will do before running it.
- Change one thing at a time.
- Keep a held-out evaluation set and avoid training on it.
- Save model configuration, tokenizer, weights, and sample outputs together.
- Learn the mathematics as it appears: probability, vectors, matrix multiplication, derivatives, and gradients.
- Ask for hints or reviews before asking for a complete solution.

The existing [reminder collector](../FineTuning/reminder_assistant/collect_example.py) is a separate application experiment. It collects fields interactively; it does not currently save a training dataset. Return to it at the fine-tuning stage.

## Next-session handoff

- Current stage: first exercise, not started.
- Next action: write a short text corpus and manually count its character transitions.
- First question to answer: why can the same character have several possible next characters?
- No model training or package installation has been performed as part of creating these guides.
