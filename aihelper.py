# credits: https://habr.com/ru/articles/1001214/

#!/usr/bin/env python3
"""ai-bash: спрашиваю по-русски — получаю bash"""
import sys, os, json, urllib.request

API_KEY = os.getenv("OPENAI_API_KEY", "local")
API_URL = os.getenv("AI_BASH_URL",
                     "http://localhost:11434/v1/chat/completions")
MODEL   = os.getenv("AI_BASH_MODEL", "dolphin3:latest") # non-thinking model, fast inference

SYSTEM = (
    "Ты — терминальный ассистент. Пользователь описывает задачу "
    "на русском языке. Отвечай ТОЛЬКО bash-командой — одной строкой. "
    "Без пояснений, без markdown, без обратных кавычек. "
    "Несколько команд — через && или |. ОС: Linux."
)

def ask(question: str) -> str:
    body = json.dumps({
        "model": MODEL,
        "temperature": 0,
        "max_tokens": 200,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user",   "content": question},
        ],
    }).encode()

    req = urllib.request.Request(API_URL, data=body, headers={
        "Content-Type":  "application/json",
        "Authorization": f"Bearer {API_KEY}",
    })

    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())

    return data["choices"][0]["message"]["content"].strip()

def main():
    if len(sys.argv) < 2:
        print("Использование: ai 'найди файлы больше 100мб'")
        sys.exit(1)

    cmd = ask(" ".join(sys.argv[1:]))
    print(f"\n  \033[1;33m➜  {cmd}\033[0m\n")

    if input("Выполнить? [y/N] ").strip().lower() in ("y", "д"):
        os.system(cmd)

if __name__ == "__main__":
    main()
