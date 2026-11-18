# LoRA vs. QLoRA vs. Full Fine-Tuning on Math

Cam Petrey and Connor Johnson, CS 445

## What this project is

We're comparing three ways to fine-tune a small language model: full fine-tuning, LoRA, and QLoRA. We train each one on math word problems from GSM8K and check three things:

- How much better it gets at math (GSM8K test accuracy)
- How much it forgets (HellaSwag, ARC-Easy, and WinoGrande scores before and after training)
- How much GPU memory it uses during training

We're basing this on "LoRA Learns Less and Forgets Less" (Biderman et al., 2024), which found that LoRA learns less than full fine-tuning but also forgets less. We want to see if that holds for a smaller model and where QLoRA fits in.

## How to run it

Install the requirements:

    pip install -r requirements.txt

Download GSM8K and print some stats about it:

    python explore_data.py

Training and evaluation code is coming next.
