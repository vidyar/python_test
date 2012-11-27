def sort(data,test=0):
    for row in data:
        pos=0
        name=row[1].replace('&nbsp','')
        answer=row[2].replace('&nbsp','')+row[3].replace('&nbsp','')
        if test == 1:
            if answer=='Y':
                print name,"is comming"
            elif answer=='N':
                print name,"is not comming"
            else:
                print name,"havent replied"
            

                
        
        

    
    