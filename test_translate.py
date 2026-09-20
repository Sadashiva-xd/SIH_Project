from translator import translate

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

print("\nChoose target language:")

for i, language in enumerate(LANGUAGES, start=1):
    print(f"{i}. {language}")

choice = int(input("\nEnter choice: "))

if choice < 1 or choice > len(LANGUAGES):
    print("Invalid choice.")
    exit()

target_language = LANGUAGES[choice - 1]

english_text = input("\nEnter English message: ")

result = translate(
    english_text,
    "English",
    target_language
)

print(f"\n{target_language}:")
print(result)