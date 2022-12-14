# This program reads from a CD Catalog and Builds arrays
# Then displays the results as title, artist, country, price, year
# References:
# https://www.geeksforgeeks.org/python-string-replace/
# 


def get_common(filename):
    try:
        filename = open("plant_catalog.xml","r")
        commons = []
        while True:
            line1 = filename.readline()
            if line1== "":
                break
            if "<COMMON>" in line1:
                line1 = line1.strip()
                print(line1)
                line1 = line1.replace('<COMMON>', '' )
                line1 = line1.replace('</COMMON>', '' )
                commons.append(line1)
    except Exception as e:
        print(e)
    return line1


def get_botanical(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        botanicals = []
        while True:
            line2 = filename.readline()
            if line2== "":
                break
            
            if "<BOTANICAL>" in line2:
                line2 = line2.strip()
                print(line2)
                line2 = line2.replace('<BOTANICAL>', '' )
                line2 = line2.replace('</BOTANICAL>', '' )
                botanicals.append(line2)
    except Exception as e:
        print(e)
    return line2

def get_zone(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        zones = []
        while True:
            line3 = filename.readline()
            if line3== "":
                break
            
            if "<ZONE>" in line3:
                line3 = line3.strip()
                print(line3)
                line3 = line3.replace('<ZONE>', '' )
                line3 = line3.replace('</ZONE>', '' )
                line3 = line3.replace('Annual', '' )
                zones.append(line3)
    except Exception as e:
        print(e)
    return line3


def get_price(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        prices = []
        while True:
            line4 = filename.readline()
            if line4== "":
                break
            
            if "<PRICE>" in line4:
                line4 = line4.strip()
                print(line4)
                line4 = line4.replace('<PRICE>', '' )
                line4 = line4.replace('</PRICE>', '' )
                line4 = line4.replace('$', '')
                prices.append(float(line4))
    except Exception as e:
        print(e)
    return line4


def get_light(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        lights = []
        while True:
            line5 = filename.readline()
            if line5== "":
                break
            
            if "<BOTANICAL>" in line5:
                line5 = line5.strip()
                print(line5)
                line5 = line5.replace('<BOTANICAL>', '' )
                line5 = line5.replace('</BOTANICAL>', '' )
                lights.append(line5)
    except Exception as e:
        print(e)
    return line5


def get_average(prices):
    total = 0
    for index in range(len(prices)):
        total += prices[index]
    average = total /len(prices)
    return average

def get_items(commons):
    items = len(commons)
    return items

        
        
def main():
    filename = 'plant_catalog.xml'
    commons = get_common(filename)
    botanicals = get_botanical(filename)
    zones = get_zone(filename)
    prices = get_price(filename)
    lights = get_light(filename)
    average = get_average(prices)
    items = get_items(commons)
    
    
main()        
        
        
        
