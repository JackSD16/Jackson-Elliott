import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
import requests


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather API App")
        self.setGeometry(400, 400, 700, 600)


        self.search = QLineEdit(self)
        self.search.setGeometry(50, 500, 400, 40)
        self.search.setStyleSheet("font-size: 20px; border: 1px solid #ccc; border-color: #FF6E00; border-radius: 4px")
        self.search.setPlaceholderText("Search for a city: Ex: Los Angeles")


        self.button = QPushButton("Search", self)
        self.button.setGeometry(470, 500, 150, 40)
        self.button.setStyleSheet("font-size: 20px; background-color: #FF6E00; border-radius: 4px;")
        self.button.clicked.connect(self.button_clicked)

        self.title = QLabel("Weather API APP", self)
        self.title.setGeometry(200, 20, 400, 50)
        self.title.setStyleSheet("font-size: 35px; font-weight: bold; font-style: italic")


        Sun = QPixmap("Sun.jpg")
        self.label = QLabel(self)
        self.label.setPixmap(Sun)
        self.label.setScaledContents(True)
        self.label.setGeometry(250, 100, 200, 200)
        self.label.show()


        self.weather_label = QLabel(self)
        self.weather_label.setGeometry(100, 320, 500, 150)
        self.weather_label.setStyleSheet("font-size: 23px; font-style: italic")
        self.weather_label.setWordWrap(True)

    def button_clicked(self):
        self.get_info()

    def get_info(self):
        city = self.search.text()
        key = ''
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=imperial'

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

              
                city_name = data['name']
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                description = data['weather'][0]['description'].title()


                info = f"City: {city_name}\nTemperature: {temp}°F\nFeels Like: {feels_like}°F\nHumidity: {humidity}%\nCondition: {description}"

                self.weather_label.setText(info)

            else:
                self.weather_label.setText("City not found. Please try again.")

        except Exception as e:
            self.weather_label.setText("Error fetching weather data.")
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
