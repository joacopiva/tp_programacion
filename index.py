## Funciones que faltan: [egreso (se empareja con el ID) (PALO)], [funcion de registrar nuevo usuario y dar de baja (PALO)], [ingreso de camiones, ingreso de internos(MATEO)], [mostrar las listas de empleados, camiones (EITO)]
#
from datetime import datetime

internos_registrados = []
externos_registrados = []
camiones_registrados = []


#Lista base de empleados
lista_empleados = [[202500,'Folgado','Mateo','Ford Fiesta','asd-123'], [202501,'Messi','Lionel','toyota hilux','oea-123']]


#Lista para registrar lo que se necesita para producir la mezcla
lista_de_produccion = []

# Materiales necesarios para producir 1 tonelada de mezcla asfáltica (en kg)
una_tonelada = [['Piedra 6/20', 300], ['Piedra 6/12', 250], ['Arena 0/6', 200], ['Arena 0/3', 100], ['Cemento asfáltico ca30', 50], ['Cemento asfáltico am3', 60]]

# Costos por tonelada de cada material
costos_de_materiales = [['Piedra 6/20', 12800], ['Piedra 6/12', 16540], ['Arena 0/6', 5500], ['Arena 0/3', 8340], ['Cemento asfáltico ca30', 1078000], ['Cemento asfáltico am3', 1697000]]

# Stock actual disponible en la planta
lista_de_materiales = [['Piedra 6/20', 6000],['Piedra 6/12', 500], ['Arena 0/6', 400], ['Arena 0/3', 150], ['Cemento asfáltico ca30', 30], ['Cemento asfáltico am3', 1200]]

# Valores mínimos que deben mantenerse en el stock para cada material
stocks_minimos = [['Piedra 6/20', 4000], ['Piedra 6/12', 3500], ['Arena 0/6', 3000], ['Arena 0/3', 1800],['Cemento asfáltico ca30', 1800], ['Cemento asfáltico am3', 500]]

#############################################################################################
#############################################################################################
def empleados_ingreso():
    empleado = {}

    id_empleado = int(input("Ingrese el ID del empleado: "))

    #Verificamos si existe un empleado con esa ID
    for registro in lista_empleados:
      if registro[0] == id_empleado:
        empleado["id_empleado"]= id_empleado
        empleado["nombre"] = str(input("Ingrese el nombre del empleado: "))
        empleado["apellido"] = str(input("Ingrese el apellido del empleado: "))
        empleado["modelo_de_auto"] = str(input("Ingrese el modelo del auto: "))
        empleado["patente"] = str(input("Ingrese la patente del auto: "))

        empleado["hora_entrada"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        internos_registrados.append(empleado) #se crea una lista de diccionarios, los cuales se visualizan aparte
        print("Ingreso cargado correctamente")
        return empleado
   
    print("No se encontro un empleado con ese ID. \n")
    return None
   
def empleados_egreso():
    print("\nRegistro de salida del predio\n")

    #Creo una variable la cual contiene la ID del empleado que se registro antes
    id_buscar = int(input("Ingrese el ID del empleado: "))

    #Recorro la lista de directorios y en el "if" comparo la variable con las ID que se registraron hasta encontrar una coincidencia.
    for empleado in internos_registrados:
        if empleado["id_empleado"] == id_buscar:
            empleado["hora_salida"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            print("salida registrada correctamente. \n")
            return empleado
    print("No se encontro un empleado con ese ID. \n")
    return None
#############################################################################################
#############################################################################################
def registrar_empleado():
# Agrega un nuevo empleado a la lista
  id_empleado = int(input("Ingrese el ID del empleado: "))

  for registro in lista_empleados:
    if registro[0] == id_empleado:
      print("Esta ID ya fue registrada, por favor intentelo nuevamente")
      return #se sale sin agregar nada


  apellido = str(input("Ingrese el apellido del empleado: "))
  nombre = str(input("Ingrese el nombre del empleado: ")) 
  vehiculo = str(input("Ingrese el vehiculo que se le asignara al empleado: "))
  patente = str(input("Ingrese la patente del vehiculo: "))

  info_empleado = [id_empleado, apellido, nombre, vehiculo, patente]
  lista_empleados.append(info_empleado)
  print("Empleado registrado correctamente.")
  print(lista_empleados)

#############################################################################################
def baja_empleado():
    viejo_empleado = int(input("Ingrese el ID del empleado que desea dar de baja: "))

    for registro in lista_empleados:
        if registro[0] == viejo_empleado:
            lista_empleados.remove(registro)  
            print("Se dio de baja el empleado correctamente.")
            return

    print("El empleado no se encuentra registrado.")
    
#############################################################################################
#############################################################################################
def ingreso_camiones():
    camionero = {}

    #Registro la ID del camionero, los datos del camion y valido el Numero de remito
    camionero["id_camionero"] = int(input("Ingrese el ID del camionero: "))
    camionero["modelo_camion"] = str(input("Ingrese el modelo del camion: "))
    camionero["patente_camion"] = str(input("Ingrese la patente del camion: "))
    camionero["remito"] = int(input("Ingrese el numero de remito: "))
    camionero["material"] = str(input("Ingrese el nombre del material que trae el camion: "))
    camionero["cantidad_de_material"] = int(input("Ingrese la cantidad de material que trajo: "))

    #se carga la hora de forma automatica de cuando ingresa el camion
    camionero["hora_entrada"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    camiones_registrados.append(camionero) #se crea una lista de diccionarios, los cuales se visualizan aparte
    return

def egreso_camiones():
    print("\nRegistro de salida del predio\n")

    #Creo una variable la cual contiene la ID del camionero que se registro antes
    id_buscar = int(input("Ingrese el ID del camionero: "))

    #Recorro la lista de directorios y en el "if" comparo la variable con las ID que se registraron hasta encontrar una coincidencia.
    for camionero in camiones_registrados:
        if camionero["id_camionero"] == id_buscar:
            camionero["hora_salida"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            print("salida registrada correctamente. \n")
            return camionero
    print("No se encontro un camionero con ese ID. \n")
    return None

def stock_planta():
    print("\n--- Modificación Manual de Stock ---")
    print("Stock Actual:")

    for i in range(len(lista_de_materiales)):
        nombre_material = lista_de_materiales[i][0]
        cantidad = lista_de_materiales[i][1]
        print(i + 1, "- ", nombre_material, ": ", cantidad, " Kg")

    opcion_material = int(input("\nSeleccione el número del material que desea modificar: "))
    if 1 <= opcion_material <= len(lista_de_materiales):
        indice_a_modificar = opcion_material - 1
        nombre_seleccionado = lista_de_materiales[indice_a_modificar][0]
        cantidad_actual = lista_de_materiales[indice_a_modificar][1]

        print("Material seleccionado:", nombre_seleccionado)
        print("Cantidad actual:", cantidad_actual, "Kg")

        nueva_cantidad = int(input("Ingrese la nueva cantidad para este material: "))
        lista_de_materiales[indice_a_modificar][1] += nueva_cantidad
        print("\n¡Stock actualizado correctamente!\n")
    else:
        print("Error: Opción no válida. Por favor, seleccione un número de la lista.")
    return



#############################################################################################
#############################################################################################
def externo_ingreso():
    externo = {}

    #Registro la informacion del externo
    externo["DNI"] = int(input("Ingrese el DNI de la persona: "))
    externo["Nombre"] = str(input("Ingrese el nombre: "))
    externo["Apellido"] = str(input("Ingrese el apellido: "))
    externo["modelo"] = str(input("Ingrese el modelo del vehiculo: "))
    externo["patente"] = str(input("Ingrese la patente del vehiculo: "))

    #se carga la hora de forma automatica
    externo["hora_entrada"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    externos_registrados.append(externo) #se crea una lista de diccionarios, los cuales se visualizan aparte
    return


def externo_egreso():
  print("\nRegistro de salida del predio\n")
  #Creo una variable la cual contiene la ID del camionero que se registro antes
  dni_buscar = int(input("Ingrese el DNI de la persona: "))
#Recorro la lista de directorios y en el "if" comparo la variable con las ID que se registraron hasta encontrar una coincidencia.
  for externo in externos_registrados:
      if externo["DNI"] == dni_buscar:
          externo["hora_salida"] = datetime.now().strftime("%Y-%m-%d %H:%M")
          print("salida registrada correctamente. \n")
          return externo
  print("No se encontro DNI. \n")
  return None


#############################################################################################
#############################################################################################

def menu_internos():
  opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Salir \nSeleccione una opcion: "))
  while opcion != 3:
    if opcion == 1:
     empleados_ingreso()
    elif opcion == 2:
      empleados_egreso()
    else:
      print("Opcion no valida")
    opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Salir \nSeleccione una opcion: "))
#############################
def menu_externos():
  opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Salir \nSeleccione una opcion: "))

  while opcion != 3:
    if opcion == 1:
     externo_ingreso()
    elif opcion == 2:
      externo_egreso()
    else:
      print("Opcion no valida")
    opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Salir \nSeleccione una opcion: "))


#####################################################################
def menu_camiones():
  opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Modificar stock \n4.Salir \nSeleccione una opcion: "))
  while opcion != 4:
    if opcion == 1:
        ingreso_camiones()
    elif opcion == 2:
        egreso_camiones()
    elif opcion == 3:
        stock_planta()
    else:
      print("Opcion no valida")
    opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Modificar stock \n4.Salir \nSeleccione una opcion: "))
  return


def control_stock(lista_de_materiales_actual, stocks_minimos_lista):
    alertas = []
    # Recorre todos los materiales del stock actual
    for material_actual, cantidad_actual in lista_de_materiales_actual:
        encontrado = False
        indice_minimos = 0
        # Busca en la lista de mínimos el mismo material
        while indice_minimos < len(stocks_minimos_lista) and not encontrado:
            material_minimo, cantidad_minima = stocks_minimos_lista[indice_minimos]
            if material_actual == material_minimo:
                encontrado = True
                if cantidad_actual <= cantidad_minima:
                    alertas.append("¡Atención! Es necesario reponer: " + material_actual)
            indice_minimos += 1
    return alertas


def calculo_materiales_x_toneladas():
# Calcula materiales y costos para una cantidad de toneladas ingresada

    produccion = int(input("Ingrese la cantidad de toneladas que desea producir: "))
    materiales_necesarios = []
    costos_calculados = []
    costo_total_final = 0

    for i in range(len(una_tonelada)):
        nombre_material = una_tonelada[i][0]
        cantidad_por_tonelada = una_tonelada[i][1]
        cantidad_total = cantidad_por_tonelada * produccion

        materiales_necesarios.append([nombre_material, cantidad_total])
    for i in range(len(costos_de_materiales)):
        nombre_material = costos_de_materiales[i][0]
        valor = costos_de_materiales[i][1]
        valor_total = valor * produccion
        costos_calculados.append([nombre_material, valor_total])
        costo_total_final += valor_total
        # Muestra informe
        print("\n--- INFORME DE PRODUCCIÓN PARA", produccion, "TONELADAS ---")
        print("\nMateriales necesarios (Nombre, Cantidad en Kg):")
        print(materiales_necesarios)
        print("\nCostos por material (Nombre, Costo Total):")
        print(costos_calculados)
        print("\nCosto Total Final de la Producción:", costo_total_final)
        print("----------------------------------------------------")
    return

def alertas_stock_minimo():

# Muestra stock actual y genera alertas si hay materiales por debajo del mínimo
    avisos_reposicion = control_stock(lista_de_materiales, stocks_minimos)
    print("\nStock de materiales disponible\n")
    print(lista_de_materiales)
    if avisos_reposicion:
        print("--- AVISO DE REPOSICIÓN DE MATERIALES ---")
        for aviso in avisos_reposicion:
            print(aviso)
    else:
        print("Todos los materiales tienen stock suficiente.")
    return

def mostrar_listas():
    
    # Mostrar listas de empleados y camiones
    print("\n--- LISTA DE EMPLEADOS ---")
    if lista_empleados:
        for empleado in lista_empleados:
            print(f"ID: {empleado[0]} | Apellido: {empleado[1]} | Nombre: {empleado[2]} | Vehículo: {empleado[3]} | Patente: {empleado[4]}")
    else:
        print("No hay empleados registrados.")

    print("\n--- LISTA DE CAMIONES ---")
    if camiones_registrados:
        for camion in camiones_registrados:
            print(f"ID Camionero: {camion['id_camionero']} | Modelo: {camion['modelo_camion']} | Patente: {camion['patente_camion']} | Remito: {camion['remito']} | Material: {camion['material']} | Cantidad: {camion['cantidad_de_material']} kg | Hora ingreso: {camion['hora_entrada']}" + (f" | Hora salida: {camion.get('hora_salida')}" if "hora_salida" in camion else ""))
    else:
        print("No hay camiones registrados.")
    return


def produccion():
    opcion1 = int(input("\n1. 'tip' materiales necesarios para la produccion \n2. control de produccion \n3. stock de materiales disponible \n4. Salir\n - Seleccione una opcion: "))

    while opcion1 != 4:
        if opcion1 == 1:

            # Muestra la receta para producir 1 tonelada de mezcla y los costos
            print("\nPara producir solo 1 tonelada (1000kg) de mezcla asfaltica se necesitan los siguientes materiales en estas cantidades.\n")
            print(una_tonelada)
            print("\nY los costos de los materiales son:\n")
            print(costos_de_materiales)

        elif opcion1 == 2:
            calculo_materiales_x_toneladas()
        elif opcion1 == 3:
            alertas_stock_minimo()
        else:
            print("Opción incorrecta, por favor inténtelo nuevamente.")
        opcion1 = int(input("\n1. 'tip' materiales necesarios para la produccion \n2. control de produccion \n3. stock de materiales disponible \n4. Salir\n - Seleccione una opcion:"))
    else:
        print("Volviendo al menu principal")
    return

################### MENU INICIAL ################################
print("\t\tBIENVENIDO")
opcion = int(input("\n1.Ingresar empleado \n2.Ingresar Externo \n3.Ingresar camion \n4.Visualizar stock \n5.Visualizar ingresos \n6.Registrar nuevo empleado \n7.Dar de baja empleado \n8.Mostrar listas de empleados y camiones \n9.Terminar programa \nSeleccione una opcion para empezar: "))

while opcion != 9:

  while opcion < 1 or opcion > 9: # Corrected condition to validate input for main menu
    print("Opcion no valida")
    opcion = int(input("\n1.Ingresar empleado \n2.Ingresar Externo \n3.Ingresar camion \n4.Visualizar stock \n5.Visualizar ingresos \n6.Registrar nuevo empleado \n7.Dar de baja empleado \n8.Mostrar listas de empleados y camiones \n9.Terminar programa \nSeleccione una opcion para empezar: "))

  if opcion == 1:
    menu_internos()

  elif opcion == 2:
    menu_externos()

  elif opcion == 3:
    menu_camiones()

  elif opcion == 4:
    produccion()

  elif opcion == 5:

    print("\nInternos registrados",internos_registrados,"\n")
    print("\nCamiones registrados",camiones_registrados, "\n")
    print("\nExternos registrados",externos_registrados)
  elif opcion == 6:
    registrar_empleado()
    
  elif opcion == 7:
    baja_empleado()
  
  elif opcion == 8:
    mostrar_listas()

  else:
    print("Programa terminado.")

  opcion = int(input("\n1.Ingresar empleado \n2.Ingresar Externo \n3.Ingresar camion \n4.Visualizar stock \n5.Visualizar ingresos \n6.Registrar nuevo empleado \n7.Dar de baja empleado \n8.Mostrar listas de empleados y camiones \n9.Terminar programa \nSeleccione una opcion para empezar: "))

print("Programa terminado.")