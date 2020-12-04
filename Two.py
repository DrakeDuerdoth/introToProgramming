
#Assignment Two

#Problem 1

def countLinesWithString(string):
    '''Returns the number of lines the string is in'''
    try:
        infile = open('shakespeare_short.txt','r',encoding='utf-8')
        lstStringTally = []
        string = string.lower()
        for line in infile:
            line = line.lower()
            if string in line:
               lstStringTally.append(string)
        infile.close()
        return(lstStringTally.count(string))
    except (FileNotFoundError):
        print('Sorry was unable to open the file.')

#Problem 2

def getMonthlySales(name,month):
    '''Returns the employee's sales for that month'''
    try:
        infile = open('widget_sales_with_id.csv','r')
        name = name.lower()
        for nameAndSales in infile:
            nameAndSales = nameAndSales.replace('\n','')
            nameAndSales = nameAndSales.lower()
            nameAndSales = nameAndSales.split(',')
            if name in nameAndSales and month in range(1,13):
               return nameAndSales[month]
        infile.close()
    except (NameError):
        None



