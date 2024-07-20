def right_triangle(a,b,c):
    #y = False
    #if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
        #y = True
    return (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a)
            #y

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if a<0 or b<0 or c<0:
        print('False')
    else:
        x = right_triangle(a,b,c)
        print(x)

if __name__ == '__main__':
    main()