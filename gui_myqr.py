import qrcode
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class QRCode(QWidget):
    def __init__(self):
        super(QRCode,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("二维码生成器")
        self.setFixedSize(300,450)
        self.show_qrcode=QLabel(self)
        self.show_qrcode.setGeometry(20,20,260,260)
        self.show_qrcode.setStyleSheet("background-color:white")
        self.input_msg=QTextEdit(self)
        self.input_msg.setPlaceholderText("请输入文字、网址")
        self.input_msg.setGeometry(20,300,260,80)
        self.btn=QPushButton(self)
        self.btn.setText("生成二维码")
        self.btn.setGeometry(20,400,260,30)
        self.btn.clicked.connect(self.make)

    def make(self):
        text=self.input_msg.toPlainText().strip()
        if text=="":
            QMessageBox.warning(self,'提示',
                                '输入不能为空！')
            return
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image()
        img.save('qr.png')
        pixmap=QPixmap('qr.png')
        self.show_qrcode.setScaledContents(True)
        self.show_qrcode.setPixmap(pixmap)

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=QRCode()
    ex.show()
    sys.exit(app.exec_())
