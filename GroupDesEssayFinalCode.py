import string
import datetime

def FindSentences(inText):
# creates a List of Sentences by looking for punctuation contained in string punctSentence
    List1 = []
    strt = 0
    global punctSentence
    ix = 0
    while ix < len(inText):
        if inText[ix] in punctSentence or ix + 1 == len(inText):
            if inText[ix] != "." or ix + 1 == len(inText) or (inText[ix + 1] == " " and inText[ix-3:ix] != "Mrs" and inText[ix-3:ix] != " St"):
                List1.append(inText[strt:ix] )
                strt = ix + 1
        ix += 1
    return(List1)

def WordCounts(sentList):
    # creates a List of Counters by looking at each Sentence and counting words for that Sentence
    CtrList1 = [0]* len(sentList)
    strt = 0
    ix = 0
    for ix in range(len(sentList)):
         for word in sentList[ix].split():
             if len(word) > 4:
                 CtrList1[ix] = CtrList1[ix] + 1
             elif len(word) > 2 and '"' not in word: # excludes short words with quotes
                 CtrList1[ix] = CtrList1[ix] + 1
    return(CtrList1)

def ComputeAvg(cntList):
# uses counter list to calculate averages
    SentenceCtr = 0
    WordCtr = 0
    for num in cntList:
        if num > 2:     # excludes sentences smaller than 3
           SentenceCtr += 1
           WordCtr = WordCtr + num
    print(SentenceCtr,WordCtr)
    return(WordCtr/SentenceCtr)

def WriteAvgRpt(WordAvg,fn):
    '''
       this routine should write out a text file with the average & date/time on a line
       if a file exists for this report (so report name must be in the text file name)
       this info needs to be appended to the already existing file
    '''
    AvgRpt = "AVG_" + fn
    line1 = "This is your average for " + fn + " " + str(WordAvg) + " On " + str(datetime.datetime.today()) + "\n"
    print(line1)
    try:
        fout = open(AvgRpt, 'a')
    except FileNotFoundError:
        fout = open(AvgRpt, 'w')
    fout.write(line1)
    fout.close()

def LongWordRept(Counts1, List1):
 '''
   this routine should write out a file of aentences larger than 10 words for a given report.
   The content can be created by searching through the list of sentence counts and finding counts larger than 10.
   It would use the index to retrieve the corresponding sentence in the sentence list and write out that sentence in the file.
'''
punctSentence = ".!?;,"

ValidInput = False
while not ValidInput:
    try:
        filename=input("Please Enter the Complete File Name ")
        f = open(filename, "r")
        rept = (f.read())
        print(rept)  #for diagnostic purposes - prints input
        ValidInput = True
        f.close()
        List1 = FindSentences(rept)   # breaks input into sentences
# diagnostic purpose - prints out each sentence
        a = 0
        for n in List1:
            a += 1
            print(a,n)
# End diagnostic
        Counts1 = WordCounts(List1)     # counts words in each sentence
        print(Counts1)                  # diagnostic only - prints list of counts
        WordAvg = ComputeAvg(Counts1)   # computes average
        print(WordAvg)                  # diagnostic only - prints Average
        WriteAvgRpt(WordAvg,filename)
        LongWordRept(Counts1,List1)     # Writes Long word rept - not yet coded
    except FileNotFoundError:
        print("Sorry Not Found")
    except PermissionError:
        print("Sorry Not Allowed")



