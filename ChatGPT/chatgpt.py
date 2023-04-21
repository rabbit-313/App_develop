import openai

openai.api_key = ''

# response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                 {'role': 'user', 'content': "こんにちは"}],
#                 temperature=0.0,
# )

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "サザエさんの家族構成を教えて。"},
        {"role": "assistant",
         "content": '''サザエさんの家族構成は以下のとおりです。
- サザエ（主人公）：主婦。夫と娘がいる。
- マスオさん（サザエの夫）：会社員。
- タラちゃん（サザエとマスオさんの息子）：小学生。後に妹が生まれる。
- サザエの父：「フグ田吾作」というペンネームで漫画家をしている。
- サザエの母：専業主婦。主に家事や子育てを担当している。
- 波平さん（サザエの兄）：漁師。妻と娘がいる。'''},
        {"role": "user", "content": "カツオは？"}
    ]
)
print(response['choices'][0]['message']['content'])