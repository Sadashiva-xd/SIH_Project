import json
from translator import translate


def json_to_simple_english(data):
    """
    Converts JSON/dictionary data into simple English sentences.
    Works recursively for nested dictionaries and lists.
    """

    sentences = []

    def simplify_key(key):
        return key.replace("_", " ").strip()

    def walk(value, key=None):
        # Dictionary
        if isinstance(value, dict):
            for child_key, child_value in value.items():
                walk(child_value, child_key)

        # List
        elif isinstance(value, list):
            readable_key = simplify_key(key) if key else "items"

            if all(not isinstance(item, (dict, list)) for item in value):
                joined = ", ".join(str(item) for item in value)
                sentences.append(
                    f"{readable_key.capitalize()} includes {joined}."
                )
            else:
                for item in value:
                    walk(item, key)

        # Boolean
        elif isinstance(value, bool):
            readable_key = simplify_key(key)

            if value:
                sentences.append(
                    f"{readable_key.capitalize()} is required."
                )
            else:
                sentences.append(
                    f"{readable_key.capitalize()} is not required."
                )

        # Normal value
        elif value is not None:
            readable_key = simplify_key(key)

            sentences.append(
                f"{readable_key.capitalize()} is {value}."
            )

    walk(data)

    return " ".join(sentences)


def explain_schema(schema, preferred_language):
    """
    Input:
        schema:
            Python dictionary OR JSON string

        preferred_language:
            Example:
            "Kannada"
            "Hindi"
            "Bengali"

    Returns:
        Simple explanation in the preferred language.
    """

    # Handle JSON string
    if isinstance(schema, str):
        try:
            schema = json.loads(schema)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input.")

    if not isinstance(schema, dict):
        raise ValueError(
            "Schema must be a Python dictionary or valid JSON object."
        )

    # Convert JSON into readable English
    english_text = json_to_simple_english(schema)

    # No translation needed
    if preferred_language.lower() == "english":
        return english_text

    # Use your offline Sarvam translator
    translated_text = translate(
        english_text,
        "English",
        preferred_language
    )

    return translated_text