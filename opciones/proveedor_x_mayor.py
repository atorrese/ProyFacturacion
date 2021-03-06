from clases.proveedor import ProveedorMayor
from utileria.archivo import Archivo
from utileria.menu import  Menu
from utileria.TableIT import printTable
from os import system
import time
def proveedorMayor():
    system('cls')
    pos = lambda y,x:'\x1b[%d;%dH'%(y,x)
    men = Menu(['1).Ingreso','2).Listado','3).Salir'],'     Menu Proveedor Mayor')
    opc = men.mostrarMenu()
    while opc != '3':
        system('cls')
        if opc == '1':
            y = 10000
            print(pos(1,25)+'Ingreso Proveedor Mayor')
            print(pos(2,25)+'')
            nom = input('Nombre......:'+pos(3,25))
            ruc = input('Ruc.........:'+pos(4,25))
            dir = input('Direccion...:'+pos(5,25))
            tel = input('Telefono....:'+pos(6,25))
            mai = input('Email.......:'+pos(7,25))
            tar = input('Tarjeta.....:'+pos(8,25))
            prov = ProveedorMayor(ruc,nom,dir,tel,mai,tar)
            arch = Archivo()
            arch.escribir('data/proveedor_mayor.txt',prov.mostrarProveedor())
            x = input('Registro Grabado, Precione una tecla para continuar...')

        elif opc == '2':
            print(pos(1,15)+'Listado Proveedor por Mayor')
            arch = Archivo()
            datos = arch.leer('data/proveedor_mayor.txt')
            tabla=[]
            tabla.append(['Ruc','Nombre','Direccion','Telefono','Email','Tarjeta'])
        
            for dato in datos:
                #tabla.append(['\x1b[0;34m'+dato[0],'\x1b[0;34m'+dato[1],'\x1b[0;34m'+dato[2],'\x1b[0;34m'+dato[3],'\x1b[0;34m'+dato[4],'\x1b[0;34m'+dato[5]])
                tabla.append([dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]])
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            x = input('\x1b[0;37m'+'Registro Grabado, Precione una tecla para continuar...')
        system('cls')
        opc = men.mostrarMenu()