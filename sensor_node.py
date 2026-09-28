import datetime

class Sensor:
    def __init__(self, sensor_id, plats, troskel_varde):
        self.sensor_id = sensor_id
        self.plats = plats
        self.troskel_varde = troskel_varde
        self.historik = [] #Lista för lagring av mätvärden i objektet

    def lagg_till_varden(self, varde):
        aktuell_tid = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        post = {"tid": aktuell_tid, "värde": varde}
        self.historik.append(post)

    def medelvarde_matvarden(self):
        # Skydd mot ZeroDivisionError 
        if len(self.historik) == 0:
            return 0, "Ingen data", "Ingen data"

        totala_varden = 0
        
        for post in self.historik:
            totala_varden += post["värde"]
        medelvarde = totala_varden / len(self.historik)

        start_tid = self.historik[0]["tid"]
        slut_tid = self.historik[-1]["tid"]
        
        return medelvarde, start_tid, slut_tid

        