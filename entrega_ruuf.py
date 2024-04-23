def ruuf(ruuf_x, ruuf_y ,panel_x, panel_y):
    if ruuf_x >=1 and ruuf_y >=1 and panel_x >=1 and panel_y >=1:
        ocupacion_vertical = (ruuf_x // panel_y) * (ruuf_y // panel_x)
        ocupacion_horizontal = (ruuf_x // panel_x) * (ruuf_y // panel_y)
        return max(ocupacion_horizontal, ocupacion_vertical)
    else:
        print("Las dimensiones deben ser mayores o iguales a uno.")

x = 3
y = 5
a = 1
b = 2

print(ruuf(x,y,a,b))