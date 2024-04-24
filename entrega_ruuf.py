def ruuf(ruuf_x, ruuf_y, panel_x, panel_y):
    if ruuf_x >= 1 and ruuf_y >= 1 and panel_x >= 1 and panel_y >= 1:
        if panel_x > ruuf_x and panel_y > ruuf_y:
            print('Caben 0')
        else:
            ocupacion_mixta_horizontal = (ruuf_x // panel_x) * (ruuf_y // panel_y) + (((ruuf_y % panel_y)//panel_x)*(ruuf_x//panel_y))
            ocupacion_mixta_vertical = (ruuf_y // panel_x) * (ruuf_x // panel_y) + (((ruuf_x % panel_y)//panel_x)*(ruuf_y//panel_y))
            max_ocupacion = max(ocupacion_mixta_horizontal, ocupacion_mixta_vertical)
            print(f'Caben {max_ocupacion}')
    else:
        print("Las dimensiones deben ser mayores o iguales a uno.")

x = 3
y = 5
a = 1
b = 2
ruuf(x, y, a, b)