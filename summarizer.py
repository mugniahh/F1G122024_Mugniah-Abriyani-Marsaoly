from transformers import BartTokenizer, BartForConditionalGeneration
import torch

MODEL_NAME = "facebook/bart-large-cnn"

tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)

device = torch.device("cpu")
model.to(device)

def summarize(text: str) -> str:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    ).to(device)

    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=180,
            min_length=80,
            num_beams=4,
            length_penalty=2.0,
            early_stopping=True
        )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
