from ollama import chat

response = chat(
    model = "qwen2.5:0.5b ",
    messages = [
        {
            "role": "user",
            "content": "What is an AI Agent?"
        }
    ]
)
print(response.message.content)