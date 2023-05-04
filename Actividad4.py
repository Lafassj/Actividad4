menu = {
    'Lunes': {
        'Menu del dia': {
            'Arroz con pollo y ensalada de papas': 7.5,
            'Tamal': 2.5,
            'Pesada': 5.5,
        },
        
    },
    'Martes': {
        'Menu del dia': {
            'Arroz chino': 6.0,
            'Arroz con coco': 5.6,
            'Licuado de frutas': 3.0,
        },
    },
    
    'Miercoles' : {
        'Menu del dia' : {
            'Carne guisada con arroz' : 4.5,
            'Cocacola': 1.0,
            'Papas fritas' : 2.0,
        },
    },
    
    'Jueves' : {
        'Menu del dia' : {
            'Bistec a la plancha': 4.25,
            'Ensalada de vegetales' : 2.5,
            'Pepsi de lata' : 1.0,
            },
        },
    'Viernes' : {
        'Menu del dia' : {
            'Pescado frito' : 13.0,
            'Pescado con patacones' : 18.0,
            'Jugo de fresa' : 3.0,
            }
        }
    }
    
# Función para mostrar el menú y solicitar la selección del usuario
def mostrar_menu():
    print('Seleccione el día de la semana:')
    for i, dia in enumerate(menu.keys()):
        print(f'{i+1}. {dia}')
    dia_seleccionado = int(input()) - 1
    dia = list(menu.keys())[dia_seleccionado]
    print(f'\nComidas disponibles para el día {dia}:')
    for tipo_comida, opciones in menu[dia].items():
        print(f'{tipo_comida}:')
        for comida, precio in opciones.items():
            print(f'  {comida} - ${precio}')
    return dia

# Función para seleccionar las comidas y calcular el total a pagar
def realizar_pedido(dia):
    total = 0
    print('\nSeleccione las comidas que desea consumir:')
    for tipo_comida, opciones in menu[dia].items():
        print(f'{tipo_comida}:')
        for comida, precio in opciones.items():
            seleccion = input(f'  {comida} - ${precio} (S/N): ')
            if seleccion.lower() == 's':
                total += precio
    print(f'\nTotal a pagar en caja: ${total}')

# Función principal para ejecutar el programa
def main():
    dia = mostrar_menu()
    realizar_pedido(dia)

if __name__ == '__main__':
    main()
