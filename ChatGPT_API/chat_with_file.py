import openai
from openai import OpenAI

# OpenAIクライアントを初期化（APIキーを使って）
client = OpenAI(api_key="sk-...")  # ←自分のAPIキーを入れてね

# ファイル読み込み
with open("info.txt", "r", encoding="utf-8") as f:
    file_contents = f.read()

# 質問入力
user_question = input("質問をどうぞ: ")

# Chat APIへ問い合わせ
response = client.chat.completions.create(
    model="gpt-4",  # または "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "以下はユーザーのメモです。質問に答える際に必ずこのメモを参考にしてください。\n" + file_contents},
        {"role": "user", "content": user_question}
    ],
    temperature=0.7
)

# 結果を表示
print("AIの回答:", response.choices[0].message.content)
