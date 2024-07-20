def rgb(r,g,b):
    hex = ''
    for x in (r,g,b):
        y = x%16
        z = int(x/16)
        if y == 10: y = 'A'
        elif y == 11: y = 'B'
        elif y == 12: y = 'C'
        elif y == 13: y = 'D'
        elif y == 14: y = 'E'
        elif y == 15: y = 'F'
        
        if z == 10: z = 'A'
        elif z == 11: z = 'B'
        elif z == 12: z = 'C'
        elif z == 13: z = 'D'
        elif z == 14: z = 'E'
        elif z == 15: z = 'F'
        #print(f'{z}{y}')
        hex = hex + f'{z}{y}'
    
    return '#'+hex

def main():
    red = int(input('r = '))
    green = int(input('g = '))
    blue = int(input('b = '))
    if 0<=red<256 and 0<=green<256 and 0<=blue<256:
        print(rgb(red,green,blue))
    else:
        print('invalid argument')

if __name__ == '__main__':
    main()