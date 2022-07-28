if __name__ == '__main__':
    from win import *

    
    app = QApplication(sys.argv)
    QApplication.setApplicationName('pcs')
    window = MainWindow()
    app.exec_()