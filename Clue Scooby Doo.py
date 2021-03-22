#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *  #Importa todos los modulos de la libreria

root = Tk() 
root.title("Clue - Scooby-Doo Edition")
root.geometry("800x800") #Define el ancho y alto de la ventana
root.resizable(0,0)

bg = PhotoImage(file = "Mapa.png")                           #Carga de imagenes
BarraMenu=PhotoImage(file = "BarraMenu.png")
imagen_biblioteca = PhotoImage(file = "biblioteca.png")
imagen_ceti = PhotoImage(file = "universidad.png")
imagen_casa = PhotoImage(file = "biblioteca.png")
imagen_pizza = PhotoImage(file = "pizzeria.png")
imagen_playa = PhotoImage(file = "Playa.png")

Fred_Img = PhotoImage(file = "Fred.png")
Velma_Img = PhotoImage(file = "Velma.png")
Shaggy_Img = PhotoImage(file = "Shaggy.png")
Daphne_Img = PhotoImage(file = "Daphne.png")
Scooby_Img = PhotoImage(file = "Scooby.png")

Marcie_Img = PhotoImage(file = "Marcie.png")
Isma_Img = PhotoImage(file = "Isma.png")
Kevin_Img = PhotoImage(file = "Kevin.png")
Heather_Img = PhotoImage(file = "Heather.png")
Jennifer_Img = PhotoImage(file = "Jennifer.png")

BarraDialogo = PhotoImage(file = "BarraDialogo.png")

#--------------------------------------------------------------------- Obtencion del malvado y distribucion de personajes/pistas
import random

nombres = ['Marcie','Isma','Heather','Kevin','Jennifer']
lugar = ['Playa', 'Pizzeria','Biblioteca','Casa','Escuela']
pista = ['Virutas de piedras recien picadas','Paginas sobre monstruos','Planos destruidos del pueblo','Residuos desconocidos','Fotografias de la pandilla']

Malvado =[nombres[random.randint(0,4)],lugar[random.randint(0,4)],pista[random.randint(0,4)]]
print(Malvado)

Mapa=[] #Lista donde se almacenará el personaje y pista que se encontrará en cada lugar
Conclusion=[]
AccionesCount=0 #Contador de acciones que realiza el usuario (MAXIMO 5)
for i in range(5):
    Mapa.append([nombres[random.randint(0,(len(nombres)-1))],lugar[random.randint(0,len(lugar)-1)],pista[random.randint(0,len(pista)-1)]])
    nombres.remove(Mapa[i][0])
    lugar.remove(Mapa[i][1])
    pista.remove(Mapa[i][2])

print(Mapa)
#------------------------------------------------------------------------
canvas1 = Canvas( root, width = 800, 
                        height = 800) 

canvas1.pack(fill = "both", expand = True) 
canvas1.pack() 

canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.create_image(0,0,image=BarraMenu,anchor="nw")

canvas1.create_text( 400, 150, 
                    text="Selecciona un lugar para investigar", fill="white",
                    font=("Helvetica",18)) 
canvas1.create_text( 400, 170, 
                    text=f"Acciones restantes: {5-AccionesCount}", fill="white",
                    font=("Helvetica",18)) 

#-------------------------------------------------- Metodos cuando se presione el boton de algun lugar
def cambia_biblioteca():
    canvas1.pack(fill = "both", expand = True) 
    canvas1.pack() 
    canvas1.create_image( 0, 0, image = imagen_biblioteca, anchor = "nw")
    ocultar_botones()
    global nom_lugar
    nom_lugar="Biblioteca"
    global i_mapa
    i_mapa=ubicar_mapa(nom_lugar)
    Destino(nom_lugar)
    
def cambia_ceti():
    canvas1.pack(fill = "both", expand = True) 
    canvas1.pack() 
    canvas1.create_image( 0, 0, image = imagen_ceti, anchor = "nw")
    ocultar_botones()
    global nom_lugar
    nom_lugar="Escuela"
    global i_mapa 
    i_mapa=ubicar_mapa(nom_lugar)
    Destino(nom_lugar)

    
def cambia_playa():
    canvas1.pack(fill = "both", expand = True) 
    canvas1.pack() 
    canvas1.create_image( 0, 0, image = imagen_playa, anchor = "nw")
    ocultar_botones()
    global nom_lugar
    nom_lugar="Playa"
    global i_mapa
    i_mapa=ubicar_mapa(nom_lugar)
    Destino(nom_lugar)
    
def cambia_pizza():
    canvas1.pack(fill = "both", expand = True) 
    canvas1.pack() 
    canvas1.create_image( 0, 0, image = imagen_pizza, anchor = "nw")
    ocultar_botones()
    global nom_lugar
    nom_lugar="Pizzeria"
    global i_mapa
    i_mapa=ubicar_mapa(nom_lugar)
    Destino(nom_lugar)
    
def cambia_casa():
    canvas1.pack(fill = "both", expand = True) 
    canvas1.pack() 
    canvas1.create_image( 0, 0, image = imagen_biblioteca, anchor = "nw")
    ocultar_botones()
    global nom_lugar
    nom_lugar="Casa"
    global i_mapa
    i_mapa=ubicar_mapa(nom_lugar)
    Destino(nom_lugar)
    
#--------------------------------------------- Mostrar/Ocultar botones del mapa    
def ocultar_botones():
    pizza.place_forget()
    ceti.place_forget()
    biblioteca.place_forget()
    casa.place_forget()
    playa.place_forget()
    
    global EnLugar
    global DialogCount
    EnLugar=1
    DialogCount=0
    
def mostrar_botones():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    pizza.place(x=90,y=315)
    ceti.place(x=120,y=540)
    biblioteca.place(x=330,y=315)
    casa.place(x=400,y=695)
    playa.place(x=450,y=450)
    
def mostrar_opciones():
    boton_uno.place(x=400,y=300)
    boton_dos.place(x=400,y=340)
    boton_tres.place(x=400,y=380)
    boton_cuatro.place(x=400,y=420)
    boton_cinco.place(x=400,y=460)

#----------------------------------------------------- Dialogo general del destino
def Destino(lugar):
    
    texto=["Fred:\nMuy bien chicos, llegamos a la "+lugar,
           "Velma: \nY al parecer no somos los unicos. \n"+Mapa[i_mapa][0]+" está aqui tambien",
           "Fred: \nEntonces, que vamos a hacer?"]
    ImgTex=[Fred_Img,Velma_Img,Fred_Img]
    
    global dialogo
    global Imagen

    if DialogCount>0 and DialogCount<len(texto):  #Para imprimir las demás lineas de texto

        canvas1.itemconfig(Imagen,image=ImgTex[DialogCount])
        canvas1.itemconfig(dialogo,text=texto[DialogCount])
        if DialogCount==2:
            boton_investigar.place(x=450,y=320)
            boton_preguntar.place(x=450,y=400)
        
    elif DialogCount>=len(texto): #Cuando se acaben las lineas de dialogo
        #print(DialogCount)
        print("Se acabo el texto")
        
    else:             #Para imprimir la primera lia de texto
        Imagen=canvas1.create_image( 0, 0, image = Fred_Img, anchor = "nw")
        dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=texto[DialogCount], anchor="nw",
                        font=("Helvetica",16))
        print(DialogCount)
#-------------------------------------------------------------
def conversar():
    print("estamos hablando")
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    global AccionesCount
    global DialogCount
    global EnLugar
    global num_dialogo #Seleccionar un dialogo en caso de que sea un inocente
    global dialogo  #Para eliminar el ultimo dialogo donde se pregunta la accion
    global Imagen
    
    canvas1.delete(Imagen)
    canvas1.delete(dialogo)
    AccionesCount+=1
    EnLugar=4
    DialogCount=0
    boton_menu.place_forget()
    num_dialogo=random.randint(0,2) #Seleccionado uno de los 3 dialogos disponibles de forma aleatoria
    HablarSospechoso()
    
def investigar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    global AccionesCount
    global EnLugar
    global DialogCount
    global dialogo  #Para eliminar el ultimo dialogo donde se pregunta la accion
    global Imagen
    
    canvas1.delete(Imagen)
    canvas1.delete(dialogo)
    AccionesCount+=1
    EnLugar=2
    DialogCount=0
    boton_menu.place_forget()
    EncontrarPista()

def HablarSospechoso():
    global dialogo
    
    lugRandom=random.randint(0,4)
    nomRandom=random.randint(0,4)
    if Mapa[nomRandom][0]==Mapa[i_mapa][0] or Mapa[nomRandom][0]==Malvado[0]:  #En caso de que salga la misma persona o el malo
        nomRandom=random.randint(0,4)
    if lugRandom==i_mapa:
        lugRandom=random.randint(0,4)
        
    dialogo1=[f"Velma: \nHola {Mapa[i_mapa][0]}.",   #Dialogo cuando se habla con el malvado
             f"{Mapa[i_mapa][0]}: \nOh, hola chicos, en qué les puedo ayudar?",
             f"Daphne: \nNos preguntabamos donde te encontrabas durante las ultimas horas",
             f"{Mapa[i_mapa][0]}: \nMmm.. bno, estaba en {Mapa[lugRandom][1]}, y recuerdo haber visto a {Mapa[nomRandom][0]} por ahí.\nDe hecho, se veia muy sospechoso y quiza dejó alguna pista ahi",
             f"Velma: \nMmmm interesante ... Muchas gracias por su ayuda, {Mapa[i_mapa][0]}",
             f"{Mapa[i_mapa][0]}: \nNo fue nada, cuidense..."]
    image=[Velma_Img,f"{Mapa[i_mapa][0]}_Img",Daphne_Img,f"{Mapa[i_mapa][0]}_Img",Velma_Img,f"{Mapa[i_mapa][0]}_Img"]
    #--------- Dialogos de sospechosos inocentes --------------
    dialogos=[[f"{Mapa[i_mapa][0]}: \nHola chicos ... y su amigo canino?",
                 "Shaggy: \nHola... alguien secuestró a Scooby y estamos buscandolo.\nNos podria decir donde ha estado la ultimas horas?",
                 f"{Mapa[i_mapa][0]}: \nOoh, pobrecito. espero lo encuentren pronto. \nEstuve en el parque tomando un descanso, de hecho, ahora que lo mencionas, ahí dejé mi celular; espero siga ahi.",
                 "Shaggy: \nScooby no pudo haber estado ahi, el solo va al parque los viernes con sus demás amigos, y hoy es martes",
                 "Fred: \nMuchas gracias por la informacion, y espero encuentre su celular",
                 f"{Mapa[i_mapa][0]}: \nMuchas gracias, y espero ustedes encuentren a Scooby"],
            [f"Fred: \nQue tal, {Mapa[i_mapa][0]}?",
                 f"{Mapa[i_mapa][0]}: \nHola chicos, ¿donde está el perro?",
                 f"Velma: \nAlguien secuestró a Scooby, y la camara de ciertas zonas estuvieron apagadas, por lo que no podemos saber quien se lo llevo. \nNos podria decir donde estuvo estas horas?",
                 f"{Mapa[i_mapa][0]}: \nEstaba en la cafeteria con un viejo amigo de la infancia. Si no me creen aqui tengo fotos que lo comprueban.",
                 "Velma: \nTe creemos, las camaras de seguridad sí estaban operando ahi, asi que el responsable no estuvo por ahí.",
                 f"{Mapa[i_mapa][0]}: \nBueno, yo me retiro, ese maraton de WandaVision me está esperando. \nEspero encuentren a su amigo y den con el malo"],
            [f"{Mapa[i_mapa][0]}: \nHola chicos, en que les puedo ayudar?",
                 f"Daphne: \nHola {Mapa[i_mapa][0]}, disculpe, nos podria ayudar diciendo donde ha estado las ultimas horas?",
                 f"{Mapa[i_mapa][0]}:Mmm... dejen recuerdo ...",
                 f"{Mapa[i_mapa][0]}:Ah, ya. Estaba con {Mapa[nomRandom][0]} en el museo de Cueva Cristal, y despues yo me dirigí a mi casa",
                 f"Velma: \nEntendido... muchas gracias, {Mapa[i_mapa][0]}"]]
    
    if Malvado[0]==Mapa[i_mapa][0]: #Si se habla con el malvado que secuentraro a Scooby----------------
        if DialogCount>0 and DialogCount<len(dialogo1):  #Para imprimir las demás lineas de texto
            canvas1.itemconfig(dialogo,text=dialogo1[DialogCount])
        
        elif DialogCount>=len(dialogo1): #Cuando se acaben las lineas de dialogo
            #print(DialogCount)
            volver_menu()
            print("Se acabo el texto")
        
        else:             #Para imprimir la primera linea de texto
            dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=dialogo1[DialogCount], anchor="nw",
                        font=("Helvetica",16))
    else:   #----------------En caso de que no sea el lugar donde raptaron a Scooby-------------------------------
        if DialogCount>0 and DialogCount<len(dialogos[num_dialogo]):  #Para imprimir las demás lineas de texto
            canvas1.itemconfig(dialogo,text=dialogos[num_dialogo][DialogCount])
        
        elif DialogCount>=len(dialogos[num_dialogo]): #Cuando se acaben las lineas de dialogo
            #print(DialogCount)
            volver_menu()
            print("Se acabo el texto")
        
        else:             #Para imprimir la primera linea de texto
            dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=dialogos[num_dialogo][DialogCount], anchor="nw",
                        font=("Helvetica",16))
    
    
def EncontrarCollar():   #Funcion para saber si Scooby fue raptado ahi o no --------------------------------
    global dialogo
    global Imagen
    
    dialogo1=["Shaggy: \nChicos, encontré el collar de Scooby. Aqui fue donde estuvo.",  #Dialogo cuando se encuentra collar
            "Daphne: \nPobrecito, debe estar asustado donde sea que esté.",
             "Shaggy: \nNo me dentendré hasta encontrar a mi mejor amigo.",
             "Fred: \nDescuida, Shaggy. Vamos a encontrarlo."]
    ImgTex1=[Shaggy_Img,Daphne_Img,Shaggy_Img,Fred_Img]
    
    dialogo2=["Velma: \nMmm... no hay nada aqui que indique que Scooby estuvo aqui", #Cuando no Scooby no fue raptado ahi
             "Fred: \nTal vez Scooby no estuvo por aquí",
             "Shaggy: \nOooh, Scooby-Doo, donde estás?..."]
    ImgTex2=[Velma_Img,Fred_Img,Shaggy_Img]
    
    if Malvado[1]==Mapa[i_mapa][1]: #Si el lugar donde se encuentran fue donde secuentraron a Scooby----------------
        if DialogCount>0 and DialogCount<len(dialogo1):  #Para imprimir las demás lineas de texto
            canvas1.itemconfig(Imagen,image =ImgTex1[DialogCount])
            canvas1.itemconfig(dialogo,text=dialogo1[DialogCount])
            
        elif DialogCount>=len(dialogo1): #Cuando se acaben las lineas de dialogo
            #print(DialogCount)
            volver_menu()
            print("Se acabo el texto")
        
        else:             #Para imprimir la primera linea de texto
            Imagen=canvas1.create_image( 0, 0, image = ImgTex1[DialogCount], anchor = "nw")
            dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=dialogo1[DialogCount], anchor="nw",
                        font=("Helvetica",16))
    else:   #----------------En caso de que no sea el lugar donde raptaron a Scooby-------------------------------
        if DialogCount>0 and DialogCount<len(dialogo2):  #Para imprimir las demás lineas de texto
            canvas1.itemconfig(Imagen,image =ImgTex2[DialogCount])
            canvas1.itemconfig(dialogo,text=dialogo2[DialogCount])
    
        elif DialogCount>=len(dialogo2): #Cuando se acaben las lineas de dialogo
            #print(DialogCount)
            volver_menu()
            print("Se acabo el texto")
        
        else:             #Para imprimir la primera linea de texto
            Imagen=canvas1.create_image( 0, 0, image = ImgTex2[DialogCount], anchor = "nw")
            dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=dialogo2[DialogCount], anchor="nw",
                        font=("Helvetica",16))
        
        
def EncontrarPista():
    global dialogo
    global EnLugar
    global DialogCount
    global Imagen
    dialogo1=["Fred:\nMuy bien, chicos, dividanse y encuentren alguna pista",  #Cuando se encuentra una pista
             "Velma: \nJinkies!, encontré una pista",
             "Velma:\nEncontre "+Malvado[2]+", pero aun no estoy segura de lo que significa",
             "Daphne:\nTal vez quien tenga a Scooby debe estar tramando algo malo"]
    ImgTex1=[Fred_Img,Velma_Img,Velma_Img,Daphne_Img]
    
    dialogo2=["Fred:\nMuy bien, chicos, dividanse y encuentren alguna pista",  #Cuando no se encuentra una pista
             "...",
             "Shaggy: \nAl parecer no hay una pista que nos ayude a encontrar a Scooby",
             "Velma: \nDebemos seguir investigando, pero tal vez no aqui"]
    ImgTex2=[Fred_Img,BarraDialogo,Shaggy_Img,Velma_Img]
    
    if Malvado[2]==Mapa[i_mapa][2]: #Si el lugar donde se encuentran hay una pista----------------
        if DialogCount>0 and DialogCount<len(dialogo1):  #Para imprimir las demás lineas de texto
            canvas1.itemconfig(Imagen,image =ImgTex1[DialogCount])
            canvas1.itemconfig(dialogo,text=dialogo1[DialogCount])
        
        elif DialogCount>=len(dialogo1): #Cuando se acaben las lineas de dialogo
            #print(DialogCount)
            DialogCount=0
            EnLugar=3
            canvas1.delete(dialogo)
            canvas1.delete(Imagen)
            EncontrarCollar()
            print("Se acabo el texto")
        
        else:             #Para imprimir la primera linea de texto
            Imagen=canvas1.create_image( 0, 0, image = ImgTex1[DialogCount], anchor = "nw")
            dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=dialogo1[DialogCount], anchor="nw",
                        font=("Helvetica",16))
    else:   #----------------En caso de que no haya pista-------------------------------
        if DialogCount>0 and DialogCount<len(dialogo2):  #Para imprimir las demás lineas de texto
            canvas1.itemconfig(Imagen,image =ImgTex2[DialogCount])
            canvas1.itemconfig(dialogo,text=dialogo2[DialogCount])
        
        elif DialogCount>=len(dialogo2): #Cuando se acaben las lineas de dialogo
            #print(DialogCount)
            DialogCount=0
            EnLugar=3
            canvas1.delete(dialogo)
            canvas1.delete(Imagen)
            EncontrarCollar()
            print("Se acabo el texto")
        
        else:             #Para imprimir la primera linea de texto
            Imagen=canvas1.create_image( 0, 0, image = ImgTex2[DialogCount], anchor = "nw")
            dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=dialogo2[DialogCount], anchor="nw",
                        font=("Helvetica",16))
    
    
#------------------------------------------------------------- Saber el valor i respecto al lugar seleccionado
def ubicar_mapa(lugar): 
    for i in range(5):
        if lugar==Mapa[i][1]:
            #print("en ubicar mapa la i en "+lugar+" es de ",i)
            return i        #En este valor está el personaje y la pista del lugar seleccionado
            break
#-------------------------------------------------------------  Acciones de volver al menu y de siguiente 
def volver_menu():
    global dialogo
    global DialogCount
    global EnLugar
    EnLugar=0
    if AccionesCount==5:
        canvas1.delete(dialogo)
        DialogCount=0
        EnLugar=5
        print("Se acabaron las acciones disponibles")
        ResolverMisterio()
            
    else:
        canvas1.pack(fill = "both", expand = True) 
        canvas1.pack() 
        canvas1.create_image( 0, 0, image = bg, anchor = "nw") #Coloca la imagen de fondo del menu
        canvas1.create_image(0,0,image=BarraMenu,anchor="nw")
        mostrar_botones()
        boton_menu.place(x=0,y=700)
        canvas1.create_text( 400, 150, 
                        text="Selecciona un lugar para investigar ", fill="white",
                        font=("Helvetica",18)) 
        canvas1.create_text( 400, 170, 
                        text=f"Acciones restantes: {5-AccionesCount}", fill="white",
                        font=("Helvetica",18)) 

def siguiente():
    global DialogCount
    global AnswerBien
    DialogCount+=1
    if EnLugar==1:
        Destino(nom_lugar)
    elif EnLugar==2: #Cuando se vaya a buscar una pista
        EncontrarPista()
    elif EnLugar==3: #Cuando se vaya a buscar el collar
        EncontrarCollar()
    elif EnLugar==4: #Cuando se vaya a conversar con la persona
        HablarSospechoso()
    elif EnLugar==5: #Cuando se va a resolver el misterio  
        if DialogCount==1:
            print("Estoy en siguiente con EnLugar=",EnLugar)
            siguiente.place_forget()
            mostrar_opciones()
        ResolverMisterio()
    elif EnLugar==6: #Cuando se van a decir los resultados
        print("Estoy en siguiente con EnLugar=",EnLugar)
        Final(AnswerBien)
        
#--------------------------------------------------------------------------- Solucion del misterio
def ResolverMisterio():
    global dialogo
    global DialogCount
    global ans
    global AnswerBien
    global EnLugar
    global Imagen
    
    DialogFinal=["Velma:\nMuy bien, es hora de resolver el misterio",
                "Velma: \nQuien es el culpable del secuestro de Scooby?",
                "Velma: \nEn donde secuestraron a Scooby?",
                "Velma: \nFinalmente, cual es el objetivo malvado del villano?"]
    if DialogCount>0 and DialogCount<len(DialogFinal):  #Para imprimir las demás lineas de texto
        canvas1.itemconfig(dialogo,text=DialogFinal[DialogCount])
        
        boton_uno.configure(text=Mapa[0][DialogCount-1])
        boton_dos.configure(text=Mapa[1][DialogCount-1])
        boton_tres.configure(text=Mapa[2][DialogCount-1])
        boton_cuatro.configure(text=Mapa[3][DialogCount-1])
        boton_cinco.configure(text=Mapa[4][DialogCount-1])

    elif DialogCount>=len(DialogFinal): #Cuando se acaben las lineas de dialogo
        #print(DialogCount)
        DialogCount=0
        EnLugar=6
        canvas1.delete(dialogo)
        canvas1.delete(Imagen)
        ans=0
        for a in 'Virutas de piedras recien picadas','Paginas sobre monstruos','Planos destruidos del pueblo','Residuos desconocidos','Fotografias de la pandilla':
            if Malvado[2]==a:
                break
            ans+=1
        AnswerBien=True
        for i in range(3):
            if Malvado[i]!=Conclusion[i]:
                AnswerBien=False
        print("Ya tengo los resultados ",EnLugar)
        boton_uno.place_forget()
        boton_dos.place_forget()
        boton_tres.place_forget()
        boton_cuatro.place_forget()
        boton_cinco.place_forget()
        siguiente.place(x=700,y=700) #Se coloca de nuevo el boton de siguiente para las lineas
        Final(AnswerBien)
        
    else:             #Para imprimir la primera linea de texto
        canvas1.create_image( 0, 0, image = bg, anchor = "nw")
        Imagen=canvas1.create_image(0,0,image=Velma_Img,anchor="nw")
        dialogo=canvas1.create_text( 30, 560, fill="white",
                    text=DialogFinal[DialogCount], anchor="nw",
                    font=("Helvetica",16))
        
def resultado(respuesta):
    global DialogCount
    global Conclusion
    
    Conclusion.append(respuesta)
    print(Conclusion)
    DialogCount+=1  
    ResolverMisterio()

def Final(r):
    global ans
    global DialogCount
    global dialogo
    global Imagen
    if r==True: #Si el usuario responde correctamente todo
        objetivos=[f"las {Malvado[2]} que encontramos como pista? \nBueno, resulta que esas virutas contienen unos minerales que solo Cueva Cristal tiene. \nEstaba extrayendo Fluorita",
                  f"las {Malvado[2]} que encontramos como pista? \nBueno, resulta que esas paginas pertenecen un libro del autor Jonathan Jacobo. \nEl libro habla sobre como crear monstruos reales",
                  f"los {Malvado[2]} que encontramos como pista? \nBueno, resulta que los planos pertenecen a los de Cueva Cristal. \nQueria destruir el pueblo para encontrar el tesoro perdido",
                  f"los {Malvado[2]} que encontramos como pista? \nBueno, analicé detalladamente esas muestras y resultaron ser draculin. \nUna sustancia que está en la saliva de los vampiros. \nObtenia las sustancias de los murcielagos y los vendia de forma ilegal",
                  f"los {Malvado[2]} que encontramos como pista? \nBueno, las imagenes correspondian a cada uno de nosotros, \nasí que estaba tratando de deshacerse de nosotros"]
        
        Dialogo_Final=["Velma: \nMuy bien, chicos, hemos resuelto el misterio. \nLa persona que secuestro a Scooby fue...",
                     f"Shaggy: \n{Malvado[0]} ??!!",
                     f"Velma: \nAsi es, {Malvado[0]} secuestró a Scooby para alejarnos de su plan",
                     "Daphne: \nClaro, cuando fuimos a hablar con el, nos intentó engañar culpando \na otras personas",
                     "Fred: \nHaciendo que el deje de ser un sospechoso y poder seguir con su plan",
                     "Shaggy: \nY cual era su plan?",
                     f"Velma: \nRecuerdas {objetivos[ans]}",
                      "Shaggy: \nMuy bien, se pudo resolver eso, pero donde está Scooby Doo?",
                      f"{Malvado[0]}: \nNunca les diré donde se encuentra su est..",
                      "SCOOBY DOOBY DOO",
                      "Shaggy: \nScooby ? ... SCOOBY !!",
                      "Scooby: \nSHAGGY !!!",
                      "Shaggy: \nAmigo, como te escapaste? estaba muy preocupado por ti",
                      "Scooby: \nEstaba encerrado en la mina abandonada de Cueva Cristal, \npero mis amigos caninos me encontraron y me salvaron",
                      "Fred: \nBueno, Scooby está de regreso con nosotros y resolvimos otro misterio",
                       f"{Malvado[0]}: \nRayos, me hubiera salido con la mia de nor ser por esos niños entrometidos \ny su estúpido perro",
                      "Scooby: \nScooby Dooby Doo !!!"]
        ImgFinal=[Velma_Img,Shaggy_Img,Velma_Img,Daphne_Img,Fred_Img,Shaggy_Img,Velma_Img,Shaggy_Img,Fred_Img,
                 Fred_Img,Shaggy_Img,Scooby_Img,Shaggy_Img,Scooby_Img,Fred_Img,Fred_Img,Scooby_Img]
        
        if DialogCount>0 and DialogCount<len(Dialogo_Final):  #Para imprimir las demás lineas de texto
            canvas1.itemconfig(Imagen,image=ImgFinal[DialogCount])
            canvas1.itemconfig(dialogo,text=Dialogo_Final[DialogCount])
        
        elif DialogCount>=len(Dialogo_Final): #Cuando se acaben las lineas de dialogo
            #print(DialogCount)
            DialogCount=0
            EnLugar=0
            canvas1.delete(dialogo)
            canvas1.delete(Imagen)
            siguiente.place_forget()
            print("Se acabo el juego")
        
        else:             #Para imprimir la primera linea de texto
            Imagen=canvas1.create_image(0,0,image=ImgFinal[DialogCount],anchor="nw")
            dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=Dialogo_Final[DialogCount], anchor="nw",
                        font=("Helvetica",16))
    else:
        Imagen=canvas1.create_image(0,0,image=Velma_Img,anchor="nw")
        dialogo=canvas1.create_text( 30, 560, fill="white",
                        text=f"Velma:Creo que aun te falta pulir tu habilidad como detective. \nCulpable:{Malvado[0]} \nLugar de secuestro:{Malvado[1]} \nPista del objetivo:{Malvado[2]}", anchor="nw",
                        font=("Helvetica",16)) 
        siguiente.place_forget()
#---------------------------------------------------------------------------  BOTONES DEL JUEGO
pizza = Button(canvas1, text="pizza", width=12, command=cambia_pizza)  #Cuando se presione un boton, se activará su metodo
pizza.place(x=90,y=315)

biblioteca = Button(canvas1, text="biblioteca", width=12, command=cambia_biblioteca)
biblioteca.place(x=330,y=315)

ceti = Button(canvas1, text="ceti", width=12, command=cambia_ceti)
ceti.place(x=120,y=540)

casa = Button(canvas1, text="casa", width=12, command=cambia_casa)
casa.place(x=400,y=695)

playa = Button(canvas1, text="playa", width=12, command=cambia_playa)
playa.place(x=450,y=450)

boton_menu = Button(canvas1, text="menu", width=12, command=volver_menu)
boton_menu.place(x=0,y=700)
siguiente = Button(canvas1, text="siguiente", width=12, command=siguiente)
siguiente.place(x=700,y=700)

boton_preguntar = Button(canvas1,text="Hablar con la persona",width="20",command=conversar,font=("Helveltica",12))
boton_investigar= Button(canvas1,text="Inspeccionar el lugar",width="20",command=investigar,font=("Helveltica",12))

boton_uno=Button(canvas1,text="",width="28",command= lambda:resultado(Mapa[0][DialogCount-1]),font=("Helveltica",12))
boton_dos=Button(canvas1,text="",width="28",command=lambda:resultado(Mapa[1][DialogCount-1]),font=("Helveltica",12))
boton_tres=Button(canvas1,text="",width="28",command=lambda:resultado(Mapa[2][DialogCount-1]),font=("Helveltica",12))
boton_cuatro=Button(canvas1,text="",width="28",command=lambda:resultado(Mapa[3][DialogCount-1]),font=("Helveltica",12))
boton_cinco=Button(canvas1,text="",width="28",command=lambda:resultado(Mapa[4][DialogCount-1]),font=("Helveltica",12))

root.mainloop() 


# In[28]:


from tkinter import *  #Importa todos los modulos de la libreria

root = Tk() 
root.title("Clue Scooby Do")
root.geometry("800x800") 
root.resizable(0,0)
bg = PhotoImage(file = "Mapa.png") 
scooby=PhotoImage(file="velma.png")
canvas1 = Canvas( root, width = 800, 
                        height = 800) 
canvas1.pack(fill = "both", expand = True) 
canvas1.pack() 
dialogo=["Hola","Hey,cambie","Otra vez","Bienvenido"]

a=0
canvas1.create_image( 0, 0, image = bg, anchor = "nw") 
canvas1.create_image(0,0,image=scooby,anchor="nw")
texto=canvas1.create_text( 0, 0, 
                    text=dialogo[a], fill="white",
                    font=("Helvetica",12),anchor="nw") 

def volver():
    global a
    global texto1
    a=a+1
    canvas1.delete(texto)
    canvas1.delete(texto1)
    texto1=canvas1.create_text( 0, 10, 
                    text=dialogo[a],anchor="w", fill="white",
                    font=(16))
    
siguiente = Button(canvas1, text="siguiente", width=12,command=volver)
siguiente.place(x=500,y=500)
root.mainloop()


# In[2]:


from tkinter import *  #Importa todos los modulos de la libreria

root = Tk() 
root.title("Clue Scooby Do")
root.geometry("650x650") 
root.resizable(0,0)

canvas1 = Canvas( root, width = 650, 
                        height = 650) 

canvas1.pack(fill = "both", expand = True) 
canvas1.pack() 

def cambia_ceti():
    ceti.configure(text="PRESIONADO")
    
ceti = Button(canvas1, text="ceti", width=12, command=cambia_ceti)
ceti.place(x=120,y=540)
root.mainloop()


# In[ ]:


for i in

