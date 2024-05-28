from groq import Groq
import os
from dotenv import load_dotenv
import pyperclip

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



