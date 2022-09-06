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
    amplitude = st.number_input("Por favor ingrese el valor de la amplitud A: ",step=1,min_value=-10,max_value=10)
    
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

    amplitud = st.number_input("Por favor ingrese el valor de la amplitud del pulso: ",step=1,min_value=0,max_value=10)
    anchura = st.number_input("Por favor ingrese el valor de la anchura del pulso: ",step=1,min_value=1,max_value=10)
    
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

    Escal=st.number_input("Ingrese el valor de la constante A: ",step=1,min_value=0,max_value=10)
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

    Escal=st.number_input("Ingrese el valor de la constante A: ",step=1,min_value=1,max_value=10)
    b=st.number_input("Ingrese el valor de la constante b: ",step=1,min_value=-5,max_value=10)
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

    m=st.number_input("Ingrese el valor de la constante m: ",step=1,min_value=-10,max_value=10)
    b=st.number_input("Ingrese el valor de la constante b: ",step=1,min_value=-10,max_value=10)

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

    a = st.number_input('Ingrese a continuacion el valor de la amplitud:',step=1,min_value=1,max_value=10)
    f = st.number_input('Ingrese a continuación el valor de la frecuencia:',step=1,min_value=1,max_value=10)

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
    f = st.number_input('Ingrese a continuación el valor de la frecuencia:',step=1,min_value=1,max_value=10)

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
elif opcion == "Secuencia de impulsos":
   
    st.title('Secuencia de impulsos')

    x = st.text_input("Ingrese el valor de los vectores de x: ",args=None)
    y = st.text_input("Ingrese el valor de los vectores de y: ",args=None)

    
    
    if len(x) != len(y):
        st.write("Ingrese vectores equivalentes")

    else:
        fig,ax=plt.subplots()
        ax.set_xlim(-1,11)
        ax.set_ylim(0,10)
        ax.stem(x,y)
        ax.set_title("Función secuencia de impulsos")
        ax.set_xlabel("Eje x")
        ax.set_ylabel("Eje y")
        ax.grid(True)
        st.pyplot(fig)


st.sidebar.subheader('Etapa 2 - Transformación de señales')

transformaciones = st.sidebar.multiselect(
     'Escoja las transformaciones que desea realizar a continuación: ',
     ['Desplazamiento', 'Escalamiento en tiempo', 'Escalamiento en amplitud'])

frames=10
graficar=st.empty()

if "Desplazamiento" in transformaciones:
    st.sidebar.subheader('Escoja a continuación cuantas unidades desea desplazar: ')
    num = st.sidebar.number_input("",step=1,min_value=-5,max_value=5)
    traslado=(x+num)
    
    for i in range(frames+1):   
        fig,ax=plt.subplots()
        ax.plot(x,y)
        ax.plot(x+i*(num)/frames,y,linestyle="dashed")
        ax.legend(['Original', 'Desplazada'])
        ax.set_title("Función Seno")
        ax.set_xlabel("Eje x")
        ax.set_ylabel("Eje y")
        ax.grid(True)
        graficar.pyplot(fig)
        
    if "Escalamiento en amplitud" in transformaciones:
        st.sidebar.subheader('Escoja a continuación cuantas unidades desea escalar: ')
        Escal= st.sidebar.number_input("",step=1,min_value=-3,max_value=3)
            
        Escal=(y*Escal)

        for i in range(frames+1):   
            fig,ax=plt.subplots()
            ax.plot(x,y)
            ax.plot(traslado, y*(1 + i*(Escal-1)/frames),linestyle="dashed")
            ax.legend(['Original', 'Desplazada'])
            ax.set_title("Función Seno")
            ax.set_xlabel("Eje x")
            ax.set_ylabel("Eje y")
            ax.grid(True)
            graficar.pyplot(fig)


        if "Escalamiento en tiempo" in transformaciones:
            st.sidebar.subheader('Escoja a continuación cuantas unidades desea escalar en el tiempo: ')
            Escal_time= st.sidebar.number_input("",step=1,min_value=-4,max_value=4)
                
            Escal_time=(x*Escal_time)

            for i in range(frames+1):   
                fig,ax=plt.subplots()
                ax.plot(x,y)
                ax.plot(traslado, y*(1 + i*(Escal_time-1)/frames),linestyle="dashed")
                ax.legend(['Original', 'Desplazada'])
                ax.set_title("Función Seno")
                ax.set_xlabel("Eje x")
                ax.set_ylabel("Eje y")
                ax.grid(True)
                graficar.pyplot(fig)

    
