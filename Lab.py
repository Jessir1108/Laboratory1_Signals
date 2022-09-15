import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import streamlit as st
import sk_dsp_comm.sigsys as ss


#TITULOS
st.sidebar.title('Laboratorio 1 - Señales y sistemas')
st.sidebar.subheader("Jessir Daniel Florez Hamburger - Mateo Jose Muñoz - Dylan Abuchaibe")
st.sidebar.subheader('Etapa 1 - Generación de señales')

#SELECCIONADOR DE SEÑALES
opcion = st.sidebar.selectbox(
     'Escoja la señal que desea generar a continuación:',
     ('Seno','Pulso','Cuadratica',"Exponencial","Lineal","Triangular","Cuadrada","Secuencia de impulsos"))

st.sidebar.write('Has seleccionado la función tipo :', opcion)

#FUNCION SENO
if opcion == "Seno":

    st.title("Función Seno")

    frecuencia = st.number_input("Por favor ingrese el valor de la frecuencia f: ",step=1,min_value=1,max_value=10)
    amplitude = st.number_input("Por favor ingrese el valor de la amplitud A: ",step=1,min_value=-10,max_value=10,value=1)
    
    paso=(1/(300*frecuencia))
    x=np.arange(0,2*np.pi,paso)
    y=np.sin(2*np.pi*frecuencia*x)
    y=y*amplitude

    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función Seno")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.set_xlim(0,np.pi)
    ax.set_ylim(-10,10)
    ax.grid(True)
    st.pyplot(fig)

#FUNCION PULSO
elif opcion == "Pulso":

    st.title("Función Pulso")

    amplitud = st.number_input("Por favor ingrese el valor de la amplitud del pulso: ",step=1,min_value=0,max_value=10,value=1)
    anchura = st.number_input("Por favor ingrese el valor de la anchura del pulso: ",step=1,min_value=1,max_value=10,value=1)
    
    visualize=anchura/2
    percentage=visualize*0.5
    x = np.arange((-visualize)-percentage,(visualize)+percentage,.002)
    x_rect = ss.rect(x,anchura)
    y=x_rect*amplitud

    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función pulso")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.set_xlim(-6,6)
    ax.set_ylim(0,10)
    ax.grid(True)
    st.pyplot(fig)

#FUNCION CUADRATICA
elif opcion == "Cuadratica":

    st.title("Función Cuadrática")
    st.latex("ax^2+2bx+c")

    Escal=st.number_input("Ingrese el valor de la constante A: ",step=1,min_value=0,max_value=10,value=1)
    B=st.number_input("Ingrese el valor de la constante B: ",step=1,min_value=0,max_value=10)
    C=st.number_input("Ingrese el valor de la cosntante C: ",step=1,min_value=0,max_value=10)

    x = np.arange(-10,10,.01)
    y = Escal*x**2+B*x+C
        
    
    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función cuadratica")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)

#FUNCION EXPONENCIAL
elif opcion == "Exponencial":
    
    st.title("Funcion Exponencial")
    st.latex("y(t)=Ae^{-bt}")

    Escal=st.number_input("Ingrese el valor de la constante A: ",step=1,min_value=1,max_value=10,value=1)
    b=st.number_input("Ingrese el valor de la constante b: ",step=1,min_value=-5,max_value=10,value=1)
    x= np.arange(0,2*np.pi,0.01)
    
    y = Escal*np.exp(-b*x)

    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función exponencial")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)
    
#FUNCION LINEAL
elif opcion=="Lineal":

    st.title("Función Lineal")
    st.latex("y=mx+b")

    m=st.number_input("Ingrese el valor de la constante m: ",step=1,min_value=-10,max_value=10,value=1)
    b=st.number_input("Ingrese el valor de la constante b: ",step=1,min_value=-10,max_value=10,value=1)

    x = np.arange(-10,10, 0.01)
    y = (m*x)+b

    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función lineal")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.set_xlim(-10,10)
    ax.set_ylim(-50,50)
    ax.grid(True)
    st.pyplot(fig)

#FUNCION TRIANGULAR
elif opcion == "Triangular":
   
    st.title('Funcion Triangular')

    a = st.number_input('Ingrese a continuacion el valor de la amplitud:',step=1,min_value=1,max_value=10,value=1)
    f = st.number_input('Ingrese a continuación el valor de la frecuencia:',step=1,min_value=1,max_value=10,value=3)

    paso=(1/(10000*f))
    x = np.arange(0,np.pi/2,paso)
    y = a*signal.sawtooth(2 *np.pi*f*x)
    
    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función triangular")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.set_xlim(0,np.pi/2)
    ax.set_ylim(-11,11)
    ax.grid(True)
    st.pyplot(fig)

#FUNCION CUADRADA
elif opcion == "Cuadrada":
   
    st.title('Funcion Cuadrada')

    a = st.number_input('Ingrese a continuacion el valor de la amplitud:',step=1,min_value=1,max_value=10)
    f = st.number_input('Ingrese a continuación el valor de la frecuencia:',step=1,min_value=1,max_value=10,value=3)

    paso=(1/(300*f))
    x = np.arange(0,np.pi/2,paso)
    y = a*signal.square(2*np.pi*f*x)
    
    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función cuadrada")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.set_xlim(0,np.pi/2)
    ax.set_ylim(-11,11)
    ax.grid(True)
    st.pyplot(fig)
    
#SECUENCIA DE IMPULSOS

if opcion=="Secuencia de impulsos":
    x = st.sidebar.text_input('x []:')
    y = st.sidebar.text_input('y []:')

    x = np.array(np.matrix(x)).ravel()
    y = np.array(np.matrix(y)).ravel()


    if len(x)!=len(y):
        st.error('Debe ingresar longitudes iguales para que pueda graficarse correctamente')
            
    else:
        fig, ax = plt.subplots()
        ax.stem(x,y)
        ax.set_title("Secuencia de impulsos")
        ax.set_xlabel("Eje x")
        ax.set_ylabel("Eje Y")
        ax.set_xlim()
        ax.grid(True)
        st.pyplot(fig)

        
#ETAPA DE TRANSFORMACION DE SEÑALES
st.sidebar.subheader('Etapa 2 - Transformación de señales')
st.sidebar.subheader("Etapa de transformaciones")

#DECLARACION DE VALORES PARA GRAFICAR
frames=15
graficar=st.empty()

#DESPLAZAMIENTO EN EL TIEMPO
Desplazamiento = st.sidebar.number_input("Ingrese cuantas unidades desea desplazar: ", step=1,min_value=-5,max_value=5,value=0)
new_x=x-Desplazamiento

#ESCALAMIENTO EN AMPLITUD
Escalamiento_a = st.sidebar.number_input("Ingrese cuantas unidades desea escalar en amplitud: ", step=0.1,min_value=0.0,max_value=10.0,value=1.0)
new_y=y*Escalamiento_a

#ESCALAMIENTO EN EL TIEMPO
Escal_time = st.sidebar.number_input("Ingrese cuantas unidades desea escalar en el tiempo: ", step=0.1,min_value=0.0,max_value=5.0,value=1.0)
animacion = st.sidebar.button('Animación')


#GRAFICAR TRANSFORMACIONES
if animacion:

#GRAFICA DE DESPLAZAMIENTO
    if opcion=="Secuencia de impulsos":
        for i in range(frames+1):   
            fig,ax=plt.subplots()
            ax.stem(x,y)
            ax.stem(x-i*(Desplazamiento)/frames,y,linefmt ="rx")
            ax.legend(['Original', 'Transformada'])
            ax.set_title("Transformaciones")
            ax.set_xlabel("Eje x")
            ax.set_ylabel("Eje y")
            ax.grid(True)
            graficar.pyplot(fig)
            
    else:
        for i in range(frames+1):   
            fig,ax=plt.subplots()
            ax.plot(x,y)
            ax.plot(x-i*(Desplazamiento)/frames,y,linestyle="dashed")
            ax.legend(['Original', 'Transformada'])
            ax.set_title("Transformaciones")
            ax.set_xlabel("Eje x")
            ax.set_ylabel("Eje y")
            ax.grid(True)
            graficar.pyplot(fig)


#GRAFICA DE ESCALAMIENTO EN AMPLITUD
    if opcion=="Secuencia de impulsos":
        for i in range(frames+1):   
            fig,ax=plt.subplots()
            ax.stem(x,y)
            ax.stem(new_x,y*(1 + i*(Escalamiento_a-1)/frames),linefmt="rx")
            ax.legend(['Original', 'Transformada'])
            ax.set_title("Transformaciones")
            ax.set_xlabel("Eje x")
            ax.set_ylabel("Eje y")
            ax.grid(True)
            graficar.pyplot(fig)

    else:
        for i in range(frames+1):   
            fig,ax=plt.subplots()
            ax.plot(x,y)
            ax.plot(new_x,y*(1 + i*(Escalamiento_a-1)/frames),linestyle="dashed")
            ax.legend(['Original', 'Transformada'])
            ax.set_title("Transformaciones")
            ax.set_xlabel("Eje x")
            ax.set_ylabel("Eje y")
            ax.grid(True)
            graficar.pyplot(fig)

#GRAFICA DE ESCALAMIENTO EN EL TIEMPO
    if opcion=="Secuencia de impulsos":
        for i in range(frames+1):   
            fig,ax=plt.subplots()
            ax.stem(x,y)
            ax.stem((new_x/(1+ i*(Escal_time-1)/frames)),new_y,linefmt="rx")
            ax.legend(['Original', 'Transformada'])
            ax.set_title("Transformaciones")
            ax.set_xlabel("Eje x")
            ax.set_ylabel("Eje y")
            ax.grid(True)
            graficar.pyplot(fig)

    else:
        for i in range(frames+1):   
            fig,ax=plt.subplots()
            ax.plot(x,y)
            ax.plot((new_x/(1+ i*(Escal_time-1)/frames)),new_y,linestyle="dashed")
            ax.legend(['Original', 'Transformada'])
            ax.set_title("Transformaciones")
            ax.set_xlabel("Eje x")
            ax.set_ylabel("Eje y")
            ax.grid(True)
            graficar.pyplot(fig)