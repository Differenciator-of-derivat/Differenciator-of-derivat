print('--------code by differenciator--------')
l=eval(input('enter any list'))
print(l)
while True:
    print('Select from following')
    print('1','Removal of Value')
    print('2','inserting value')
    print('3','Adding only 1 value')
    print('4','Adding more than 2 value')
    print('5','Length of list')
    print('6','Clearing list')
    print('7','Reversing String')
    print('8','Sorting of list')
    print('9','Counting the times the value occured')
    print('10','Removal of value using pop')
    print('11','Exit from program')
    n=int(input('What do you want to choose'))
    if n==1:
        x=eval(input('enter the value to be removed'))
        l.remove(x)
        print(l)
    if n==2:
        x=eval(input('enter the value to be inserted'))
        y=int(input('enter index of place'))
        l.insert(y,x)
        print(l)
    if n==3:
        x=eval(input('enter the value to be added'))
        l.append(x)
        print(l)
    if n==4:
        x=eval(input('enter the values to be added'))
        l.extend(x)
        print(l)
    if n==5:
        x=len(l)
        print(x)
    if n==6:
        l.clear()
        print(l)
    if n==7:
        l.reverse()
        print(l)
    if n==8:
        print('1','sort')
        print('2','sorting in decending order')
        p=int(input('enter the selected option'))
        if p==1:
            l.sort()
            print(l)
        if p==2:
            x=sorted(l,reverse=True)
            print(x)
    if n==9:
        x=eval(input('value to be counted'))
        y=l.count(x)
        print(y)
    if n==10:
        x=eval(input('enter index of value to be removed'))
        y=l.pop(x)
        print(l)
        print('removed value',y)
    if n==11:
        print('Jaldi waha se hato')
        break


    
print('Teleporting to String Manupulation')
while True:
    s=input('enter any string')
    print('Select from following')
    print('1','Length of string')
    print('2','Capitalizing 1st letter')
    print('3','counting values in string')
    print('4','find index value where sub string occurs')
    print('5','to check whether string is alphanumeric or not')
    print('6','to check whether string is alphabetic or not')
    print('7','to ceck whether values in string are numeric')
    print('8','to check whether all values in string are in lower case or not')
    print('9','to check whether string contain only white spaces')
    print('10','to check whether all values are in upper case or not')
    print('11','to convert all values in lower case')
    print('12','to convert all values in upper case')
    print('13','Removal of white spaces')
    print('14','to check whether string starts with given sub string or not')
    print('15','convert string in title cased version')
    print('16','to check whether string is in title case or not')
    print('17','replaceing selected value in string')
    print('18','Joining costomised character after each value of string')
    print('19','spliting the string based on given character')
    print('20','Spliting the string at occurence of the seperator')
    print('21','Exit from program')
    t=int(input('what do you want to perform'))
    if t==1:
        z=len(s)
        print(z)
    if t==2:
        z=s.capitalize()
        print(z)
    if t==3:
        z=input('enter value to be counted')
        y=int(input('enter starting of range'))
        w=int(input('enter ending of range'))
        x=s.count(z,y,w)
        print(x)
    if t==4:
        print('1','using find()')
        print('2','using index()')
        n=int(input('which method you want to choose'))
        z=input('enter value to be found')
        if n==1:
            x=s.find(z)
            print(x)
        if n==2:
            x=s.index(z)
            print(x)
    if t==5:
        z=s.isalnum()
        print(z)
    if t==6:
        z=s.isalpha()
        print(z)
    if t==7:
        z=s.isdigit()
        print(z)
    if t==8:
        z=s.islower()
        print(z)
    if t==9:
        z=s.isspace()
        print(z)
    if t==10:
        z=s.isupper()
        print(z)
    if t==11:
        z=s.lower()
        print(z)
    if t==12:
        z=s.upper()
        print(z)
    if t==13:
        print('1','To remove only leading white spaces')
        print('2','to remove trailing whitespaces')
        print('3','to remove both leading and trailing white spaces')
        n=int(input('enter the option you want to choose'))
        if n==1:
            x=s.lstrip()
            print([x])
        if n==2:
            y=s.rstrip()
            print([y])
        if n==3:
            z=s.strip()
            print([z])
        else:
            print('enter valid option')
    if t==14:
        x=input('enter substring to continue')
        print('1','To check whether string start with given sub string')
        print('2','To check whether string end with given sub string')
        n=int(input('select option'))
        if n==1:
            z=s.startswith(x)
            print(z)
        if n==2:
            z=s.endswith(x)
            print(z)
        else:
            print('bhai kayde me sahi option select kar')
    if t==15:
        z=s.title()
        print(z)
    if t==16:
        z=s.istitle()
        print(z)
    if t==17:
        x=input('enter substring you want to replace')
        y=input('enter substring you want as relacement')
        z=s.replace(x,y)
        print(z)
    if t==18:
        x=input('enter character you want to see after string iterator')
        print('1','After each character of iterator')
        print('2','after each word in form of list')
        print('3','After each word in form of tuple')
        n=int(input('enter the option'))
        if n==1:
            z=x.join(s)
            print(z)
        if n==2:
            p=input('enter new word')
            q=input('enter new word')
            r=x.join([s,p,q])
            print(r)
        if n==3:
            p=input('enter new word')
            q=input('enter new word')
            r=x.join((s,p,q))
            print(r)
        else:
            print('bhai/behan please sahi option select kro')
    if t==19:
        print('1','split on whitespaces')
        print('2','split using custom character')
        n=int(input('Enter the option'))
        if n==1:
            x=s.split()
            print(x)
        if n==2:
            x=input('enter character on whose basis you want to split the string')
            z=s.split(x)
            print(z)
        else:
            print('enter valid option')
    if t==20:
        p=input('enter letter to be used as seperator')
        z=s.partition(p)
        print(z)
    if t==21:
        print('Thanks for using this program')
        break
print('Teleporting to Calculator')
while True:
    print('Select from following options')
    print('1','')
    print('2','')
    print('3','')
    print('4','')
    print('5','')
    print('6','')
    print('7','')
    print('8','')
    print('9','')
    print('10','')
    print('11','')
    print('12','')
    print('13','')
    print('14','')
    print('15','')
    print('16','')
    
        
        
            

