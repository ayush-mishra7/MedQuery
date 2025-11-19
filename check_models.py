from groq import Groq

client = Groq(api_key="API_KEY_HERE")

models = client.models.list()

for m in models.data:
    print(m.id)
