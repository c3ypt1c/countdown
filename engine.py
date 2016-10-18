import time, itertools;

def getFromInternet(resourceURL):
    import urllib;
    from urllib import request;
    f = request.urlopen(resourceURL);
    fd = f.read();
    f.close();
    del f;
    return fd

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

    def decodeAndSort(fd):
        print ( "Decoding" );
        try: fd = fd.decode();
        except: pass;
        fd = fd.lower().split("\r\n");                              #decoding from UTF-8 to string and splitting into actual words
        dd = {};
        for x in fd: dd[str(x)] = str(x);
        print ( "Decoded successfully" );
        suc = True;
        del fd;
        return dd;
        
    suc = False;                                                    #Weather it succeeded....
    timePerWord = 5;
    timePerRefresh = 1;
    errorLog = [];
    web = "http://lukaszbaldy.ga/words.txt"
    shhh = False;                                                   #Quiet mode...

    try:
        print ( "Reading..." );
        f = open ( "words.txt", "rb" );
        fd = f.read();
        f.close();
        del f;                                                      #saves a pointer of memory or so...
        print ( "Success!" );
        try:
            dd = decodeAndSort(fd);
            suc = True;
        except:
            print ( "Decoding and Sorting Failed..." );
    except:
        print ( "Reading Failed... Trying Internet..." );
        try:
            dd = decodeAndSort(getFromInternet(web));
            print ( "Internet method successful..." );
            suc = True;
        except:
            print ("Internet method failed...");

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
                    tttt = time.time() + timePerRefresh;
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
                    s = 0 + hrm[x[0]];
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

def menu(bo):
    if bo:
        return """
1. Numbers round.
2. Words round.""";
    else:
        return """
1. Numbers round.
x. Words round. (No dict)""";
while True:
    print ( menu(words.suc) );
    c = input("1/2> ")
    if c == "1":
        print ( "Maths round... (Press Ctr+c to go back)" );
        while True:
            try:
                c = []
                for x in range(7):
                    if x == 6:
                        c.append(int(input("Target> ")));
                    else:
                        c.append(int(input(str(x+1)+"> ")));
                break;
            except:
                pass;
            
        o = 0;
        oo = False;
        
        while True:
            if oo:
                ntt = c[6] + o;
                sol = math.countMath(c[0], c[1], c[2], c[3], c[4], c[5], ntt);
                if sol != None:
                    break;
                else:
                    print ( "No solutions found for", ntt ); 
                oo = not oo;
            else:
                ntt = c[6] - o;
                sol = math.countMath(c[0], c[1], c[2], c[3], c[4], c[5], ntt);
                if sol != None:
                    break;
                else:
                    o+= 1;
                    print ( "No solutions found for", ntt ); 
                
                oo = not oo;               
            
        soll = [];
        for x in sol:
            i = 0;
            st = "" + str(x[1][0]) + " ";
            while True:
                try:
                    st += str (x[0][i]) + " " + str(x[1][i+1]) + " "; 
                    i+= 1;
                except:
                    break;
            st+= "= " + str ( ntt );
            soll.append(st);
            
        if len( sol ) == 0:
            print ( "There are no solutions." );
        else:
            if o != 0:
                print ( "There are", len ( sol ), "solutions. Offset:", -c[6] + ntt );
            else:
                print ( "There are", len ( sol ), "solutions" );
            print ( "Best solutions:" );
            if len ( sol ) < 3:
                for x in sol:
                    print ( x );
            else:
                for x in range(3):
                    print ( str ( x + 1 ) + ".", soll[x] );

            print ( "View all?");

