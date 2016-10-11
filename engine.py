import time, itertools;

class words:
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
        del f;                                                      #saves a pointer of memory or so...
        print ( "Success!" );
        try:
            print ( "Decoding" );
            fd = fd.decode().lower().split("\r\n");                 #decoding from UTF-8 to string and splitting into actual words
            dd = {};
            for x in fd: dd[str(x)] = str(x);
            print ( "Success :D" );
            del fd;
        except:
            print ( "Decoding and Sorting Failed" );
    except:
        print ( "Reading Failed" );

    def find(dic, string):
        i = 9;
        sol = [];
        tttt = time.time() + 1;
        o = 0;
        t = math.exp(4) + math.exp(5) + math.exp(6) + math.exp(7) + math.exp(8) + math.exp(9);
        while True:
            for x in itertools.permutations(string, i):
                s = "";
                for y in x: s+= y;
                try: sol.append(dd[s]);
                except: pass;
                if tttt < time.time():
                    tttt = time.time() + 5;
                    print ( words.prog(o, t), str( round( o * 100 / t, 2 ) ) + "%", o, t )
                o += 1;
            if i == 4:
                return None;
            if len(sol) == 0:
                i-= 1;
            else:
                return sol;

class math():
    def exp(a):
        b = 1;
        for x in range(1, a+1):
            b = b * a;
        return b;
            
    def countMath(n1,n2,n3,n4,n5,n6,tar):
        signs = [1,2,3,4];
        numbs = [[1,2,3,4,5,6],7];
        hrn = {1:"+", 2:"-", 3:"*", 4:"/"};
        hrm = {1:eval(str(n1)), 2:eval(str(n2)), 3:eval(str(n3)), 4:eval(str(n4)), 5:eval(str(n5)), 6:eval(str(n6)), 7:eval(str(tar))};
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
                            elif y[ii] == 2: s -= hrm[x[ii+1]];
                            elif y[ii] == 3: s = s * hrm[x[ii+1]];
                            elif y[ii] == 4: s = s / hrm[x[ii+1]];
                        except:
                            break;
                        ii += 1;

                    if s == hrm[numbs[1]]:
                        sol.append([[ hrn[iii] for iii in y], [hrm[iii] for iii in x]]);
            i += 1;
        if len( sol ) != 0: return sol;
        else: return None;

##def menu():
##    return """
##1. Numbers round.
##2. Words round.""";
##while True:  ##Commented out for testing.
##    print ( menu() );
##    yn();
    
##Letters it has...










