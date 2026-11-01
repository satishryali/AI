# Set up the neural-network workspace

Do this after the count-based exercise. These are instructions for you to run; the environment has not been installed or verified yet.

## Windows setup

1. Check [PyTorch's official installation selector](https://pytorch.org/get-started/locally/) for its current supported Python versions and Windows/CUDA installation command.
2. In VS Code, open a PowerShell terminal in this learning folder.
3. With a supported Python interpreter installed, create a separate environment:

```powershell
python -m venv .venv
```

4. Select that environment with VS Code's **Python: Select Interpreter** command. You can use its executable directly without activating PowerShell scripts:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

5. Use the pip arguments provided by the official selector with this environment's Python. Select Windows, Pip, Python, and a CUDA option supported by your driver. Do not guess a CUDA package URL or install a CPU-only build if you want GPU training.
6. Check the driver separately:

```powershell
nvidia-smi
```

7. Verify PyTorch in the new environment:

```powershell
.\.venv\Scripts\python.exe -c "import torch; print('PyTorch:', torch.__version__); print('CUDA:', torch.cuda.is_available()); print('Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')"
```

Expected for GPU work: CUDA is `True` and the device is your RTX 3050. If not, check the selected interpreter, installed PyTorch build, and driver compatibility. Avoid reinstalling unrelated packages at random.

## Before a long training run

- Start with batch size 1 and a short sequence, such as 64 or 128 tokens.
- Run a few training steps, validation, saving, loading, and generation first.
- Measure peak GPU memory and actual training tokens/second after warm-up.
- Keep the computer ventilated; monitor temperature and power behavior with `nvidia-smi`.
- Keep datasets, virtual environments, and large checkpoints out of Git. Add project-specific ignore rules before creating them.
- Record installed versions, configuration, seed, and dataset identity.

If you run out of GPU memory, reduce batch size or context length, then model width/layers. Gradient accumulation can combine multiple small batches into an effective larger batch; it does not reduce the memory required for one sequence. CPU offloading is a later experiment with speed tradeoffs.

## Estimate time from a measurement

```text
total training tokens = sum of tokens processed across all training passes
training seconds ≈ total training tokens / measured training tokens per second
```

Include repeated epochs in the total. Add time for validation, saving, and interruptions. Generated tokens/second is not the same measurement as training tokens/second.

No speed such as 1,000 tokens/second is assumed for this computer.
