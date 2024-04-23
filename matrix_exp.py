x = 3
y = 5
a = 1
b = 2

row = 0
column = 0
c = 0
panel_e1 = a
panel_e2 = b

while row < x and column < y:
    row += panel_e1
    column += panel_e2
    c += 1
    print(row,column)
print(c)
     