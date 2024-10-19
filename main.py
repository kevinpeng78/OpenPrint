from printer import printer


p = printer(10.4, 20, 2, 0, 'PLA')
'''
p.move(0, 0, .28, 0, 2000, False, False)
p.move(0, 100, 0, .5, 2000)
p.move(10, 0, p.zPos, 0, 2000, False, False)
p.move(0, 100, 0, .5, 2000)
p.move(20, 0, p.zPos, 0, 2000, False, False)
p.move(0, 100, 0, .5, 2000)
p.move(30, 0, p.zPos, 0, 2000, False, False)
p.move(0, 100, 0, .5, 2000)
p.move(40, 0, p.zPos, 0, 2000, False, False)
p.move(0, 100, 0, .5, 2000)
p.move(50, 0, p.zPos, 0, 2000, False, False)
p.move(0, 100, 0, .5, 2000)
p.print()
'''

#script to print stairs
#n - connected lines
p.move(0, 0, .2, 0, 0, False)
def ssp(n_lines, n_layers, len, wid, L, e):
    o_lines = n_lines
    for layer in range(0, n_layers):
        if (layer % 2 == 0):
            d = 1
        else:
            d = -1
        for line in range(0, n_lines):
            if (line % 2 == 0):
                c = 1
            else:
                c = -1 
            if (o_lines % 2 == 0 and layer % 2 == 1):
                p.move(0, -len * c * d, 0, e, 2000)
            else:
                p.move(0, len * c * d, 0, e, 2000)
            if (line != (n_lines - 1)):
                p.move(wid * d, 0, 0, e, 2000)
        p.move(0, 0, L, 0, 2000)
        if (layer % 2 == 1 and layer != n_layers - 1):
            p.move(wid, -len, 0, 0, 2000)
        n_lines = n_lines - 1
p.move(15, 10, .2, 0, 2000, False)

#20 layers
#increase length of line

for i in range(0, 5):
    ssp(20, 20, 20, 1, .05, .05)
    if i != 4:
        p.move(30, -20, -p.zPos + .2, 0, 2000)

p.move(15, 70, .2, 0, 2000, False)
for i in range(0, 5):
    ssp(20, 20, 20, 1, .10, .05)
    if i != 4:
        p.move(30, -20, -p.zPos + .2, 0, 2000)
p.move(15, 140, .2, 0, 2000, False)
for i in range (0, 5):
    ssp(20, 20, 20, 1, .15, .05)
    if i != 4:
        p.move(30, -20, -p.zPos + .2, 0, 2000)
p.move(15, 210, .2, 0, 2000, False )
for i in range (0, 5):
    ssp(20, 20, 20, 1, .20, .05)
    if i != 4:
        p.move(30, -20, -p.zPos + .2, 0, 2000)
p.print()





        
    
    
