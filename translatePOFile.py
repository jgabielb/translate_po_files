import os
from tqdm import tqdm
import settings
from dataUtil import validate_settings, read_all_files, create_translation_dict, translate_po_file, open_translation_dict

def main():
    validate_settings()
    po_files = read_all_files(settings.PO_INPUT_FOLDER)
    
    dict_data = open_translation_dict(settings.DICT_NAME)

    transDict = create_translation_dict(translation_dict = dict_data)

    for filename in tqdm(po_files.keys(), desc="Translating files"):
        translate_po_file(os.path.join(settings.PO_INPUT_FOLDER, filename),transDict)

if __name__ == "__main__":
    main()