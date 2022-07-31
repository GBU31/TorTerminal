import os
from win import *


if __name__ == '__main__':

    
    app = QApplication(sys.argv)
    QApplication.setApplicationName(f"proxychainsShell-{os.popen('id -u -n').readline().strip()}")
    window = MainWindow()
    app.exec_()
