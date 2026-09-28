from sensor_node import Sensor

def main():

    aktiva_sensorer =  []

    kor_system = True

    #Start av while-loop med menyval
    while kor_system:
        print("\n--- SCADA TELEMETRI CENTRAL---")
        print("1. Registrera nya sensor")
        print("2. Inmatning av mätvärden")
        print("3. Registrerade sensorer")
        print("4. Sammanställning av märvärden sensor")
        print("5. Ändra informationen på en sensor")
        print("6. Ta bort en sensor")
        print("7. Avsluta")

        val = input("Ange ett val: ")

        #Registrera en sensor
        if val == "1":
            print("\n REGISTRERING")
            s_id = input("Ange sensor ID (ex. S-101): ")
            s_plats = input("Ange sensorns placering: ")
            s_troskel = float(input("Ange larmtröskeln på sensorn (numreriska): "))

            #Ny sensor läggs till i listan
            ny_sensor = Sensor(s_id, s_plats, s_troskel)
            aktiva_sensorer.append(ny_sensor)
            print(f"Systemmeddelande: Sensor:{s_id} är driftsatt.")

        #Lägger till ett nytt mätvärde på en sensor
        elif val == "2":
            print("\n INMATNING AV NYTT MÄTVÄRDE")
            sok_sensorID = input("Ange vilken senosor som du vill lägga in nytt värde för: ")
            sensor_funnen = False
            
            for sensor in aktiva_sensorer:
                if sensor.sensor_id == sok_sensorID:
                    sensor_funnen = True
            
                    try:
                        nytt_varde = float(input("Lägg det nya värdet på sensorn (Numreriskt)"))
                        sensor.lagg_till_varden(nytt_varde)
                        print(f"Systemmeddelande: Värde {nytt_varde} tillaggt")

                        if nytt_varde > sensor.troskel_varde:
                            print(f"!!! LARM !!! Varde {nytt_varde} överstiger godkänd nivå")

                    except ValueError:
                        print("Fel inmatning. Mata in ett numreriskt värde (tex. 44.5)")
                    break

            if not sensor_funnen:
                print(f"Sensor {sok_sensorID} kunde inte hittas i anläggnings register")

        #Lista över registrerade sensorer
        elif val == "3":
            print(" SAMTLIGA REGISTRERADE SENSORER")

            for sensor in aktiva_sensorer:
                print(f"\n{sensor.sensor_id}")
                print(f"{sensor.plats}")
                print(f"{sensor.troskel_varde}")

        #Sammanställning av mätvärden hos en sensor
        elif val == "4":
            print("\n[ SAMMANSTÄLLNING MÄTVÄRDEN HOS VALD SENSOR ]")
            vald_sensor = input("Mata in sensorID som du vill ha ut mätvärden på: ")
            sensor_funnen = False

            
            for sensor in aktiva_sensorer:
                if sensor.sensor_id == vald_sensor:
                    sensor_funnen = True
                    print(f"Mätvärden för sensor {vald_sensor}:\n")

                    for varden in sensor.historik:
                        print(f"Tid: {varden['tid']} | Värde: {varden['värde']}")

                    snitt, start, slut = sensor.medelvarde_matvarden()
                    print(f"\nMedelvärde: {snitt}")
                    print(f"Beräknat från perioden: {start} till {slut}")
                    break
            
            if not sensor_funnen:
                print(f"Sensor {vald_sensor} existerar inte i registret.")
                
                

        #Ändra informatinen på en sensor
        elif val == "5":
            print("\n[ KORRIGERING AV SENSORDATA ]")
            sok_id = input("Ange Sensor ID att kalibrera om: ")
            sensor_funnen = False

            for sensor in aktiva_sensorer:
                if sensor.sensor_id == sok_id:
                    sensor_funnen = True
                    print(f"Hittade {sok_id}. Tryck Enter utan att skriva något för att behålla nuvarande värde.")
                    
                    ny_plats = input(f"Ny plats (nuvarande: {sensor.plats}): ")
                    if ny_plats != "":
                        sensor.plats = ny_plats
                    
                    ny_troskel = input(f"Ny larmtröskel (nuvarande: {sensor.troskel_varde}): ")
                    if ny_troskel != "":
                        try:
                            sensor.troskel_varde = float(ny_troskel)
                        except ValueError:
                            print("Fel: Tröskeln måste vara numerisk. Det gamla värdet bibehålls.")
                    
                    print(f"Systemmeddelande: Sensor {sok_id} är uppdaterad.")
                    break
            
            if not sensor_funnen:
                print("Fel: Sensorn existerar inte i anläggningens register.")

        #Ta bort en sensor
        elif val == "6":
            print("\n[ DEMONTERING AV SENSOR ]")
            sok_id = input("Ange Sensor ID att skrota: ")
            sensor_funnen = False

            for sensor in aktiva_sensorer:
                if sensor.sensor_id == sok_id:
                    sensor_funnen = True
                    # Funktion för att radera ett element ur en lista
                    aktiva_sensorer.remove(sensor)
                    print(f"Systemmeddelande: Sensor {sok_id} har demonterats och raderats från registret.")
                    break
            
            if not sensor_funnen:
                print("Fel: Sensorn existerar inte i anläggningens register.")
           
        #Stäng ner programmet
        elif val == "7":
            print("Stänger ner anläggningen...")
            kor_system = False

        else:
            print("Felaktig inmatning... Ange ett numreiskt tal mellan 1-7: ")

if __name__ == "__main__":
    main()


