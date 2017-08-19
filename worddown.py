def main(url):
    from urllib import request
    try:
        f = request.urlopen(url);
        fd = f.read()
        f.close()
        try:
            f = open ( url.split("/")[len(url.split("/"))-1], "wb" )
            f.write(fd);
            f.close()
        except:
            print ( "Warn: Unable to write to:", url.split("/")[len(url.split("/"))-1] )
            return fd
    except:
        print ( "Error: Unable to download file..." )

    try: return fd;
    except: return None;
    
    

