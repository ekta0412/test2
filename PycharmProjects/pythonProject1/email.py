# email validation

#number of characters more than 6--
#first letter alpha--
#. -4 or -3--
#no uppercase
#@ . _
#no space--

#ektadutt@gmail.com #

a = input()
k,b,i=0,0,0
print("Email u entered is:", a)
if len(a) >= 6:
    if a[0].isalpha():
        if (a[-4] == ".") ^ (a[-3] == "."):
            for i in a:
                if i.isspace():
                    k = 1
                elif i.isalpha():
                    if i == i.upper():
                        b = 1
                elif i=="@" or i=="." or i=="_" :
                    continue
                elif i== i.isdigit() :
                    continue
            if k == 1 or b == 1:
                print("wrong email 4")
            else:
                print("right")

        else:
            print("wrong entry 3")
    else:
        print("wrong entry 2")
else:
    print("wrong entry1")
