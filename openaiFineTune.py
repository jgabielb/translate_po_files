import openai
import settings

def uploadFileOpenAI(fineTuneFile):
    openai.api_key = settings.OPENAI_KEY
    fileDetails = openai.File.create(
    file=open(fineTuneFile, "rb"),
    purpose='fine-tune'
    )
    return fileDetails

def getFileStatus(openaiFileID):
    openai.api_key = settings.OPENAI_KEY
    fileStatusDetails = openai.File.retrieve(openaiFileID)
    return fileStatusDetails.status

def genFineTune(openaiFileID):
    openai.api_key = settings.OPENAI_KEY
    fineTuneJob = openai.FineTuningJob.create(training_file=openaiFileID, model="gpt-3.5-turbo")
    return fineTuneJob.id

def getFineTuneStatus(fineTuneID):
    openai.api_key = settings.OPENAI_KEY
    fineTuneJobDetails = openai.FineTuningJob.retrieve(fineTuneID)
    return fineTuneJobDetails.status