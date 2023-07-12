from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class BMIWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('SISTEM PERHITUNGAN BERAT BADAN IDEAL')
        
        self.input_label = QLabel("Masukkan berat badan (kg):")
        self.input_weight = QLineEdit()
        
        self.input_label2 = QLabel("Masukkan tinggi badan (cm):")
        self.input_height = QLineEdit()
        
        self.result_label = QLabel("BMI:")
        self.result_value = QLabel("")
        
        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.clicked.connect(self.calculateBMI)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_weight)
        layout.addWidget(self.input_label2)
        layout.addWidget(self.input_height)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_value)
        layout.addWidget(self.calculate_button)
        
        self.setLayout(layout)
    
    def calculateBMI(self):
        weight_text = self.input_weight.text()
        height_text = self.input_height.text()
        
        # Periksa apakah masukan berupa angka
        if not weight_text.isdigit() or not height_text.isdigit():
            QMessageBox.warning(self, "Kesalahan", "Tolong masukkan angka.")
            return
        
        weight = float(weight_text)
        height = float(height_text) / 100
        
        # Periksa apakah berat atau tinggi adalah 0
        if weight == 0 or height == 0:
            QMessageBox.warning(self, "Kesalahan", "Berat atau tinggi tidak boleh 0.")
            return
        
        bmi = weight / (height ** 2)
        
        self.result_value.setText(str(bmi))
        
        category = ""
        if bmi < 18.5:
            category = "Kurus"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Gemuk"
        else:
            category = "Obesitas"
        
        QMessageBox.information(self, "Kategori BMI", "Kategori BMI Anda: " + category)


app = QApplication([])
window = BMIWidget()
window.show()
app.exec_()
