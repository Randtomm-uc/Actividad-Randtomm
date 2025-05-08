# requisitos:

# Es hombre

# mayor de 18 años

# nacionalidad chilena


print('Ingrese su género: Hombre = H  Mujer = H  Otro : O')

valida = None

genero = input()

if genero != 'H':

    print('No puede ser enlistado en el servicio militar debido a la conscripción masculina.')

else: 

    print('Ingrese su edad: ')

    while valida != 'VALIDA':

        edad = int(input())

        if edad <= 0:

            valida = 'INVALIDO'

            print('Ingrese una edad válida')

        elif edad > 0 and edad < 18:

            print('No puede ser enlistado en el servicio militar debido a la minoria legal')
            break
        
        else: 

            valida = 'VALIDA'

    if valida == 'VALIDA':
        
        print('Usted esta apto para ejercer el Servicio, se le considerara para el sorteo y notificara de su selección en los proximos dias.')

        print('Caso de tener alguna dificultad médica, debe notificarla al cantón mas cercano a su domicilio.')







