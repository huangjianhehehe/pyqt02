from PySide2.QtWidgets import QApplication,QMessageBox,QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys,os


class Stats:
    def __init__(self):
        qfile_stats = QFile("ui/mywindow.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)


def main():
    app = QApplication(sys.argv)
    widgets = Stats()
    widgets.ui.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()