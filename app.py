import openai

openai.api_key = open("key.txt", "r").read().strip("\n")

def chat(inp, message_history, role="user"):

    # Append the input message to the message history
    message_history.append({"role": role, "content": f"{inp}"})

    # Generate a chat response using the OpenAI API
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )

    # Grab just the text from the API completion response
    reply_content = completion.choices[0].message.content

    # Append the generated response to the message history
    message_history.append({"role": "assistant", "content": f"{reply_content}"})

    # Return the generated response and the updated message history
    return reply_content, message_history

message_history = [
    {"role": "user", "content": """ "Welcome to the Realm of Mystical Adventures, a world where magic and 
    mystery collide. 
    Your decisions will shape the fate of your character and the world around them. 
    Choose wisely, for every choice has consequences  every choice the user needs to pick
    from 2-4 options that you provide. Once the user pick one of those options,
    you will state what happens next and present new options and then repeats.
    If you understand, say, OK, and begin when I say "begin." When you present
    the story, no further commentary, and then option like "Option 1 :" "Option 2:"
    ...etc."""},
    {"role": "assistant", "content":f"""OK, I understand. 
                                        Begin when you're ready."""}
]

replay_content, message_history = chat("begin", message_history)

for _ in range(3):
    print(replay_content)
    next_inp = input("Enter your response: ")
    replay_content, message_history = chat(replay_content, message_history)

