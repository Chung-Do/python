import re
x = ""
while x != "quit":
    x = input()
    #line2
    if (len(x)==6):
        print("my length is 6")
    #line3
    if(x[0] in "aeiuo" and len(x) >=4):
        for i in range(4):
         print(x[1] + x[2] + x[3] )
    #line4
    if(x in ["ls","cat","rev","pwd"]):
        print(f"i know the command {x} !!")
    #line5
    if (x.startswith("0") and not x.endswith("9")):
        c = re.findall(r'\d', x)
        for i in c:
            print(i)
        