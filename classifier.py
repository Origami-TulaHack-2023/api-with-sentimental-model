import os
import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

device = "cuda:0" if torch.cuda.is_available() else "cpu"

@torch.no_grad()
def get_prediction(reviews, save_model=False):
    labels = ['neutral', 'positive', 'negative']
    tokenizer = BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment')

    model = torch.load('model.pt').to(device)
    model.eval()

    predictions = []
    for review in reviews:
        inputs = tokenizer(review, max_length=512, padding=True, truncation=True, return_tensors='pt').to(device)
        outputs = model(**inputs)
        predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
        predicted = torch.argmax(predicted, dim=1).cpu().numpy()
        predictions.append(labels[int(predicted)])

    return predictions