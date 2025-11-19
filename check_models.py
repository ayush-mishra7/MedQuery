from groq import Groq

client = Groq(api_key="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")

models = client.models.list()

for m in models.data:
    print(m.id)
