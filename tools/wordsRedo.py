def engine(fd):
    fd = fd.decode();fd = fd.split("\n");new = [];mins = 4;maxs = 9;
    for x in fd:
        if len ( x ) >= mins and len ( x ) <= maxs: new.append(str( x ))
    s = "";
    for x in new: s += str ( x ) + "\n";
    fp = "words.txt";f = open ( fp, "wb" );f.write(s[0:len(s)-1].encode());f.close();print ( "Old size: " , len ( fd ) );print ( "New size: " , len ( new ) );print ( "Thrown  : " , len ( fd ) - len ( new ) );return s[0:len(s)-1];
