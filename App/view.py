"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
#from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(data_organization):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(data_organization)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Obtener dato dado un ID")
    print("11- Ordenar información")
    print("0- Salir")

def load_data(control,ruta):
    """
    Carga los datos
    """
    ruta=cf.data_dir + 'Dian\Salida_agregados_renta_juridicos_AG-small.csv'
    data = controller.load_data(control, ruta)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    #print(controller.req_1(control))
    print(controller.saldo_mayor_por_anio(control))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print(controller.req_2(control))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print(controller.req_3(control))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req_4(control))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print(controller.req_5(control))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(controller.req_6(control))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req_7(control))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))

# Se crea el controlador asociado a la vista
control = new_controller("ARRAY_LIST")

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                ruta=cf.data_dir + 'Dian\Salida_agregados_renta_juridicos_AG-small.csv'
                data = load_data(control, ruta)
                print("La cantidad de datos cargados son " + str(lt.size(data["data"]))+ ("\n"))
                
                print(data["data"]["elements"][0])
                print("\n" + "////////////////////////////////////////////////////////////////////////////" + "\n")
                print(data["data"]["elements"][1])
                print("\n" + "////////////////////////////////////////////////////////////////////////////" + "\n")
                print(data["data"]["elements"][2]) 
                print("\n" + "////////////////////////////////////////////////////////////////////////////" + "\n")               
                print(data["data"]["elements"][-3])
                print("\n" + "////////////////////////////////////////////////////////////////////////////" + "\n")
                print(data["data"]["elements"][-2])
                print("\n" + "////////////////////////////////////////////////////////////////////////////" + "\n")
                print(data["data"]["elements"][-1])
                
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)
            
            elif int(inputs) == 11:
                size = input("Indique tamaño de la muestra:5,10,20,50, 0 si es small o \n1 si es large\n")
                if int(size)==5:
                    ruta=cf.data_dir + 'Dian\Salida_agregados_renta_juridicos_AG-5pct.csv'
                elif int(size)==10:
                    ruta=cf.data_dir + 'Dian\Salida_agregados_renta_juridicos_AG-10pct.csv'
                elif int(size)==20:
                    ruta=cf.data_dir + 'Dian\Salida_agregados_renta_juridicos_AG-20pct.csv'
                elif int(size)==50:
                    ruta=cf.data_dir + 'Dian\Salida_agregados_renta_juridicos_AG-50pct.csv'
                elif int(size)==0:
                    ruta=cf.data_dir + 'Dian\Salida_agregados_renta_juridicos_AG-small.csv'
                elif int(size)==1:
                    ruta=cf.data_dir + 'Dian\Salida_agregados_renta_juridicos_AG-large.csv'
                
                print("Seleccione el tipo de ordenamiento")
                sortType = input("1.Shell Sort\n2.Insertion Sort\n3.SelectionSort\n4.Merge sort \n5.Quick sort\n")
                org=input("Cómo desea organizar los datos: 1. Array\n2.Singled linked\n")
                if int(org)==1:
                    org="ARRAY_LIST"
                elif int(org)==2:
                    org="SINGLE_LINKED"
                control = controller.new_controller(org)
                data = load_data(control,ruta)
                result = controller.sort(data, int(lt.size(data["data"])), int(sortType))
                print("Su tamaño es:"+str(int(lt.size(data["data"]))))
                print("El programa tardó: "+ str(round(result,2))+" ms") 

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
