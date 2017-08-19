import time, itertools, wrds;
wsetComp = len(wrds.wset) != 0

def getFromInternet(resourceURL):
    import urllib;
    from urllib import request;
    f = request.urlopen(resourceURL);
    fd = f.read();
    f.close();
    del f;
    return fd

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
    print ( menu(wsetComp) );
    c = input("1/2> ")
    if c == "1":
        print ( "Maths round... (Press Ctr+c to go back)" );
        while True:
            try:
                c = [];
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
        start = time.time();
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

        print ( "Calculation took:", str( round(time.time() - start, 2) ) + "s" );
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

            nn = False;
            while True:
                print ( "View all? (or number of solutions to view)");
                try:
                    c = input ( "y/n/0> ").lower();
                    try:
                        c = int ( c );
                        nn = True;
                    except:
                        c = str ( c )[0];
                        
                    if c > len( soll ) and nn:
                        nn = False;
                        print ( c, "is bigger than", str ( len( soll ) ) + ". Do you expect the extra solutions to jump out of thin air?" );
                    else:
                        break;
                except TypeError:
                    break;
                except:
                    pass;
                
            if nn:
                for x in range(c): print ( str ( x + 1 ) + ".", soll[x] );
            elif c == "y":
                for x in range( len( soll ) ): print ( str ( x + 1 ) + ".", soll[x] );
            else:
                pass;
            
    elif c == "2" and wsetComp:            
        wrds.main()

