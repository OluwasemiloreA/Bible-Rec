import math
import sys

global bookcount
bookcount = 66
otbookcount = 39
ntbookcount = 27

def needtoread():
    #Doesnt work. Supposed to remove read chapters
    with open('ReadNT.txt','r') as readnt, open('ReadOT.txt','r') as readot, open('OTBooks.txt','r') as ot, open('NTBooks.txt','r') as nt:
        print('You need to read:')
        print('Old testament:')
        for line in ot:
            print('test')
            for comp in readot:
                #print('reach')
                if line != comp:
                    #print('test')
                    print(line.replace('\n',''))
                else:
                    break
            
    
                
        print('')
        print('New Testament')
        for line in nt:
            for comp in readnt:
                if line != comp:
                    break
                print(line.replace('\n',''))
    print('')
            

def readcompletion():
    try:
        with open('ReadNT.txt','r') as readnt, open('ReadOT.txt','r') as readot, open('OTBooks.txt','r') as ot, open('NTBooks.txt','r') as nt:
            #ERROR try statement requires both to exsist
            print('You need to read:')
            print('Old testament:')
            for line in ot:
                print(line.replace('\n',''))
            print('')
            print('New Testament')
            for line in nt:
                print(line.replace('\n',''))
            print('')
            otrcount = 0
            ntrcount = 0
            print('You have read:')
            print('Old testament:')
            for line in readot:
                otrcount = otrcount + 1
                print(line.replace('\n',''))
            print('')
            print('New Testament')
            for line in readnt:
                ntrcount = ntrcount + 1
                print(line.replace('\n',''))
            fullcount = otrcount + ntrcount
            print(f'You have read {otrcount} books in the Old testament and {ntrcount} books in the New testament \nAll together you have read {fullcount} books. This is {percent(fullcount,bookcount)} of the bible.\n')
        
    except FileNotFoundError:
        print("You haven't recorded reading any.\n")

def percent(a,b):
    perc = (a/b)*100
    perc = math.trunc(perc)
    percent = str(perc)+'%'
    return percent

def recordread():
    #works but it is possible to input the same book multiple times. and fix the formatting
    inputflag = input('What testament do you want to record a book in? (Old/New) ')
    inputflag = inputflag.capitalize()
    while inputflag != 'Old' and inputflag != 'New':
        print('Sorry. Try the selection again.')
        inputflag = input('What testament do you want to record a book in? (Old/New) ')
        inputflag = inputflag.capitalize()
    if inputflag == 'Old':
        with open('ReadOT.txt','a') as readfile, open('OTBooks.txt','r') as otlist:
            linearray = []
            recarray = []
            for line in otlist:
                recarray.append(line)
                line = line.split(': ')
                linearray = linearray + line
            print(" 1: Genesis \n 2: Exodus \n 3: Leviticus \n 4: Numbers \n 5: Deuteronomy \n 6: Joshua \n 7: Judges \n 8: Ruth \n 9: 1st Samuel \n 10: 2nd Samuel \n 11: 1st Kings \n 12: 2nd Kings \n 13: 1st Chronicles \n 14: 2nd Chronicles \n 15: Ezra \n 16: Nehemiah \n 17: Esther \n 18: Job \n 19: Psalms \n 20: Proverbs \n 21: Ecclesiastes \n 22: Song of Solomon \n 23: Isaiah \n 24: Jeremiah \n 25: Lamentations \n 26: Ezekiel \n 27: Daniel \n 28: Hosea \n 29: Joel \n 30: Amos \n 31: Obadiah \n 32: Jonah \n 33: Micah \n 34: Nahum \n 35: Habakkuk \n 36: Zephaniah \n 37: Haggai \n 38: Zechariah \n 39: Malachi \n")
            while True:
                record = int(input('Select the number of the book you would like to record: '))
                if record <= otbookcount and record > 0:
                    break
                else:
                    print("The number you have selected is unavaliable or you have read it already. Try again.\n")
            finishrec(readfile,linearray,recarray,record)
            
    if inputflag == 'New':
        with open('ReadNT.txt','a') as readfile, open('NTBooks.txt','r') as ntlist:
            linearray = []
            recarray = []
            for line in ntlist:
                recarray.append(line)
                line = line.replace('\n','')
                line = line.split(': ')
                linearray = linearray + line
            print(" 1: Matthew  \n 2: Mark  \n 3: Luke  \n 4: John  \n 5: Acts  \n 6: Romans  \n 7: 1st Corinthians  \n 8: 2nd Corinthians  \n 9: Galatians  \n 10: Ephesians  \n 11: Philippians  \n 12: Colossians  \n 13: 1st Thessalonians  \n 14: 2nd Thessalonians  \n 15: 1st Timothy  \n 16: 2nd Timothy  \n 17: Titus  \n 18: Philemon  \n 19: Hebrews  \n 20: James  \n 21: 1st Peter  \n 22: 2nd Peter  \n 23: 1st John  \n 24: 2nd John  \n 25: 3rd John  \n 26: Jude  \n 27: Revelation \n")
            while True:
                record = int(input('Select the number of the book you would like to record: '))
                if record <= ntbookcount and record > 0:
                    break
                else:
                    print("The number you have selected is unavaliable or you have read it already. Try again.\n")
            finishrec(readfile,linearray,recarray,record)       

def finishrec(readfile,linearray,recarray,record):
    selectbook = linearray[record*2-1]
    selectbook = selectbook.replace('\n','')
    readfile.write(recarray[record-1])
    print(f'You have recorded reading {selectbook}. Well done.\n')

def endprog():
    print("Thank you for using Bible Rec! See you soon.")
    sys.exit()

print('Welcome to Bible Rec! Record your journey through the bible.')
flag = True
while flag:
    print("Select the number corresponding to what you would like to do: \n" +
                             "1) Record completing a book\n" +
                             "2) Check bible completion rate\n" +
                             "3) Check which books you need to read\n" +
                             "4) Exit the program\n")
    choice = int(input('Choice: '))
    print('')
    if str(choice) == '1':
        recordread()
    elif (str(choice) == '2'):
        readcompletion()
    elif (str(choice) == '3'):
        needtoread()
    elif (str(choice) == '4'):
        endprog()