from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView

 
app = QApplication()
window = QMainWindow()
browser = QWebEngineView()

browser.setUrl(QUrl("https://github.com/"))
window.setCentralWidget(browser)

 
window.show()
app.exec_()
