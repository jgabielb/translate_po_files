from dataUtil import store_json_files, create_message_dict, save_to_file, validate_settings_fine_tune
import settings

def main():
    validate_settings_fine_tune()
    # Read JSON files from directory and store their content in a dictionary
    data_from_directory = store_json_files(settings.FINE_TUNE_INPUT_DIR)
    #print("Data from JSON files:", data_from_directory)
    
    # Extract user and assistant content from the first JSON file (for demonstration purposes)
    for getKey in data_from_directory['fineTuneInput.json'].keys():
        user_content = getKey
        decodedValue = str(data_from_directory['fineTuneInput.json'][getKey])
        encodedValue = decodedValue.encode('utf-8').hex()
        assistant_content = encodedValue

        #print(f"Key: {user_content}")

        message_data = create_message_dict(user_content, assistant_content)
        #print("Message Dictionary:", message_data)

        save_to_file(message_data)

# Call the main function
if __name__ == "__main__":
    main()
