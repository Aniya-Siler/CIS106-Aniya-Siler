# This program reads from a CD Catalog and Builds arrays
# Then displays the results as title, artist, country, price, year
# References:
# https://www.geeksforgeeks.org/python-string-replace/
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-7/


def get_common(filename):
    try:
        filename = open("plant_catalog.xml", "r")
        c = []
        while True:
            line1 = filename.readline()
            if line1== "" :
                break
            if "<COMMON>" in line1:
                line1 = line1.strip()
                line1 = line1.replace('<COMMON>', '')
                line1 = line1.replace('</COMMON>', '')
                c.append(line1)
    except Exception as e:
        print(e)
    return c


def get_botanical(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        b = []
        while True:
            line2 = filename.readline()
            if line2== "" :
                break
            
            if "<BOTANICAL>" in line2:
                line2 = line2.strip()
                line2 = line2.replace('<BOTANICAL>', '')
                line2 = line2.replace('</BOTANICAL>', '')
                b.append(line2)
    except Exception as e:
        print(e)
    return b


def get_zone(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        z = []
        while True:
            line3 = filename.readline( )
            if line3== "":
                break
            
            if "<ZONE>" in line3:
                line3 = line3.strip()
                line3 = line3.replace('<ZONE>', '')
                line3 = line3.replace('</ZONE>', '')
                z.append(line3)
    except Exception as e:
        print(e)
    return z


def get_price(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        p = []
        while True:
            line4 = filename.readline( )
            if line4== "":
                break
            
            if "<PRICE>" in line4:
                line4 = line4.strip()
                line4 = line4.replace('<PRICE>', '')
                line4 = line4.replace('</PRICE>', '')
                line4 = line4.replace('$', '')
                p.append(float(line4))
    except Exception as e:
        print(e)
    return p


def get_light(filename):
    try:
        filename = open('plant_catalog.xml', 'r')
        l = []
        while True:
            line5 = filename.readline()
            if line5== "":
                break
            
            if "<LIGHT>" in line5:
                line5 = line5.strip( )
                line5 = line5.replace('<LIGHT>', '')
                line5 = line5.replace('</LIGHT>', '')
                l.append(line5)
    except Exception as e:
        print(e)
    return l


def get_a(p):
    total = 0
    for index in range(len(p)):
        total += p[index]
    a = total /len(p)
    return a


def get_i(c):
    i = len(c)
    return i


def display_results(c, b, z, l, p, a, i):
    for j in range(36):
        print(c[j] + '(' + b[j] + ')' + ' - ' + z[j] + ' - ' + l[j] + ' - ' + '$' + str(p[j]))
    print(str(i) + ' items' + ' - ' + '$' + str(a))
        
        
def main():
    filename = 'plant_catalog.xml'
    c = get_common(filename)
    b = get_botanical(filename)
    z = get_zone(filename)
    p = get_price(filename)
    l = get_light(filename)
    a = get_a(p)
    i = get_i(c)
    display_results(c, b, z, l, p, a, i)
    
    
main()        
        
        
        


