f = open("24.txt")
abc = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0,
"O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "X": 0, "Y": 0, "Z": 0, "U": 0, "W": 0, "V": 0}
string = f.read()
print(string)

for i in range(len(string)):
    if string[i] == "E":
        abc[string[i+1]] += 1
maxi = 0
maxistr = ""

for i in abc:
    if int(abc.get(i)) > maxi:
        maxi = abc.get(i)
        maxistr = i
        
print(maxi)
print(maxistr)
