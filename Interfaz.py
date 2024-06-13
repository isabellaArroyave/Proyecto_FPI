import tkinter as tk
from tkinter import ttk
import random
from io import open
import os
from tkinter import messagebox
import random
import string
from PIL import Image, ImageTk

#=========================================Ventana para registrarse=======================================================================
#========================================================================================================================================
#========================================================================================================================================


def read_user():
    gender = gender_text.get()
    first_name = name_text.get()
    last_name = lastname_text.get()
    identification = id_text.get()
    nationality = nationality_text.get()
    telephone = telephone_text.get()
    email = email_text.get()
    numero_tarjeta = numero_tarjeta_text.get()
    fecha_vencimiento = fecha_vencimiento_text.get()
    cvv = cvv_text.get()
    saldo = saldo_text.get()
    try:
        if len(numero_tarjeta) != 16:
            raise ValueError("Credit card number must have 16 digits")
        if len(cvv) != 3:
            raise ValueError("CVV must have 3 digits")
        if len(saldo) == 0:
            raise ValueError("Balance cannot be blank")
        if len(telephone) != 10:
            raise ValueError("Telephone must have 10 digits")
        if fecha_vencimiento[2] != "/": # 06/06
            raise ValueError("Expiration date must be in format dd/mm")
        if len(fecha_vencimiento) != 5:
            raise ValueError("Expiration date must be in format dd/mm")
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
        if not email:
            raise ValueError("Email cannot be blank")
        if not numero_tarjeta:
            raise ValueError("Credit card number cannot be blank")
        if not fecha_vencimiento:
            raise ValueError("Expiration date cannot be blank")
        if not cvv:
            raise ValueError("CVV cannot be blank")
        if not saldo:
            raise ValueError("Balance cannot be blank")
        if comprobar_correo(email):
            messagebox.showerror("Error", "Email already exists")
            raise ValueError("Email already exists")
        
        
        # email = email_verification()

        # Guardar datos del usuario
        with open("user_data.txt", "a") as file:
            file.write(f"\n{gender},{first_name},{last_name},{identification},{nationality},{telephone},{email},{numero_tarjeta},{fecha_vencimiento},{cvv},{saldo}")
    except ValueError:
        messagebox.showerror("Error", "Please fill all the fields")
def comprobar_correo(correo):
    print(correo)
    print("@" not in correo)
    print("." not in correo)
    if "@" not in correo and "." not in correo:
        return False
    else:
        with open("user_data.txt", "r") as e_file: 
            emails = e_file.read().strip()  # Elimina espacios en blanco al inicio y al final
            if len(emails) == 0:  
                return False
            emails = emails.split("\n")
            all_emails = [mail.split(",") for mail in emails]
            for i in range(len(all_emails)):
                if correo == all_emails[i][6]:
                    return True
        return False
def main_windows():
    windows = tk.Tk()
    windows.title("Registrate")
    windows.geometry("1200x950")
    windows.resizable(0,0)
    windows.configure(bg="#FF7D81")

    global name_text, lastname_text, gender_text, nationality_text, telephone_text, email_text, id_text
    global numero_tarjeta_text, fecha_vencimiento_text, cvv_text, saldo_text

    main_framed = tk.Frame(windows, bg="white", highlightthickness=2)
    main_framed.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.99, relheight=0.99)

    welcome_label = tk.Label(main_framed, text="REGISTER", font=("Arial", 14, "bold"), bg="#FF7D81")
    welcome_label.pack(pady=10)

    # Primera fila
    row1_frame = tk.Frame(main_framed, bg="#FF7D81")
    row1_frame.pack(fill="x", pady=10)

    name_label = tk.Label(row1_frame, text="Name", font=("Arial", 11), bg="#FF7D81", width=12)
    name_label.pack(side="left", padx=10)

    name_text = tk.Entry(row1_frame, font=("Arial", 14), width=10)
    name_text.pack(side="left", padx=10)

    lastname_label = tk.Label(row1_frame, text="Last Name", font=("Arial", 11), bg="#FF7D81", width=12)
    lastname_label.pack(side="left", padx=10)

    lastname_text = tk.Entry(row1_frame, font=("Arial", 14), width=10)
    lastname_text.pack(side="left", padx=10)

    gender_label = tk.Label(row1_frame, text="Gender", font=("Arial", 11), bg="#FF7D81", width=12)
    gender_label.pack(side="left", padx=10)

    gender_text = tk.Entry(row1_frame, font=("Arial", 14), width=10)
    gender_text.pack(side="left", padx=10)

    nationality_label = tk.Label(row1_frame, text="Nationality", font=("Arial", 11), bg="#FF7D81", width=12)
    nationality_label.pack(side="left", padx=10)

    nationality_text = tk.Entry(row1_frame, font=("Arial", 14), width=10)
    nationality_text.pack(side="left", padx=10)

    # Segunda fila
    row2_frame = tk.Frame(main_framed, bg="#FF7D81")
    row2_frame.pack(fill="x", pady=10)

    telephone_label = tk.Label(row2_frame, text="Telephone", font=("Arial", 11), bg="#FF7D81", width=12)
    telephone_label.pack(side="left", padx=10)

    telephone_text = tk.Entry(row2_frame, font=("Arial", 14), width=10)
    telephone_text.pack(side="left", padx=10)

    email_label = tk.Label(row2_frame, text="Email", font=("Arial", 11), bg="#FF7D81", width=12)
    email_label.pack(side="left", padx=10)

    email_text = tk.Entry(row2_frame, font=("Arial", 14), width=10)
    email_text.pack(side="left", padx=10)

    id_label = tk.Label(row2_frame, text="ID", font=("Arial", 11), bg="#FF7D81", width=12)
    id_label.pack(side="left", padx=10)

    id_text = tk.Entry(row2_frame, font=("Arial", 14), width=10)
    id_text.pack(side="left", padx=10)

    # Tercera fila
    row3_frame = tk.Frame(main_framed, bg="#FF7D81")
    row3_frame.pack(fill="x", pady=10)

    numero_tarjeta_label = tk.Label(row3_frame, text="Credit Card Number", font=("Arial", 11), bg="#FF7D81", width=12)
    numero_tarjeta_label.pack(side="left", padx=10)

    numero_tarjeta_text = tk.Entry(row3_frame, font=("Arial", 14), width=10)
    numero_tarjeta_text.pack(side="left", padx=10)

    fecha_vencimiento_label = tk.Label(row3_frame, text="Expiration Date", font=("Arial", 11), bg="#FF7D81", width=12)
    fecha_vencimiento_label.pack(side="left", padx=10)

    fecha_vencimiento_text = tk.Entry(row3_frame, font=("Arial", 14), width=10)
    fecha_vencimiento_text.pack(side="left", padx=10)

    cvv_label = tk.Label(row3_frame, text="CVV", font=("Arial", 11), bg="#FF7D81", width=12)
    cvv_label.pack(side="left", padx=10)

    cvv_text = tk.Entry(row3_frame, font=("Arial", 14), width=10)
    cvv_text.pack(side="left", padx=10)

    saldo_label = tk.Label(row3_frame, text="Balance", font=("Arial", 11), bg="#FF7D81", width=12)
    saldo_label.pack(side="left", padx=10)

    saldo_text = tk.Entry(row3_frame, font=("Arial", 14), width=10)
    saldo_text.pack(side="left", padx=10)

    def windows_check_in():
        read_user()
        windows.destroy()
        log_in()

    check_in_button = tk.Button(main_framed, text="Sign in", font=("Arial", 14), command=windows_check_in, bg="light green")
    check_in_button.pack(side="bottom", pady=20)

    windows.mainloop()

    def windows_check_in():
        read_user()
        windows.destroy()
        log_in()

    check_in_button = tk.Button(main_framed, text="Sign in to", font=("Times New Roman", 14), command=windows_check_in, bg="light green")
    check_in_button.pack(side="bottom", anchor="s", pady=50)

    windows.mainloop()

    def windows_check_in():
        read_user()
        windows.destroy()
        log_in()

    check_in_buttom = tk.Button(windows, text="Sign in to", font = ("Times New Roman", 14), command = windows_check_in, bg = "light green")
    check_in_buttom.pack(side = "bottom", anchor = "s", pady= 50)

#==================================================Ventanas de inicio sesion=======================================================
#========================================================================================================================================
#========================================================================================================================================

def user_existence():
    email = e_text.get()
    if email_verification():
        with open("user_data.txt", "r") as e_file: 
            emails = e_file.read()
            if emails == "":
                messagebox.showerror("Error", "Email not found, please register")
                main_windows()
                return 
            emails = emails.split("\n")
            all_emails = [mail.split(",") for mail in emails]
            for i in range(len(all_emails)):
                if email  == all_emails[i][6]:
                    messagebox.showinfo("Welcome", "Welcome to the airline")
                    searcher(email)
                    
                    return
            messagebox.showerror("Error", "Email not found, please register")
            main_windows()
    else:        
        log_in()
        return 
def email_verification():
    email = e_text.get()
    while True:
            try:
                if "@" in email and "." in email:
                    print("Email verified")
                    return True
                else:
                    raise ValueError("Email not accepted, please enter a valid email.")
                    
            except:
                messagebox.showerror("Error", "Email not accepted, please enter a valid email.")
                sesion.witdraw()
                return False     
            
def log_in():
    global sesion, e_text
    mensaje = []
    sesion = tk.Tk()
    sesion.resizable(1,1)
    sesion.title("Log in")
    sesion.geometry("1200x950")
    sesion.config(bg="#FF7D81")
    def enter_data():
        sesion.withdraw()
        user_existence()

    main_framed = tk.Frame(sesion, bg="white", highlightthickness=2)
    main_framed.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.99, relheight=0.99)

    frame_diam = tk.Label(sesion, bg="white", borderwidth=1, highlightbackground="black", highlightthickness=3)
    frame_diam.place(relx=0.5, rely=0.5, anchor="center", width=310, height=400)

    email = tk.Label(sesion, text = "Email", font = ("Arial", 14), fg = "white", bg="#0B666A")
    email.place(relx= 0.5, rely= 0.45, anchor= "n")  

    e_text = tk.Entry(sesion, font = ("Arial", 11), bg="white")
    e_text.place(relx= 0.5, rely= 0.5, anchor= "n", width=200, height=40)
    mensaje.append(e_text.get())
    
    def check(mensaje):
        sesion.destroy()
        check_in(mensaje)
    

    
    sesion_buttom = tk.Button(sesion, text = "Check-in", font = ("arial", 11), command=lambda:check(mensaje), bg = "#FF7D81")
    sesion_buttom.pack(side = "bottom", anchor = "s", pady= 50) 
    
    sesion_buttom = tk.Button(sesion, text = "Log in", font = ("arial", 11), command = enter_data, bg = "#FF7D81")
    sesion_buttom.place(relx=0.5, rely= 0.6, anchor="center", width= 200) 

    sesion.mainloop()

#============================Ventana check in=====================================================================================
#============================================================================================================================================
#========================================================================================================================================


def check_in(mensaje):
    check = tk.Tk()
    check.title("Airlines")
    check.geometry("1200x950")
    check.configure(bg = "pink")
    check.resizable(0,0)

    code_label = tk.Label(check, text="Code", font=("Times New Roman", 18), bg="pink")
    code_label.place(relx=0.24, rely=0.4)

    code_entry = tk.Entry(check, font=("Arial", 14))
    code_entry.place(relx=0.15, rely=0.47)
    mensaje.append(code_entry.get())
    lastname_label = tk.Label(check, text="Last Name", font=("Times New Roman", 18), bg="pink")
    lastname_label.place(relx=0.64, rely=0.4)

    lastname_entry = tk.Entry(check, font=("Arial", 14))
    lastname_entry.place(relx=0.55, rely=0.47)
    mensaje.append(lastname_entry.get())

    
    def pase_asiento(mensaje):
        check.destroy()
        ticket(mensaje)

    check_in_button = tk.Button(check, text="Check-in", font=("Times New Roman", 14),command=lambda: pase_asiento(mensaje), bg="light green")
    check_in_button.place(relx=0.5, rely=0.6, anchor="n")

    check.mainloop()







#============================Ventanas de los 100 botones=====================================================================================
#============================================================================================================================================
#========================================================================================================================================

def flights_m():
    flights = []
    with open('flights1.txt', 'r') as file:
        for line in file:
            flight_data = line.strip().split(',')
            flight_data[4] = int(flight_data[4])
            flight_data[5] = int(flight_data[5])
            flight_data[6] = int(flight_data[6])
            flights.append(flight_data)
    return flights

def filter_flights_by_route(origin, destination):
    flights = flights_m()
    return [flight for flight in flights if flight[7] == origin and flight[8] == destination]

def get_dates_for_route(flights):
    return sorted(set(flight[1] for flight in flights))

def create_flight_buttons(tab, flights, correo):
    def seats(mensaje):
        with open("user_data.txt", "r") as personas:
            personas = personas.read()
            personas = personas.split("\n")
            personas = [persona.split(",") for persona in personas]
        for i in range(len(personas)):
            if correo == personas[i][6]:
                datos = []
                datos.append(personas[i][1])
                datos.append(personas[i][2])
                datos.append(personas[i][3])
                datos.append(personas[i][4])
                datos.append(personas[i][5])
                datos.append(personas[i][6])
                datos.append(personas[i][7])
                datos.append(personas[i][8])
                datos.append(personas[i][9])
                datos.append(personas[i][10])
                mensaje.append(datos)
                
        print(mensaje)
        search.destroy()
        seats_Airplane(mensaje)

    for i, flight in enumerate(flights):
        flight_text = f"""          {flight[2]}  - - - - - - - - - - - - - -  {flight[3]} 

From   COP {flight[6]}"""
       
        vuelos_frame = tk.Frame(tab, bg="BLUE", bd=1, relief="solid")
        vuelos_frame.pack(fill='x', pady=5)

        select_button = tk.Button(vuelos_frame, text=flight_text, font=("Arial", 11), command=lambda f=flight: seats(f), bg= "white", fg="black")
        select_button.pack(fill="x")

def show_cheapest_flights(correo):
    for tab in date_tabs.tabs():
        tab_id = date_tabs.index(tab)
        tab_widget = date_tabs.nametowidget(tab)

        # Get flight buttons in the current tab
        flight_frames = tab_widget.winfo_children()

        # Extract flight prices and associated frames
        flight_info = []
        for frame in flight_frames:
            for button in frame.winfo_children():
                flight_text = button.cget("text")
                price_str = flight_text.split("COP ")[1]
                price = float(price_str.replace(",", ""))
                flight_info.append((price, frame))

        # Find the cheapest flight
        if flight_info:
            cheapest_flight_frame = min(flight_info, key=lambda x: x[0])[1]
            for frame in flight_frames:
                frame.pack_forget()  # Hide all flight frames
            cheapest_flight_frame.pack(fill='x', pady=5)   # Show only the cheapest flight

def select_flight(correo):
    origin = origin_entry.get()
    destination = dest_entry.get()

    filtered_flights = filter_flights_by_route(origin, destination)
    dates = get_dates_for_route(filtered_flights)

    for widget in date_tabs.winfo_children():
        widget.destroy()

    if dates:
        for date in dates:
            tab = ttk.Frame(date_tabs)
            date_tabs.add(tab, text=date)
            flights_for_date = [flight for flight in filtered_flights if flight[1] == date]
            create_flight_buttons(tab, flights_for_date, correo)
    else:
        no_flights_tab = ttk.Frame(date_tabs)
        date_tabs.add(no_flights_tab, text="No flights")
        no_flights_label = tk.Label(no_flights_tab, text="We're sorry, we don't have available flights", font=("Arial", 13))
        no_flights_label.pack(fill='x', pady=5)

def searcher(correo):
    global origin_entry, dest_entry, search, date_tabs
    search = tk.Tk()
    search.resizable(0,0)
    search.config(bg="#FF7D81")
    search.title("Flight Searcher")
    search.geometry("1200x950")

    main_frame = tk.Frame(search, bg="white", bd=10)
    main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.99, relheight=0.99)

    scuare = tk.Label(search, bg="white", borderwidth=1, highlightbackground="black", highlightthickness=2.5)
    scuare.place(relx=0.5, rely=0.1, anchor="center", width=1155, height=158)

    scuare2 = tk.Label(search, bg="white", borderwidth=1, highlightbackground="black", highlightthickness=2.5)
    scuare2.place(relx=0.5, rely=0.22, anchor="center", width=1155, height=206)

    scuare3 = tk.Label(search, bg="white", borderwidth=1, highlightbackground="black", highlightthickness=3)
    scuare3.place(relx=0.25, rely=0.21, anchor="center", width=525, height=158)

    scuare4 = tk.Label(search, bg="white", borderwidth=1, highlightbackground="black", highlightthickness=3)
    scuare4.place(relx=0.75, rely=0.21, anchor="center", width=450, height=158)

    scuare6 = tk.Label(search, bg="#FF7D81", borderwidth=1, highlightbackground="black", highlightthickness=3, font=("ARIAL", 14))
    scuare6.place(relx=0.25, rely=0.07, anchor="center", width=450, height=55)

    scuare7 = tk.Label(search, bg="#FF7D81", borderwidth=1, highlightbackground="black", highlightthickness=3, font=("ARIAL", 14))
    scuare7.place(relx=0.75, rely=0.07, anchor="center", width=450, height=55)

    scuare5 = tk.Label(search, bg="#FF7D81", borderwidth=1, highlightbackground="black", highlightthickness=3, text="FLIGHTS", font=("ARIAL", 14))
    scuare5.place(relx=0.5, rely=0.04, anchor="center", width=450, height=75)

    origin_label = tk.Label(search, text="ORIGIN                                     ", font=("Arial", 12), bg="white")
    origin_label.place(relx=0.14, rely=0.18, anchor="center")

    origin_options = ["Santa Marta", "Bogota", "Cartagena", "Medellin", "Cali"]
    origin_entry = ttk.Combobox(search, values=origin_options, state='readonly', font=("arial", 11))
    origin_entry.place(relx=0.14, rely=0.22, anchor="center", width=210, height=30)
    origin_entry.set("Choose the origin")

    destino_label = tk.Label(search, text="DESTINATION                            ", font=("Arial", 12), bg="white")
    destino_label.place(relx=0.34, rely=0.18, anchor="center")

    dest_entry = ttk.Combobox(search, values=origin_options, state='readonly', font=("arial", 11))
    dest_entry.place(relx=0.34, rely=0.22, anchor="center", width=210, height=30)
    dest_entry.set("Choose the destination")

    search_button = tk.Button(search, text="Search", font=("Arial", 12), command=lambda: select_flight(correo), bg="lightblue")
    search_button.place(relx=0.5, rely=0.3, anchor="center", width=450)

    filter_button = tk.Button(search, text="CHEAPER OPTION", font=("Arial", 11), command=lambda: show_cheapest_flights(correo), bg="#D6E5AE")
    filter_button.place(relx=0.75, rely=0.21, width=300, anchor="center")

    date_tabs = ttk.Notebook(search)
    date_tabs.place(relx=0.5, rely=0.65, anchor="center", width=1155, height=616)

    search.mainloop()


#================================Ventana de los seats===========================================================================
#===================================================================================================================================
#========================================================================================================================================


def crear_asientos(frame1, row, column):
    for r in range(row):
        for c in range(column):
            asiento_id = f"{chr(65+c)}{r+1}"
            if 1 <= (r+1) <= 4:
                bg_color = "#D5E6B0"
            elif 5 <= (r+1) <= 8:
                bg_color = "#A0C2E5"
            else:
                bg_color = "#FF7D81"
            
            etiqueta = tk.Label(frame1, text=asiento_id, width=5, height=2,
                                bg=bg_color, relief="raised", borderwidth=1,
                                highlightbackground="black", highlightthickness=2)
            etiqueta.grid(row=r, column=c, padx=5, pady=5)

def seats_Airplane(mensaje):
    seats = tk.Tk()
    seats.title("Airplane Seat Selection")
    seats.geometry("1200x950")
    seats.resizable(1, 1)

    main_frame = tk.Frame(seats, bg="white", bd=10)
    main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.99, relheight=0.99)

    frame1 = tk.Frame(main_frame, bg="white", borderwidth=1, highlightbackground="black", highlightthickness=2)
    frame1.place(relx=0.8, rely=0.5, anchor="center")

    row = 12  # Número de filas de asientos
    column = 6  # Número de columnas de asientos

    seats_title = tk.Label(seats, text="SEATS PLACEMENT", bg="white", font=("Arial", 18))
    seats_title.place(relx=0.8, rely=0.08, anchor="center")

    seats.configure(bg="#FF7D81")

    deco = tk.Label(seats, bg="black")
    deco.place(relx=0.2, rely=0.2, anchor="center", width=320, height=1511)

    deco2 = tk.Label(seats, bg="white")
    deco2.place(relx=0.2, rely=0.2, anchor="center", width=310, height=1511)

    crear_asientos(frame1, row, column)

    # # Cargar y redimensionar imágenes
    # imagen_a = Image.open("frog.png").resize((320, 180))
    # imagen_d = Image.open("cinamoroll.png").resize((320, 180))
    # imagen_p = Image.open("pochaco.png").resize((320, 180))

    # # Crear PhotoImage
    # img = ImageTk.PhotoImage(imagen_a)
    # imgd = ImageTk.PhotoImage(imagen_d)
    # imgp = ImageTk.PhotoImage(imagen_p)

    # # Guardar referencias a las imágenes
    # seats.img = img
    # seats.imgd = imgd
    # seats.imgp = imgp

    # # Mostrar imágenes
    # imagen_muestra = tk.Label(seats, image=img, borderwidth=1, highlightbackground="white", highlightthickness=2)
    # imagen_muestra.place(relx=0.45, rely=0.14, anchor="center")

    # imagen_muestrad = tk.Label(seats, image=imgd, borderwidth=1, highlightbackground="white", highlightthickness=2)
    # imagen_muestrad.place(relx=0.45, rely=0.48, anchor="center")

    # imagen_muestrap = tk.Label(seats, image=imgp, borderwidth=1, highlightbackground="white", highlightthickness=2)
    # imagen_muestrap.place(relx=0.45, rely=0.8, anchor="center")


    def aluminium_category(mensaje):
        seats.destroy()
        aluminium(mensaje)


    aluminio_label = tk.Button(seats, text="Aluminium", font=("Arial", 13), bg="#C7A780", command=lambda: aluminium_category(mensaje))
    aluminio_label.place(relx=0.4, rely=0.155)

    def diamond_category(mensaje):
        seats.destroy()
        diamond(mensaje)
    
    diamante_label = tk.Button(seats, text="Diamond", font=("Arial", 13), bg="#C7A780", command=lambda: diamond_category(mensaje))
    diamante_label.place(relx=0.4, rely=0.5)

    def premium_category(mensaje):
        seats.destroy()
        premium(mensaje)
    
    premium_label = tk.Button(seats, text="Premium", font=("Arial", 13), bg="#C7A780", command=lambda: premium_category(mensaje))
    premium_label.place(relx=0.4, rely=0.82)

    aluminio_info = tk.Label(seats, bg="#D5E6B0", text="""1 artículo personal (bolso) (Debe caber debajo del asiento)

1 equipaje de mano (10 kg) (Desde $195.100 COP)

Equipaje de bodega (23 kg) (Desde $175.600 COP)

Asiento Economy (Aleatoria-clasificado Aluminio)

Cambios de vuelo (No es permitido)

Reembolso (No es permitido)""", font=("Arial", 10), wraplength=260, anchor='w', borderwidth=1, highlightbackground="black", highlightthickness=3)

    aluminio_info.place(relx=0.2, rely=0.17, anchor="center", width=280, height=280)

    diamante_info = tk.Label(seats, bg="#A0C2E5", text="""1 artículo personal (bolso) (Debe caber debajo del asiento)

1 equipaje de bodega (23 kg) (Debe caber en el compartimiento superior)

1 equipaje de mano (10 kg) (Entrega el equipaje en el counter)

Asiento Economy (Filas específicas disponibles de manera aleatoria)

Cambios de vuelo (No es permitido)

Reembolso (No es permitido)""", font=("Arial", 10), wraplength=260, anchor='w', borderwidth=1, highlightbackground="black", highlightthickness=3)

    diamante_info.place(relx=0.2, rely=0.5, anchor="center", width=280, height=280)

    premium_info = tk.Label(seats, bg="#FF7D81", text="""1 artículo personal (bolso) (Debe caber debajo del asiento)

1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)

1 equipaje de bodega (23 kg) (Entrega el equipaje en el counter)

Asiento Plus (Sujeto a disponibilidad-clasificado Premium)

Cambios de vuelo (Sin cargo por cambio, antes del vuelo)

Reembolso (No es permitido)""", font=("Arial", 10), wraplength=260, anchor='w', borderwidth=1, highlightbackground="black", highlightthickness=3)

    premium_info.place(relx=0.2, rely=0.83, anchor="center", width=280, height=280)

    def regresar_buscador():
        seats.destroy()
        searcher(correo)

    back_asientos_button = tk.Button(seats, text="Back", font=("Arial", 11), command=regresar_buscador, bg="lightblue")
    back_asientos_button.place(relx=0.95, rely=0.9, anchor="n", width=200)

    seats.mainloop()


#========================Ventana donde se muestra los seats de la categoria aluminium==============================================================================================
#========================================================================================================================================
#========================================================================================================================================
def create_aluminium_seats(frame_alum, row_alum, column_alum):
    seats = []
    for r in range(row_alum):
        for c in range(column_alum):
            aluminium_id_seat = f"{chr(65+c)}{r+1}"
            if 1 <= (r+1) <= 4:
                bg_color = "lightblue" if 1 <= (r+1) <= 4 else "white"
            elif 5 <= (r+1) <= 8:
                bg_color = "lightgreen"
            else:
                bg_color = "lightcoral"
            alum_label = tk.Label(frame_alum, text=aluminium_id_seat, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            alum_label.grid(row=r, column=c, padx=5, pady=5)
            seats.append(alum_label)
    return seats

def switch_color_seat(seats, boton, mensaje):
    if seats:
        seat = random.choice(seats)
        mensaje.append(seat.cget("text"))
        seat.config(bg="orange") 
        boton.config(state=tk.DISABLED)   
  
def aluminium(mensaje):
    global windows_alum
    windows_alum = tk.Tk()
    windows_alum.title("Aluminium Seats")
    windows_alum.geometry("1200x900")
    windows_alum.configure(bg="#FFF9ED")

    row_alum = 4  # Número de filas de seats
    column_alum = 6  # Número de columnas de seats
    frame_alum = tk.Frame(windows_alum, bg="#FFF9ED")
    frame_alum.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_alum.configure(bg="#FFF9ED")

    seats = create_aluminium_seats(frame_alum, row_alum, column_alum)


    alum_buttom = tk.Button(windows_alum, text="Aluminium", font = ("Times New Roman", 14),
                    command=lambda: switch_color_seat(seats, alum_buttom, mensaje), bg = "light blue")
    alum_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")
    print(mensaje)

    def payment_(mensaje):
        windows_alum.destroy()
        mensaje.append("Aluminium")
        print(mensaje)
        pay_method(mensaje)

    pay_aluminium = tk.Button(windows_alum, text="Pay flight", font = ("Times New Roman", 14), command=lambda:payment_(mensaje) , bg = "lightcoral")
    pay_aluminium.place(relx= 0.45, rely= 0.6, anchor= "n")

    def back_to_seats_alum(mensaje):
        windows_alum.destroy()
        seats_Airplane(mensaje)
        seats_Airplane.deiconify()

    back_aluminium_button = tk.Button(windows_alum, text="Back", font=("Arial", 13),command=lambda:back_to_seats_alum(mensaje), bg="lightblue")
    back_aluminium_button.place(relx=0.2, rely=0.65, anchor="n")


    windows_alum.mainloop()

#========================Ventana donde se muestra los seats de la categoria Premium=====================================================
#========================================================================================================================================
#========================================================================================================================================

def create_premium_seats(frame_prem, row_prem, column_prem, mensaje):
    prem_seats = []

    for r in range(8, 8 + row_prem):
        for c in range(column_prem):
            premium_id_seat = f"{chr(65+c)}{r+1}"
            bg_color = "lightcoral" if 8 <= (r+1) <= 12 else "white"
            
            label_prem = tk.Button(frame_prem, text=premium_id_seat, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            label_prem.config(command=lambda b= label_prem: switch_color(b, prem_seats, mensaje))
            label_prem.grid(row=r-8, column=c, padx=5, pady=5)
            prem_seats.append(label_prem)
    return prem_seats


def switch_color(boton, prem_seats,mensaje):
    boton.config(bg="orange")
    for seat in prem_seats:
        if seat != boton:  # Asegura que el botón seleccionado no se deshabilite
            seat.config(state=tk.DISABLED)
        seat.config(state=tk.DISABLED)
    print(seat.cget("text"))
    mensaje.append(boton.cget("text"))


def premium (mensaje):
    windows_prem = tk.Tk()
    windows_prem.title("Premium Seats")
    windows_prem.geometry("1200x900")
    windows_prem.configure(bg="#FFF9ED")

    row_prem = 4  # Número de filas de seats
    column_prem = 6  # Número de columnas de seats
    frame_prem = tk.Frame(windows_prem, bg="#FFF9ED")
    frame_prem.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_prem.configure(bg="#FFF9ED")

    def payment_(mensaje):
        windows_prem.destroy()
        mensaje.append("Premium")
        print(mensaje)
        
        pay_method(mensaje)

    prem_buttom = tk.Button(windows_prem, text="Premium", font = ("Times New Roman", 14) , bg = "lightcoral")
    prem_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    pay_premium = tk.Button(windows_prem, text="Pay flight", font = ("Times New Roman", 14), command=lambda: payment_(mensaje) , bg = "lightcoral")
    pay_premium.place(relx= 0.55, rely= 0.6, anchor= "n")

    def back_to_seats():
        windows_prem.destroy()
        seats_Airplane()
        seats_Airplane.deiconify()

    back_premium_button = tk.Button(windows_prem, text="Back", font=("Arial", 13),command=back_to_seats, bg="lightblue")
    back_premium_button.place(relx=0.2, rely=0.65, anchor="n")

    create_premium_seats(frame_prem, row_prem, column_prem, mensaje)

    windows_prem.mainloop()    

def pay_method(mensaje):
    global payment
    payment = tk.Tk()
    payment.title("Payment Methods")
    payment.geometry("800x600")
    payment.resizable(0,0)

    data_label = tk.Label(payment, text="Card Data", font=("Arial", 16))
    data_label.place(relx=0.4, rely=0.01)

    payment_label = tk.Label(payment, text="Owner Name", font=("Arial", 13))
    payment_label.place(relx=0.22, rely=0.17)

    payment_entry = tk.Label(payment, text= f"{mensaje[9][1]}" , font=("Arial", 13), bg="lightgreen")
    payment_entry.place(relx=0.3, rely=0.22, anchor="n")

    number_label = tk.Label(payment, text="Card Number", font=("Arial", 13))
    number_label.place(relx=0.22, rely=0.27)

    number_entry = tk.Label(payment, text= f"{mensaje[9][6]}" , font=("Arial", 13), bg="lightgreen")
    number_entry.place(relx=0.3, rely=0.32, anchor="n")

    cvv_label = tk.Label(payment, text="CVV", font=("Arial", 13))
    cvv_label.place(relx=0.27, rely=0.37)

    cvv_entry = tk.Label(payment, text= f"{mensaje[9][8]}" , font=("Arial", 13), bg="lightgreen")
    cvv_entry.place(relx=0.3, rely=0.42, anchor="n")

    expiration_label = tk.Label(payment, text="Due Date (MM/AA)", font=("Arial", 13))
    expiration_label.place(relx=0.16, rely=0.47)

    expiration_entry = tk.Label(payment, text= f"{mensaje[9][7]}" , font=("Arial", 13), bg="lightgreen")
    expiration_entry.place(relx=0.3, rely=0.52, anchor="n")

    balance_label = tk.Label(payment, text="Current Balance", font=("Arial", 13))
    balance_label.place(relx=0.27, rely=0.57)
    saldo = 0
    if mensaje[11] == "Aluminium":
        total_payment = tk.Label(payment, text=f"Total to Pay: {mensaje[4]} ", font=("Arial", 13))
        saldo = mensaje[4]
    if mensaje[11] == "Diamond":
        total_payment = tk.Label(payment, text=f"Total to Pay: {mensaje[5]} ", font=("Arial", 13))
        saldo = mensaje[5]
    if mensaje[11] == "Premium":
        total_payment = tk.Label(payment, text=f"Total to Pay: {mensaje[6]} ", font=("Arial", 13))
        saldo = mensaje[6]
    total_payment.place(relx=0.3, rely=0.62, anchor="n")

    def go_ticket(mensaje):
        payment.destroy()
        ticket(mensaje)
        ticket_v.deiconify()
    def comprobar_saldo(valor,mensaje):
        print(valor)
        print(mensaje[9][9])
        if int(mensaje[9][9]) >= int(valor):
            messagebox.showinfo("Payment", "Payment successful")
            mensaje[9][9] = str(int(mensaje[9][9]) - int(valor))
            go_ticket(mensaje)
        else:
            payment.destroy()
            messagebox.showerror("Error", "Insufficient balance")
            log_in()
            
    pay_button = tk.Button(payment, text="Pay", font=("Arial", 13),command=lambda:(comprobar_saldo(saldo,mensaje)), bg="lightblue")
    pay_button.place(relx=0.5, rely=0.65, anchor="n")

    def back_to_premium():
        payment.destroy()
        premium()
        premium.deiconify()

    back_pay_button = tk.Button(payment, text="Back", font=("Arial", 13),command=back_to_premium, bg="lightblue")
    back_pay_button.place(relx=0.2, rely=0.65, anchor="n")


    payment.mainloop()



#========================Ventana donde se muestra los seats de la categoria diamond===============================================
#========================================================================================================================================
#========================================================================================================================================
def create_diamond_seats(frame_diam, row_diam, column_diam):
    diam_seats = []
    for r in range(4, 4 + row_diam):
        for c in range(column_diam):
            diamond_id_seat = f"{chr(65+c)}{r+1}"
            bg_color = "lightgreen" if r < 8 else "white"
            
            label_diam = tk.Label(frame_diam, text=diamond_id_seat, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            label_diam.grid(row=r-4, column=c, padx=5, pady=5)
            diam_seats.append(label_diam)
    return diam_seats

def switch_color_seat_diam(diam_seats, boton, mensaje):
    if diam_seats:
        diamond_seat = random.choice(diam_seats)
        mensaje.append(diamond_seat.cget("text"))
        diamond_seat.config(bg="orange")
        boton.config(state=tk.DISABLED)
    
def diamond(mensaje):
    windows_diam = tk.Tk()
    windows_diam.title("Diamond Seats")
    windows_diam.geometry("1200x900")
    windows_diam.configure(bg="#FFF9ED")

    row_diam = 4  # Número de filas de seats
    column_diam = 6  # Número de columnas de seats
    frame_diam = tk.Frame(windows_diam, bg="#FFF9ED")
    frame_diam.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_diam.configure(bg="#FFF9ED")

    diam_seats = create_diamond_seats(frame_diam, row_diam, column_diam)


    diam_buttom = tk.Button(windows_diam, text="Diamond", font = ("Times New Roman", 14),
                    command=lambda: switch_color_seat_diam(diam_seats, diam_buttom, mensaje), bg = "lightgreen")
    diam_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    def payment_(mensaje):
        windows_diam.destroy()
        mensaje.append("Diamond")
        print(mensaje)
        pay_method(mensaje)

    pay_diamond = tk.Button(windows_diam, text="Pay flight", font = ("Times New Roman", 14), command=lambda:payment_(mensaje) , bg = "lightcoral")
    pay_diamond.place(relx= 0.45, rely= 0.6, anchor= "n")

    def back_to_diamond_seats():
        windows_diam.destroy()
        seats_Airplane(mensaje)
        # seats_Airplane.deiconify()

    back_diamond_button = tk.Button(windows_diam, text="Back", font=("Arial", 13),command=back_to_diamond_seats, bg="lightblue")
    back_diamond_button.place(relx=0.2, rely=0.65, anchor="n")



    windows_diam.mainloop()

#========================Ventana donde se muestra los seats de la categoria Premium=====================================================
#========================================================================================================================================
#========================================================================================================================================

def create_premium_seats(frame_prem, row_prem, column_prem, mensaje):
    prem_seats = []

    for r in range(8, 8 + row_prem):
        for c in range(column_prem):
            premium_id_seat = f"{chr(65+c)}{r+1}"
            bg_color = "lightcoral" if 8 <= (r+1) <= 12 else "white"
            
            label_prem = tk.Button(frame_prem, text=premium_id_seat, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            label_prem.config(command=lambda b= label_prem: switch_color(b, prem_seats, mensaje))
            label_prem.grid(row=r-8, column=c, padx=5, pady=5)
            prem_seats.append(label_prem)
    return prem_seats


def switch_color(boton, prem_seats,mensaje):
    boton.config(bg="orange")
    for seat in prem_seats:
        if seat != boton:  # Asegura que el botón seleccionado no se deshabilite
            seat.config(state=tk.DISABLED)
        seat.config(state=tk.DISABLED)
    print(seat.cget("text"))
    mensaje.append(boton.cget("text"))


def premium (mensaje):
    windows_prem = tk.Tk()
    windows_prem.title("Premium Seats")
    windows_prem.geometry("1200x900")
    windows_prem.configure(bg="#FFF9ED")

    row_prem = 4  # Número de filas de seats
    column_prem = 6  # Número de columnas de seats
    frame_prem = tk.Frame(windows_prem, bg="#FFF9ED")
    frame_prem.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_prem.configure(bg="#FFF9ED")

    def payment_(mensaje):
        windows_prem.destroy()
        mensaje.append("Premium")
        print(mensaje)
        
        pay_method(mensaje)

    prem_buttom = tk.Button(windows_prem, text="Premium", font = ("Times New Roman", 14) , bg = "lightcoral")
    prem_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    pay_premium = tk.Button(windows_prem, text="Pay flight", font = ("Times New Roman", 14), command=lambda: payment_(mensaje) , bg = "lightcoral")
    pay_premium.place(relx= 0.55, rely= 0.6, anchor= "n")

    def back_to_seats():
        windows_prem.destroy()
        seats_Airplane(mensaje)
        seats_Airplane.deiconify()

    back_premium_button = tk.Button(windows_prem, text="Back", font=("Arial", 13),command=back_to_seats, bg="lightblue")
    back_premium_button.place(relx=0.2, rely=0.65, anchor="n")

    create_premium_seats(frame_prem, row_prem, column_prem, mensaje)

    windows_prem.mainloop()    

def pay_method(mensaje):
    global payment
    payment = tk.Tk()
    payment.title("Payment Methods")
    payment.geometry("800x600")
    payment.resizable(0,0)

    data_label = tk.Label(payment, text="Card Data", font=("Arial", 16))
    data_label.place(relx=0.4, rely=0.01)

    payment_label = tk.Label(payment, text="Owner Name", font=("Arial", 13))
    payment_label.place(relx=0.22, rely=0.17)

    payment_entry = tk.Label(payment, text= f"{mensaje[9][1]}" , font=("Arial", 13), bg="lightgreen")
    payment_entry.place(relx=0.3, rely=0.22, anchor="n")

    number_label = tk.Label(payment, text="Card Number", font=("Arial", 13))
    number_label.place(relx=0.22, rely=0.27)

    number_entry = tk.Label(payment, text= f"{mensaje[9][6]}" , font=("Arial", 13), bg="lightgreen")
    number_entry.place(relx=0.3, rely=0.32, anchor="n")

    cvv_label = tk.Label(payment, text="CVV", font=("Arial", 13))
    cvv_label.place(relx=0.27, rely=0.37)

    cvv_entry = tk.Label(payment, text= f"{mensaje[9][8]}" , font=("Arial", 13), bg="lightgreen")
    cvv_entry.place(relx=0.3, rely=0.42, anchor="n")

    expiration_label = tk.Label(payment, text="Due Date (MM/AA)", font=("Arial", 13))
    expiration_label.place(relx=0.16, rely=0.47)

    expiration_entry = tk.Label(payment, text= f"{mensaje[9][7]}" , font=("Arial", 13), bg="lightgreen")
    expiration_entry.place(relx=0.3, rely=0.52, anchor="n")

    balance_label = tk.Label(payment, text="Current Balance", font=("Arial", 13))
    balance_label.place(relx=0.27, rely=0.57)
    saldo = 0
    if mensaje[11] == "Aluminium":
        total_payment = tk.Label(payment, text=f"Total to Pay: {mensaje[4]} ", font=("Arial", 13))
        saldo = mensaje[4]
    if mensaje[11] == "Diamond":
        total_payment = tk.Label(payment, text=f"Total to Pay: {mensaje[5]} ", font=("Arial", 13))
        saldo = mensaje[5]
    if mensaje[11] == "Premium":
        total_payment = tk.Label(payment, text=f"Total to Pay: {mensaje[6]} ", font=("Arial", 13))
        saldo = mensaje[6]
    total_payment.place(relx=0.3, rely=0.62, anchor="n")

    def go_ticket(mensaje):
        payment.destroy()
        ticket(mensaje, 0)
        ticket_v.deiconify()
    def comprobar_saldo(valor,mensaje):
        print(valor)
        print(mensaje[9][9])
        if int(mensaje[9][9]) >= int(valor):
            messagebox.showinfo("Payment", "Payment successful")
            mensaje[9][9] = str(int(mensaje[9][9]) - int(valor))
            go_ticket(mensaje)
        else:
            payment.destroy()
            messagebox.showerror("Error", "Insufficient balance")
            log_in()
            
    pay_button = tk.Button(payment, text="Pay", font=("Arial", 13),command=lambda:(comprobar_saldo(saldo,mensaje)), bg="lightblue")
    pay_button.place(relx=0.5, rely=0.65, anchor="n")

    def back_to_premium():
        payment.destroy()
        premium()
        premium.deiconify()

    back_pay_button = tk.Button(payment, text="Back", font=("Arial", 13),command=back_to_premium, bg="lightblue")
    back_pay_button.place(relx=0.2, rely=0.65, anchor="n")


    payment.mainloop()

#================================================Tiquete de viaje========================================================================================
#========================================================================================================================================
#========================================================================================================================================

def ticket(mensaje,tipo):
    global ticket_v
    ticket_v = tk.Tk()
    ticket_v.title("Bording Pass")
    ticket_v.geometry("1200x600")
    ticket_v.resizable(0,0)

    ticket_frame = tk.Frame(ticket_v,bg="darkblue")
    ticket_frame.place(relx= 0.5, rely= 0.5, anchor= "center", height= 600, width= 1000)

    def generar_boarding_pass(mensaje):
        letra_inicial = mensaje[9][1][0]
        def generate_random_code():
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            return code

        random_code = generate_random_code()
        print(random_code)
        codigo = f"{letra_inicial}-{random_code}"
        return codigo
    boarding_pass = generar_boarding_pass(mensaje)
    mensaje.append(boarding_pass)
    title_label = tk.Label(ticket_frame, text=f"Bording Pass : {mensaje[12]}", font=("Arial", 14),fg="white",bg="darkblue")
    title_label.pack()

    ticket_frame1 = tk.Frame(ticket_v,bg="pink") 
    ticket_frame1.place(relx= 0.5, rely= 0.53, anchor= "center", height= 400, width= 1000)



    name_label = tk.Label(ticket_frame1, text=f"Name passenger : {mensaje[9][1]} {mensaje[9][2]} ", font=("Arial", 12),fg="black",bg="pink")
    name_label.place(relx=0.1,rely=0.06)
    
    origin_label = tk.Label(ticket_frame1, text=f"Origin :{mensaje[7]} ", font=("Arial", 12),fg="black",bg="pink")
    origin_label.place(relx=0.1,rely=0.4)

    destiny_label = tk.Label(ticket_frame1, text=f"Destination :{mensaje[8]}", font=("Arial", 12),fg="black",bg="pink")
    destiny_label.place(relx=0.1,rely=0.7)

    flight_label = tk.Label(ticket_frame1, text=f"Flight : {mensaje[0]}", font=("Arial", 12),fg="black",bg="pink")
    flight_label.place(relx=0.6,rely=0.3)

    date_label = tk.Label(ticket_frame1, text=f"Date {mensaje[1]}", font=("Arial", 12),fg="black",bg="pink")
    date_label.place(relx=0.8,rely=0.3)

    hour_label = tk.Label(ticket_frame1, text=f"Hour {mensaje[2]} - {mensaje[3]}", font=("Arial", 12),fg="black",bg="pink")
    hour_label.place(relx=0.8, rely=0.7)
    
    boton_confirmar = tk.Button(ticket_frame1, text="Confirm", font=("Arial", 13),command= lambda: (ticket_v.destroy(),guardar_informacion_vuelo(mensaje),guardar_informacion_vuelo(mensaje),log_in()), bg="lightblue")
    boton_confirmar.place(relx=0.5, rely=0.9, anchor="n")

    if tipo == 1:
        show_seats = tk.Label(ticket_frame1, text=f"Asiento : {mensaje[0]}", font=("Arial", 12),fg="black",bg="pink")
        show_seats.place(relx=0.6,rely=0.45)
    

def guardar_informacion_vuelo(mensaje):
    print("Pase")
    correo_persona = mensaje[9][5]
    with open("user_data.txt", "r") as file:
        datos = file.read()
        datos = datos.split("\n")
        datos = [dato.split(",") for dato in datos]
    

    with open("user_data_flight.txt", "w") as file:
        for dato in datos:
            datos_enviar =[]
            if dato[6]== correo_persona:
                datos_enviar.append(mensaje[12])
                datos_enviar.append(mensaje[0])
                datos_enviar.append(dato[6])
                datos_enviar.append(dato[2])

            file.write(",".join(datos_enviar))
            file.write("\n")
            

    


    file_path = fr"vuelo_{mensaje[0]}.txt"
    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write(f"{mensaje[0]},")
            file.write(f"{mensaje[1]},")
            file.write(f"{mensaje[2]},")
            file.write(f"{mensaje[3]},")
            if mensaje[11] == "Aluminium":
                file.write(f"{mensaje[4]},")
            if mensaje[11] == "Diamond":
                file.write(f"{mensaje[5]},")
            if mensaje[11] == "Premium":
                file.write(f"{mensaje[6]},")
            file.write(f"{mensaje[7]},")
            file.write(f"{mensaje[8]},")
            file.write(f"{mensaje[10]},")
            file.write(f"{mensaje[11]},")
            file.write(f"{mensaje[9][1]},")
            file.write(f"{mensaje[12]}")
            
            file.write("\n")
            file.close()
    else:        
        with open(file_path, "w") as file:
            file.write(f"{mensaje[0]},")
            file.write(f"{mensaje[1]},")
            file.write(f"{mensaje[2]},")
            file.write(f"{mensaje[3]},")
            if mensaje[11] == "Aluminium":
                file.write(f"{mensaje[4]},")
            if mensaje[11] == "Diamond":
                file.write(f"{mensaje[5]},")
            if mensaje[11] == "Premium":
                file.write(f"{mensaje[6]},")
            file.write(f"{mensaje[7]},")
            file.write(f"{mensaje[8]},")
            file.write(f"{mensaje[10]},")
            file.write(f"{mensaje[11]},")
            file.write(f"{mensaje[9][1]},")
            file.write(f"{mensaje[12]}")
            file.write("\n")
            file.close()


if __name__ == '__main__':
    log_in()
    
    
#la ventana del Check-in esta hecha en google keep