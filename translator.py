from llama_cpp import Llama

print("Loading Sarvam Translate...")

llm = Llama(
    model_path="./models/sarvam-translate.Q4_K_M.gguf",
    n_ctx=1024,
    n_threads=8,
    verbose=False
)

print("Translation model loaded!")


def _translate_once(text, target_language):
    response = llm.create_chat_completion(
        messages=[
            {
                "role": "system",
                "content": f"Translate the text below to {target_language}."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.0,
        max_tokens=300
    )

    return response["choices"][0]["message"]["content"].strip()


def translate(text, source_language, target_language):

    # Same language
    if source_language.lower() == target_language.lower():
        return text

    # Indic -> English
    if target_language.lower() == "english":
        return _translate_once(text, "English")

    # English -> Indic
    if source_language.lower() == "english":
        return _translate_once(text, target_language)

    # Indic -> Indic:
    # first translate to English
    english = _translate_once(text, "English")

    # then English -> target Indic language
    result = _translate_once(english, target_language)

    return result