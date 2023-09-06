# PO file Translation with chatGPT

## License

This script is open-source and free to use. Please provide appropriate credit if you use or modify this script for your projects.

## Translating .PO Files

The `translatePOFile.py` script facilitates the translation of `.po` files using a pre-generated translation dictionary.

### Dependencies

- `os`
- `tqdm`
- `settings`
- `dataUtil`

### Setup

1. Ensure you've set up configurations in the `settings.py` file and have the required `.po` files in the specified directory.
2. Make sure the `dataUtil` module is present and correctly imported.

### Usage

Run the `translatePOFile.py` script:

```bash
python translatePOFile.py
```

### Notes

- The script uses a translation dictionary to translate `.po` files. Ensure the dictionary is available and correctly formatted.
- If the dictionary is not present, the script will generate a new one based on the `.po` files.

## GPT Translation Script

This script provides functionalities to translate English content into Latin American Spanish using OpenAI's GPT models. The primary target audience for these translations is educational institutions.

### Dependencies

- `openai`
- `json`
- `settings`

Ensure you have these modules installed before running the script.

### Features

1. **Davinci Translation**: Uses the `text-davinci-003` engine to translate English content to Latin American Spanish. This can be achieved using the `translate_with_gpt_davinci(prompt)` function.
2. **GPT-3 Translation**: Converts the input prompt into a hexadecimal string, translates it using the `gpt-3.5-turbo-16k` model, and then returns the translated content in hexadecimal format. Use the `translate_with_gpt3(prompt)` function for this.

### Setup

1. Ensure you have an active OpenAI account and API key.
2. Update the `settings.py` file with your OpenAI API key.

### Usage

```python
import gptTranslation as gt

# Translate using Davinci
translated_text_davinci = gt.translate_with_gpt_davinci("Your English content here")

# Translate using GPT-3
translated_text_gpt3 = gt.translate_with_gpt3("Your English content here")
```

### Notes

- Ensure your API calls do not exceed OpenAI's rate limits.
- Always be cautious about the content you translate, especially if it's sensitive information.

### License

This script is open-source and free to use. Please provide appropriate credit if you use or modify this script for your projects.

## Google Cloud Translation

Apart from OpenAI's GPT models, this repository also provides functionalities to translate content using Google Cloud's Translation services.

### Dependencies

- `google.cloud`

### Setup

1. Set up a Google Cloud account and enable the Translation API.
2. Download the service account JSON key and update the `settings.py` file with the path to this key.

### Usage

```python
import googleTranslation as gt

# Translate using Google Cloud Translation
translated_text_google = gt.translate_text("Your English content here")
```

### Notes

- Google Cloud might incur costs based on the amount of text translated. Monitor your usage to avoid unexpected charges.

## Fine-tuning Data Generation

The `genFineTune.py` script helps generate data suitable for fine-tuning models. It reads data from JSON files, processes the content, and saves the refined data in a structured format.

### Dependencies

- `dataUtil`
- `settings`

### Setup

1. Update the `settings.py` file with the appropriate directory paths and other configuration settings related to fine-tuning data generation.
2. Ensure you have the required JSON files in the specified directory.

### Usage

Run the `genFineTune.py` script:

```bash
python genFineTune.py
```

### Notes

- This script assumes that the input data is structured in a specific way in the JSON files. Ensure that the format matches the expected structure.

## OpenAI Fine-tuning

The `openaiFineTune.py` script provides functionalities to fine-tune OpenAI models using specific training data.

### Dependencies

- `openai`
- `settings`

### Setup

1. Update the `settings.py` file with your OpenAI API key and other relevant configuration settings.
2. Prepare your fine-tuning data in the required format.

### Usage

```python
import openaiFineTune as oft

# Upload a file for fine-tuning to OpenAI
file_details = oft.uploadFileOpenAI("path_to_your_fine_tune_file.txt")

# Check the status of an uploaded file
file_status = oft.getFileStatus(file_details.id)

# Start a fine-tuning job
fine_tune_job_id = oft.genFineTune(file_details.id)

# Check the status of a fine-tuning job
fine_tune_status = oft.getFineTuneStatus(fine_tune_job_id)
```

### Notes

- Ensure that your fine-tuning data adheres to OpenAI's guidelines and format requirements.
- Monitoring the status of your uploaded files and fine-tuning jobs can help you track their progress and troubleshoot any issues.

## Starting Fine-tuning on OpenAI

The `startFineTune.py` script automates the process of starting a fine-tuning job on OpenAI using a specific dataset.

### Dependencies

- `openai`
- `settings`
- `openaiFineTune`

### Setup

1. Ensure you've already set up configurations in the `settings.py` file and have the required dataset ready.
2. Make sure the `openaiFineTune` module is present and correctly imported.

### Usage

Run the `startFineTune.py` script:

```bash
python startFineTune.py
```

### Notes

- The script continuously checks the status of the uploaded file and the fine-tuning job. Ensure you have a stable internet connection while running the script.
- Monitor your OpenAI usage as fine-tuning can consume a significant amount of API calls.

## Data Utilities

The `dataUtil.py` script offers utility functions to facilitate the processing and translation of `.po` files.

### Dependencies

- `settings`
- `tqdm`
- `polib`
- `googleTranslation`

### Features

1. **Hexadecimal Check**: The `is_hex(s)` function checks if a string represents a hexadecimal value.
2. **Settings Validation**: The `validate_settings()` function verifies various configurations from the `settings` module.
3. **File Processing**: The `process_file(filename, translation_dict)` function processes a `.po` file, translates its entries using Google Translation, and updates a dictionary with the translations.
4. **Batch Processing**: The `create_translation_dict(directory, translation_dict)` function processes all `.po` files in a directory concurrently.

### Usage

These utility functions can be imported and used in other scripts for processing and translating `.po` files.

### Notes

- Ensure your `.po` files are correctly structured.
- Monitor your translation API usage to avoid unexpected charges.
