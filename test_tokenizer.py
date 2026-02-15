from tokenizer import build_tokenizer, encode, decode

text = "oi"
stoi, itos = build_tokenizer(text)

tokens = encode(text, stoi)
print("Tokens:", tokens)

print("Decode:", decode(tokens, itos))
