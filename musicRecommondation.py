import openai

openai.api_key = "your_actual_api_key_here"

def chat_with_gpt(prompt, max_tokens=30):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "recommend music according to moods"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError:
        return "You have exceeded your API quota. Please check your OpenAI plan and billing details."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit", "stop"]:
            print("Goodbye! If you have more questions, feel free to ask.")
            break

        response = chat_with_gpt(user_input)
        print("Music:", response)
