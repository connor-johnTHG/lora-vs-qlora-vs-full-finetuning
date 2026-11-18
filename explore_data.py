from datasets import load_dataset

# Download GSM8K
gsm8k = load_dataset("openai/gsm8k", "main")

# How many problems are in each split
print("Train problems:", len(gsm8k["train"]))
print("Test problems:", len(gsm8k["test"]))

# Look at one example
example = gsm8k["train"][0]
print("\nExample question:")
print(example["question"])
print("\nExample answer:")
print(example["answer"])
