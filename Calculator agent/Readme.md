You
 │
 │ "What is 25 × 48?"
 ▼
┌─────────────────────┐
│    Calculator Agent │
│                     │
│  LLM decides:       │
│  "I need calculator"│
└──────────┬──────────┘
           │
           ▼
    ┌─────────────┐
    │ calculator  │
    │   25 × 48   │
    └──────┬──────┘
           │
           ▼
         1200
           │
           ▼
┌─────────────────────┐
│        LLM          │
│ "The answer is..."  │
└─────────────────────┘
           │
           ▼
         You

#project structure 


 calculator-agent/
       ├── agent.py
       ├── calculator.py
       └── README.md

Architecture : 
                    USER
                      │
                      ▼
              ┌───────────────┐
              │  Python Agent │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   Qwen2 0.5B  │
              │   (Ollama)    │
              └───────┬───────┘
                      │
                "use calculator"
                      │
                      ▼
              ┌───────────────┐
              │ Python Tool   │
              │  Calculator   │
              └───────┬───────┘
                      │
                    1200
                      │
                      ▼
              ┌───────────────┐
              │   Qwen2 0.5B  │
              └───────┬───────┘
                      │
                      ▼
                    USER


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

response : Run chat() take whatever it returns and store it in a variable called response.

chat : calling the chat function. providing the chat multiple named arguments.

model : which model is handling this request. provide the model name in the string. Why the name is important since your systems contains multiple models already. We are telling ollama use this particular model.

messages : This is probably the most important part of understanding LLMs

