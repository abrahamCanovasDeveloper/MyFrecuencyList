import pandas as pd
import re
import os

INPUT_FOLDER = "./input/"
OUTPUT_FOLDER = "./output/"
IGNORED_WORDS = [
    "a",
    "abaft",
    "aboard",
    "about",
    "above",
    "absent",
    "across",
    "afore",
    "after",
    "against",
    "along",
    "alongside",
    "amid",
    "amidst",
    "among",
    "amongst",
    "an",
    "anenst",
    "apropos",
    "apud",
    "around",
    "as",
    "aside",
    "astride",
    "at",
    "athwart",
    "atop",
    "barring",
    "before",
    "behind",
    "below",
    "beneath",
    "beside",
    "besides",
    "between",
    "beyond",
    "but",
    "by",
    "circa",
    "concerning",
    "despite",
    "down",
    "during",
    "except",
    "excluding",
    "failing",
    "following",
    "for",
    "forenenst",
    "from",
    "given",
    "in",
    "including",
    "inside",
    "into",
    "lest",
    "like",
    "mid",
    "midst",
    "minus",
    "modulo",
    "near",
    "next",
    "notwithstanding",
    "of",
    "off",
    "on",
    "onto",
    "opposite",
    "out",
    "outside",
    "over",
    "pace",
    "past",
    "per",
    "plus",
    "pro",
    "qua",
    "regarding",
    "round",
    "sans",
    "save",
    "since",
    "than",
    "through",
    "throughout",
    "till",
    "times",
    "to",
    "toward",
    "towards",
    "under",
    "underneath",
    "unlike",
    "until",
    "unto",
    "up",
    "upon",
    "versus",
    "via",
    "vice",
    "with",
    "within",
    "without",
    "worth",
]
WHITE_SPACE = " "
LENGTH_MIN = 2
FORMAT = ".txt"




for file in os.listdir(INPUT_FOLDER):       #Check folder and file format
    if file.endswith(FORMAT):

        tempList = []   #List where storage all required words
        txtFile = open(INPUT_FOLDER + file, "rt", encoding="utf8")  # Get input txt
        for line in txtFile.readlines():
            cleanedLine = re.sub("[^A-Za-z]+", WHITE_SPACE, line)
            cleanedLine = cleanedLine.lower()
            for cleandWord in cleanedLine.split(WHITE_SPACE):
                if cleandWord not in IGNORED_WORDS and len(cleandWord) > LENGTH_MIN:
                    tempList.append(cleandWord)
        txtFile.close()

        #Definitely lists where storage one time each word and count from templist how many 
        listWord = []
        listFrecuency = []
        for word in tempList:
            if word not in listWord:
                listWord.append(word)
                listFrecuency.append(tempList.count(word))

        # CREATE DATAFRAME
        data = {"Word": listWord, "Frecuency": listFrecuency}
        df = pd.DataFrame(data)
        df.to_csv(OUTPUT_FOLDER + file.removesuffix(FORMAT) + ".csv", index=False)