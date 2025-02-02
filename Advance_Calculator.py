# from PyQt5 import QtCore, QtGui, QtWidgets

# class Calculator(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Advanced Calculator")
#         self.setGeometry(100, 100, 500, 700)  # Bigger Window
#         self.initUI()

#     def initUI(self):
#         self.expression = ""  # Stores the current input
        
#         # Display label
#         self.outputlabel = QtWidgets.QLabel(self)
#         self.outputlabel.setGeometry(20, 20, 460, 100)  # Bigger Display
#         self.outputlabel.setFont(QtGui.QFont("Arial", 32))
#         self.outputlabel.setStyleSheet("background-color: white; border: 3px solid black; padding-right: 15px;")
#         self.outputlabel.setAlignment(QtCore.Qt.AlignRight)
#         self.outputlabel.setText("0")

#         # Button Layout
#         buttons = [
#             ('%', 20, 140), ('C', 130, 140), ('<<', 240, 140), ('/', 350, 140),
#             ('7', 20, 240), ('8', 130, 240), ('9', 240, 240), ('x', 350, 240),
#             ('4', 20, 340), ('5', 130, 340), ('6', 240, 340), ('-', 350, 340),
#             ('1', 20, 440), ('2', 130, 440), ('3', 240, 440), ('+', 350, 440),
#             ('+/-', 20, 540), ('0', 130, 540), ('.', 240, 540), ('=', 350, 540),
#         ]

#         self.buttons = {}
#         for text, x, y in buttons:
#             self.buttons[text] = QtWidgets.QPushButton(text, self)
#             self.buttons[text].setGeometry(x, y, 110, 90)  # Bigger Buttons
#             self.buttons[text].setFont(QtGui.QFont("Arial", 24))
#             self.buttons[text].setStyleSheet(
#                 "background-color: lightgray; border-radius: 15px; padding: 8px;"
#                 "border: 2px solid gray;")
#             self.buttons[text].clicked.connect(lambda checked, t=text: self.press_it(t))

#         # Styling specific buttons
#         self.buttons['='].setStyleSheet("background-color: green; color: white; border-radius: 15px; font-size: 26px;")
#         self.buttons['C'].setStyleSheet("background-color: red; color: white; border-radius: 15px; font-size: 26px;")
#         self.buttons['<<'].setStyleSheet("background-color: orange; color: white; border-radius: 15px; font-size: 26px;")
#         self.buttons['+'].setStyleSheet("background-color: blue; color: white; border-radius: 15px; font-size: 26px;")
#         self.buttons['-'].setStyleSheet("background-color: blue; color: white; border-radius: 15px; font-size: 26px;")
#         self.buttons['x'].setStyleSheet("background-color: blue; color: white; border-radius: 15px; font-size: 26px;")
#         self.buttons['/'].setStyleSheet("background-color: blue; color: white; border-radius: 15px; font-size: 26px;")

#     def press_it(self, pressed):
#         """Handles button clicks"""
#         if pressed == "C":
#             self.expression = ""
#             self.outputlabel.setText("0")
#         elif pressed == "<<":
#             self.expression = self.expression[:-1] if self.expression else ""
#             self.update_display()
#         elif pressed == "=":
#             try:
#                 # Replace 'x' with '*' for evaluation
#                 result = eval(self.expression.replace("x", "*").replace("%", "/100"))
#                 # Format to 4 decimal places
#                 formatted_result = f"{result:.4f}"
#                 self.expression = formatted_result  # Store full result
#                 self.update_display()
#             except:
#                 self.outputlabel.setText("Error")
#                 self.expression = ""
#         elif pressed == "+/-":
#             if self.expression and not self.expression.startswith("-"):
#                 self.expression = "-" + self.expression
#             elif self.expression.startswith("-"):
#                 self.expression = self.expression[1:]
#             self.update_display()
#         else:
#             if self.outputlabel.text() == "0" or self.outputlabel.text() == "Error":
#                 self.expression = pressed
#             else:
#                 self.expression += pressed
#             self.update_display()

#     def update_display(self):
#         """Updates the display and limits output length"""
#         max_length = 12  # Maximum characters to display
#         if len(self.expression) > max_length:
#             self.outputlabel.setText(self.expression[:max_length] + "...")
#         else:
#             self.outputlabel.setText(self.expression)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = Calculator()
#     window.show()
#     sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1200)
        MainWindow.setStyleSheet("background-color: #f0f0f0;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Display
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 10, 780, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.display.setFont(font)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000;
                border: 2px solid #888;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        self.display.setObjectName("display")

        # Degree/Radian Switch
        self.mode_group = QtWidgets.QGroupBox(self.centralwidget)
        self.mode_group.setGeometry(QtCore.QRect(620, 120, 160, 60))
        self.mode_group.setStyleSheet("background-color: #ddd; border-radius: 5px;")
        self.mode_group.setTitle("")

        self.deg_mode = QtWidgets.QRadioButton(self.mode_group)
        self.deg_mode.setGeometry(QtCore.QRect(10, 15, 60, 30))
        self.deg_mode.setText("Deg")
        self.deg_mode.setChecked(True)
        
        self.rad_mode = QtWidgets.QRadioButton(self.mode_group)
        self.rad_mode.setGeometry(QtCore.QRect(80, 15, 60, 30))
        self.rad_mode.setText("Rad")

        # Buttons Layout
        self.buttons = {
            'sin': (10, 200), 'cos': (150, 200), 'tan': (290, 200), 'π': (430, 200), 'e': (570, 200),
            'sin⁻¹': (10, 290), 'cos⁻¹': (150, 290), 'tan⁻¹': (290, 290), 'xʸ': (430, 290), '√': (570, 290),
            'x³': (10, 380), 'x²': (150, 380), 'eˣ': (290, 380), '10ˣ': (430, 380), '%': (570, 380),
            '(': (10, 470), ')': (150, 470), '1/x': (290, 470), 'ln': (430, 470), 'log': (570, 470),
            '7': (10, 560), '8': (150, 560), '9': (290, 560), '+': (430, 560), 'Back': (570, 560),
            '4': (10, 650), '5': (150, 650), '6': (290, 650), '-': (430, 650), 'Ans': (570, 650),
            '1': (10, 740), '2': (150, 740), '3': (290, 740), '×': (430, 740), 'M+': (570, 740),
            '0': (10, 830), '.': (150, 830), 'EXP': (290, 830), '÷': (430, 830), 'M-': (570, 830),
            '±': (10, 920), 'RND': (150, 920), 'AC': (290, 920), '=': (430, 920), 'MR': (570, 920)
        }

        self.create_buttons()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button functionality
        self.setup_connections()
        self.memory = 0

    def create_buttons(self):
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)

        self.button_objects = {}
        for btn_text, pos in self.buttons.items():
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setGeometry(QtCore.QRect(pos[0], pos[1], 130, 80))
            btn.setFont(font)
            btn.setText(btn_text)

            if btn_text in ['+', '-', '×', '÷', '=', '^', '√', 'log', 'ln', 'EXP', '%']:
                btn.setStyleSheet("background-color: #ffcccb; color: #000; border-radius: 10px;")
            elif btn_text in ['sin', 'cos', 'tan', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'xʸ', 'eˣ', '10ˣ', 'π', 'e']:
                btn.setStyleSheet("background-color: #add8e6; color: #000; border-radius: 10px;")
            else:
                btn.setStyleSheet("background-color: #d3d3d3; color: #000; border-radius: 10px;")

            self.button_objects[btn_text] = btn

    def setup_connections(self):
        for btn_text, btn in self.button_objects.items():
            if btn_text not in ['=', 'AC', 'Back', 'M+', 'M-', 'MR', 'Ans']:
                btn.clicked.connect(lambda _, b=btn_text: self.add_to_display(b))
            elif btn_text == '=':
                btn.clicked.connect(self.calculate_result)
            elif btn_text == 'AC':
                btn.clicked.connect(self.clear_display)
            elif btn_text == 'Back':
                btn.clicked.connect(self.backspace)
            elif btn_text == 'M+':
                btn.clicked.connect(self.memory_add)
            elif btn_text == 'M-':
                btn.clicked.connect(self.memory_subtract)
            elif btn_text == 'MR':
                btn.clicked.connect(self.memory_recall)

    def add_to_display(self, value):
        current_text = self.display.text()
        if value == 'x²':
            self.display.setText(current_text + '**2')
        elif value == 'x³':
            self.display.setText(current_text + '**3')
        elif value == 'xʸ':
            self.display.setText(current_text + '**')
        else:
            self.display.setText(current_text + value)

    def calculate_result(self):
        try:
            expression = self.display.text()
            expression = expression.replace('÷', '/')
            expression = expression.replace('×', '*')
            expression = expression.replace('√', 'math.sqrt')
            expression = expression.replace('π', str(math.pi))
            expression = expression.replace('e', str(math.e))
            expression = expression.replace('^', '**')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')
            if self.rad_mode.isChecked():
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
            else:
                expression = expression.replace('sin', 'math.sin(math.radians')
                expression = expression.replace('cos', 'math.cos(math.radians')
                expression = expression.replace('tan', 'math.tan(math.radians')
            result = eval(expression)
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error")

    def clear_display(self):
        self.display.clear()

    def backspace(self):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])

    def memory_add(self):
        try:
            self.memory += float(self.display.text())
        except ValueError:
            pass

    def memory_subtract(self):
        try:
            self.memory -= float(self.display.text())
        except ValueError:
            pass

    def memory_recall(self):
        self.display.setText(str(self.memory))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enhanced Scientific Calculator"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())