import urllib

while True:
    host = raw_input("Enter Website Target: ")
    if "http://" not in host:
        host = "http://" + host
    try:
        site = urllib.urlopen(host)

        for key , value in site.headers.items():

            print key + ":" + value
    except:
        print "check your internet connection or enter a valid url!"