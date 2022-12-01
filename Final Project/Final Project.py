# This program reads from a CD Catalog and Builds arrays
# Then displays the results as title, artist, country, price, year
# References:
#


def get_title(filename):
    filename = open("Catalog.txt","r")
    title = []
    line1 = filename.readline()
    line1 = filename.readline()
    while True:
        line1 = filename.readline()
        if line1== "":
            break
        else:
            line1 = line1.strip()
def main():
    filename = 'Catalog.txt'
    title = get_title(filename)
    
main()        
        
        
        

