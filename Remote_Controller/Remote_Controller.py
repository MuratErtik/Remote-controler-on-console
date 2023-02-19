import sqlite3

import time

import random


class Remote_Controller():

    def __init__(self, TV_status=" turn off", TV_sound=0, Channel_list=list(), Channel=""):

        self.TV_status = TV_status

        self.TV_sound = TV_sound

        self.Channel_list = Channel_list

        self.Channel = Channel

        self.Create_Connection()

        self.Channel_List()

    def Create_Connection(self):

        self.conn = sqlite3.connect("Channel_list.db")
        self.cursor = self.conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS Channel_List(

        Name TEXT)"""
        self.cursor.execute(query)
        self.conn.commit()

    def Finish_Connection(self):

        self.conn.close()

    def Channel_List(self):

        query = """SELECT * FROM Channel_List"""
        self.list1 = self.cursor.fetchall()
        self.Channel_list = self.list1

    def On_TV(self):

        if self.TV_status == "turn on":
            print("TV has been already turns on!")

        else:
            print("TV turns on .....")
            time.sleep(3)
            self.TV_status = "turn on"

    def Off_TV(self):
        if self.TV_status == "turn off":
            print("TV has been already turns off!")

        else:
            print("TV turns off.....")
            time.sleep(3)
            self.TV_status = "turn off"

    def Sound_Settings(self):

        while True:
            query = input(
                " Press '>' for increase the volume \n Presss '<' for reduce the volume\n Write 'mute' for volume = 0\n Press 'q' for exit ")

            if query == "q":
                print("Sound is updating.....")
                time.sleep(3)
                print("Sound:", self.TV_sound)
                break

            elif query == ">":
                if self.TV_sound != 100:
                    print("Increasing the sound....")
                    time.sleep(1)
                    self.TV_sound = self.TV_sound + 1
                    print("The sound has been increased...")

            elif query == "<":
                if self.TV_sound != 0:
                    print("Decreases sound....")
                    time.sleep(1)
                    self.TV_sound = self.TV_sound - 1
                    print("Volume has been reduced.")

            elif query == "mute":
                print("waiting...")
                time.sleep(1)
                self.TV_sound = 0



            else:
                print("You select invalid action! Please enter correct action")

    def Add_Channel(self):
        New_Channel = input("Please enter which channel you want to adding:")
        query = "SELECT * FROM Channel_List WHERE Name = ?"
        self.cursor.execute(query, (New_Channel,))
        self.list1 = self.cursor.fetchall()
        time.sleep(3)

        if len(self.list1) != 0:
            print("This channel has been already added!")

        else:
            query2 = """INSERT INTO Channel_List VALUES (?)"""
            self.cursor.execute(query2, (New_Channel,))
            self.conn.commit()
            print("Adding....")

    def Delete_Channel(self):

        Delete_Channel = input("Please enter which channel you want to deleting:")
        print("Deleting.....")
        time.sleep(3)
        query = """SELECT * FROM Channel_List WHERE Name = ?"""
        self.cursor.execute(query, (Delete_Channel,))
        self.list1 = self.cursor.fetchall()

        if len(self.list1) == 0:
            print("There is no such channel!")

        else:
            query = """DELETE FROM Channel_List WHERE Name = ?"""
            self.cursor.execute(query, (Delete_Channel,))
            self.conn.commit()
            print("The channel has been deleted.")

    def Show_Channel_List(self):

        print("The channel list is opening.....")
        time.sleep(3)
        query = """SELECT * FROM Channel_List"""
        self.cursor.execute(query)
        self.list1 = self.cursor.fetchall()

        if len(self.list1) == 0:
            print("Channel list empty!")

        else:
            j = 1
            for i in self.list1:
                print("{}.)".format(j), i)
                j = j + 1

    def Random_Channel(self):

        query = """SELECT * FROM Channel_List"""
        self.cursor.execute(query)
        self.list1 = self.cursor.fetchall()

        print("Chancing the channel...")
        time.sleep(3)
        rnd = random.randint(0, len(self.list1) - 1)
        self.Channel = self.list1[rnd]
        print("The channel that is currently open:", self.Channel)

    def Choosen_Channel(self):

        answer = int(input("Please enter number of channel which channel want you open:"))

        if len(self.list1) >= answer:
            print("Channel opens...")
            time.sleep(3)
            self.Channel = self.list1[answer - 1]
            print("Channel:", self.Channel)

        else:
            print("İnvalid selection!")

    def __str__(self):

        query = """SELECT * FROM Channel_List"""
        self.cursor.execute(query)
        self.list1 = self.cursor.fetchall()

        return " TV Status: {}\n TV Sound: {}\n Channel: {}\n Channel List: {}\n".format(self.TV_status, self.TV_sound,
                                                                                         self.Channel, self.list1)


rmtcntroller = Remote_Controller()

print(""""


***************************************************

           REMOTE CONTROLLER APPLICATION

***************************************************


1.) Turn on the TV

2.) Turn off the TV

3.) Sound Settings

4.) Add Channel

5.) Delete Channel

6.) Show the channel list

7.) Random Channel

8.) Choosen Channel

9.) Informations of TV


Please press 'q' for close the application


****************************************************


""")

while True:
    action = input("Select your action you want to do in App: ")

    if action == "q":

        print("Application is closing...")
        time.sleep(3)
        print("Closed")
        break



    elif action == "1":

        rmtcntroller.On_TV()




    elif action == "2":

        rmtcntroller.Off_TV()




    elif action == "3":

        if rmtcntroller.TV_status == "turn on":
            rmtcntroller.Sound_Settings()

        else:
            print("TV is turn off")

    elif action == "4":

        if rmtcntroller.TV_status == "turn on":
            rmtcntroller.Add_Channel()

        else:
            print("TV is turn off")


    elif action == "5":

        if rmtcntroller.TV_status == "turn on":
            rmtcntroller.Delete_Channel()

        else:
            print("TV is turn off")


    elif action == "6":

        if rmtcntroller.TV_status == "turn on":
            rmtcntroller.Show_Channel_List()

        else:
            print("TV is turn off")



    elif action == "7":

        if rmtcntroller.TV_status == "turn on":
            rmtcntroller.Random_Channel()

        else:
            print("TV is turn off")

    elif action == "8":

        if rmtcntroller.TV_status == "turn on":
            rmtcntroller.Choosen_Channel()

        else:
            print("TV is turn off")

    elif action == "9":

        if rmtcntroller.TV_status == "turn on":
            print(rmtcntroller)

        else:
            print("TV is turn off")


    else:
        print("You select invalid action! Please enter correct action")