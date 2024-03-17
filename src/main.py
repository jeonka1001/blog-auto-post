from openai import OpenAI
from readfile import read_conf

data = read_conf("src/conf/secret.json")
key = "{0}".format(data["secret_key"])

subject = "감자"

client = OpenAI(
    api_key=key,
    organization='org-NfVtd19tPHBhRpmuEQcTWa2K'
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "네이버 블로그 포스팅을 위한 형식으로 {0} 에 대해서 이목을 끌만한 제목과 내용을 작성해줘 내용에는 그림을 포함하기 좋은 위치를 <그림> 으로 작성해주면 좋겠어 좋겠어".format(subject)}],
    temperature=0.7
)

blog_content = ''
for value in (chat_completion.choices):
    for key, val in value:
        if key == "message":
            for k, v in val:
                if k == "content":
                    blog_content = v

# DALL-E를 사용하여 이미지 생성 요청
response = client.images.generate(
  model="dall-e-3",
  prompt="{0}을 그려줘".format(subject),
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

result = blog_content.replace('<그림>', image_url, -1)

print(result)
