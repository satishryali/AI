# Resources in learning order

Choose one main resource at a time. Read or watch a small section, implement its idea, then explain it in your own words. Links were checked on 2026-10-30; installation requirements can change.

## Main learning sequence

1. [Neural Networks: Zero to Hero — Andrej Karpathy](https://github.com/karpathy/nn-zero-to-hero): begin with micrograd for gradients, then makemore for character prediction. Use the linked lectures and code together.
2. [Let's build GPT — companion repository](https://github.com/karpathy/ng-video-lecture): use when you reach causal attention and your first Transformer. Scale configurations down for your GPU.
3. [Build nanoGPT](https://github.com/karpathy/build-nanogpt): a later look at a more complete GPT implementation and training workflow. Do not assume the full GPT-2 reproduction will fit or finish conveniently on your hardware.
4. [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/): use alongside tokenizer and pretrained-model experiments. Consult the relevant chapter rather than reading everything before coding.
5. [Hugging Face smol course](https://huggingface.co/learn/smol-course/unit0/1): use at the fine-tuning stage, after you understand a basic training loop. Its emphasis is post-training, not building your first network.

## Reference shelf

- [PyTorch installation selector](https://pytorch.org/get-started/locally/): current environment and installation instructions.
- [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html): tensors, autograd, models, optimization, and saving/loading.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762): original Transformer paper. Read attention sections after building a small example; the original model includes an encoder and decoder, while your GPT project uses a decoder-style architecture.
- [PEFT quantization guide](https://huggingface.co/docs/peft/developer_guides/quantization): LoRA with quantized base models, useful after ordinary fine-tuning makes sense.
- [Retrieval-Augmented Generation paper](https://arxiv.org/abs/2005.11401): background reading when you reach retrieval. Your first retrieve-and-prompt experiment need not reproduce the paper's training architecture.

## Questions to keep asking

- What is the input, and what is the expected output?
- What is learned, and what was hard-coded?
- Which tensor dimensions represent batch, sequence, vocabulary, and embedding width?
- What does the loss measure?
- What evidence would show that the model memorized instead of generalizing?
- What would change if I doubled the data rather than the parameters?
- What can I test with a smaller model before scaling up?
