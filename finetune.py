from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import Dataset
import pandas as pd


model_name = "distilgpt2"

tokenizer=AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

df = pd.read_csv('./data/engineers.csv')


texts = []


for _, row in df.iterrows():
    text = f"Engineer {row['name']} specializes in {row['specialization']} and earns {row['salary']} per year."
    texts.append({"text":text})


dataset = Dataset.from_list(texts)
print(dataset)
print(dataset[0])
