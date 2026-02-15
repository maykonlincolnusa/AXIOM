import torch
from mini_model import MiniGPT

vocab_size = 20
model = MiniGPT(vocab_size)

x = torch.randint(0, vocab_size, (5,))
out = model(x)

print("Output shape:", out.shape)
