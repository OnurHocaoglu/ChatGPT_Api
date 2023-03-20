import openai

# pip install openai

API_KEY = open("API_KEY","r").read() # API KEY 
openai.api_key = API_KEY


chat_log =[]

while True:
    print("Çıkış yapmak için 'quit' yazmanız yeterlidir.")
    user_message = input("ChatGPT'ye ne sormak istersiniz? : ")
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role":"user","content": user_message})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= chat_log)
        assistant_response = response['choices'][0]['message']['content']
        print("ChatGPT:", assistant_response.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})


# onurhocaoglu.com 