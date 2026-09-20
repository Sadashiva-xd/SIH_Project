from schema_explainer import explain_schema

LANGUAGES = [
    "Hindi",
    "Bengali",
    "Gujarati",
    "Kannada",
    "Malayalam",
    "Marathi",
    "Odia",
    "Punjabi",
    "Tamil",
    "Telugu"
]

data = {
    "crop": "Tomato",
    "temperature": 28,
    "soil_moisture": 65,
    "fertilizer_required": True,
    "recommendation": "Apply nitrogen fertilizer"
}

print("\nChoose preferred language:")

for i, language in enumerate(LANGUAGES, start=1):
    print(f"{i}. {language}")

choice = int(input("\nEnter choice: "))

if choice < 1 or choice > len(LANGUAGES):
    print("Invalid choice.")
    exit()

preferred_language = LANGUAGES[choice - 1]

result = explain_schema(
    data,
    preferred_language
)

print(f"\n{preferred_language}:")
print(result)