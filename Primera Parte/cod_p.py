import random

flight_purchases = {}

def flihgt_book(flights, choice, flight_purchases):
    ### aqui pondria el vuelo elegido por el usuario, pa hacer una plantilla de esta mierda
    ### vamos a suponer que tengo una variable "flight_selected" que seria el vuelo que el usuario selecciono
    ### tambien tengo que hacer lo de que escoja el numero de vuelos que quiere comprar
    ### ahi me disculpan el desorden chachos, mucho texto.
    ### variable para el numero de vuelos que quiere comprar = choice SOLO ES MIENTRAS BUSCO BIEN COMO PONERLO
    ### flights = lista de vuelos 
    
    flights = tabladevuelos()

    ### crear choice para que el usuario ingrese cuantos vuelos quiere comprar

    if choice < 1 or choice > len(flights):
        print("Invalid")
        return
    flight_selected = flights[choice - 1][0]  # Obtener el código del vuelo seleccionado
    if flight_selected in flight_purchases and flight_purchases[flight_selected] >= 72:
        print("We're sorry, the flight is fully booked.")
        ## Llama a la función de vuelos disponibles otra vez para ver si quiere escoger otro
        return
    else:
        purchases_number = int(input("Enter the number of seats you want to buy: "))
        if flight_selected in flight_purchases:
            flight_purchases[flight_selected] += purchases_number
        else:
            flight_purchases[flight_selected] = purchases_number

def card_verification():
    while True:
        try:
            card_num = input("Enter your card number: ")
            if len(card_num) < 16 or len(card_num) > 16:
                raise ValueError("The card number must be 16 digits")
            cvv = input("Enter the cvv: ")     
            if len(cvv) < 3 or len(cvv) > 3:
                raise ValueError("The cvv must be 3 digits")
            print("verified")
            return card_num
        except:
            print("Please, enter the information correctly", ValueError)

def read_user():
    while True:
        try:
            gender = str(input("GENDER: "))
            first_name = str(input("FIRST NAME: "))
            last_name = str(input("LAST NAME: "))
            identification = int(input("ID: "))
            nationality = str(input("NATIONALITY: "))
            telephone = int(input("TELEPHONE: "))
            # email = input("EMAIL: ")
            email = email_verification()

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

            break
        except ValueError:
            print("The data you have entered is not correct")

def email_verification():
    while True:
            try:
                email = input("EMAIL: ")

                if "@" in email and "." in email:
                    print("Email verified")
                    return email
            except:
                raise ValueError("Email not accepted, please enter a valid email.")

def user_existence(email):
    with open("user_emails.txt", "r") as e_file: 
        emails = e_file.readlines()
        emails = [i.strip() for i in emails]
        if email in emails:
            return True
        else:
            return False

def login():
    email = input("Enter your email: ")

    if user_existence(email) is True:      
        print("SUCCESSFUL LOGIN") ### aca se supone que ya tiene una cuenta creada entonces debe direccionarlo
                                  ### a comprar los vuelos pero me da weba buscar cual era esa funcion
    else:
        print("Youre not registered. Please create an account")
        read_user()

def seat_assigment_alum():
    alum = ['A9', 'A10', 'A11', 'A12',
            'B9', 'B10', 'B11', 'B12',
            'C9', 'C10', 'C11', 'C12',
            'D9', 'D10', 'D11', 'D12',
            'E9', 'E10', 'E11', 'E12',
            'F9', 'F10', 'F11', 'F12']

    alumi = random.choice(alum)
    seats_alum = seats_alum.remove(alum)
    return alumi

def seat_assigment_diam():
    diam = ['A5', 'A6', 'A7', 'A8',
            'B5', 'B6', 'B7', 'B8',
            'C5', 'C6', 'C7', 'C8',
            'D5', 'D6', 'D7', 'D8',
            'E5', 'E6', 'E7', 'E8',
            'F5', 'F6', 'F7', 'F8',]
    
    diamo = random.choice(diam)
    seats_diam = seats_diam.remove(diam)
    return diamo

def seat_assigment_premium():
    premium = ['A1', 'A2', 'A3', 'A4',
               'B1', 'B2', 'B3', 'B4',
               'C1', 'C2', 'C3', 'C4',
               'D1', 'D2', 'D3', 'D4',
               'E1', 'E2', 'E3', 'E4',
               'F1', 'F2', 'F3', 'F4',]
    print("AVAILABLE SEATS")
    print(premium)

    choosen_seat = input("Please, select your seat: ")

    aux = choosen_seat #auxiliar para imprimir el asiento del usuario NO ESTÁ TERMINADO, NO ME HAGAN BULLYING#

    if choosen_seat in premium:
        premium.remove(choosen_seat)
    else:
        print("The seat you entered is not available")
    print("AVAILABLE SEATS")
    print(premium)

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
    ori = str(input("Flight origin: "))
    dest = str(input("Flight destination: "))
    date = int(input("Date of the flight (YYYY-MM-DD): "))
    service = str(input("Select a service: Aluminum, Diamond, Premium"))

    available_flights = [fly for fly in tabladevuelos() if fly[7] == ori and fly[8] == dest and fly[1] == date]

    if len(available_flights) == 0:
        print("We're sorry, we don't have available flights")
    else:
        for fly in available_flights:
            print(f"""FLIGHT: {fly[0]}
                      DEPARTURE TIME: {fly[2]}
                      ARRIVAL TIME: {fly[3]}""")
            
    price(fly, service)
            
def price(fly, service):
    while True:
        try:
            if service.lower() == "aluminum":
                option_one = str(input("Hand luggage (yes/no): "))
                option_two = str(input("baggage (yes/no): "))
                if option_one == "yes" and option_two == "yes":
                    return fly[4] + 370700
                elif option_one == "yes":
                    return fly[4] + 195100
                elif option_two == "yes":
                    return fly[4] + 175600
                elif option_one == "no" and option_two == "no":
                    return fly[4]
                else:
                    raise ValueError    
            elif service.lower() == "diamond":
                return fly[5]
            elif service.lower() == "premium":
                return fly[6]
            else:
                raise ValueError("The service entered is not valid") 
        except:
            raise ValueError("Invalid input. Please enter 'yes' or 'no'")
        

def user_name():
    with open("user_data.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            if i.startswith("First name:"):
                return i.split(": ")[1].strip()

def generate_code(first_name):
    name = first_name.upper()    
    code = name[0] 
    for i in range(6):
        code += random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return code
    
if __name__=='__main__':
    pass