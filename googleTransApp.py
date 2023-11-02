import sys
from PyQt5 import uic  # QTdesiner에서 만든 ui룰 불러와주는 클래스
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


form_class = uic.loadUiType("ui/transUI.ui")[0]


class GoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스의 초기화자를 호출
        self.setupUi(self)  # 제작해 놓은 ui를 연결
        self.setWindowTitle('구글 번역기')
        self.setWindowIcon(QIcon('icon/google.png'))
        self.statusBar().showMessage('Google Trans App v1.0')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 프로그램을 종료 시키기 위한 명령
    myApp = GoogleTrans()
    myApp.show()
    sys.exit(app.exec_())  # 프로그램을 종료 시키기 위한 명령





