import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('Login')

        self.userLabel = QLabel('Username:', self)
        self.userLabel.move(50, 50)
        self.userEdit = QLineEdit(self)
        self.userEdit.move(150, 50)

        self.passLabel = QLabel('Password:', self)
        self.passLabel.move(50, 100)
        self.passEdit = QLineEdit(self)
        self.passEdit.move(150, 100)
        self.passEdit.setEchoMode(QLineEdit.Password)

        self.loginButton = QPushButton('Login', self)
        self.loginButton.move(150, 150)
        self.loginButton.clicked.connect(self.login)

        self.setGeometry(500, 500, 400, 250)
        self.show()

    def login(self):

        username = self.userEdit.text()
        password = self.passEdit.text()

        if username == 'admin' and password == 'password':
            QMessageBox.information(self, 'Login Successful', 'Welcome ' + username + '!')
        else:
            QMessageBox.warning(self, 'Login Failed', 'Incorrect username or password. Please try again.')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())
