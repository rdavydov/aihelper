#!/usr/bin/env python3
"""aihelper: ask in English — get bash commands"""
import sys, os, json, urllib.request

YANDEX_CLOUD_FOLDER = "abc"
YANDEX_CLOUD_API_KEY = "efg"
YANDEX_CLOUD_MODEL = "qwen3-235b-a22b-fp8/latest"

API_KEY = os.getenv("YANDEX_CLOUD_API_KEY", YANDEX_CLOUD_API_KEY)
API_URL = "https://ai.api.cloud.yandex.net/v1/chat/completions"
MODEL   = f"gpt://{YANDEX_CLOUD_FOLDER}/{YANDEX_CLOUD_MODEL}"
FOLDER  = os.getenv("YANDEX_CLOUD_FOLDER", YANDEX_CLOUD_FOLDER)

SYSTEM = (
    "You are a terminal assistant. The user describes the task "
    "in English. Answer ONLY with a single line bash command. "
    "No explanation, no markdown, no backticks. "
    "Multiple commands — use && or |. OS: Linux."
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
        "x-folder-id":   FOLDER,          # Yandex Cloud requires folder ID
    })

    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())

    return data["choices"][0]["message"]["content"].strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: ai 'find files larger than 100 MB'")
        sys.exit(1)

    cmd = ask(" ".join(sys.argv[1:]))
    print(f"\n  \033[1;33m➜  {cmd}\033[0m\n")

    if input("Execute? [y/N] ").strip().lower() in ("y", "д"):
        os.system(cmd)

if __name__ == "__main__":
    main()
