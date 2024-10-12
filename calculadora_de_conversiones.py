import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

#VENTANA 
window = ThemedTk(theme="Kroc")
window.title("conversiones")
window.geometry("420x380")
window.configure(bg="tan")


notebook = ttk.Notebook(window)
notebook.pack(pady=2, expand=True)
frame3 = tk.Frame(notebook, width=400, height=280, bg="Lightblue")
frame3.pack(fill='both', expand=True)
notebook.add(frame3, text='Convertidor de unidades')


#FRAME 3: CONVERITIDOR DE UNIDADES
#ESPACIO PARA DEFINIR FUNCIONES
#FUNCION DESPUES DE COMBOBOX
def opcion_seleccionada(event):
    if comboconv.get():
        comboconv.config(state="disabled")
        boton_inicio.pack()
        campos.pack()
        
#FUNCIÓN PARA BORRAR COSAS ANTERIORES
def limpiar_campos():
    for widget in campos.winfo_children():
        widget.destroy()
        
#funcion para cambiar opcion
def cambiar_opcion():
    limpiar_campos()
    comboconv.set("")
    comboconv.config(state="readonly")
    cambiar_opcion_buton.pack_forget()
   

#FUNCIONES PARA LAS CCONVERSIONES
def conversion():
    limpiar_campos()
    boton_inicio.pack_forget()
    conv = comboconv.get()
    
    def resultado(num):
        resultado_e.delete(0, tk.END)
        resultado_e.insert(0,num)
    
    def convertir():
        if conv == 'decimal-octal':
         d=int(input_1.get())
         num= oct(d)
         resultado(str(num))
        elif conv == 'octal-decimal':
         octal_number = str(input_1.get())
         num= int(str(octal_number),8)
         resultado(int(num))
        elif conv == 'binario-hexadecinal':
         b= str(input_1.get())
         d = (int(str(b),2))
         num= hex(d)
         resultado(str(num))
        elif conv == 'hexadecimal-binario':
         n=str(input_1.get())
         d = int(n,16)
         num= bin(d)
         resultado(str(num))
    
    
    if conv == 'decimal-octal':
        tk.Label(campos, text="Ingrese el numero decimal que quiera convertir ").pack()
        input_1 = tk.Entry(campos)
        input_1.pack()

    elif conv == 'octal-decimal':
        tk.Label(campos, text="Ingrese el numero octal que quiera convertir").pack()
        tk.Label(campos, text="(recuerde que no existen los numeros '8, 9' en este sistema )").pack()
        input_1 = tk.Entry(campos)
        input_1.pack()

    elif conv == 'binario-hexadecinal':
        tk.Label(campos, text="Ingrese el numero binario que quiera convertir").pack()
        input_1 = tk.Entry(campos)
        input_1.pack()

    elif conv == 'hexadecimal-binario':
        tk.Label(campos, text="Ingrese el numero hexadecimal que quiera convertir").pack()
        input_1 = tk.Entry(campos)
        input_1.pack()

    boton_conversion=tk.Button(campos, text='convertir', bg='white',command=convertir)
    boton_conversion.pack()
     #ETIQUETA Y CAMPO PARA MOSTRAR EL RESULTADO DE LA CONVERSION
    resultado_label = tk.Label(campos, text="Resultado:")
    resultado_e = tk.Entry(campos)
    resultado_label.pack(pady=10)
    resultado_e.pack(pady=10)
    cambiar_opcion_buton.pack(pady=20)



#ETIQUETA PRINCIPAL
tk.Label(frame3, text="Seleccione la conversión que desea realizar").pack(pady=20)

#COMBOBOX DE OPCIONES 
comboconv =ttk.Combobox (frame3,
                        width='30',
                        state="readonly",
                        values=['decimal-octal','octal-decimal','binario-hexadecinal','hexadecimal-binario'])
comboconv.pack()

#EVENTO GENERDO POR EL COMBOBOX
comboconv.bind('<<ComboboxSelected>>', opcion_seleccionada)

#BOTONES EN VENTANA 
boton_inicio =tk.Button(frame3, text='seleccione para iniciar conversión',command=conversion)
#boton cambair opcion
cambiar_opcion_buton= tk.Button(frame3, text='pulse para cambiar opcion de conversion', command=cambiar_opcion)
campos = tk.Frame(frame3)

window.mainloop()