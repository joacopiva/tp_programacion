## Funciones que faltan: [egreso (se empareja con el ID)], [funcion de registrar nuevo usuario y dar de baja (PALO)], [ingreso de camiones (), ingreso de internos], [mostrar las listas de empleados, camiones (EITO)]
## hola















from pickle import TRUE
from datetime import datetime

ingreso_internos = []
ingreso_externos = []
ingreso_camiones = []
lista_empleados = [[202500,'Folgado','Mateo','Ford Fiesta','asd-123'], [202501,'Messi','Lionel','toyota hilux','oea-123']]
#estado = True


#############################################################################################
#############################################################################################
def empleados_ingreso(estado):
  id_empleado = int(input("Ingrese el ID del empleado: "))
  modelo_de_auto = str(input("Ingrese el modelo del auto: "))
  patente = str(input("Ingrese la patente del auto: "))
  now = datetime.today()

 # if estado == True:
  if ingreso_internos == True: ## Buscar si existen los empleados mediante un For JOACO

    print("Error: El empleado con ID", id_empleado, "ya tiene un ingreso activo.")
  else:
    informacion_empleado = [id_empleado, modelo_de_auto, patente, now] #cambiar la matriz, por un diccionario --  cambiar variable a dic_informacion_empleado_deldia JOACO
    ingreso_internos.append(informacion_empleado)
    print("Empleado ingresado correctamente al predio.")

  return

def validar_ingreso(id_empleado):
  ingreso_activo = False
  for registro in ingreso_internos:
    if registro[1] == id_empleado:
      if len(registro) < 6:
        ingreso_activo = True
        #estado = ingreso_activo
  #return estado
  return ingreso_activo


def empleados_egreso():
  print("CHAU")
  return





#############################################################################################
#############################################################################################
def externo_ingreso():
  print("HOLA")
  return



def externo_egreso():
  print("CHAU")
  return




#############################################################################################
#############################################################################################
def Ingreso_camiones():
  print("HOLA")
  return


def egreso_camiones():
  print("CHAU")
  return







#############################################################################################
#############################################################################################
#############################################################################################
def menu_internos():
  opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Salir \nSeleccione una opcion: "))
  while opcion != 3:
    if opcion == 1:
     empleados_ingreso(estado)
    elif opcion == 2:
      empleados_egreso()
    else:
      print("Opcion no valida")
    opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Salir \nSeleccione una opcion: "))


#############################
def menu_externos():
  #opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Salir \nSeleccione una opcion: "))
  print("HOLA")
  return

#############################
def menu_camiones():
  #opcion = int(input("\n1.Cargar ingreso \n2.Cargar egreso \n3.Salir \nSeleccione una opcion: "))
  print("HOLA")
  return




################### MENU INICIAL ################################
print("\t\tBIENVENIDO")
opcion = int(input("\n1.Ingresar empleado \n2.Ingresar Externo \n3.Ingresar camion \n4.Visualizar ingresos \n5.Terminar programa \nSeleccione una opcion para empezar: "))

while opcion != 5:

  while opcion < 1 or opcion > 5: # Corrected condition to validate input for main menu
    print("Opcion no valida")
    opcion = int(input("\n1.Ingresar empleado \n2.Ingresar Externo \n3.Ingresar camion \n4.Visualizar ingresos \n5.Terminar programa \nSeleccione una opcion para empezar: "))

  if opcion == 1:
    menu_internos()

  elif opcion == 2:
    menu_externos()

  elif opcion == 3:
    menu_camiones()

  elif opcion == 4:
    print(ingreso_internos)

  else:
    print("Programa terminado.")

  opcion = int(input("\n1.Ingresar empleado \n2.Ingresar Externo \n3.Ingresar camion \n4.Visualizar ingresos \n5.Terminar programa \nSeleccione una opcion para empezar: "))


print("Programa terminado.")