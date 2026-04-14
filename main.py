from chatbot import handle_query

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    response = handle_query(query)
    print("Bot:", response)