import torch

# 检查 PyTorch 版本
print(f"PyTorch 版本: {torch.__version__}")

# 检查 GPU 是否可用
print(f"CUDA 是否可用: {torch.cuda.is_available()}")