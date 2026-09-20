from llama_cpp import Llama

print("Loading Sarvam model...")

llm = Llama(
    model_path="./models/sarvam-1.Q4_K_S.gguf",
    n_ctx=1024,
    n_threads=8,
    verbose=False
)

print("Model loaded successfully!")

response = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": (
                "You are a translation engine. "
                "Translate the user's text exactly into the requested target language. "
                "Return only the translated text. "
                "Do not explain. Do not add notes. Do not repeat the source text."
            )
        },
        {
            "role": "user",
            "content": """
Source language: Kannada
Target language: English

Text:
ನಾನು ಕಾಲೇಜಿಗೆ ಹೋಗುತ್ತಿದ್ದೇನೆ.
"""
        }
    ],
    max_tokens=80,
    temperature=0.0
)

print("\nResponse:")
print(response["choices"][0]["message"]["content"].strip())
