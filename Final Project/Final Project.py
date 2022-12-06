# This program reads from a CD Catalog and Builds arrays
# Then displays the results as title, artist, country, price, year
# References:
# https://www.geeksforgeeks.org/python-string-replace/


def get_title(filename):
    try:
        filename = open("Catalog.txt", "r")
        title = []
        line1 = filename.readline()
        line1 = filename.readline()
        while True:
            line1 = filename.readline()
            if line1== "":
                break
            else:
                line1 = line1.replace("<TITLE>", "" )
                line1 = line1.replace("</TITLE>", "" )
                line1 = line1.strip()
                
                print(line1)
    except Exception as e:
        print(e)
        
        
def main():
    filename = 'Catalog.txt'
    title = get_title(filename)
    
main()        
        
        
        

