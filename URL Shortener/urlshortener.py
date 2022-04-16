
import pyshorteners as ps

def shortenURL(url):

    if url == "" or None or False:
        print("Insert a valid link!")
        shortenURL()

    else:
        printURL = ps.Shortener().tinyurl.short(url)
        print("Here is your shorten url!"  + printURL)
        return

shortenURL(input("Insert your url here: "
))

#Just a simple program made in 5 minutes 
#For grasping new Python Libraries
