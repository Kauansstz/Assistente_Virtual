import requests
from time import sleep


class Climate:
    def __init__(self):
        pass

    def climate_of_the_region(self):
        sleep(1)
        api = "https://wttr.in/palhoça"  # Getting an api with weather, percentage of rain at 4 times (Morning, beginning/Late afternoon and Night)
        response = requests.get(api)
        CLIMA = response.text
        return print(CLIMA)