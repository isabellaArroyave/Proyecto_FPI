import tkinter as tk
from tkinter import ttk

import customtkinter as ctk

#=========================================Ventana para registrarse=======================================================================
def read_user(gender, first_name, last_name, identification, nationality, telephone, email):

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

    texto_genero = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_genero.pack(pady=10)

    etiqueta_nacionalidad = tk.Label(marco_derecha, text = "Nacionalidad", font=("Times New Roman", 18), fg="white", bg="#0B666A")
    etiqueta_nacionalidad.pack(pady=10)
    
    texto_nacionalidad = tk.Entry(marco_derecha, font=("Arial", 14))
    texto_nacionalidad.pack(pady=10)

    gender = texto_genero.get()
    first_name = texto_nombre.get()
    last_name = texto_apellido.get()
    identification = texto_id.get()
    nationality = texto_nacionalidad.get()
    telephone = texto_telefono.get()
    email = texto_correo.get()

    read_user(gender, first_name, last_name, identification, nationality, telephone, email)

    def windows_check_in():
        windows.destroy()
        travel_windows()
        travel_windows.deiconify()

    check_in_buttom = tk.Button(windows, text="Registrarme", font = ("Times New Roman", 14), command = windows_check_in, bg = "light green")
    check_in_buttom.pack(side = "bottom", anchor = "s", pady= 50)

#============================Ventanas de inicio sesion=====================================================================================
def user_existence(correo_entry):
    with open("user_emails.txt", "w") as e_file: 
        emails = e_file.readlines()
        emails = [i.strip() for i in emails]
        if correo_entry in emails:
            pass # tiene que llevarme a la ventana del buscador
        else:
            read_user()

def email_verification(correo_entry): ##arreglar parametro
    while True:
            try:
                if "@" in correo_entry and "." in correo_entry:
                    print("Email verified")
                    return correo_entry
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

    # frame1 = tk.Frame(seats, bg="#FFF9ED")
    # frame1.place(relx= 0.8, rely= 0.1, anchor= "n")
    
    correo = tk.Label(sesion, text = "Correo Electronico", font = ("Times New Roman", 18), fg = "white", bg="#0B666A")
    correo.place(relx= 0.5, rely= 0.3, anchor= "n")

    correo_entry = tk.Entry(sesion, font = ("Times New Roman", 14), bg="#58FF9F")
    correo_entry.place(relx= 0.5, rely= 0.45, anchor= "n")
    
    sesion_buttom = tk.Button(sesion, text = "Verificar", font = ("Times New Roman", 14), command = lambda: user_existence(correo_entry.get()), bg = "light green")
    sesion_buttom.pack(side = "bottom", anchor = "s", pady= 50)
    
    sesion_buttom = tk.Button(sesion, text = "Iniciar", font = ("Times New Roman", 14), command = ingreso_dato, bg = "light green")
    sesion_buttom.pack(side = "bottom", anchor = "s", pady= 50)

    sesion.mainloop()



#============================Ventanas de los 100 botones=====================================================================================
#============================================================================================================================================

def tabladevuelos():
    flights = [['Z328', '2024-06-5', '08:13:00', '10:35:00', 244463, 538669, 1666594, 'Santa Marta', 'Bogota'],
['X633', '2024-06-6', '02:55:00', '05:58:00', 483669, 640186, 4023518, 'Santa Marta', 'Cartagena'],
['G611', '2024-06-12', '16:50:00', '17:07:00', 295876, 915371, 2684321, 'Medellin', 'Santa Marta'],
['N891', '2024-06-13', '07:15:00', '11:48:00', 438164, 692289, 2927741, 'Cali', 'Bogota'],
['E350', '2024-06-26', '15:52:00', '17:10:00', 279458, 506496, 1066916, 'Cartagena', 'Bogota'],
['J773', '2024-06-6', '10:21:00', '11:03:00', 293612, 972660, 4265332, 'Bogota', 'Santa Marta'],
['B552', '2024-06-13', '13:28:00', '15:29:00', 390970, 781301, 2636179, 'Cali', 'Bogota'],
['I352', '2024-06-19', '18:33:00', '20:33:00', 112548, 607120, 3138340, 'Cartagena', 'Medellin'],
['Y874', '2024-06-5', '15:17:00', '16:50:00', 108548, 889209, 4215978, 'Santa Marta', 'Cartagena'],
['A823', '2024-06-19', '02:55:00', '06:03:00', 286051, 887727, 1794728, 'Medellin', 'Bogota'],
['J837', '2024-06-5', '17:01:00', '18:02:00', 182306, 601733, 3060789, 'Cartagena', 'Bogota'],
['Z343', '2024-06-19', '13:47:00', '17:42:00', 248460, 849734, 1382792, 'Cali', 'Medellin'],
['E747', '2024-06-19', '06:53:00', '09:52:00', 426098, 767319, 4081864, 'Medellin', 'Bogota'],
['D141', '2024-06-27', '17:29:00', '20:54:00', 330781, 531990, 2817297, 'Cartagena', 'Bogota'],
['E387', '2024-06-26', '03:32:00', '07:00:00', 473622, 609433, 2821653, 'Cartagena', 'Medellin'],
['P636', '2024-06-12', '10:52:00', '12:50:00', 183918, 644497, 3018149, 'Santa Marta', 'Bogota'],
['K776', '2024-06-6', '19:01:00', '21:36:00', 340848, 968318, 1259865, 'Santa Marta', 'Cali'],
['W556', '2024-06-19', '21:50:00', '23:03:00', 169404, 896128, 4830564, 'Cartagena', 'Medellin'],
['L703', '2024-06-19', '07:09:00', '07:17:00', 107432, 765044, 1848939, 'Santa Marta', 'Cali'],
['L890', '2024-06-20', '11:09:00', '13:32:00', 391458, 673038, 4485596, 'Medellin', 'Cartagena'],
['G714', '2024-06-20', '08:01:00', '10:34:00', 368435, 552773, 3427251, 'Bogota', 'Cartagena'],
['H152', '2024-06-12', '19:12:00', '23:48:00', 143776, 899772, 3900612, 'Cartagena', 'Santa Marta'],       
['I966', '2024-06-26', '08:57:00', '09:37:00', 228361, 600499, 2154222, 'Cartagena', 'Cali'],
['R874', '2024-06-19', '05:31:00', '08:40:00', 185702, 943771, 4208738, 'Cartagena', 'Santa Marta'],       
['U929', '2024-06-19', '15:02:00', '17:21:00', 115796, 647904, 2932337, 'Bogota', 'Medellin'],
['E389', '2024-06-6', '16:46:00', '20:32:00', 420182, 557153, 4055065, 'Cali', 'Medellin'],
['L505', '2024-06-12', '04:52:00', '05:23:00', 378191, 677832, 1759483, 'Medellin', 'Cali'],
['J786', '2024-06-26', '15:44:00', '16:20:00', 464673, 723388, 4718254, 'Cali', 'Bogota'],
['I506', '2024-06-26', '12:13:00', '13:48:00', 156761, 955557, 4359006, 'Medellin', 'Cartagena'],
['W151', '2024-06-27', '01:46:00', '03:28:00', 158668, 887450, 1527895, 'Santa Marta', 'Bogota'],
['I657', '2024-06-5', '23:46:00', '2:48:00', 227358, 920227, 3299390, 'Bogota', 'Medellin'],
['A722', '2024-06-6', '12:32:00', '14:25:00', 335925, 718598, 3201428, 'Medellin', 'Santa Marta'],
['G542', '2024-06-27', '10:15:00', '12:58:00', 364902, 620659, 3822832, 'Cali', 'Bogota'],
['R419', '2024-06-13', '18:45:00', '21:11:00', 263221, 823412, 1802097, 'Cali', 'Bogota'],
['K387', '2024-06-12', '08:52:00', '12:58:00', 111358, 837315, 1740776, 'Medellin', 'Cartagena'],
['I684', '2024-06-6', '18:25:00', '22:33:00', 268461, 861073, 4378830, 'Santa Marta', 'Cartagena'],        
['T366', '2024-06-6', '15:59:00', '16:30:00', 441718, 551893, 1443926, 'Bogota', 'Medellin'],
['G973', '2024-06-27', '07:51:00', '09:59:00', 107735, 812320, 4667378, 'Cartagena', 'Medellin'],
['P628', '2024-06-20', '20:47:00', '21:45:00', 259683, 878251, 1406197, 'Cali', 'Bogota'],
['V577', '2024-06-20', '19:47:00', '23:12:00', 321437, 838480, 2594022, 'Bogota', 'Medellin'],
['Y916', '2024-06-5', '19:05:00', '20:07:00', 146788, 717336, 2479818, 'Bogota', 'Medellin'],
['C616', '2024-06-6', '14:43:00', '19:14:00', 251102, 768356, 3231604, 'Bogota', 'Medellin'],
['Z502', '2024-06-27', '02:33:00', '04:46:00', 135039, 739155, 3841687, 'Santa Marta', 'Medellin'],        
['O706', '2024-06-19', '03:33:00', '08:12:00', 108543, 552765, 4776384, 'Cartagena', 'Medellin'],
['A425', '2024-06-12', '05:16:00', '07:38:00', 428767, 803167, 3465554, 'Bogota', 'Cartagena'],
['A643', '2024-06-27', '02:41:00', '06:50:00', 133731, 965070, 1155231, 'Bogota', 'Santa Marta'],
['C594', '2024-06-6', '20:14:00', '22:16:00', 179770, 755917, 3525256, 'Cartagena', 'Cali'],
['X712', '2024-06-5', '04:28:00', '05:47:00', 367356, 997236, 2511543, 'Santa Marta', 'Cartagena'],        
['X517', '2024-06-26', '13:23:00', '16:23:00', 409500, 657451, 2024557, 'Cali', 'Cartagena'],
['M302', '2024-06-20', '15:15:00', '17:10:00', 138614, 638674, 4057270, 'Cartagena', 'Cali'],
['X448', '2024-06-12', '14:57:00', '16:48:00', 256801, 649687, 2492053, 'Medellin', 'Bogota'],
['K415', '2024-06-6', '01:59:00', '02:58:00', 118208, 955980, 3967119, 'Cartagena', 'Cali'],
['N999', '2024-06-20', '00:02:00', '01:28:00', 113404, 742916, 3870717, 'Cali', 'Bogota'],
['Q579', '2024-06-19', '10:13:00', '13:46:00', 442756, 900225, 4970730, 'Bogota', 'Cali'],
['O632', '2024-06-5', '10:46:00', '11:04:00', 450503, 759587, 3350417, 'Cali', 'Medellin'],
['W768', '2024-06-5', '00:14:00', '02:37:00', 309428, 530313, 3146101, 'Cartagena', 'Santa Marta'],        
['N700', '2024-06-20', '17:02:00', '21:47:00', 428761, 586568, 4387318, 'Cali', 'Medellin'],
['A198', '2024-06-13', '10:07:00', '11:34:00', 471496, 637023, 3708333, 'Santa Marta', 'Cali'],
['N508', '2024-06-20', '07:49:00', '11:17:00', 380455, 885626, 1079810, 'Cali', 'Bogota'],
['S830', '2024-06-26', '06:11:00', '08:05:00', 136210, 609050, 1031737, 'Medellin', 'Bogota'],
['B193', '2024-06-12', '11:55:00', '16:16:00', 322687, 776707, 3559620, 'Santa Marta', 'Medellin'],        
['N925', '2024-06-20', '20:09:00', '23:27:00', 348655, 584679, 2803067, 'Bogota', 'Cali'],
['O805', '2024-06-19', '08:11:00', '12:14:00', 180125, 637210, 4660148, 'Cartagena', 'Cali'],
['B165', '2024-06-20', '00:21:00', '03:01:00', 285230, 798592, 4037787, 'Medellin', 'Cali'],
['Q419', '2024-06-6', '18:09:00', '20:04:00', 336342, 966902, 3843081, 'Santa Marta', 'Bogota'],
['H905', '2024-06-6', '11:56:00', '13:11:00', 345069, 702454, 1287428, 'Cali', 'Santa Marta'],
['R873', '2024-06-6', '00:14:00', '04:15:00', 209011, 932430, 2499023, 'Santa Marta', 'Cali'],
['T810', '2024-06-6', '22:03:00', '00:13:00', 353905, 622617, 1739971, 'Medellin', 'Santa Marta'],
['R507', '2024-06-20', '03:35:00', '05:14:00', 338290, 891960, 3268081, 'Cartagena', 'Bogota'],
['E279', '2024-06-27', '03:32:00', '07:31:00', 112594, 535012, 2407140, 'Cali', 'Bogota'],
['T179', '2024-06-5', '21:42:00', '23:56:00', 194995, 970417, 3446179, 'Medellin', 'Bogota'],
['E348', '2024-06-6', '14:21:00', '17:45:00', 200805, 661664, 1423079, 'Cartagena', 'Cali'],
['V809', '2024-06-5', '15:17:00', '18:30:00', 412564, 851500, 4680941, 'Santa Marta', 'Medellin'],
['D483', '2024-06-12', '04:31:00', '09:24:00', 232173, 607087, 4661950, 'Cali', 'Cartagena'],
['F592', '2024-06-20', '20:57:00', '23:35:00', 387337, 666898, 4024585, 'Medellin', 'Cartagena'],
['B209', '2024-06-6', '07:51:00', '10:33:00', 422422, 832491, 3948879, 'Santa Marta', 'Cartagena'],        
['F812', '2024-06-26', '04:51:00', '08:56:00', 100947, 539536, 3632244, 'Cali', 'Cartagena'],
['X552', '2024-06-26', '04:54:00', '07:10:00', 271127, 656834, 4845023, 'Cartagena', 'Santa Marta'],       
['I848', '2024-06-5', '07:45:00', '12:08:00', 180814, 648460, 4560674, 'Cartagena', 'Bogota'],
['J755', '2024-06-20', '02:52:00', '07:15:00', 352497, 973921, 4954962, 'Cali', 'Medellin'],
['Y216', '2024-06-19', '02:44:00', '05:12:00', 339920, 690835, 3549467, 'Cartagena', 'Santa Marta'],       
['G442', '2024-06-12', '01:09:00', '03:41:00', 346049, 850291, 4890999, 'Medellin', 'Cali'],
['V932', '2024-06-12', '16:57:00', '18:53:00', 368937, 836969, 2128948, 'Santa Marta', 'Medellin'],        
['Q252', '2024-06-20', '08:20:00', '13:01:00', 477214, 801662, 4676437, 'Cartagena', 'Cali'],
['D848', '2024-06-27', '11:08:00', '14:48:00', 239379, 992500, 3004583, 'Bogota', 'Santa Marta'],
['S569', '2024-06-5', '14:40:00', '16:24:00', 198988, 955922, 4074101, 'Bogota', 'Medellin'],
['I656', '2024-06-13', '20:31:00', '23:13:00', 283863, 587002, 3987051, 'Medellin', 'Cali'],
['S129', '2024-06-6', '18:08:00', '19:08:00', 377016, 650034, 1915104, 'Medellin', 'Cartagena'],
['N232', '2024-06-5', '16:35:00', '19:08:00', 186616, 590890, 2616295, 'Medellin', 'Santa Marta'],
['M191', '2024-06-20', '03:11:00', '07:02:00', 343481, 664520, 3274677, 'Cartagena', 'Medellin'],
['H180', '2024-06-20', '00:19:00', '02:53:00', 314037, 672798, 3793121, 'Santa Marta', 'Cali'],
['V900', '2024-06-19', '10:39:00', '13:52:00', 361362, 575041, 4335294, 'Santa Marta', 'Cali'],
['Q449', '2024-06-27', '18:37:00', '20:56:00', 407816, 703210, 4323741, 'Santa Marta', 'Cali'],
['R250', '2024-06-26', '16:28:00', '18:29:00', 478289, 965855, 2387745, 'Cali', 'Bogota'],
['T654', '2024-06-26', '12:11:00', '14:20:00', 358074, 736442, 4444497, 'Santa Marta', 'Bogota'],
['Y804', '2024-06-12', '14:28:00', '16:34:00', 261803, 548104, 1150859, 'Cali', 'Bogota'],
['E971', '2024-06-12', '22:07:00', '23:12:00', 362030, 972110, 1721417, 'Santa Marta', 'Cartagena'],       
['U728', '2024-06-12', '15:55:00', '18:43:00', 352021, 909057, 3924712, 'Santa Marta', 'Medellin'],
['U522', '2024-06-13', '12:46:00', '14:54:00', 169490, 503891, 2723741, 'Bogota', 'Cartagena'],
['V560', '2024-06-26', '08:41:00', '11:20:00', 118816, 675485, 2104917, 'Santa Marta', 'Cali']]
    
    return flights


def select_flight():
    ori = origen_entry.get()
    dest = destino_entry.get()

    available_flights = [fly for fly in tabladevuelos() if fly[8] == dest and fly[7] == ori]
    
    # Clear any existing buttons in the frame 'buscar' before adding new ones
    for widget in buscar.winfo_children():
        widget.destroy()

    def asientos():
        buscar.destroy()
        seats_Airplane()
        seats_Airplane.deiconify()
    
    if available_flights:
        for i, fly in enumerate(available_flights):
            flight_text = f"FLIGHT: {fly[0]}, DEPARTURE TIME: {fly[2]}, ARRIVAL TIME: {fly[3]}"
            vuelos_button = tk.Button(buscar, text=flight_text, font=("Arial", 13), bg="pink", command=asientos)
            vuelos_button.pack(fill='x', pady=5)  # Adjust placement as needed
    else:
        no_flights_label = tk.Label(buscar, text="We're sorry, we don't have available flights", font=("Arial", 13))
        no_flights_label.pack(fill='x', pady=5)

# Add these entries to your root or another frame, and then bind/select_flight to a button or an event

    
    # vuelos = tk.Label(buscar, font=("Arial", 13), bg="darkblue")
    # vuelos.place(relx= 0.5, rely= 0.5, anchor= "center", height= 400, width= 700)
    

    

    #if len(available_flights) == 0:
    #     print("We're sorry, we don't have available flights")
        
    ####ESTO PUEDE SERVIR PARA EL BOLETO

    # else:
    #     for fly in available_flights:
    #         print(f"""FLIGHT: {fly[0]}
    #                   DEPARTURE TIME: {fly[2]}
    #                   ARRIVAL TIME: {fly[3]}""")

def buscador():
    global vuelos, destino_entry, origen_entry, buscar
    buscar = tk.Tk()
    buscar.title("Buscador de vuelos")
    buscar.geometry("800x600")

    origen_label = tk.Label(buscar, text="Origen", font=("Arial", 13))
    origen_label.place(relx= 0.17, rely= 0.05)

    opciones_origen = ["Santa Marta", "Bogotá", "Cartagena", "Medellin", "Cali"]
    origen_entry = ttk.Combobox(buscar, values=opciones_origen, state='readonly')
    origen_entry.place(relx= 0.1, rely= 0.1)
    origen_entry.set("Escoja el origen")

    #

    fecha_label = tk.Label(buscar, text="Fecha", font=("Arial", 13))
    fecha_label.place(relx= 0.47, rely= 0.05)

    opciones_fecha = ["2024-06-5", "2024-06-6", "2024-06-12", "2024-06-13", "2024-06-19", "2024-06-20", "2024-06-26", "2024-06-27"]
    fecha_entry = ttk.Combobox(buscar, values=opciones_fecha, state='readonly')
    fecha_entry.place(relx= 0.4, rely= 0.1)
    fecha_entry.set("Escoja la fecha")

    #

    destino_label = tk.Label(buscar, text="Destino", font=("Arial", 13))
    destino_label.place(relx= 0.77, rely= 0.05)

    opciones_destino = ["Santa Marta", "Bogotá", "Cartagena", "Medellin", "Cali"]
    destino_entry = ttk.Combobox(buscar, values=opciones_destino, state='readonly')
    destino_entry.place(relx= 0.7, rely= 0.1)
    destino_entry.set("Escoja el destino")

    def asientos():
        buscar.destroy()
        seats_Airplane()
        seats_Airplane.deiconify()

    verificar_buttom = tk.Button(buscar, text = "Verificar", font = ("Times New Roman", 14),command=select_flight, bg = "light green")
    verificar_buttom.pack(side = "bottom", anchor = "s", pady= 50)

    # available_flights = verificar_buttom.get()

    vuelos = tk.Label(buscar, font=("Arial", 13), bg="darkblue")
    vuelos.place(relx= 0.5, rely= 0.5, anchor= "center", height= 400, width= 700)


    buscar.mainloop()


#================================Ventana de los asientos===========================================================================
#===================================================================================================================================



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
        # seats.destroy()
        aluminio()
        aluminio.deiconify()

    aluminio_buttom = tk.Button(seats, text="Aluminio", font = ("Times New Roman", 14), command=categoria_alum , bg = "light blue")
    aluminio_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    def categoria_diam():
        # seats.destroy()
        diamante()
        diamante.deiconify()

    diamante_buttom = tk.Button(seats, text="Diamante", font = ("Times New Roman",14), command = categoria_diam ,bg = "light green")
    diamante_buttom.place(relx= 0.55, rely= 0.44, anchor= "n")

    def categoria_premium():
        # seats.destroy()
        premium()
        premium.deiconify()

    premium_buttom = tk.Button(seats, text="Premium", font = ("Times New Roman", 14), command =categoria_premium, bg = "lightcoral")
    premium_buttom.place(relx= 0.55, rely= 0.66, anchor= "n")


    crear_asientos(frame1, row, column)
    seats.mainloop()

#========================Ventana donde se muestra los asientos de la categoria Aluminio==============================================================================================
def crear_asientos_alum(frame_alum, row_alum, column_alum):
    for r in range(row_alum):
        for c in range(column_alum):
            asiento_id_alum = f"{chr(65+c)}{r+1}"
            if 1 <= (r+1) <= 4:
                bg_color = "lightblue"
            elif 5 <= (r+1) <= 8:
                bg_color = "lightgreen"
            else:
                bg_color = "lightcoral"
            etiqueta_alum = tk.Label(frame_alum, text=asiento_id_alum, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            etiqueta_alum.grid(row=r, column=c, padx=5, pady=5)
    

def aluminio ():
    windows_alum = tk.Tk()
    windows_alum.title("Asientos en aluminio")
    windows_alum.geometry("1200x900")
    windows_alum.configure(bg="#FFF9ED")

    row_alum = 4  # Número de filas de asientos
    column_alum = 6  # Número de columnas de asientos
    frame_alum = tk.Frame(windows_alum, bg="#FFF9ED")
    frame_alum.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_alum.configure(bg="#FFF9ED")

    alum_buttom = tk.Button(windows_alum, text="Aluminio", font = ("Times New Roman", 14), bg = "light blue")
    alum_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    def pago_():
        windows_alum.destroy()
        medio_pago()
        medio_pago.deiconify()

    pay_aluminio = tk.Button(windows_alum, text="Pay flight", font = ("Times New Roman", 14), command=pago_ , bg = "lightcoral")
    pay_aluminio.place(relx= 0.45, rely= 0.6, anchor= "n")

    crear_asientos_alum(frame_alum, row_alum, column_alum)

    windows_alum.mainloop()

#========================Ventana donde se muestra los asientos de la categoria Diamante==============================================================================================
def crear_asientos_diam(frame_diam, row_diam, column_diam):
    for r in range(row_diam):
        for c in range(column_diam):
            asiento_id_diam = f"{chr(65+c)}{r+1}"
            if 1 <= (r+1) <= 4:
                bg_color = "lightgreen"
            
            etiqueta_diam = tk.Label(frame_diam, text=asiento_id_diam, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            etiqueta_diam.grid(row=r, column=c, padx=5, pady=5)
    

def diamante ():
    windows_diam = tk.Tk()
    windows_diam.title("Asiento en Diamante")
    windows_diam.geometry("1200x900")
    windows_diam.configure(bg="#FFF9ED")

    row_diam = 4  # Número de filas de asientos
    column_diam = 6  # Número de columnas de asientos
    frame_diam = tk.Frame(windows_diam, bg="#FFF9ED")
    frame_diam.place(relx= 0.8, rely= 0.1, anchor= "n")
    windows_diam.configure(bg="#FFF9ED")

    diam_buttom = tk.Button(windows_diam, text="Diamante", font = ("Times New Roman", 14), bg = "lightgreen")
    diam_buttom.place(relx= 0.55, rely= 0.2, anchor= "n")

    def pago_():
        windows_diam.destroy()
        medio_pago()
        medio_pago.deiconify()

    pay_diamond = tk.Button(windows_diam, text="Pay flight", font = ("Times New Roman", 14), command=pago_ , bg = "lightcoral")
    pay_diamond.place(relx= 0.45, rely= 0.6, anchor= "n")

    crear_asientos_diam(frame_diam, row_diam, column_diam)


    windows_diam.mainloop()

#========================Ventana donde se muestra los asientos de la categoria Premium==============================================================================================
def crear_asientos_prem(frame_prem, row_prem, column_prem):
    for r in range(row_prem):
        for c in range(column_prem):
            asiento_id_prem = f"{chr(65+c)}{r+1}"
            if 1 <= (r+1) <= 4:
                bg_color = "lightcoral"
            
            etiqueta_prem = tk.Button(frame_prem, text=asiento_id_prem, width=5, height=2, 
                                bg= bg_color, relief="raised", borderwidth=1)
            etiqueta_prem.config(command=lambda b= etiqueta_prem: cambiar_color(b))
            etiqueta_prem.grid(row=r, column=c, padx=5, pady=5)

def cambiar_color(boton):
    boton.config(bg="orange")

def premium ():
    windows_prem = tk.Tk()
    windows_prem.title("Asiento en Premium")
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

    crear_asientos_prem(frame_prem, row_prem, column_prem)



    windows_prem.mainloop()    

def medio_pago():
    pago = tk.Tk()
    pago.title("Medios de pago")
    pago.geometry("800x600")
    pago.resizable(0,0)

    dato_label = tk.Label(pago, text="Datos de la Tarjeta", font=("Arial", 16))
    dato_label.place(relx=0.4, rely=0.01)

    pago_label = tk.Label(pago, text="Nombre del titular", font=("Arial", 13))
    pago_label.place(relx=0.22, rely=0.17)

    pago_entry = tk.Entry(pago, font=("Arial", 13), bg="lightgreen")
    pago_entry.place(relx=0.3, rely=0.22, anchor="n")

    number_label = tk.Label(pago, text="Numero de tarjeta", font=("Arial", 13))
    number_label.place(relx=0.22, rely=0.27)

    numero_entry = tk.Entry(pago, font=("Arial", 13), bg="lightgreen")
    numero_entry.place(relx=0.3, rely=0.32, anchor="n")

    cvv_label = tk.Label(pago, text="CVV", font=("Arial", 13))
    cvv_label.place(relx=0.27, rely=0.37)

    cvv_entry = tk.Entry(pago, font=("Arial", 13), bg="lightgreen")
    cvv_entry.place(relx=0.3, rely=0.42, anchor="n")

    vencimiento_label = tk.Label(pago, text="Fecha de vencimiento (MM/AA)", font=("Arial", 13))
    vencimiento_label.place(relx=0.16, rely=0.47)

    vencimiento_entry = tk.Entry(pago, font=("Arial", 13), bg="lightgreen")
    vencimiento_entry.place(relx=0.3, rely=0.52, anchor="n")

    total_pagar = tk.Label(pago, text="Total a pagar: (ejemplo) $2.225.000", font=("Arial", 13))
    total_pagar.place(relx=0.35, rely=0.6)

    pay_button = tk.Button(pago, text="Pay", font=("Arial", 13), bg="lightblue")
    pay_button.place(relx=0.5, rely=0.65, anchor="n")

    


    pago.mainloop()


if __name__ == '__main__':
    # main_windows()
    #medio_pago()
    inicio_sesion()    
    
#la ventana del Check-in esta hecha en google keep