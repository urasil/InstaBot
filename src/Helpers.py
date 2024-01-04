import os

def isLineInFile(filePath, targetLine):
    try: 
        with open(filePath, "r") as f:
            for line in f:
                if targetLine == line.strip():
                    return True
            return False
    except FileNotFoundError:
        print("File not found")
        return False
    except Exception as e:
        print("Error while reading file: ", e)
        return False
    
def addNewlines(text, maxChars=60):
    length = len(text)
    if length < maxChars:
        return text
    else:
        i = maxChars
        while i < length:
            if text[i] == " ":
                text = text[:i] + "\n" + text[i+1:]
                i += maxChars  
            else:
                i += 1
        return text
    
def removeImages(folderPath):
    for fileName in os.listdir(folderPath):
        filePath = os.path.join(folderPath, fileName)
        if os.path.isfile(filePath):
            os.remove(filePath)
            


