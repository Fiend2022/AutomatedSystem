import sqlite3



class UsersDataBase:

    def __init__(self):
        self.dataBaseName = 'users.db'
        self.connection = sqlite3.connect(self.dataBaseName)
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )
        ''')
        if not self.__userExistCheck('admin'):
            self.cursor.execute('INSERT INTO Users (username, password) VALUES (?, ?)', ('admin', 'R1fmabe55'))
        self.connection.commit()
        return

    def createNewUser(self, userName: str, password: str):
        if not self.__userExistCheck(userName):
            self.cursor.execute('INSERT INTO Users (username, password) VALUES (?, ?)', (userName, password))
            self.connection.commit()
            return True
        else:
            return False

    def deleteUser(self, userName: str):

        if self.__userExistCheck(userName):
            self.cursor.execute('DELETE FROM Users WHERE username = ?', (userName,))
            self.connection.commit()
        else:
            print('This user doesnt exist!')

        return

    def updatePassword(self, userName: str, newPass: str):

        if self.__userExistCheck(userName):
            self.cursor.execute('UPDATE Users SET password = ? WHERE username = ?', (newPass, userName))

            self.connection.commit()
        else:
            print('This user doesnt exist!')
        return

    def __userExistCheck(self, userName:str):
        self.cursor.execute('SELECT username FROM Users WHERE username = ?', (userName,))
        exist = self.cursor.fetchone()
        return exist
    def __del__(self):
        self.connection.close()
    def autentification(self, userName:str, password:str):
        user = self.__userExistCheck(userName)
        if not user:
            return False
        else:
            self.cursor.execute('SELECT password FROM Users WHERE username = ?', (userName,))
            paswd = self.cursor.fetchone()
            if paswd[0] == password:
                return True
            else:
                return False


