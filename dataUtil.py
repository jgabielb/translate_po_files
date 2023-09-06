import settings
import os, sys
from tqdm import tqdm
#from gptTranslation import translate_with_davinci, translate_with_gpt3, translate_with_gpt35, translate_with_gpt_davinci
from googleTranslation import translate_text
import concurrent.futures
import polib
import json

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def validate_settings():
    if not settings.OPENAI_KEY:
        print('OPENAI_KEY is not defined. Please fill this variable in settings file')
        sys.exit(2)

    if not settings.GOOGLE_CREDENTIALS:
        print('GOOGLE_CREDENTIALS is not defined. Please fill this variable in settings file')
        sys.exit(2)

    if not settings.PO_INPUT_FOLDER:
        print('PO_INPUT_FOLDER is not defined. Please fill this variable in settings file')
        sys.exit(2)

    if not settings.PO_OUTPUT_FOLDER:
        print('PO_OUTPUT_FOLDER is not defined. Please fill this variable in settings file')
        sys.exit(2)

    if not settings.DICT_NAME:
        print('DICT_NAME is not defined. Please fill this variable in settings file')
        sys.exit(2)

    if not settings.TARGET_LANGUAGE:
        print('TARGET_LANGUAGE is not defined. Please fill this variable in settings file')
        sys.exit(2)
    return True

def process_file(filename, translation_dict):
    po = polib.pofile(filename)
    for entry in tqdm(po, desc=f"Processing {filename}"):
        #key = hashlib.sha256(entry.msgid.encode()).hexdigest()
        key = entry.msgid.encode('utf-8').hex()
        if key not in translation_dict:
            try:
               translation_dict[key] = translate_text(entry.msgid)
            except Exception as e:
               print(f"An error occurred when processing the file {filename}: {str(entry.msgid)}")
    return translation_dict

def create_translation_dict(directory=settings.PO_INPUT_FOLDER, translation_dict={}):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        filenames = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".po")]
        futures = {executor.submit(process_file, filename, translation_dict): filename for filename in filenames}
        for future in concurrent.futures.as_completed(futures):
            translation_dict.update(future.result())

    # Save the dictionary to a JSON file
    with open(settings.DICT_NAME, 'w', encoding='utf-8') as f:
        json.dump(translation_dict, f, ensure_ascii=False, indent=4)

    return translation_dict

def translate_po_file(filename, translation_dict, output_dir=settings.PO_OUTPUT_FOLDER):
    # Load the .po file
    po = polib.pofile(filename)

    # Define the base name for the output files
    base_name = os.path.basename(filename).rsplit('.', 1)[0]

    # Open the log file
    with open(os.path.join(output_dir, base_name + '_log.txt'), 'w', encoding='utf-8') as log_file:
        # Iterate over all entries in the .po file
        for entry in po:
            # Use the hash of the untranslated string as the key
            #key = hashlib.sha256(entry.msgid.encode()).hexdigest()
            key = entry.msgid.encode('utf-8').hex()

            if key in translation_dict:
                # If the translation exists in the dictionary, use it
                translated_text = translation_dict[key]
            else:
                # Otherwise, translate the msgid and assign it to msgstr
                print(f"###Key - {key} - Translating {entry.msgid} ###")
                translated_text = translate_text(entry.msgid)
                # And add it to the dictionary
                translation_dict[key] = translated_text

            entry.msgstr = translated_text

            # Write the msgid and translated text to the log file
            log_file.write(f"{entry.msgid}\t{translated_text}\n")

    # Save the updated .po file
    translated_filename = os.path.join(output_dir, base_name + '_translated.po')
    po.save(translated_filename)

    return translated_filename

def read_all_files(directory=settings.PO_INPUT_FOLDER):
    files_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith(".po"):
            # Load the .po file
            po = polib.pofile(os.path.join(directory, filename))
            files_dict[filename] = po
    return files_dict

def open_translation_dict(translation_dict=settings.DICT_NAME):
    try:
        with open(translation_dict, encoding='utf-8') as json_file:
           data = json.load(json_file)
    except Exception as e:
           data = {}
    return data

def read_directory(directory_path):
    """List all files in the given directory."""
    return os.listdir(directory_path)

def is_json_file(filename):
    """Check if the file is a JSON file."""
    return filename.endswith('.json')

def read_json_file(filepath):
    """Read a JSON file and return its content."""
    with open(filepath, 'r',encoding='utf-8') as f:
        return json.load(f)

def store_json_files(directory_path):
    """Store contents of all JSON files in the given directory in a dictionary."""
    files = read_directory(directory_path)
    json_files_content = {}

    for file in files:
        if is_json_file(file):
            filepath = os.path.join(directory_path, file)
            json_files_content[file] = read_json_file(filepath)

    return json_files_content

def create_message_dict(user_content, assistant_content):
    """Create a dictionary with specific message structure using provided content."""
    return {"messages": [{"role": "system", "content": "You will recieve a hexadecimal value and your task is decode the hexadecimal into utf8 string, translate the content of this string to spanish, encode the translated text to hexadecimal, as result you must return only the hexadecimal value of the translated text"},{"role": "user", "content": user_content},{"role": "assistant", "content": assistant_content}]}

def save_to_file(data, filename=settings.FINE_TUNE_OUTPUT_NAME):
    if not os.path.exists(settings.FINE_TUNE_OUTPUT_DIR):
        os.makedirs(settings.FINE_TUNE_OUTPUT_DIR)
    
    filepath = os.path.join(settings.FINE_TUNE_OUTPUT_DIR, filename)
    
    with open(filepath, 'a') as f:
        json.dump(data, f)
        f.write('\n')
    
    print(f"Data saved to {filepath}")

def validate_settings_fine_tune():
    if not settings.OPENAI_KEY:
        print('OPENAI_KEY is not defined. Please fill this variable in settings file')
        sys.exit(2)

    if not settings.FINE_TUNE_INPUT_DIR:
        print('FINE_TUNE_INPUT_DIR is not defined. Please fill this variable in settings file')
        sys.exit(2)

    if not settings.FINE_TUNE_OUTPUT_DIR:
        print('FINE_TUNE_OUTPUT_DIR is not defined. Please fill this variable in settings file')
        sys.exit(2)

    if not settings.FINE_TUNE_OUTPUT_NAME:
        print('FINE_TUNE_OUTPUT_NAME is not defined. Please fill this variable in settings file')
        sys.exit(2)
    return True