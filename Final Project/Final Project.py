# This program reads from a CD Catalog and Builds arrays
# Then displays the results as title, artist, country, price, year
# References:
# https://www.geeksforgeeks.org/python-string-replace/
# 


def get_title(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        titles = []
        line1 = filename.readline()
        line1 = filename.readline()
        line1 = filename.readline()
        while True:
            line1 = filename.readline()
            if line1== "":
                break
            else:
                if line1 == '<COMMON>' or line1 == '</COMMON>':
                    print(line1)
                    line1 = line1.strip()
                    line1 = line1.replace('<COMMON>', '' )
                    line1 = line1.replace('</COMMON>', '' )
                    title = line1
                    titles.append(title)
    except Exception as e:
        print(e)
        
        
def main():
    filename = 'plant_catalog.xml'
    title = get_title(filename)
    
main()        
        
        
        
