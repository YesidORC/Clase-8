from RegistrEEG import *

def main():
    sis = Sistema()
    while True:
        print("Ingrese:\n 1 Nuevo paciente\n 2 Editar paciente\n 3 Eliminar un paciente\n 4- Cargar y guardar paciente\n 5- Ver cantidad de visitas de pacientes\n 6-Salir del sistema")
        valor = validar("Valor: ")
        if valor == 1:
            cedula = validar("Ingrese la cedula: ")
            if sis.verificarExiste(cedula) == True:
                print(f"Paciente ya esta en el sistema...verifique la cedula ingresada {cedula}")
                continue
            else:
                p=Paciente()
                p.AsignarNombre(input("Nombre: "))
                p.asignarCedula(cedula)
                p.asignarGenero(input("Género: "))
                numVis =  validar (f"Ingrese la cantidad de visitas que va ingresar del paciente {p.verNombre()}: ")
                for i in range(0,numVis):
                    dia = validar("Ingrese dia:")
                    mes = validar("Ingrese mes:")
                    año = validar("Ingrese año:")
                    f = datetime.datetime(año, mes, dia).strftime("%x")
                    if p.verificarExiste(f) == True:
                        print("Ya existe  visita, ingrese otra porfavor")
                        continue
                    v = Visita()
                    v.asignarFecha(f)
                    v.asignarRegistro(f'Pacientes_{p.verCedula()}')
                    v.asignarNotas(input("Ingrese Observaciones: "))
                    ind=v.verIndice()
                    ind.asignarPot_A1(validarf("Ingrese a1= "))
                    ind.asignarPot_A2(validarf("Ingrese a2= "))
                    ind.asignarPot_B(validarf("Ingrese b= "))
                    ind.asignarPot_D(validarf("Ingrese d= "))
                    ind.asignarPot_G(validarf("Ingrese g= "))
                    ind.asignarPot_T(validarf("Ingrese t= "))
                    # v.asignarIndice(ind)
                    p.ingresarVistas(v)

                sis.ingresarPac(p)
        elif valor == 2: #Edición de Paciente
            cedula = validar("Ingrese Cedula")
            if sis.verificarExiste(cedula) == True:
                pac = sis.verPac(cedula)
                opcion = validar("Ingresar parar editar:\n1- Nombre\n2- Cédula\n3- Género\n4- Visita\n5- Salir\n Opción:  ")
                if opcion == 1:
                    pac.AsignarNombre(input("Ingrese nuevo nombre: "))
                elif opcion == 2:
                    pac.asignarCedula(validar("Ingrese nueva cédula: "))
                    sis.eliminarPac(cedula)
                    sis.ingresarPac(pac)
                elif opcion == 3:
                    pac.asignarGenero(input("Ingrese nuevo género: "))   
                elif opcion == 4:
                    dia = validar("Ingrese dia:")
                    mes = validar("Ingrese mes:")
                    año = validar("Ingrese año:")
                    f = datetime.datetime(año, mes, dia).strftime("%x")
                    if pac.verificarExiste(f) == True:
                        visi = pac.verVisita(f)
                        menu = validar("Ingrese para editar: \n1- Fecha \n2- Registro \n3- Nota \n4- Indice\n 5- Eliminar vista\n Opcion : ")
                        if menu == 1:
                            dia = validar("Ingrese nuevo dia: ")
                            mes = validar("Ingrese nuevo mes: ")
                            año = validar("Ingrese nuevo año: ")
                            f = datetime.datetime(año, mes, dia).strftime("%x")
                            visi.asignarFecha(f)
                            pac.eliminarVista(f)
                            pac.asignarVisita(visi)
                        elif menu == 2:
                            visi.asignarRegistro(input("Ingrese nueva Registro: ") )
                        elif menu == 3:
                            notaExistente = visi.verNotas()
                            visi.asignarNotas(input("Ingrese nueva Nota complementaria: ")+notaExistente) 
                        elif menu == 4:
                            I = visi.verIndice()
                            I.asignarPot_A1(validarf("a1= "))
                            I.asignarPot_A2(validarf("a1= "))
                            I.asignarPot_B(validarf("b= "))
                            I.asignarPot_G(validarf("g= "))
                            I.asignarPot_D(validarf("d= "))
                            I.asignarPot_T(validarf("t= "))
                        elif menu == 5:
                            pac.eliminarVisita(visi.verFecha())
        
        elif valor == 3: # Elimiar Paciente
            cedula = validar("Ingrese la cedula: ")
            if sis.verificarExiste(cedula) == False:
                print("Paciente no existe ...")
            else:
                sis.eliminarPac(cedula)

        elif valor ==  4: # Cargar y guardar inforamacion a archivo txt
            cedula = validar("Ingrese Cedula")
            if sis.verificarExiste(cedula) == True:
                p = sis.verPac(cedula)
                p = sis.recuperaPac(cedula)
                archivo = open(f"Paciente_{p.verNombre()}.txt",'w')
                archivo.write(p.verNombre()+ "\n" )
                archivo.write(str(p.verCedula())+ "\n" )
                archivo.write(p.verGenero()+ "\n" )
                for i in p.verListadoVisitas():
                    archivo.write(p.verVisita(i).verFecha()+ "\n" )
                    archivo.write(p.verVisita(i).verRegistro()+ "\n" )
                    archivo.write(p.verVisita(i).verNotas()+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_A1())+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_A2())+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_B()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_D()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_G()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_T()) + "\n") 


        elif valor == 5:
            cedula = validar("Ingrese Cedula")
            if sis.verificarExiste(cedula) == True:
                p = sis.verPac(cedula)
                cv = len(p.verListadoVisitas())
                print(f"El paciente {p.verNombre()} tiene {cv} visitas")

        elif valor == 6:
            break

        else:
            print("Opción no válida, intentelo nuevamente....")

if __name__ == '__main__':
    main()                       


