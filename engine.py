class words:
    class fun:
        def find ( array, findc ):  #Outputs if true then position.
            auth = False
            tick = 0
            for x in array:
                auth = auth or x == findc
                if auth: break
                tick+= 1
            return [auth, tick]

        def dfind ( dic, findc ):   #Outputs if true then position.
            auth = False
            tick = 0
            for x in dic:
                auth = auth or dic[x] == findc
                if auth: break
                tick+= 1
            return [auth, tick]

        def order(word):
            basket = {}
            order = [[],[]]
            tick = 0
            for x in str( word ):
                f = dfind(basket, x)
                if not f[0]:
                    basket[f[1]] = x
                order[0].append(f[1])
                tick += 1

            order[1] = basket

            return order

        def prog( x, outOf, size=40, char="/", brackets=True, brackeType = "<>" ):
            per = ( ( x ) / outOf )                       #Percentage of shaded in
            charA = ( ( per ) * size )                    #Undertale :D
            charA = int ( charA )
            string = ""
            for x in range(charA):string += char
            for x in range( size - charA ):string += " "
            if brackets: string = brackeType[0] + string + brackeType[1]

            return string
 
    import time

    timePerWord = 5
    timePerRefresh = 5
    errorLog = []
    shhh = False

    try:
        print ( "Reading" )
        f = open ( "words.txt", "rb" )
        fd = f.read()
        f.close()
        del f                                                       #saves a byte of memory or so...
        print ( "Success!" )
        try:
            print ( "Decoding" )
            fd = fd.decode().lower().split("\r\n")                  #decoding from UTF-8 to string and splitting into actual words
            wordl = []
                                                                    #Format so I do not forget:
            combd = {}                                              #combd = {[combination]:[{letters},...  ],  ...}
                                                                    #letters = { 0:letter, 1:letter,... }
            print ( "Success!")
            tttt = time.time() + timePerRefresh
            tick = 0
            print ( "Sorting")
            prog = len ( fd )
            for x in fd:
                try:
            
                    try:
                        y = x.lower()                               #Removes capitals that would mess up future code. 
                    except: pass                                    #Better safe than sorry
                
                    tt = time.time()                                #Unknown Hangs :( Program will skips some words
                    auth = False
                    while tt + timePerWord >= time.time():
                        try:
                            wordl[len(y)].append(y)                 #Sorting into word lenghs
                            auth = True
                            break                                   #This helps as the computer will
                        except IndexError:                          #only look in the lenghs of the
                            wordl.append([])                        #word and not all of the arrat
                                                                    #which ultimatley optimises the code :D
                    if not auth:
                        raise NameError("Word took too long")

                    auth = False
                    tt = time.time() 
                    t = fun.order(y)
                    while tt + timePerWord >= time.time():
                        try:
                            combd[str(t[0])].append(t[1])           #THIS WAS combd[str(t[0])].append(t[1][0]) AND WAS A BUG!
                            auth = True
                            break
                        except KeyError:                            #Fixed so that other errors don't ruin the rest of the dict.
                            combd[str(t[0])]=[]                     #You can't use a list as a key but stringing a list
                                                                    #is an amazing idea I had :D
                    if not auth:
                        raise NameError("Word took too long")

                    tick += 1
                    if tttt < time.time():
                        tttt = time.time() + timePerRefresh
                        print ( "\n" * 50)
                        print ( fun.prog(tick, prog), str( round( tick * 100 / prog, 2 ) ) + "%" )
                
                except NameError as e:
                    if not shhh:
                        print ( "Error with word:", x )
                    errorLog.append([e,x])
                except Exception as e:
                    errorLog.append([e,x])
                
            del fd                                                  #Spares some memory from dictslib. I don't really need file data.
            print ( "Success :D" )
        except:
            print ( "Decoding and Sorting Failed" )
    except:
        print ( "Reading Failed" )

    alphadict = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    letters = []
    for x in alphabet: letters.append(x)



##Yes/ No interface
def yn(ss="Y/N> "):
    s = input(ss).lower()[0];
    if s == "y": return True;
    elif s == "n": return False;
    else: return None;

def menu():
    return """
1. Numbers round.
2. Words round.""";

while True:
    print ( menu() );
    yn();















