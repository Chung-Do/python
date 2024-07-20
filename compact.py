def compact(array):
    for i in array:
        if i == "None":
            array.remove(i)
    return array

def main():
    a = input().split()    
    if a is not None: 
        x = compact(a)
        print (x)
   
    

if __name__ == '__main__':
    main()