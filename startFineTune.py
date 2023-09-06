from time import sleep
import openai
import settings
from openaiFineTune import uploadFileOpenAI, getFileStatus, genFineTune, getFineTuneStatus


def main():
    fineTuneFile = filepath = os.path.join(settings.FINE_TUNE_OUTPUT_DIR, settings.FINE_TUNE_OUTPUT_NAME)
    fileDetails = uploadFileOpenAI(fineTuneFile)

    uploadStatus = getFileStatus(fileDetails.id)
    while uploadStatus != 'processed':
        uploadStatus = getFileStatus(fileDetails.id)
        print(f"File {fileDetails.id}, status: {fileStatus}")
        sleep(10)

    if uploadStatus == 'processed':
        fineTuneJob = genFineTune(fileDetails.id)
        fineTuneStatus = getFineTuneStatus(fineTuneJob)
    while fineTuneStatus != 'succeeded':
        fineTuneStatus = getFineTuneStatus(fineTuneJob)
        print(f"Fine tune: {fineTuneJob}, status: {fineTuneStatus}")
        sleep(10)
    print(f"Job: {fineTuneJob} DONE!")

if __name__ == "__main__":
    main()