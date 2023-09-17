import pyperclip as prc
import openai
openai.api_key = "API_KEY"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{
        "role": "user",
        "content": prompt 
    }]

    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature=0,
    )

    return response.choices[0].message["content"]

my_dictionary = {}

word = prc.waitForNewPaste()

prompt = f"""
Give meaning, pronounciation, synonyms and antonyms of the text delimited by triple backticks \ 
into detail.
```{word}```
"""
response = get_completion(prompt)
print(response)

my_dictionary.update({word : response})

print(my_dictionary)

