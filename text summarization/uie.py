# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 700)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QTextEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 531, 441))
        self.lineEdit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QTextEdit(Dialog)
        # self.lineEdit_2 = QtWidgets.QTextEdit
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 160, 531, 441))
        self.lineEdit_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "create"))
        self.lineEdit_2.setReadOnly(True)
        self.pushButton.clicked.connect(self.fun_1)

    def fun_1(self):



        # result= (self.lineEdit.text())

        text=self.lineEdit.toPlainText()


        # In[3]:

        stemmer = SnowballStemmer("english")
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)

        # In[16]:

        print(words)

        # In[4]:

        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue

            word = stemmer.stem(word)

            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1

        # In[5]:

        # print(freqTable)

        # In[6]:

        sentences = sent_tokenize(text)
        sentenceValue = dict()

        # In[17]:

        # print(sentences)

        # In[7]:

        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        # print("Word =>", word)
                        # print("Sentence =>", sentence)
                        sentenceValue[sentence] += freq
                    else:
                        # print("Word =>", word)
                        # print("Sentence =>", sentence)
                        sentenceValue[sentence] = freq

        # In[8]:

        # print(sentenceValue)

        # In[9]:

        len(words)
        # len(sentenceValue)

        # In[10]:

        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]

        # In[11]:

        sumValues

        # In[12]:

        average = int(sumValues / len(sentenceValue))

        # In[13]:

        average

        # In[14]:

        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence

        # In[15]:

        result= (summary)
        print(result)



        self.lineEdit_2.setText(str(result))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

