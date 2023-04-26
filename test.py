import random

import function
from function import *
import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QSizePolicy, QScrollArea
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QTimer
i = 0
answer = 'azerty'
class ChatBot(QWidget):
    def __init__(self):
        super().__init__()
        # self.i = 0
        self.initUI()
        self.connectSignals()

    def initUI(self):
        self.setWindowTitle('ChatBot')
        self.setFixedSize(600, 1000)

        self.setAutoFillBackground(True)
        palette = self.palette()
        background_image = QPixmap("funny.jpg")
        palette.setBrush(QPalette.Window,
                         QBrush(background_image.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.setPalette(palette)
        self.setStyleSheet("border-radius: 20px;")

        """
        # positionne ma fenêtre au coin supérieur gauche
        screen_geometry = QApplication.desktop().availableGeometry()
        self.move(screen_geometry.x(), screen_geometry.y())
        """

        # positionne ma fenêtre au coin supérieur droit
        screen_geometry = QApplication.desktop().availableGeometry()
        self.move(screen_geometry.width() - self.width(), 0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.message_widget = QWidget()
        self.message_area = QVBoxLayout(self.message_widget)
        self.message_area.setAlignment(Qt.AlignTop)
        self.message_area.setSpacing(15)

        self.scroll_area.setWidget(self.message_widget)

        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("background-color: transparent;")
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.addWidget(self.scroll_area)


        # Ajoutez le contenu à la zone de message comme avant.
        self.user_message = QTextEdit()
        self.user_message.setStyleSheet(
            'background-color: white; border-radius: 10px; font-family: Monotype Corsiva; font-size: 25px; padding-left: 10px')
        self.user_message.setFixedHeight(40)
        self.user_message.setPlaceholderText("Tapez votre message...")
        self.user_message.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.user_message.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.send_button = QPushButton('Okay')
        self.send_button.setStyleSheet(
            'background-color: #0084ff; font-family: Monotype Corsiva; font-size: 20px; color: white; border-radius: 10px;')
        self.send_button.setFixedHeight(40)
        self.send_button.setFixedWidth(80)

        self.bottom_bar = QHBoxLayout()
        self.bottom_bar.addWidget(self.user_message)
        self.bottom_bar.addWidget(self.send_button)
        self.bottom_bar.setSpacing(10)
        self.bottom_bar.setContentsMargins(10, 10, 10, 10)
        self.bottom_bar.setAlignment(Qt.AlignBottom)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.scroll_widget)
        self.main_layout.addLayout(self.bottom_bar)
        self.greet()

    def scrollToBottom(self):
        scrollbar = self.scroll_area.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def greet(self):
        bot_response01 = 'Hello! My name is Apasize. I was created in April 2023.'
        QTimer.singleShot(1000, lambda: self.addMessage(bot_response01, False))
        bot_response02 = 'Please, remind me your name.'
        QTimer.singleShot(2000, lambda: self.addMessage(bot_response02, False))

    def remind_name(self, message):
        bot_response = 'What a great name you have, ' + message + '!'
        QTimer.singleShot(1500, lambda: self.addMessage(bot_response, False))
        bot_response01 = 'Let me guess your age.'
        QTimer.singleShot(3000, lambda: self.addMessage(bot_response01, False))
        bot_response02 = 'Enter remainders of dividing your age by 3, 5 and 7.'
        QTimer.singleShot(4000, lambda: self.addMessage(bot_response02, False))

    def guess_age_and_enjoy(self, message):
        remainders = message.split(',') # couper en fonction de l'espace la saisie de l'utilisateur
        #print(remainders)
        if(remainders and remainders[0] and remainders[1] and remainders[2]):
            rem3 = int(remainders[0])
            rem5 = int(remainders[1])
            rem7 = int(remainders[2])
        else:
            rem3 = 0
            rem5 = 0
            rem7 = 0
        age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

        bot_response = "You are " + str(age) + " years old; that's a good time to start programming!"
        QTimer.singleShot(1000, lambda: self.addMessage(bot_response, False))



        bot_message = "Let's test your Projects knowledge."
        QTimer.singleShot(2000, lambda: self.addMessage(bot_message, False))
        # write your code here
        quiz = ["What technologies and tools does the Find_Me project use ?",
                "What technologies and tools does the PlantVision use ?",
                "What technologies and tools does the StressZero use ?",
                "What technologies and tools does the PerfectWriting use ?",
                "What technologies and tools does the MyMonotoringCamera use ?",
                "What technologies and tools does the Otakumate use ?",
                "What technologies and tools does the HomeLinks use ?"]

        response = {
            'response00': ('Supervised Learning', 'Computer Vision', 'Internet Of Objects', 'Deep Learning', 'All above'),
            'response01': ('Data Clustering', 'Supervised Learning', 'Computer Vision', 'MyFavoriteHero', 'Deep Learning'),
            'response02': ('Computer Vision', 'Internet Of Objects', 'Deep Learning', 'Supervised Learning', 'Akaza_Dono'),
            'response03': ('Supervised Learning', 'To be an otaku', 'Deep Learning', ' Kit ARDUINO', 'Computer Vision'),
            'response04': ('Deep Learning', 'Supervised Learning', 'Internet Of Objects', 'Computer Vision', 'Eren Jäger'),
            'response05': ('Python', 'Computer Vision', 'Internet Of Objects', 'Supervised Learning', 'Boobs and imagination'),
            'response06': ('Internet Of Objects', 'Supervised Learning', 'All above', 'Data Clustering', 'Have a girl friend')

        }

        answers = {
            'response00': ['1,3'],
            'response01': ['2,3,5'],
            'response02': ['1,3,4'],
            'response03': ['1,3,5'],
            'response04': ['1,2,4'],
            'response05': ['1,4'],
            'response06': ['3']

        }

        tmp = random.randint(0, 6)
        resp = str('response0' + str(tmp))
        bot_response01 = quiz[tmp] + '\n' + '1. ' + response[resp][0] + '\n' + '2. ' + response[resp][1] + '\n' + '3. ' + \
                       response[resp][2] + '\n' + '4. ' + response[resp][3] + '\n' + '5. ' + response[resp][4]
        QTimer.singleShot(3000, lambda: self.addMessage(bot_response01, False))


        global answer
        answer = answers[resp][0]

    def test(self, message):

        if(message == answer):
            bot_message01 = 'Congratulations!!!'
            QTimer.singleShot(1000, lambda: self.addMessage(bot_message01, False))
            bot_message02 = 'Now you have unlocked the level allowing you to use commands to control our IoT tool!'
            QTimer.singleShot(1500, lambda: self.addMessage(bot_message02, False))
            bot_message = 'How can I help you? Enter your command'
            QTimer.singleShot(2000, lambda: self.addMessage(bot_message, False))
        else:
            bot_message01 = 'GAME OVER!!!'
            QTimer.singleShot(1000, lambda: self.addMessage(bot_message01, False))
            bot_message02 = 'You love anime too much! Baaaka!'
            QTimer.singleShot(1500, lambda: self.addMessage(bot_message02, False))
            bot_message03 = "Don't even try anymore. you can't..."
            QTimer.singleShot(2000, lambda: self.addMessage(bot_message03, False))





    def command(self, command):
        # décomposition de la commande
        command_words = command.split(" ")

        # appel de la fonction permettant de trouver clairement ce que l'utilisateur veut
        user_prompt = function.prompt(command_words)
        #print(user_prompt)
        bot_response = 'A few moments...'
        QTimer.singleShot(500, lambda: self.addMessage(bot_response, False))
        send_prompt(user_prompt)

        action = user_prompt.split(' ')[0]
        #print(action)
        if action == "temp":
            bot_message = 'Your results.\n'+function.get_message().split('\n')[0]
            #print(bot_message)
            QTimer.singleShot(1200, lambda: self.addMessage(bot_message, False))
        if action =="hum":
            bot_message = 'Your results.\n'+function.get_message().split('\n')[0]
            QTimer.singleShot(1200, lambda: self.addMessage(bot_message, False))

    def addMessage(self, message, isUser):
        message_label = QLabel(message)
        message_label.setWordWrap(True)

        message_label.setStyleSheet(
            'background-color: #EDEDED; border-radius: 10px; padding: 5px; font-family: Monotype Corsiva; font-size: 20px;')

        if isUser:
            message_layout = QHBoxLayout()
            message_layout.addWidget(QLabel())
            message_layout.addWidget(message_label)
        else:
            message_layout = QHBoxLayout()
            message_layout.addWidget(message_label)
            message_layout.addWidget(QLabel())

        message_layout.setContentsMargins(-10, 5, 10, 5)

        self.message_area.addLayout(message_layout)
        self.scroll_area.ensureWidgetVisible(self.message_widget)

    def execute(self):
        global i, answer
        #print(i)
        #print(self.send_button.isChecked())
        command_list = ['name', 'age', 'test', 'command']
        if command_list[i] == 'name':
            message = self.sendUserMessage()
            self.remind_name(message)
            i += 1
        elif command_list[i] == 'age':
            message = self.sendUserMessage()
            self.guess_age_and_enjoy(message)
            i += 1
        elif command_list[i] == 'test':
            message = self.sendUserMessage()
            self.test(message)
            i += 1
        elif command_list[i] == 'command':
            commande = self.sendUserMessage()
            self.command(commande)


    def sendUserMessage(self):
        message_text = self.user_message.toPlainText()
        QTimer.singleShot(0, lambda: self.addMessage(message_text, True))
        #print(message_text)

        self.user_message.clear()

        # Set focus back to the user message QTextEdit
        self.user_message.setFocus()
        return message_text

    def connectSignals(self):
        self.setLayout(self.main_layout)
        self.send_button.clicked.connect(self.execute)
        #self.user_message.returnPressed.connect(self.execute)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chatbot = ChatBot()
    #chatbot.connectSignals()
    chatbot.show()
    sys.exit(app.exec_())



"""
    def connectSignals(self):
        self.i += 1
        print(self.send_button.isChecked())
        command_list = ['greet', 'name', 'age', 'test', 'command']
        self.setLayout(self.main_layout)
        if command_list[self.i - 1] == 'greet':
            self.greet()
            print(self.send_button.isChecked())

        elif self.send_button.isChecked():
            print(self.send_button.isChecked())
            #if command_list[self.i - 1] == 'name':
            self.sendUserMessage()
            self.remind_name()
        elif command_list[self.i - 1] == 'age':
            if self.send_button.isChecked():
                self.guess_age()
        elif command_list[self.i - 1] == 'test':
            if self.send_button.isChecked():
                self.test()
        elif command_list[self.i - 1] == 'command':
            if self.send_button.isChecked():
                self.command()
        print(self.send_button.isChecked())
        #self.send_button.clicked.connect(self.remind_name)
    
"""