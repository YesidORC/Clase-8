import os
import datetime

class Indices:
 #constructor
    def __init__(self,a=0,b=0,c=0,d=0,e=0,f=0):
        #Atributos de la clase
        self.__pot_d = a
        self.__pot_t = b
        self.__pot_a1 = c
        self.__pot_a2 = d
        self.__pot_b = e
        self.__pot_g = f
#Metodos propiedades
    def verPot_D(self):
        return self.__pot_d
    def asignarPot_D(self,p):
        self.__pot_d = p

    def verPot_T(self):
        return self.__pot_t
    def asignarPot_T(self,p):
        self.__pot_t = p

    def verPot_A1(self):
        return self.__pot_a1
    def asignarPot_A1(self,p):
        self.__pot_a1 = p

    def verPot_A2(self):
        return self.__pot_a2
    def asignarPot_A2(self,p):
        self.__pot_a2 = p

    def verPot_B(self):
        return self.__pot_b
    def asignarPot_B(self,p):
        self.__pot_b = p

    def verPot_G(self):
        return self.__pot_g
    def asignarPot_G(self,p):
        self.__pot_g = p


class Visita:
    def __init__(self):
        #Atributos de la clase
        self.__fecha = datetime.datetime.now().strftime("%x")
        self.__registro = ''
        self.__notas = ''
        #La visita tiene una clase indice que se inicializa vacia
        self.__indice = Indices() # SOlo se guarda un objeto tipo Indices

 # Métodos
    def verFecha(self):
        return self.__fecha
    def asignarFecha(self,f):
        self.__fecha = f

    def verRegistro(self):
        return self.__registro
    def asignarRegistro(self,r):
        self.__registro = r

    def verNotas(self):
        return self.__notas
    def asignarNotas(self,n):
        self.__notas = n

    def verIndice(self):
        return self.__indice
    def asignarIndice(self,i):
        self.__indice = i

class Paciente:
    def __init__(self):
        #Atributos de la clase
        self.__nombre = ''
        self.__cedula = 0
        self.__genero = ''
        #Un paciente tiene muchas visitas, en este ejemplo los trabajamos
        #como diccionarios
        self.__visitas = {} # Clave-->fecha, valor-->Visita

    def verNombre(self):
        return self.__nombre
    def AsignarNombre(self,n):
        self.__nombre = n

    def verCedula(self):
        return self.__cedula
    def asignarCedula(self,c):
        self.__cedula = c

    def verGenero(self):
        return self.__genero
    def asignarGenero(self,g):
        self.__genero = g

    def verVisita(self,f):
        return self.__visitas.get(f)
    def verListadoVisitas(self):
        return self.__visitas
    def ingresarVistas(self,v):
        self.__visitas[v.verFecha()]=v

    def verificarExiste(self,f):
        return f in self.__visitas
    def eliminarVisita(self,f):
        del self.__visitas[f] 

class Sistema:
    def __init__(self):
        self.__pacientes = {} #la llave seria la cedula y el valor el paciente dueño de dicha cedula

    def verificarExiste(self,c):
        return c in self.__pacientes

    def ingresarPac(self,p):
        self.__pacientes[p.verCedula()]=p

    def eliminarPac(self,c):
        del self.__pacientes[c]

    def verPac(self,c):
        return self.__pacientes[c]

    def cargarGuardar(self):
        pass

def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("Ingrese un dato numérico...")
    return valor
def validarf(msj):
    while True:
        try:
            valor = float(input(msj))
            break
        except ValueError:
            print("Ingrese un dato numérico...")
    return valor

def main():
    w= Sistema()
    x= Paciente()
    g= Visita()
    w.ingresarPac(x)
    print("Hola mundo cruel")


if __name__ == '__main__':
    main()

    
    