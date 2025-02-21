from transformers import GPT2Tokenizer
from datasets import load_dataset

# Загрузка токенизатора GPT-2
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Чтение датасета
def preprocess_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        texts = f.readlines()

    # Токенизация данных
    encodings = tokenizer("\n".join(texts), truncation=True, padding=True, max_length=512)

    # Сохранение обработанных данных
    with open(output_file, 'w', encoding='utf-8') as f:
        for encoding in encodings['input_ids']:
            f.write(f"{encoding}\n")

preprocess_data('data/dataset.txt', 'data/processed_data.txt')
