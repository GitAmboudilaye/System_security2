import requests

class Alarm_Requests():
    def __init__(self, zone1, zone2, zone3, zone4, status):
        self.url = 'http://10.1.10.89:5000/system/alarm'
        self.data = {
            'zone1': zone1,
            'zone2': zone2,
            'zone3': zone3,
            'zone4': zone4,
            'status': status,
        }

    def send_requests(self):
        try:
            response = requests.post(self.url, json=self.data)
            if response.status_code == 200:
                print("Envoi réussi")
            else:
                print(f"Status code est : {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(e)
