import time, itertools;

class words:
    class fun:
        def find ( array, findc ):                                      #Outputs if true then position.
            auth = False;
            tick = 0;
            for x in array:
                auth = auth or x == findc;
                if auth: break;
                tick+= 1;
            return [auth, tick];

        def dfind ( dic, findc ):                                       #Outputs if true then position.
            auth = False;
            tick = 0;
            for x in dic:
                auth = auth or dic[x] == findc;
                if auth: break;
                tick+= 1;
            return [auth, tick];

        def prog( x, outOf, size=40, char="/", brackets=True, brackeType = "<>" ):
            per = ( ( x ) / outOf );                                    #Percentage of shaded in
            charA = ( ( per ) * size );                                 #Undertale :D
            charA = int ( charA );
            string = "";
            for x in range(charA):string += char;
            for x in range( size - charA ):string += " ";
            if brackets: string = brackeType[0] + string + brackeType[1];
            return string;

    timePerWord = 5;
    timePerRefresh = 5;
    errorLog = [];
    shhh = False;

    try:
        print ( "Reading" );
        f = open ( "words.txt", "rb" );
        fd = f.read();
        f.close();
        del f;                                                          #saves a pointer of memory or so...
        print ( "Success!" );
        try:
            print ( "Decoding" );
            fd = fd.decode().lower().split("\r\n");                     #decoding from UTF-8 to string and splitting into actual words
            wordl = [];

            print ( "Success!");
            tttt = time.time() + timePerRefresh;
            tick = 0;
            print ( "Sorting");
            prog = len ( fd );
            for x in fd:
                try:
                    try:
                        y = x.lower();                                  #Removes capitals that would mess up future code. 
                    except: pass;                                       #Better safe than sorry
                
                    tt = time.time();                                   #Unknown Hangs :( Program will skips some words
                    auth = False;
                    while tt + timePerWord >= time.time():
                        try:
                            wordl[len(y)].append(y);                    #Sorting into word lenghs
                            auth = True;
                            break;                                      #This helps as the computer will
                        except IndexError:                              #only look in the lenghs of the
                            wordl.append([]);                           #word and not all of the array
                                                                        #which ultimatley optimises the code :D
                    if not auth:
                        raise NameError("Word took too long");

                    tick += 1;
                    if tttt < time.time():
                        tttt = time.time() + timePerRefresh;
                        print ( "\n" * 50);
                        print ( fun.prog(tick, prog), str( round( tick * 100 / prog, 2 ) ) + "%" );
                
                except NameError as e:
                    if not shhh: print ( "Error with word:", x );
                    errorLog.append([e,x]);
                except Exception as e:
                    errorLog.append([e,x]);
                
            del fd                                                      #Spares some memory from dictslib. I don't really need file data.
            print ( "Success :D" );
        except:
            print ( "Decoding and Sorting Failed" );
    except:
        print ( "Reading Failed" );

class math(): pass;


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
##while True:  ##Commented out for testing.
##    print ( menu() );
##    yn();
    

def countMath(n1,n2,n3,n4,n5,n6,tar):
    signs = [1,2,3,4];
    numbs = [[1,2,3,4,5,6],7];
    hrn = {1:"+", 2:"-", 3:"*", 4:"/"};
    hrm = {1:eval(n1), 2:eval(n2), 3:eval(n3), 4:eval(n4), 5:eval(n5), 6:eval(n6), 7:eval(tar)};
    sol = [];
    i = 0;
    while i != 6:
        for x in itertools.permutations(numbs[0], i+1):
            x = list( x );
            for y in itertools.product(signs, repeat=i):
                s = 0;
                s += hrm[x[0]];
                ii = 0;
                while True:
                    try:
                        if y[ii] == 1: s += hrm[x[ii+1]];
                        if y[ii] == 2: s -= hrm[x[ii+1]];
                        if y[ii] == 3: s = s * hrm[x[ii+1]];
                        if y[ii] == 4: s = s / hrm[x[ii+1]];
                    except:
                        break;
                    ii += 1;

                if s == hrm[numbs[1]]:
                    sol.append([[ hrn[iii] for iii in y], [hrm[iii] for iii in x]]);
        i += 1;
    return sol;













