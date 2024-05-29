from groq import Groq
import os
from dotenv import load_dotenv
import pyperclip
import keyboard  # Importiere das keyboard Modul

run = True

def run_import():
    if __name__ == '__main__':
        load_dotenv()
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": pyperclip.paste(),
                }
            ],
            model="llama3-8b-8192",
            max_tokens=50,  # Limit the response length
            stop=["."],  # Stop at the first period
            temperature=0.2,  # Make output more deterministic
            top_p=0.5  # Focus on the most probable tokens
        )

        pyperclip.copy(chat_completion.choices[0].message.content)

while run:
    # Überprüfe, ob die Taste 'k' gedrückt wird
    if keyboard.is_pressed('k'):
        run_import()

    # Überprüfe, ob die Tastenkombination 'Strg + Ü' gedrückt wird
    if keyboard.is_pressed('ctrl+ü'):
        run = False  # Beende die Schleifen

# Hier kannst du aufräumen, wenn nötig
print("Programm beendet.")
