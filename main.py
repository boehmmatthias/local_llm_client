from groq import Groq
import os
from dotenv import load_dotenv
import pyperclip
import keyboard  # Importiere das keyboard Modul

import1 = True
run = True

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_dir, "style/calc.css")

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
        )

        pyperclip.copy(chat_completion.choices[0].message.content)

while run:
    # Überprüfe, ob die Taste 'k' gedrückt wird
    if keyboard.is_pressed('k') and import1:
        run_import()
        import1 = False  # Stelle sicher, dass die Schleife nur einmal ausgeführt wird

    # Überprüfe, ob die Taste 'ü' gedrückt wird
    if keyboard.is_pressed('ctrl+ü'):
        run = False  # Beende die Schleifen

# Hier kannst du aufräumen, wenn nötig
print("Programm beendet.")
