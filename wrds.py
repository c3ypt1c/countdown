url = "https://raw.githubusercontent.com/c3ypt1c/Dictionary/master/words.txt"
from time import time as esec
import config
##Support for translations

##Init Stage 1
try:
    print ( "Info: Loading words" )
    f = open( url.split("/")[len(url.split("/"))-1], "rb" )
    fd = f.read()
    f.close()
    del f
except FileNotFoundError:
    print ( "Info: No words found, downloading file" )
    import worddown
    try:
        fd = worddown.main(url)
        print ( "Info: Downloaded Sucessfully" )
    except:
        print ( "Error: Unrecoverable error" )
        
if len( fd ) == 0:
    print ( "Warn: File created but nothing is in it? Did you delete it?" )
    print ( "Info: No words found, downloading file" )
    import worddown
    try:
        fd = worddown.main(url)
    except:
        print ( "Error: Unrecoverable error" )

try: del downdown
except: pass

##Init Stage 2 (Advanced Indexing)
wset = {}
#wset = { lengh:{ set:[words] }}

start = esec()
fd = fd.decode()
fdx = fd.split("\n")
i = 0
skip = 0
for x in fdx:
    strlenx = str(len(x))
    if (int (strlenx) > config.maxLengh) or ( int(strlenx) < config.maxLengh) or (x in config.forbiddenChar):
        skip+=1;
    else:
        i+=1;
        strsetx = str(set(x))
        try: wset[strlenx][strsetx].append(x.lower())
        except:
            try: wset[strlenx][strsetx] = [x]
            except: wset[strlenx] = {strsetx:[x]}
#Main
print ( "Info: Took",round(esec() - start),"seconds to scan", i + skip, "words" )
print ( "Info: indexed",i,"words")
print ( "Info: Skipped",skip,"words")

        
def main():
    global wset;
    print ( "\nInfo: Input all letters then enter an empty string" )
    l = ""
    i = 0
    while True:
        i+= 1
        x = input(str(i)+"> ")
        if x == "": break
        else: l+= x;
    try:
        pw = wset[str(len(l))][str(set(l))]
        print ( "Info: Possible Words:", len(pw) )
        if len(pw) > 10:
            yn = input ("Ask: Print all words? Y/N>" )
            if yn.lower()[0] == "y":
                i = 0
                for x in pw:
                    i+=1
                    print ( i, x, sep='. ' )
            else:
                print ( pw[0] )
        else:
            for x in pw:
                i+=1
                print ( i, x, sep='. ' )
    except:
        print ( "Info: No words found" )
        pw = []






