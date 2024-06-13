import tkinter as tk
from tkinter import ttk
import random

#=========================================Ventana para registrarse=======================================================================
#========================================================================================================================================
#========================================================================================================================================

def read_user():

    gender = texto_genero.get()
    first_name = texto_nombre.get()
    last_name = texto_apellido.get()
    identification = texto_id.get()
    nationality = texto_nacionalidad.get()
    telephone = texto_telefono.get()
    email = texto_correo.get()

    try:
        if not gender:
            raise ValueError("Gender cannot be blank")
        if not first_name:
            raise ValueError("First name cannot be blank")
        if not last_name:
            raise ValueError("Last name cannot be blank")
        if not identification:
            raise ValueError("Identification cannot be blank")
        if not nationality:
            raise ValueError("Nationality cannot be blank")
        if not telephone:
            raise ValueError("Telephone cannot be blank")
        email = email_verification(email)

        with open("user_data.txt", "a") as file:
            file.write(f"Gender: {gender}\n")
            file.write(f"First name: {first_name}\n")
            file.write(f"Last name: {last_name}\n")
            file.write(f"ID: {identification}\n")
            file.write(f"Nationality: {nationality}\n")
            file.write(f"Telephone: {telephone}\n")
            file.write(f"Email: {email}\n")

        with open("user_emails.txt", "a") as e_file:
            e_file.write(email + "\n")

            # break
    except ValueError:
        print("The data you have entered is not correct")

def main_windows():
    windows = tk.Tk()
    windows.title("Registro")
    windows.geometry("800x600")
    windows.resizable(0,0)
    windows.configure(bg="#23BAC4")

    global texto_nombre, texto_apellido, texto_correo, texto_id, texto_telefono, texto_genero, texto_nacionalidad


    etiqueta_welcome = tk.Label(windows, text="Welcome to airlines", font=("Times New Roman", 18, "bold"), fg="white", bg="#0B666A")
    etiqueta_welcome.pack(padx=100)

    
    marco_izquierda = tk.Frame(windows,bg="#23BAC4")
    marco_izquierda.pack(side = "left", padx=50)

    marco_derecha = tk.Frame(windows,bg="#23BAC4")
    marco_derecha.pack(side = "right", padx=50)

    etiqueta_nombre = tk.Label(marco_izquierda, text="Name", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_nombre.pack(pady=10)


    texto_nombre = tk.Entry(marco_izquierda,font=("Arial", 14))
    texto_nombre.pack(pady=10)

    etiqueta_apellido = tk.Label(marco_izquierda, text="Last Name", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_apellido.pack(pady=10)

    texto_apellido = tk.Entry(marco_izquierda,font=("Arial", 14))
    texto_apellido.pack(pady=10)

    etiqueta_correo = tk.Label(marco_izquierda, text="Email", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_correo.pack(pady=10)


    texto_correo = tk.Entry(marco_izquierda,font=("Arial", 14))
    texto_correo.pack(pady=10)

    etiqueta_id = tk.Label(marco_derecha, text = "ID", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_id.pack(pady=10)

    
    texto_id = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_id.pack(pady=10)

    etiqueta_telefono = tk.Label(marco_derecha, text = "Telephone", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_telefono.pack(pady=10)

    texto_telefono = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_telefono.pack(pady=10)

    etiqueta_genero = tk.Label(marco_derecha, text = "Gender", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_genero.pack(pady=10)

    texto_genero = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_genero.pack(pady=10)

    etiqueta_nacionalidad = tk.Label(marco_derecha, text = "Nacionality", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_nacionalidad.pack(pady=10)
    
    texto_nacionalidad = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_nacionalidad.pack(pady=10)

    def windows_check_in():
        windows.destroy()
        inicio_sesion()
        inicio_sesion.deiconify()

    check_in_buttom = tk.Button(windows, text="Registrarme", font = ("Times New Roman", 14), command = windows_check_in, bg = "light green")
    check_in_buttom.pack(side = "bottom", anchor = "s", pady= 50)

#==================================================Ventanas de inicio sesion=======================================================
#========================================================================================================================================
#========================================================================================================================================

def user_existence():
    email = correo_entry.get()
    with open("user_emails.txt", "r") as e_file: 
        emails = e_file.readlines()
        emails = [i.strip() for i in emails]
        if email in emails:
            buscador()
        else:
            main_windows()

def email_verification(): ##arreglar parametro
    email = texto_correo.get()
    while True:
            try:
                if "@" in email and "." in email:
                    print("Email verified")
                    return email
            except:
                raise ValueError("Email not accepted, please enter a valid email.")
            
def inicio_sesion():
    sesion = tk.Tk()
    sesion.title("Iniciar sesión")
    sesion.geometry("800x600")

    def ingreso_dato():
        sesion.destroy()
        buscador()
        buscador.deiconify()

    global correo_entry

    # frame1 = tk.Frame(seats, bg="#FFF9ED")
    # frame1.place(relx= 0.8, rely= 0.1, anchor= "n")
    
    correo = tk.Label(sesion, text = "Email", font = ("Times New Roman", 18), fg = "white", bg="#0B666A")
    correo.place(relx= 0.5, rely= 0.3, anchor= "n")  

    correo_entry = tk.Entry(sesion, font = ("Times New Roman", 14), bg="#58FF9F")
    correo_entry.place(relx= 0.5, rely= 0.45, anchor= "n")
    
    sesion_buttom = tk.Button(sesion, text = "Log in", font = ("Times New Roman", 14), command =user_existence, bg = "light green")
    sesion_buttom.pack(side = "bottom", anchor = "s", pady= 50)
    
    sesion_buttom = tk.Button(sesion, text = "Iniciar", font = ("Times New Roman", 14), command = ingreso_dato, bg = "light green")
    sesion_buttom.pack(side = "bottom", anchor = "s", pady= 50)   ###ESTO SE VA A CONVERTIR EN NUESTRO BOTON DE CHECK IN

    # def regresar_seats():
    #     windows_prem.destroy()
    #     seats_Airplane()
    #     seats_Airplane.deiconify()

    

    sesion.mainloop()



#============================Ventanas de los 100 botones=====================================================================================
#============================================================================================================================================
#========================================================================================================================================


def tabladevuelos():
    flights = []
    with open(r'Segunda Parte\flights1.txt', 'r') as file:
        for line in file:
            flight_data = line.strip().split(',')
            flight_data[4] = int(flight_data[4])
            flight_data[5] = int(flight_data[5])
            flight_data[6] = int(flight_data[6])
            flights.append(flight_data)
    return flights



def filter_flights_by_route(origin, destination):
    flights = tabladevuelos()
    return [flight for flight in flights if flight[7] == origin and flight[8] == destination]

def get_dates_for_route(flights):
    return sorted(set(flight[1] for flight in flights))

def create_flight_buttons(flights_frame, flights):
    def asientos():
        buscar.destroy()
        seats_Airplane()
        seats_Airplane.deiconify()
    
    for widget in flights_frame.winfo_children():
        widget.destroy()
    
    if flights:
        for flight in flights:
            flight_text = f"FLIGHT: {flight[0]}, DEPARTURE TIME: {flight[2]}, ARRIVAL TIME: {flight[3]}"
            vuelos_button = tk.Button(flights_frame, text=flight_text, font=("Arial", 13), bg="pink", command=asientos)
            vuelos_button.pack(fill='x', pady=5)
    else:
        no_flights_label = tk.Label(flights_frame, text="We're sorry, we don't have available flights", font=("Arial", 13))
        no_flights_label.pack(fill='x', pady=5)

def select_flight():
    origin = origen_entry.get()
    destination = destino_entry.get()

    filtered_flights = filter_flights_by_route(origin, destination)
    dates = get_dates_for_route(filtered_flights)
    
    for widget in date_tabs.winfo_children():
        widget.destroy()

    if dates:
        for date in dates:
            tab = ttk.Frame(date_tabs)
            date_tabs.add(tab, text=date)
            flights_for_date = [flight for flight in filtered_flights if flight[1] == date]
            create_flight_buttons(tab, flights_for_date)
    else:
        no_flights_tab = ttk.Frame(date_tabs)
        date_tabs.add(no_flights_tab, text="No flights")
        no_flights_label = tk.Label(no_flights_tab, text="We're sorry, we don't have available flights", font=("Arial", 13))
        no_flights_label.pack(fill='x', pady=5)

def buscador():
    global vuelos, destino_entry, origen_entry, buscar, fecha_entry, date_tabs
    buscar = tk.Tk()
    buscar.title("Flight Searcher")
    buscar.geometry("800x600")

    origen_label = tk.Label(buscar, text="Origin", font=("Arial", 13))
    origen_label.place(relx= 0.17, rely= 0.05)

    opciones_origen = ["Santa Marta", "Bogota", "Cartagena", "Medellin", "Cali"]
    origen_entry = ttk.Combobox(buscar, values=opciones_origen, state='readonly')
    origen_entry.place(relx= 0.1, rely= 0.1)
    origen_entry.set("Choose the origin")

    destino_label = tk.Label(buscar, text="Destination", font=("Arial", 13))
    destino_label.place(relx= 0.67, rely= 0.05)

    destino_entry = ttk.Combobox(buscar, values=opciones_origen, state='readonly')
    destino_entry.place(relx= 0.6, rely= 0.1)
    destino_entry.set("Choose the destination")

    search_button = tk.Button(buscar, text="Search", font=("Arial", 13), command=select_flight, bg="lightblue")
    search_button.place(relx= 0.45, rely= 0.2)

    date_tabs = ttk.Notebook(buscar)
    date_tabs.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.65)

    buscar.mainloop()


#================================Ventana de los asientos===========================================================================
#===================================================================================================================================
#========================================================================================================================================




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
    seats.title("Airplane Seat Selection")
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

    aluminio_buttom = tk.Button(seats, text="Aluminium", font = ("Times New Roman", 14), command=categoria_alum , bg = "light blue")
    aluminio_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    def categoria_diam():
        seats.destroy()
        diamante()
        diamante.deiconify()

    diamante_buttom = tk.Button(seats, text="Diamond", font = ("Times New Roman",14), command = categoria_diam ,bg = "light green")
    diamante_buttom.place(relx= 0.55, rely= 0.44, anchor= "n")

    def categoria_premium():
        seats.destroy()
        premium()
        premium.deiconify()

    premium_buttom = tk.Button(seats, text="Premium", font = ("Times New Roman", 14), command =categoria_premium, bg = "lightcoral")
    premium_buttom.place(relx= 0.55, rely= 0.66, anchor= "n")

    def regresar_buscador():
        seats.destroy()
        buscador()
        buscador.deiconify()

    back_asientos_button = tk.Button(seats, text="Back", font=("Arial", 13),command=regresar_buscador, bg="lightblue")
    back_asientos_button.place(relx=0.2, rely=0.76, anchor="n")


    crear_asientos(frame1, row, column)
    seats.mainloop()

#========================Ventana donde se muestra los asientos de la categoria Aluminio==============================================================================================
#========================================================================================================================================
#========================================================================================================================================

def crear_asientos_alum(frame_alum, row_alum, column_alum):
    asientos = []
    for r in range(row_alum):
        for c in range(column_alum):
            asiento_id_alum = f"{chr(65+c)}{r+1}"
            if 1 <= (r+1) <= 4:
                bg_color = "lightblue" if 1 <= (r+1) <= 4 else "white"
            elif 5 <= (r+1) <= 8:
                bg_color = "lightgreen"
            else:
                bg_color = "lightcoral"
            etiqueta_alum = tk.Label(frame_alum, text=asiento_id_alum, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            etiqueta_alum.grid(row=r, column=c, padx=5, pady=5)
            asientos.append(etiqueta_alum)
    return asientos

def cambiar_color_asiento(asientos, boton):
    if asientos:
        asiento = random.choice(asientos)
        asiento.config(bg="orange") 
        boton.config(state=tk.DISABLED)   

def aluminio():
    windows_alum = tk.Tk()
    windows_alum.title("Aluminium Seats")
    windows_alum.geometry("1200x900")
    windows_alum.configure(bg="#FFF9ED")

    row_alum = 4  # Número de filas de asientos
    column_alum = 6  # Número de columnas de asientos
    frame_alum = tk.Frame(windows_alum, bg="#FFF9ED")
    frame_alum.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_alum.configure(bg="#FFF9ED")

    asientos = crear_asientos_alum(frame_alum, row_alum, column_alum)


    alum_buttom = tk.Button(windows_alum, text="Aluminium", font = ("Times New Roman", 14),
                    command=lambda: cambiar_color_asiento(asientos, alum_buttom), bg = "light blue")
    alum_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    def pago_():
        windows_alum.destroy()
        medio_pago()
        medio_pago.deiconify()

    pay_aluminio = tk.Button(windows_alum, text="Pay flight", font = ("Times New Roman", 14), command=pago_ , bg = "lightcoral")
    pay_aluminio.place(relx= 0.45, rely= 0.6, anchor= "n")

    def regresar_seats_alum():
        windows_alum.destroy()
        seats_Airplane()
        seats_Airplane.deiconify()

    back_aluminio_button = tk.Button(windows_alum, text="Back", font=("Arial", 13),command=regresar_seats_alum, bg="lightblue")
    back_aluminio_button.place(relx=0.2, rely=0.65, anchor="n")


    windows_alum.mainloop()


#========================Ventana donde se muestra los asientos de la categoria Diamante===============================================
#========================================================================================================================================
#========================================================================================================================================
def crear_asientos_diam(frame_diam, row_diam, column_diam):
    diam_asientos = []
    for r in range(4, 4 + row_diam):
        for c in range(column_diam):
            asiento_id_diam = f"{chr(65+c)}{r+1}"
            bg_color = "lightgreen" if r < 8 else "white"
            
            etiqueta_diam = tk.Label(frame_diam, text=asiento_id_diam, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            etiqueta_diam.grid(row=r-4, column=c, padx=5, pady=5)
            diam_asientos.append(etiqueta_diam)
    return diam_asientos

def cambiar_color_asiento_diam(diam_asientos, boton):
    if diam_asientos:
        asiento_diam = random.choice(diam_asientos)
        asiento_diam.config(bg="orange")
        boton.config(state=tk.DISABLED)
    

def diamante ():
    windows_diam = tk.Tk()
    windows_diam.title("Diamond Seats")
    windows_diam.geometry("1200x900")
    windows_diam.configure(bg="#FFF9ED")

    row_diam = 4  # Número de filas de asientos
    column_diam = 6  # Número de columnas de asientos
    frame_diam = tk.Frame(windows_diam, bg="#FFF9ED")
    frame_diam.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_diam.configure(bg="#FFF9ED")

    diam_asientos = crear_asientos_diam(frame_diam, row_diam, column_diam)


    diam_buttom = tk.Button(windows_diam, text="Diamond", font = ("Times New Roman", 14),
                    command=lambda: cambiar_color_asiento_diam(diam_asientos, diam_buttom), bg = "lightgreen")
    diam_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    def pago_():
        windows_diam.destroy()
        medio_pago()
        medio_pago.deiconify()

    pay_diamond = tk.Button(windows_diam, text="Pay flight", font = ("Times New Roman", 14), command=pago_ , bg = "lightcoral")
    pay_diamond.place(relx= 0.45, rely= 0.6, anchor= "n")

    def regresar_seats_diam():
        windows_diam.destroy()
        seats_Airplane()
        seats_Airplane.deiconify()

    back_diamond_button = tk.Button(windows_diam, text="Back", font=("Arial", 13),command=regresar_seats_diam, bg="lightblue")
    back_diamond_button.place(relx=0.2, rely=0.65, anchor="n")



    windows_diam.mainloop()

#========================Ventana donde se muestra los asientos de la categoria Premium=====================================================
#========================================================================================================================================
#========================================================================================================================================

def crear_asientos_prem(frame_prem, row_prem, column_prem):
    prem_asientos = []

    for r in range(8, 8 + row_prem):
        for c in range(column_prem):
            asiento_id_prem = f"{chr(65+c)}{r+1}"
            bg_color = "lightcoral" if 8 <= (r+1) <= 12 else "white"
            
            etiqueta_prem = tk.Button(frame_prem, text=asiento_id_prem, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            etiqueta_prem.config(command=lambda b= etiqueta_prem: cambiar_color(b, prem_asientos))
            etiqueta_prem.grid(row=r-8, column=c, padx=5, pady=5)
            prem_asientos.append(etiqueta_prem)
    return prem_asientos

def cambiar_color(boton, prem_asientos):
    boton.config(bg="orange")
    for asiento in prem_asientos:
        asiento.config(state=tk.DISABLED)


def premium ():
    windows_prem = tk.Tk()
    windows_prem.title("Premium Seats")
    windows_prem.geometry("1200x900")
    windows_prem.configure(bg="#FFF9ED")

    row_prem = 4  # Número de filas de asientos
    column_prem = 6  # Número de columnas de asientos
    frame_prem = tk.Frame(windows_prem, bg="#FFF9ED")
    frame_prem.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_prem.configure(bg="#FFF9ED")

    def pago_():
        windows_prem.destroy()
        medio_pago()
        medio_pago.deiconify()

    prem_buttom = tk.Button(windows_prem, text="Premium", font = ("Times New Roman", 14) , bg = "lightcoral")
    prem_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    

    pay_premium = tk.Button(windows_prem, text="Pay flight", font = ("Times New Roman", 14), command=pago_ , bg = "lightcoral")
    pay_premium.place(relx= 0.55, rely= 0.6, anchor= "n")

    def regresar_seats():
        windows_prem.destroy()
        seats_Airplane()
        seats_Airplane.deiconify()

    back_premium_button = tk.Button(windows_prem, text="Back", font=("Arial", 13),command=regresar_seats, bg="lightblue")
    back_premium_button.place(relx=0.2, rely=0.65, anchor="n")

    crear_asientos_prem(frame_prem, row_prem, column_prem)

    windows_prem.mainloop()    

def medio_pago():
    pago = tk.Tk()
    pago.title("Payment Methods")
    pago.geometry("800x600")
    pago.resizable(0,0)

    dato_label = tk.Label(pago, text="Card Data", font=("Arial", 16))
    dato_label.place(relx=0.4, rely=0.01)

    pago_label = tk.Label(pago, text="Owner Name", font=("Arial", 13))
    pago_label.place(relx=0.22, rely=0.17)

    pago_entry = tk.Entry(pago, font=("Arial", 13), bg="lightgreen")
    pago_entry.place(relx=0.3, rely=0.22, anchor="n")

    number_label = tk.Label(pago, text="Card Number", font=("Arial", 13))
    number_label.place(relx=0.22, rely=0.27)

    numero_entry = tk.Entry(pago, font=("Arial", 13), bg="lightgreen")
    numero_entry.place(relx=0.3, rely=0.32, anchor="n")

    cvv_label = tk.Label(pago, text="CVV", font=("Arial", 13))
    cvv_label.place(relx=0.27, rely=0.37)

    cvv_entry = tk.Entry(pago, font=("Arial", 13), bg="lightgreen")
    cvv_entry.place(relx=0.3, rely=0.42, anchor="n")

    vencimiento_label = tk.Label(pago, text="Due Date (MM/AA)", font=("Arial", 13))
    vencimiento_label.place(relx=0.16, rely=0.47)

    vencimiento_entry = tk.Entry(pago, font=("Arial", 13), bg="lightgreen")
    vencimiento_entry.place(relx=0.3, rely=0.52, anchor="n")

    total_pagar = tk.Label(pago, text="Total to Pay: (ejemplo) $2.225.000", font=("Arial", 13))
    total_pagar.place(relx=0.35, rely=0.6)

    def go_ticket():
        pago.destroy()
        tickete()
        tickete.deiconify()

    pay_button = tk.Button(pago, text="Pay", font=("Arial", 13),command=go_ticket, bg="lightblue")
    pay_button.place(relx=0.5, rely=0.65, anchor="n")

    def regresar_premium():
        pago.destroy()
        premium()
        premium.deiconify()

    back_pay_button = tk.Button(pago, text="Back", font=("Arial", 13),command=regresar_premium, bg="lightblue")
    back_pay_button.place(relx=0.2, rely=0.65, anchor="n")


    pago.mainloop()

#================================================Tiquete de viaje========================================================================================
#========================================================================================================================================
#========================================================================================================================================

def tickete():
    ticket = tk.Tk()
    ticket.title("Bording Pass")
    ticket.geometry("800x600")
    ticket.resizable(0,0)

    ticket_frame = tk.Frame(ticket,bg="darkblue")
    ticket_frame.place(relx= 0.5, rely= 0.5, anchor= "center", height= 200, width= 500)

    

    title_label = tk.Label(ticket_frame, text="Bording Pass", font=("Arial", 14),fg="white",bg="darkblue")
    title_label.pack()

    ticket_frame1 = tk.Frame(ticket,bg="pink")
    ticket_frame1.place(relx= 0.5, rely= 0.53, anchor= "center", height= 173, width= 500)




    name_label = tk.Label(ticket_frame1, text="Name passenger", font=("Arial", 12),fg="black",bg="pink")
    name_label.place(relx=0.1,rely=0.06)
    
    origin_label = tk.Label(ticket_frame1, text="Origin", font=("Arial", 12),fg="black",bg="pink")
    origin_label.place(relx=0.1,rely=0.4)

    destiny_label = tk.Label(ticket_frame1, text="Destination", font=("Arial", 12),fg="black",bg="pink")
    destiny_label.place(relx=0.1,rely=0.7)

    vuelo_label = tk.Label(ticket_frame1, text="Vuelo", font=("Arial", 12),fg="black",bg="pink")
    vuelo_label.place(relx=0.6,rely=0.3)

    seat_label = tk.Label(ticket_frame1, text="Seat", font=("Arial", 12),fg="black",bg="pink")
    seat_label.place(relx=0.6,rely=0.7)

    seat_label1 = tk.Label(ticket_frame1, text="El asiento que selecciono", font=("Arial", 11),fg="black",bg="pink")
    seat_label1.place(relx=0.6,rely=0.84)


    date_label = tk.Label(ticket_frame1, text="Date", font=("Arial", 12),fg="black",bg="pink")
    date_label.place(relx=0.8,rely=0.3)

    hour_label = tk.Label(ticket_frame1, text="Hour", font=("Arial", 12),fg="black",bg="pink")
    hour_label.place(relx=0.8, rely=0.7)

    ticket.mainloop()
    


if __name__ == '__main__':
    tickete()
    inicio_sesion()    
    
#la ventana del Check-in esta hecha en google keep
