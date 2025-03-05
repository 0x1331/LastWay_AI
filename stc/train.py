from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def load_and_preprocess_data():
    dataset = load_dataset('text', data_files={'train': 'data/processed_data.txt'}, split='train')
    def tokenize_function(examples):
        return tokenizer(examples['text'], return_tensors="pt", truncation=True, padding="max_length", max_length=512)

    return dataset.map(tokenize_function, batched=True)

dataset = load_and_preprocess_data()

training_args = TrainingArguments(
    output_dir="./results",          # директория для сохранения результатов
    evaluation_strategy="epoch",     # периодичность оценок
    learning_rate=5e-5,              # скорость обучения
    per_device_train_batch_size=8,   # размер батча
    per_device_eval_batch_size=8,    # размер батча для оценки
    num_train_epochs=3,             # количество эпох
    weight_decay=0.01,               # регуляризация
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

trainer.train()
