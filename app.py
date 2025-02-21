import torch
from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# Название модели GPT-2
model_name = "gpt2-xl"

# Инициализация токенизатора и модели
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Инициализация устройства (CPU/GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"response": "Ошибка: пустой запрос"}), 400

        # Токенизация входного текста
        inputs = tokenizer.encode(user_input, return_tensors="pt").to(device)

        # Генерация ответа моделью GPT-2
        output = model.generate(
            inputs,
            max_length=100,  # Ограничение максимальной длины ответа
            min_length=10,   # Минимальная длина, чтобы ответ не был слишком коротким
            num_return_sequences=1,
            temperature=0.7,
            top_k=40,
            top_p=0.85,
            no_repeat_ngram_size=2,
            pad_token_id=tokenizer.eos_token_id,
            early_stopping=True
        )
        
        response = tokenizer.decode(output[0], skip_special_tokens=True).strip()

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"response": f"Ошибка: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

