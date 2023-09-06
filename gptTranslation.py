import openai
import json
import settings

def translate_with_gpt_davinci(prompt):
    # Add your OpenAI API key here
    openai.api_key = settings.OPENAI_KEY

    # Construct the prompt
    prompt = f'Translate the following from English to latam Spanish, the target are educational instituitions: "{prompt}"'

    # Make the API call
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60
    )

    # Extract the translated text from the response
    translated_text = response.choices[0].text.strip() # type: ignore

    return translated_text

def translate_with_gpt3(prompt):
    # Add your OpenAI API key here
    openai.api_key = settings.OPENAI_KEY

    prompt = prompt.encode('utf-8').hex() 

    # Make the API call
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[
    {"role": "system", "content": "You have the objective to save data traffic, so the content of you reponse must be short, also keep in mind that our target audience are people from educational institutes"},
    {"role": "user", "content": f"could you convert the hexadecimal string '{prompt}' into utf-8, do the translation from english to latin american spanish and return the spanish version converted to hexa in json format, consider the following key name hex, utf-8, translation and translation_hex"}
  ],
    temperature=0.2,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

    # Extract the translated text from the response
    try:
       jsonResp = json.loads(response.choices[0].message.content) # type: ignore
    except json.decoder.JSONDecodeError:
        jsonResp = {}
        jsonResp["translation_hex"] = prompt
    try:
       translated_text = jsonResp["translation_hex"]
    except json.decoder.JSONDecodeError:
        print (f"!!!!!{response.choices[0].message.content}!!!!!") # type: ignore
    if not is_hex(translated_text):
        #print (f"{prompt} - {translated_text}")
        translated_text = translate_with_gpt_davinci(bytes.fromhex(prompt).decode('utf-8'))
        #print (translated_text)
        translated_text = translated_text.encode('utf-8').hex()
    
    try:
       #print (f"{prompt} - {translated_text}")
       translated_text = bytes.fromhex(translated_text).decode('Windows-1254')
    except UnicodeDecodeError:
        #print (f"{prompt} - {translated_text}")
        translated_text = bytes.fromhex(translated_text).decode('utf-8')
    except ValueError:
        translated_text = translated_text

    return translated_text

def translate_with_gpt35(prompt):
    # Add your OpenAI API key here
    openai.api_key = settings.OPENAI_KEY

    prompt = prompt.encode('utf-8').hex() 

    # Make the API call
    response = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:personal::7qnmnL2r",
    messages=[
    {"role": "system", "content": "You will recieve a hexadecimal value and your task is decode the hexadecimal into utf8 string, translate the content of this string to spanish, encode the translated text to hexadecimal, as result you must return only the hexadecimal value of the translated text"},
    {"role": "user", "content": f"{prompt}"}
  ],
    temperature=1.1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

    # Extract the translated text from the response
    jsonResp = response.choices[0].message.content # type: ignore
    
    try:
       #print (f"{prompt} - {translated_text}")
       translated_text = bytes.fromhex(jsonResp).decode('Windows-1254')
    except UnicodeDecodeError:
        #print (f"{prompt} - {translated_text}")
        translated_text = bytes.fromhex(jsonResp).decode('utf-8')
    except ValueError:
        translated_text = jsonResp

    return translated_text

def translate_with_davinci(prompt):
    # Add your OpenAI API key here
    openai.api_key = settings.OPENAI_KEY

    #prompt = prompt.encode('utf-8').hex() 

    # Make the API call
    response = openai.Edit.create(
    model="text-davinci-edit-001",
    input=prompt,
    instruction="In this task you will be given a string input which must be translated to Latin America Spanish and you must keep the original format.",
    temperature=1,
    top_p=1
)
    translated_text = response.choices[0].text # type: ignore
    return translated_text