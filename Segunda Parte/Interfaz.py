import tkinter as tk

#==========================Ventana seleccion de usuario==============================================================

def travel_windows():
    windows_for_destination = tk.Tk()
    windows_for_destination.title("Usuario")
    windows_for_destination.geometry("800x600")
    windows_for_destination.resizable(0,0)
    windows_for_destination.configure(bg="#FFF9ED")

    frame = tk.Frame(windows_for_destination, bg= "#F5A3C8")
    frame.pack(expand= True)
    etiqueta_destination = tk.Label(frame, text = "¿Ya tienes una cuenta?",font = ("Times New Roman", 18 ), fg = "white", bg="#F5A3C8")

    etiqueta_destination.grid(row = 1, column= 0, padx= 100, pady= 50)

    marco_izquierdo_for_destination = tk.Frame(windows_for_destination, bg="#FFF9ED")
    marco_izquierdo_for_destination.pack(side = "left", padx = 50)

    marco_derecho_for_destination = tk.Frame(windows_for_destination, bg="#FFF9ED")
    marco_derecho_for_destination.pack(side = "right", padx = 50)



    # etiqueta_origen = tk.Label(marco_izquierdo_for_destination, text = "Origen", font = ("Times New Roman", 18), fg = "white", bg="#0B666A")
    # etiqueta_origen.pack(pady = 10)

    # texto_origen_entry = tk.Entry(marco_izquierdo_for_destination, font = ("Times New Roman", 14))
    # texto_origen_entry.pack(pady = 10)

    # etiqueta_destino = tk.Label(marco_derecho_for_destination, text = "Destino", font = ("Times New Roman", 18), fg = "white", bg="#0B666A")
    # etiqueta_destino.pack(pady = 10)

    # texto_destino_entry = tk.Entry(marco_derecho_for_destination, font = ("Times New Roman", 14))
    # texto_destino_entry.pack(pady = 10)

    # etiqueta_fecha = tk.Label(marco_derecho_for_destination, text = "Fecha", font = ("Times New Roman", 18), fg = "white", bg="#0B666A")
    # etiqueta_fecha.pack(pady = 10)

    # texto_fecha_entry = tk.Entry(marco_derecho_for_destination, font = ("Times New Roman", 14))
    # texto_fecha_entry.pack(pady = 10)

    def tengo_cuenta():
        windows_for_destination.destroy()
        inicio_sesion()
        inicio_sesion.deiconify()

    def registro():
        windows_for_destination.destroy()
        main_windows()
        main_windows.deiconify()

    
    registrarse_buttom = tk.Button(marco_izquierdo_for_destination, text = "Registrarme", font = ("Times New Roman",14),command=registro, bg = "light green")
    registrarse_buttom.pack(side = "bottom", anchor = "s", pady = 50)

    cuenta_buttom = tk.Button(marco_derecho_for_destination, text = "Ya tengo cuenta", font = ("Times New Roman",14),command=tengo_cuenta, bg = "light green")
    cuenta_buttom.pack(side = "bottom", anchor = "s", pady = 50)

    windows_for_destination.mainloop()

#=========================================Ventana para registrarse=======================================================================

def main_windows():
    windows = tk.Tk()
    windows.title("Registro")
    windows.geometry("800x600")
    windows.resizable(0,0)
    windows.configure(bg="#23BAC4")


    etiqueta_welcome = tk.Label(windows, text="Welcome to airlines", font=("Times New Roman", 18, "bold"), fg="white", bg="#0B666A")
    etiqueta_welcome.pack(padx=100)

    
    marco_izquierda = tk.Frame(windows,bg="#23BAC4")
    marco_izquierda.pack(side = "left", padx=50)

    marco_derecha = tk.Frame(windows,bg="#23BAC4")
    marco_derecha.pack(side = "right", padx=50)

    etiqueta_nombre = tk.Label(marco_izquierda, text="Primer Nombre", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_nombre.pack(pady=10)

    texto_nombre = tk.Entry(marco_izquierda,font=("Arial", 14))
    texto_nombre.pack(pady=10)

    etiqueta_apellido = tk.Label(marco_izquierda, text="Primer Apellido", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_apellido.pack(pady=10)

    texto_apellido = tk.Entry(marco_izquierda,font=("Arial", 14))
    texto_apellido.pack(pady=10)

    etiqueta_correo = tk.Label(marco_izquierda, text="Correo Electronico", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_correo.pack(pady=10)

    texto_correo = tk.Entry(marco_izquierda,font=("Arial", 14))
    texto_correo.pack(pady=10)


    etiqueta_id = tk.Label(marco_derecha, text = "Identificacion", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_id.pack(pady=10)
    
    texto_id = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_id.pack(pady=10)

    etiqueta_telefono = tk.Label(marco_derecha, text = "Telefono", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_telefono.pack(pady=10)
    
    texto_telefono = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_telefono.pack(pady=10)

    etiqueta_genero = tk.Label(marco_derecha, text = "Genero", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_genero.pack(pady=10)
    
    texto_apellido = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_apellido.pack(pady=10)

    etiqueta_nacionalidad = tk.Label(marco_derecha, text = "Nacionalidad", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_nacionalidad.pack(pady=10)
    
    texto_nacionalidad = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_nacionalidad.pack(pady=10)

    def windows_check_in():
        windows.destroy()
        travel_windows()
        travel_windows.deiconify()

    check_in_buttom = tk.Button(windows, text="Registrarme", font = ("Times New Roman", 14), command = windows_check_in, bg = "light green")
    check_in_buttom.pack(side = "bottom", anchor = "s", pady= 50)

#============================Ventanas de inicio sesion=====================================================================================

def inicio_sesion():
    sesion = tk.Tk()
    sesion.title("Iniciar sesión")
    sesion.geometry("800x600")

    def ingreso_dato():
        sesion.destroy()
        iniciar_interfaz()
        iniciar_interfaz.deiconify()

    sesion_buttom = tk.Button(sesion, text = "Iniciar", font = ("Times New Roman", 14), command = ingreso_dato, bg = "light green")
    sesion_buttom.pack(side = "bottom", anchor = "s", pady= 50)

    sesion.mainloop()


#============================Ventanas de los 100 botones=====================================================================================
#============================================================================================================================================

opciones = [
    ['Z328', '2024-06-5', '08:13:00', '10:35:00',  'Santa Marta', 'Bogota'],
    ['X633', '2024-06-6', '02:55:00', '05:58:00',  'Santa Marta', 'Cartagena'],
    ['G611', '2024-06-12', '16:50:00', '17:07:00',  'Medellin', 'Santa Marta'],
    ['J786', '2024-06-26', '15:44:00', '16:20:00',  'Cali', 'Bogota'],
    [ 'I506', '2024-06-26', '12:13:00', '13:48:00',  'Medellin', 'Cartagena'],
    ['W151', '2024-06-27', '01:46:00', '03:28:00',  'Santa Marta', 'Bogota'],
    ['I657', '2024-06-5', '23:46:00', '2:48:00', 'Bogota', 'Medellin'],
    ['A722', '2024-06-6', '12:32:00', '14:25:00', 'Medellin', 'Santa Marta'],
    ['G542', '2024-06-27', '10:15:00', '12:58:00',  'Cali', 'Bogota'],
    ['R419', '2024-06-13', '18:45:00', '21:11:00',  'Cali', 'Bogota'],
    ['K387', '2024-06-12', '08:52:00', '12:58:00',  'Medellin', 'Cartagena'],
    ['I684', '2024-06-6', '18:25:00', '22:33:00',  'Santa Marta', 'Cartagena'],
    ['T366', '2024-06-6', '15:59:00', '16:30:00',  'Bogota', 'Medellin'],
    ['G973', '2024-06-27', '07:51:00', '09:59:00', 'Cartagena', 'Medellin'],
    ['P628', '2024-06-20', '20:47:00', '21:45:00',  'Cali', 'Bogota'],
    ['V577', '2024-06-20', '19:47:00', '23:12:00',  'Bogota', 'Medellin'],
    ['Y916', '2024-06-5', '19:05:00', '20:07:00',  'Bogota', 'Medellin'],
    ['C616', '2024-06-6', '14:43:00', '19:14:00',  'Bogota', 'Medellin'],
   ['Z502', '2024-06-27', '02:33:00', '04:46:00', 'Santa Marta', 'Medellin'],
['O706', '2024-06-19', '03:33:00', '08:12:00',  'Cartagena', 'Medellin'],
['A425', '2024-06-12', '05:16:00', '07:38:00',  'Bogota', 'Cartagena'],
['A643', '2024-06-27', '02:41:00', '06:50:00',  'Bogota', 'Santa Marta'],
['C594', '2024-06-6', '20:14:00', '22:16:00',  'Cartagena', 'Cali'],
['X712', '2024-06-5', '04:28:00', '05:47:00',  'Santa Marta', 'Cartagena'],
['X517', '2024-06-26', '13:23:00', '16:23:00', 'Cali', 'Cartagena'],
['M302', '2024-06-20', '15:15:00', '17:10:00',  'Cartagena', 'Cali'],
['X448', '2024-06-12', '14:57:00', '16:48:00',  'Medellin', 'Bogota'],
['K415', '2024-06-6', '01:59:00', '02:58:00',  'Cartagena', 'Cali'],
['N999', '2024-06-20', '00:02:00', '01:28:00',  'Cali', 'Bogota'],
['Q579', '2024-06-19', '10:13:00', '13:46:00', 'Bogota', 'Cali'],
['O632', '2024-06-5', '10:46:00', '11:04:00',  'Cali', 'Medellin'],
['W768', '2024-06-5', '00:14:00', '02:37:00',  'Cartagena', 'Santa Marta'],
['N700', '2024-06-20', '17:02:00', '21:47:00',  'Cali', 'Medellin'],
['A198', '2024-06-13', '10:07:00', '11:34:00',  'Santa Marta', 'Cali'],
['N508', '2024-06-20', '07:49:00', '11:17:00', 'Cali', 'Bogota'],
['S830', '2024-06-26', '06:11:00', '08:05:00', 'Medellin', 'Bogota'],
['B193', '2024-06-12', '11:55:00', '16:16:00', 'Santa Marta', 'Medellin'] ,
['N925', '2024-06-20', '20:09:00', '23:27:00', 'Bogota', 'Cali'],
['O805', '2024-06-19', '08:11:00', '12:14:00', 'Cartagena', 'Cali'],
['B165', '2024-06-20', '00:21:00', '03:01:00', 'Medellin', 'Cali'],
['Q419', '2024-06-6', '18:09:00', '20:04:00', 'Santa Marta', 'Bogota'],
['H905', '2024-06-6', '11:56:00', '13:11:00', 'Cali', 'Santa Marta'],
['R873', '2024-06-6', '00:14:00', '04:15:00', 'Santa Marta', 'Cali'],
['T810', '2024-06-6', '22:03:00', '00:13:00', 'Medellin', 'Santa Marta'],
['R507', '2024-06-20', '03:35:00', '05:14:00', 'Cartagena', 'Bogota'],
['E279', '2024-06-27', '03:32:00', '07:31:00', 'Cali', 'Bogota'],
['T179', '2024-06-5', '21:42:00', '23:56:00',  'Medellin', 'Bogota'],
['E348', '2024-06-6', '14:21:00', '17:45:00', 'Cartagena', 'Cali'],
['V809', '2024-06-5', '15:17:00', '18:30:00', 'Santa Marta', 'Medellin'],
['D483', '2024-06-12', '04:31:00', '09:24:00', 'Cali', 'Cartagena'],
['F592', '2024-06-20', '20:57:00', '23:35:00', 'Medellin', 'Cartagena'],
['B209', '2024-06-6', '07:51:00', '10:33:00',  'Santa Marta', 'Cartagena'] ,
['F812', '2024-06-26', '04:51:00', '08:56:00', 'Cali', 'Cartagena'],
['X552', '2024-06-26', '04:54:00', '07:10:00', 'Cartagena', 'Santa Marta'] ,
['I848', '2024-06-5', '07:45:00', '12:08:00', 'Cartagena', 'Bogota'],
['J755', '2024-06-20', '02:52:00', '07:15:00', 'Cali', 'Medellin'],
['Y216', '2024-06-19', '02:44:00', '05:12:00', 'Cartagena', 'Santa Marta'] ,
['G442', '2024-06-12', '01:09:00', '03:41:00', 'Medellin', 'Cali'],
['V932', '2024-06-12', '16:57:00', '18:53:00', 'Santa Marta', 'Medellin']   ,
['Q252', '2024-06-20', '08:20:00', '13:01:00',  'Cartagena', 'Cali'],
['D848', '2024-06-27', '11:08:00', '14:48:00',  'Bogota', 'Santa Marta'],
['S569', '2024-06-5', '14:40:00', '16:24:00',  'Bogota', 'Medellin'],
['I656', '2024-06-13', '20:31:00', '23:13:00',  'Medellin', 'Cali'],
['S129', '2024-06-6', '18:08:00', '19:08:00',  'Medellin', 'Cartagena'],
['N232', '2024-06-5', '16:35:00', '19:08:00', 'Medellin', 'Santa Marta'],
['M191', '2024-06-20', '03:11:00', '07:02:00', 'Cartagena', 'Medellin'],
['H180', '2024-06-20', '00:19:00', '02:53:00', 'Santa Marta', 'Cali'],
['V900', '2024-06-19', '10:39:00', '13:52:00', 'Santa Marta', 'Cali'],
['Q449', '2024-06-27', '18:37:00', '20:56:00', 'Santa Marta', 'Cali'],
['R250', '2024-06-26', '16:28:00', '18:29:00', 'Cali', 'Bogota'],
['T654', '2024-06-26', '12:11:00', '14:20:00', 'Santa Marta', 'Bogota'],
['Y804', '2024-06-12', '14:28:00', '16:34:00', 'Cali', 'Bogota'],
['E971', '2024-06-12', '22:07:00', '23:12:00', 'Santa Marta', 'Cartagena'] ,
['U728', '2024-06-12', '15:55:00', '18:43:00',  'Santa Marta', 'Medellin'],
['U522', '2024-06-13', '12:46:00', '14:54:00',  'Bogota', 'Cartagena'],
['V560', '2024-06-26', '08:41:00', '11:20:00', 'Santa Marta', 'Cali'],
]


contadores = [0] * len(opciones)

# Configuración de la paginación
botones_por_pagina = 10
pagina_actual = 0
total_paginas = (len(opciones) + botones_por_pagina - 1) // botones_por_pagina

def incrementar_contador(i):
    contadores[i] += 1
    labels[i].config(text=f"{opciones[i]}: {contadores[i]}")

def crear_botones(inicio, fin):
    for i in range(inicio, fin):
        boton = tk.Button(frame, text=f"{opciones[i]}", command=lambda i=i: incrementar_contador(i))
        boton.grid(row=i % 18, column=0, pady=5)
        botones.append(boton)
        labels[i] = tk.Label(frame, text=f"{opciones[i]}: {contadores[i]}")
        labels[i].grid(row=i % 18, column=1, padx=10)

def cambiar_pagina(direccion):
    global pagina_actual
    if direccion == "adelante":
        pagina_actual += 1
    elif direccion == "atras":
        pagina_actual -= 1

    if pagina_actual < 0:
        pagina_actual = 0
    elif pagina_actual >= total_paginas:
        pagina_actual = total_paginas - 1

    actualizar_botones()

def actualizar_botones():
    for boton in botones:
        boton.grid_forget()
    inicio = pagina_actual * botones_por_pagina
    fin = min((pagina_actual + 1) * botones_por_pagina, len(opciones))
    crear_botones(inicio, fin)

    if pagina_actual == total_paginas - 1:
        boton_extra.grid(row=19, column=0, columnspan=2, pady=20)
    else:
        boton_extra.grid_forget()

def iniciar_interfaz():
    global frame, frame_botones_pagina, root, labels, botones, boton_extra
    root = tk.Tk()
    root.geometry("1200x900")
    root.resizable(0,0)
    root.configure(bg="#23BAC4")
    root.title("Contadores de Opciones")

    global labels, botones
    labels = {}
    botones = []

    frame = tk.Frame(root,bg="#338DFF")
    frame.grid(row=0, column=0)

    crear_botones(0, min(botones_por_pagina, len(opciones)))

    frame_botones_pagina = tk.Frame(root, bg = "#23BAC4")
    frame_botones_pagina.grid(row=1, column=0, pady=10)

    btn_atras = tk.Button(frame_botones_pagina, text="Página anterior", command=lambda: cambiar_pagina("atras"), bg="#68FF33")
    btn_atras.grid(row=0, column=0, padx=5)

    btn_adelante = tk.Button(frame_botones_pagina, text="Página siguiente", command=lambda: cambiar_pagina("adelante"), bg="#68FF33")
    btn_adelante.grid(row=0, column=1, padx=5)

    boton_extra = tk.Button(root, text="Done", bg="#FFD700", command=asientos)

    root.mainloop()

#================================Ventana de los asientos===========================================================================
#===================================================================================================================================
def asientos():
    root.destroy()
    seats_Airplane()
    seats_Airplane.deiconify()


def crear_asientos(frame1, row, column):
    for r in range(row):
        for c in range(column):
            asiento_id = f"{chr(65+c)}{r+1}"
            if 1 <= (r+1) <= 4:
                bg_color = "lightblue"
            elif 5 <= (r+1) <= 8:
                bg_color = "lightgreen"
            else:
                bg_color = "lightcoral"
            etiqueta = tk.Label(frame1, text=asiento_id, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            etiqueta.grid(row=r, column=c, padx=5, pady=5)

def seats_Airplane():
    seats = tk.Tk()
    seats.title("Selección de Asientos de Avión")
    seats.geometry("1200x900")
    seats.resizable(1,1)
    

    row = 12  # Número de filas de asientos
    column = 6  # Número de columnas de asientos
    frame1 = tk.Frame(seats, bg="#FFF9ED")
    frame1.place(relx= 0.8, rely= 0.1, anchor= "n")
    seats.configure(bg="#FFF9ED")


    def categoria_alum():
        seats.destroy()
        aluminio()
        aluminio.deiconify()

    aluminio_buttom = tk.Button(seats, text="Aluminio", font = ("Times New Roman", 14), command=categoria_alum , bg = "light blue")
    aluminio_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    def categoria_diam():
        seats.destroy()
        diamante()
        diamante.deiconify()

    diamante_buttom = tk.Button(seats, text="Diamante", font = ("Times New Roman",14), command = categoria_diam ,bg = "light green")
    diamante_buttom.place(relx= 0.55, rely= 0.44, anchor= "n")

    def categoria_premium():
        seats.destroy()
        premium()
        premium.deiconify()

    premium_buttom = tk.Button(seats, text="Premium", font = ("Times New Roman", 14), command =categoria_premium, bg = "lightcoral")
    premium_buttom.place(relx= 0.55, rely= 0.66, anchor= "n")


    crear_asientos(frame1, row, column)
    seats.mainloop()

#========================Ventana donde se muestra los asientos de la categoria Aluminio==============================================================================================

def aluminio ():
    windows_alum = tk.Tk()
    windows_alum.title("Asientos en aluminio")
    windows_alum.geometry("800x600")
    windows_alum.mainloop()

#========================Ventana donde se muestra los asientos de la categoria Diamante==============================================================================================


def diamante ():
    winwdows_diam = tk.Tk()
    winwdows_diam.title("Asiento en Diamante")
    winwdows_diam.geometry("800x600")
    windows_diam.mainloop()

#========================Ventana donde se muestra los asientos de la categoria Premium==============================================================================================


def premium ():
    winwdows_prem = tk.Tk()
    winwdows_prem.title("Asiento en Premium")
    winwdows_prem.geometry("800x600")
    windows_prem.mainloop()    


if __name__ == '__main__':
    #main_windows()
    travel_windows()
    
#la ventana del Check-in esta hecha en google keep