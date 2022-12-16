# This program reads from a CD Catalog and Builds arrays
# Then displays the results as title, artist, country, price, year
# References:
# https://www.geeksforgeeks.org/python-string-replace/
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-7/


def get_common(filename):
    try:
        filename = open("plant_catalog.xml", "r")
        commons = []
        while True:
            line1 = filename.readline()
            if line1== "" :
                break
            if "<COMMON>" in line1:
                line1 = line1.strip()
                line1 = line1.replace('<COMMON>', '')
                line1 = line1.replace('</COMMON>', '')
                commons.append(line1)
    except Exception as e:
        print(e)
    return commons


def get_botanical(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        botanicals = []
        while True:
            line2 = filename.readline()
            if line2== "" :
                break
            
            if "<BOTANICAL>" in line2:
                line2 = line2.strip()
                line2 = line2.replace('<BOTANICAL>', '')
                line2 = line2.replace('</BOTANICAL>', '')
                botanicals.append(line2)
    except Exception as e:
        print(e)
    return botanicals


def get_zone(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        zones = []
        while True:
            line3 = filename.readline( )
            if line3== "":
                break
            
            if "<ZONE>" in line3:
                line3 = line3.strip()
                line3 = line3.replace('<ZONE>', '')
                line3 = line3.replace('</ZONE>', '')
                zones.append(line3)
    except Exception as e:
        print(e)
    return zones


def get_price(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        prices = []
        while True:
            line4 = filename.readline( )
            if line4== "":
                break
            
            if "<PRICE>" in line4:
                line4 = line4.strip()
                line4 = line4.replace('<PRICE>', '')
                line4 = line4.replace('</PRICE>', '')
                line4 = line4.replace('$', '')
                prices.append(float(line4))
    except Exception as e:
        print(e)
    return prices


def get_light(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        lights = []
        while True:
            line5 = filename.readline()
            if line5== "":
                break
            
            if "<LIGHT>" in line5:
                line5 = line5.strip()
                line5 = line5.replace('<LIGHT>', '')
                line5 = line5.replace('</LIGHT>', '')
                lights.append(line5)
    except Exception as e:
        print(e)
    return lights


def get_average(prices):
    total = 0
    for index in range(len(prices)):
        total += prices[index]
    average = total /len(prices)
    average = round(average, 2)
    return average

def get_items(commons):
    items = len(commons)
    return items

def display_results(commons, botanicals, zones, lights, prices, average, items):
    for j in range(36):
        print(commons[j] + '(' + botanicals[j] + ')' + ' - ' + zones[j] + ' - ' + lights[j] + ' - ' + '$' + str(prices[j]))
    print(str(items) + ' items' + ' - ' + '$' + str(average))
        
        
def main():
    filename = 'plant_catalog.xml'
    commons = get_common(filename)
    botanicals = get_botanical(filename)
    zones = get_zone(filename)
    prices = get_price(filename)
    lights = get_light(filename)
    average = get_average(prices)
    items = get_items(commons)
    display_results(commons, botanicals, zones, lights, prices, average, items)
    
    
main()        
        
        
        
