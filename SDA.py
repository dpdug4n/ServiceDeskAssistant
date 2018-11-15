from gui_SDA import Ui_L3TServiceDeskAssistant
from PyQt5 import QtCore, QtGui, QtWidgets

class myMainWindow(QtWidgets.QMainWindow, Ui_L3TServiceDeskAssistant):
    def __init__(self, parent=None):
        super(myMainWindow, self).__init__(parent)  # call init of QMainWindow, or QWidget or whatever)
        self.setupUi(self)  # call the function that actually does all the stuff you set up in QtDesigner
        self.btnGenerate.clicked.connect(self.generate_click)
        self.btnClear.clicked.connect(self.clear_click)
        self.btnRequest.clicked.connect(self.request_click)
        self.btnAccessGranted.clicked.connect(self.accessGranted_click)
        self.btnClearFields.clicked.connect(self.clearFields_click)

    def generate_click(self):
        ticketNumber = self.txtTicketNumber.text()
        EUName = self.txtEUName.text()
        phoneNumber = self.txtPhoneNumber.text()
        index = self.cmbAttempt.currentIndex()
        if index == 0:
            self.txtCBOutput.setPlainText(
            "Hello "+EUName+",\n\nWe attempted to contact you at "+phoneNumber+
            " in regards to ticket "+ticketNumber+" and were unable to reach you. Please contact the Service Desk for further assistance. \n\nThank you!"
            )
        elif index == 1:
            self.txtCBOutput.setPlainText(
            "Hello "+EUName+",\n\nThis is our second attempt to contact you at "+phoneNumber+
            " in regards to ticket "+ticketNumber+". Please be advised, "+
            "we will set your ticket into a resolved status after our third attempt to reach you."+
            " If this issue is already resolved, please let us know by responding to this email."+
            " If you still need assistance, please contact the Service Desk at your earliest convenience"+
            "\n\nThank you!"
            )
        elif index == 2:
            self.txtCBOutput.setPlainText(
            "Hello "+EUName+",\n\nThis is our third attempt to contact you at "+phoneNumber+
            " in regards to ticket "+ticketNumber+". We are now placing your ticket into a "+
            "resolved status. If you still need assistance, please contact the Service Desk "+
            "within 5 business days to have your ticket reopened. \n\nThank you!"
            )

    def clear_click(self):
        self.txtTicketNumber.setText("")
        self.txtEUName.setText("")
        self.txtPhoneNumber.setText("")
        self.cmbAttempt.setCurrentIndex(0)
        self.txtCBOutput.setPlainText("")

    def request_click(self):
        EuName = self.txtEuName.text()
        pernr = self.txtPERNR.text()
        folderpath = self.txtFolderPath.text()
        access = str(self.cmbAccess.currentText())
        self.txtOutput.setPlainText(
        "Hello,\n\n"+EuName+"("+pernr+") is requesting "+access+" to shared folder:\n\n"+
        folderpath+"\n\n As the listed POCs, please reply back with your approval or denial.\n\n"+
        "Thank you!"
        )

    def accessGranted_click(self):
        ticketNumber = self.txtPocTicketNumber.text()
        folderpath = self.txtFolderPath.text()
        EuName = self.txtEuName.text()
        self.txtOutput.setPlainText(
        "Approval has come back for ticket "+ticketNumber+". You have been given access to the shared folder:\n\n"+
        folderpath+"\n\nThese changes require a restart of your machine and can take anywhere between"+
        "15 minutes to 24 hours to go into effect. I will resolve the ticket at this time, "+
        "but if you are unable to access the shared folder after 24 hours, please contact "+
        "the Service Desk and reference ticket "+ticketNumber+" so that we can assist you further."+
        "\n\n Thank you!"
        )
    def clearFields_click(self):
        self.txtEuName.setText("")
        self.txtPERNR.setText("")
        self.txtFolderPath.setText("")
        self.cmbAccess.setCurrentIndex(0)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
