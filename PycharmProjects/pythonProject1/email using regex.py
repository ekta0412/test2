import re
print("Plz enter email")
a = input()
email ="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
if re.search(email, a):
    print("Right one")
else:
    print("Wrong")

# ^ searches the email that it shud start with alphabet a-z
# \ allows . and _
# ? allows . and _ only once
# $ searches character at place from left to right