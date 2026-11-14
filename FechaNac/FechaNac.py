import sys

print("Programa que dado tu año, mes y dia de nacimiento; imprime la fecha en formato yy/mm/dd.")

while True:
    try:
        year = int(input("Año (1900-2026): "))
        if 1900 <= year <= 2026:
            break
        else:
            print("El año debe estar entre [1900, 2026]")
    except ValueError:
        print("Error: El valor ingresado no es un entero", file = sys.stderr)
    except:
        print("Ha ocurrido un error inesperado", file = sys.stderr)
        
print("""1) Enero
2) Febrero
3) Marzo
4) Abril
5) Mayo
6) Junio
7) Julio
8) Agosto
9) Septiembre
10) Octubre
11) Noviembre
12) Diciembre""")
while True:
    try:
        month = int(input("Mes (1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print("El mes debe estar entre [1, 12]")
    except ValueError:
        print("Error: El valor ingresado no es un entero", file = sys.stderr)
    except:
        print("Ha ocurrido un error inesperado", file = sys.stderr)
     
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    while True:
        try:
            day = int(input("Dia (1-31): "))
            if 1 <= day <= 31:
                break
            else:
                print("El dia debe estar entre [1, 31]")
        except ValueError:
            print("Error: El valor ingresado no es un entero", file = sys.stderr)
        except:
            print("Ha ocurrido un error inesperado", file = sys.stderr)
elif month == 4 or month == 6 or month == 9 or month == 11:
    while True:
        try:
            day = int(input("Dia (1-30): "))
            if 1 <= day <= 30:
                break
            else:
                print("El dia debe estar entre [1, 30]")
        except ValueError:
            print("Error: El valor ingresado no es un entero", file = sys.stderr)
        except:
            print("Ha ocurrido un error inesperado", file = sys.stderr)
else:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        while True:
            try:
                day = int(input("Dia (1-29): "))
                if 1 <= day <= 29:
                    break
                else:
                    print("El dia debe estar entre [1, 29]")
            except ValueError:
                print("Error: El valor ingresado no es un entero", file = sys.stderr)
            except:
                print("Ha ocurrido un error inesperado", file = sys.stderr)
    else:
        while True:
            try:
                day = int(input("Dia (1-28): "))
                if 1 <= day <= 28:
                    break
                else:
                    print("El dia debe estar entre [1, 28]")
            except ValueError:
                print("Error: El valor ingresado no es un entero", file = sys.stderr)
            except:
                print("Ha ocurrido un error inesperado", file = sys.stderr)
                
date = f"{year % 100:02d}{month:02d}{day:02d}"

print("Tu fecha de nacimiento es: " + date)