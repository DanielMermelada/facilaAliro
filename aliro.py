import tkinter as tk
import subprocess
import os
import ctypes
import webbrowser

def ejecutar():
    comando = entrada_comando.get()
    
    #Prevenir errores
    comando_lower = comando
    if "CMD".lower() in comando_lower or "Time".lower() in comando_lower or "date".lower() in comando_lower:
        comando = "help"
        ctypes.windll.user32.MessageBoxW(0, "🤖 Este comando requiere un input directo y no está disponible 🤖", "⛔ Cuidado ⛔", 1)
        print("🤖 Este comando requiere un input directo y no está disponible 🤖")

    ejecutar_comando(comando)

def ejecutar_comando(comando):
    try:
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        comando_finalizado = False
        
        def actualizar_texto():
            nonlocal comando_finalizado
            
            linea = proceso.stdout.readline()
            if linea:
                texto_resultados.config(state=tk.NORMAL)
                texto_resultados.insert(tk.END, linea)
                texto_resultados.see(tk.END)
                texto_resultados.config(state=tk.DISABLED)
                #Actualiza la ventana nuevamente después de 20 ms
                ventana.after(20, actualizar_texto)
            elif not comando_finalizado:
                comando_finalizado = True
                texto_resultados.config(state=tk.NORMAL)
                texto_resultados.insert(tk.END, "\n🦊 COMANDO FINALIZADO (Puede poner otro) 🦊\n \n")
                texto_resultados.see(tk.END)
                texto_resultados.config(state=tk.DISABLED)
        
        actualizar_texto()
    
    except Exception as e:
        texto_resultados.config(state=tk.NORMAL)
        texto_resultados.insert(tk.END, str(e))
        texto_resultados.config(state=tk.DISABLED)

def borrar_texto(event):
    if entrada_comando.get() == "Ingresa aquí el comando (Avanzado)":
        entrada_comando.delete(0, tk.END)
        entrada_comando.config(fg="black")

def restaurar_texto(event):
    if entrada_comando.get() == "":
        entrada_comando.insert(0, "Ingresa aquí el comando (Avanzado)")
        entrada_comando.config(fg="gray")

def ejecutar_ipconfig():
    ejecutar_comando("ipconfig")

def ping_google():
    ejecutar_comando("ping google.com")

def tracert_google():
    ejecutar_comando("tracert google.com")

def netstat():
    ejecutar_comando("netstat")

def ipconfig():
    ejecutar_comando("ipconfig")

def scan():
    ejecutar_comando("Hostname")

def CleanMgr():
    ejecutar_comando("CleanMgr")

def slmgr_dli():
    ejecutar_comando("slmgr/dli")

def getmac():
    ejecutar_comando("getmac")

def SYSTEMINFO():
    ejecutar_comando("SYSTEMINFO")

def KLIST():
    ejecutar_comando("KLIST")

def TASKLIST():
    ejecutar_comando("TASKLIST")

def msinfo32():
    ejecutar_comando("msinfo32")

def WHOAMI():
    ejecutar_comando("WHOAMI")

def Explorer():
    ejecutar_comando("Explorer")

def eventvwr():
    ejecutar_comando("eventvwr")

def nslookup_google():
    ejecutar_comando("nslookup google.com")

def abrir_ventana():
    ventana_nueva = tk.Toplevel(ventana)
    ventana_nueva.title("🤖 Comandos para tu uso 🤖")
    ventana_nueva.geometry("765x420")
    ventana_nueva.resizable(False, False)
    ventana_nueva.configure(bg="#FFCCCC", relief="raised", bd=10)

    texto_resultadovent_frame = tk.Frame(ventana_nueva, bg="#FFCCCC", bd=10, relief="ridge")
    texto_resultadovent_frame.place(x=70, y=345, width=220, height=45)
    texto_resultadovent = tk.Text(texto_resultadovent_frame, font=("Helvetica", 12), bd=0)
    texto_resultadovent.pack(side="left", fill="both", expand=True)
    texto_resultadovent.insert(tk.END, "🖱️ Comandos de red 🖱️")
    texto_resultadovent.config(state=tk.DISABLED, bg="black", fg="#65fe08")

    texto_resultadosvent_frame = tk.Frame(ventana_nueva, bg="#FFCCCC", bd=10, relief="ridge")
    texto_resultadosvent_frame.place(x=414, y=345, width=280, height=45)
    texto_resultadosvent = tk.Text(texto_resultadosvent_frame, font=("Helvetica", 12), bd=0)
    texto_resultadosvent.pack(side="left", fill="both", expand=True)
    texto_resultadosvent.insert(tk.END, "⌨️ Comandos de administración ⌨️")
    texto_resultadosvent.config(state=tk.DISABLED, bg="black", fg="#65fe08")

    subtitulosVent = tk.Label(ventana_nueva, text="🦝", font=("Helvetica", 140), bg="#FFCCCC", fg="white")
    subtitulosVent.place(x=90, y=240, anchor="sw", width=188, height=188)

    subtitulosVent = tk.Label(ventana_nueva, text="🦝", font=("Helvetica", 140), bg="#FFCCCC", fg="white")
    subtitulosVent.place(x=458, y=240, anchor="sw", width=188, height=188)

    subtitulosVent = tk.Label(ventana_nueva, text="🤖", font=("Helvetica", 40), bg="#FFCCCC", fg="white")
    subtitulosVent.place(x=327, y=390, anchor="sw", width=50, height=50)
    
    #Lista de comandos
    comandos = [
        ("🪐 Revisa pings a internet a través de Google 🪐", ping_google),
        ("🪐 Diagnostico de red por Google (DEMORA) 🪐", tracert_google),
        ("🪐 Revisa los datos de Google 🪐", nslookup_google),
        ("🔌 Mira a que estas conectado (DEMORA) 🔌", netstat),
        ("🔌 Mira tu configuración de IP 🔌", ipconfig),
        ("🔌 Muestra las MACs de los dispositivos 🔌", getmac),
        ("🔑 Mira el nombre de tu host 🔑", scan),
        ("🔑 Muestra tus tickets de seguridad 🔑", KLIST),
        ("💻 Muestra la información de tu equipo 💻", SYSTEMINFO),
        ("💻 Revisa tu licencia de Windows 💻", slmgr_dli),
        ("ℹ️ Abre la información del sistema ℹ️", msinfo32),
        ("ℹ️ Revisa todo lo que está corriendo de fondo ℹ️", TASKLIST),
        ("👦 Revisa quien eres actualmente en este PC 👦", WHOAMI),
        ("🚮 Limpia la basura de tu equipo 🚮", CleanMgr),
        ("📁 Revisa los logs de tu equipo 📁", eventvwr),
        ("📁 Abre tu explorador de archivos 📁", Explorer)
        
    ]
    
    for i, (nombre, comando) in enumerate(comandos):
        boton = tk.Button(ventana_nueva, text=nombre, command=comando, font=("Helvetica", 12))
        boton.grid(row=i % 8, column=i // 8, padx=5, pady=5)

def cerrar_aplicacion():
    ventana.destroy()

def limpiar_resultados():
    texto_resultados.config(state=tk.NORMAL)
    texto_resultados.delete(1.0, tk.END)
    texto_resultados.config(state=tk.DISABLED)
    texto_resultados.config(state=tk.NORMAL)
    texto_resultados.insert(tk.END, "🧽 Limpio y como nuevo... 🧽\n \n")
    texto_resultados.see(tk.END)
    texto_resultados.config(state=tk.DISABLED)

def abrir_link_1():
    webbrowser.open("https://github.com/DanielMermelada/facilaAliro")

def abrir_link_2():
    webbrowser.open("https://www.paypal.me/DabaloDenmeDInero")

ventana = tk.Tk()
ventana.title("Facila Aliro v1.0")
ventana.geometry("800x510")
ventana.resizable(False, False)

ventana.configure(bg="#FFCCCC", relief="ridge", bd=10)

directorio_actual = os.path.dirname(os.path.abspath(__file__))

ruta_logo = os.path.join(directorio_actual, "logo.png")

ruta_pay = os.path.join(directorio_actual, "Pay.png")
logoPay = tk.PhotoImage(file=ruta_pay)
logoPay = logoPay.subsample(20)

ruta_git = os.path.join(directorio_actual, "Git.png")
logoGit = tk.PhotoImage(file=ruta_git)
logoGit = logoGit.subsample(20)

if os.path.exists(ruta_logo):
    ventana.iconphoto(True, tk.PhotoImage(file=ruta_logo).subsample(3))

def cargar_logo():
    if os.path.exists(ruta_logo):
        logo = tk.PhotoImage(file=ruta_logo)
        logo = logo.subsample(20)
        logo_label = tk.Label(ventana, image=logo, bg="#FFCCCC")
        logo_label.image = logo
        logo_label.place(x=735, y=485, anchor="sw", width=40, height=40)
    else:
        print("Error: No se encontró el archivo de logo")

subtitulo = tk.Label(ventana, text="", bg="#FFC2D1")
subtitulo.place(x=0, y=490, anchor="sw", width=400, height=490)

subtitulo = tk.Label(ventana, text="", bg="white")
subtitulo.place(x=395, y=490, anchor="sw", width=10, height=490)

subtitulo = tk.Label(ventana, text="", bg="#FFC2D1")
subtitulo.place(x=405, y=490, anchor="sw", width=5, height=490)

subtitulo = tk.Label(ventana, text="", bg="#FFCCCC")
subtitulo.place(x=390, y=490, anchor="sw", width=5, height=490)

entrada_comando = tk.Entry(ventana, width=50, font=("Helvetica", 12), fg="gray", bd=4, relief="sunken")
entrada_comando.place(x=50, y=60)
entrada_comando.insert(tk.END, "Ingresa aquí el comando (Avanzado)")
entrada_comando.bind("<FocusIn>", borrar_texto)
entrada_comando.bind("<FocusOut>", restaurar_texto)

boton_ejecutar = tk.Button(ventana, text="Ejecutar comando (Avanzado) 🫵", command=ejecutar, bg="black", fg="#65fe08" ,borderwidth=5, padx=10, pady=5, relief=tk.RAISED, font=("Helvetica", 12))
boton_ejecutar.place(x=250, y=100)

boton_comandos_ipconfig = tk.Button(ventana, text="Comandos (La experiencia ideal) 🤖", command=abrir_ventana, bg="white", borderwidth=5, padx=10, pady=5, relief=tk.RAISED, font=("Helvetica", 12))
boton_comandos_ipconfig.place(x=250, y=160)

boton_cerrar = tk.Button(ventana, text="❎", command=cerrar_aplicacion, bg="#FF6961", fg="white", borderwidth=10, padx=1, pady=1, relief=tk.RAISED, font=("Helvetica", 12))
boton_cerrar.place(x=720, y=10)

boton_limpiar = tk.Button(ventana, text="🧹", command=limpiar_resultados, bg="cyan", borderwidth=10, padx=3, pady=1, relief=tk.RAISED, font=("Helvetica", 12))
boton_limpiar.place(x=720, y=70)

boton_link_1 = tk.Button(ventana,  image=logoGit, command=abrir_link_1, relief="raised", bd=5, bg="white",font=("Helvetica", 20))
boton_link_1.place(x=5, y=385, anchor="sw", width=40, height=40)

boton_link_2 = tk.Button(ventana, image=logoPay, command=abrir_link_2, relief="raised", bd=5, bg="white",  font=("Helvetica", 20))
boton_link_2.place(x=5, y=435, anchor="sw", width=40, height=40)

texto_resultados_frame = tk.Frame(ventana, bg="#FFCCCC", bd=10, relief="ridge")
texto_resultados_frame.place(x=50, y=215, width=700, height=220)
texto_resultados_scrollbar = tk.Scrollbar(texto_resultados_frame, orient="vertical")
texto_resultados_scrollbar.pack(side="right", fill="y")
texto_resultados = tk.Text(texto_resultados_frame, font=("Helvetica", 12), yscrollcommand=texto_resultados_scrollbar.set, bd=0)
texto_resultados.pack(side="left", fill="both", expand=True)
texto_resultados_scrollbar.config(command=texto_resultados.yview)

texto_resultado_frame = tk.Frame(ventana, bg="#FFCCCC", bd=10, relief="ridge")
texto_resultado_frame.place(x=375, y=440, width=320, height=45)
texto_resultado = tk.Text(texto_resultado_frame, font=("Helvetica", 12), bd=0)
texto_resultado.pack(side="left", fill="both", expand=True)
texto_resultado.insert(tk.END, "😺Gracias por preferir esta aplicación...😺")
texto_resultado.config(state=tk.DISABLED, bg="black", fg="#FF69B4")

texto_resultados.insert(tk.END, "🦊 Una vez que selecciones una de las opciones (Tanto avanzada como de comandos) encontrarás aquí tus resultados 🦊\n \n")
texto_resultados.config(state=tk.DISABLED, bg="black", fg="#65fe08")

subtitulo = tk.Label(ventana, text="👍 Desarrolador: Daniel Barco López 👍", relief="ridge", bd=2, font=("Helvetica", 12, "italic"), bg="white", fg="gray")
subtitulo.place(x=10, y=480, anchor="sw", width=300, height=25)

subtitulo = tk.Label(ventana, text="💕 Bienvenid@ a Facila Aliro v1.0: Código... sin tanto código 💕", relief="ridge", bd=2, font=("Helvetica", 18, "italic"), bg="white", fg="gray")
subtitulo.place(x=10, y=50, anchor="sw", width=700, height=40)

subtitulo = tk.Label(text="🦝", font=("Helvetica", 90), bg="#FFC2D1", fg="white")
subtitulo.place(x=85, y=210, anchor="sw", width=118, height=118)

subtitulo = tk.Label(text="🦝", font=("Helvetica", 90), bg="#FFCCCC", fg="white")
subtitulo.place(x=585, y=210, anchor="sw", width=118, height=118)

ventana.after(100, cargar_logo)
ventana.mainloop()