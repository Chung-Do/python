def to_l33t(string):
    string2 = ""
    for i in string:
        j = ''
        if i == 'a' or i.lower() == 'a': j = '4'
        elif i == 'e' or i == "E": j = '3'
        elif i == 'i' or i == "I": j = '1'
        elif i == 'o' or i == "O" : j = '0'
        elif i == 'u' or i == "U": j = '8'
        else:
             j = i
        string2 += j
    return string2
    

def main():
        string = input()
        print(to_l33t(string))
if __name__ == '__main__':
    main()