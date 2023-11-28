import user
import usersBase
import accsesMatrix
from os import remove
class Admin(user.User):
    def __init__(self, dataBase:usersBase.UsersDataBase, matrix:accsesMatrix.AccessMatrix):
        self.db = dataBase
        self.matrix = matrix
        files = self.matrix.getAllFiles()
        a = [7 for i in range(0,len(files))]
        user.User.__init__(self, "admin", files, [7] * len(files))

    def createNewObject(self, objName:str):
        if objName in self.matrix.getAllFiles():
            print("This file exist!")
            return
        n = len(self.matrix.getAllUsers())
        fileData = []
        fileData.append(objName)
        fileData.append('7')
        for i in range(1,n):
            fileData.append('0')
        self.matrix.addCol(fileData)
        file = open(objName, 'w')
        file.close()
        self.accesses[objName] = 7

    def createNewUser(self, userName, password='1'):
        if not self.db.createNewUser(userName, password):
            print('This user exist!')
            return
        n = len(self.matrix.getAllFiles())
        userData = []
        userData.append(userName)
        for i in range(0,n):
            userData.append('0')
        self.matrix.addLine(userData)

    def changeUsersAccess(self, userName, objectName, access):
        if not userName in self.matrix.getAllUsers():
            print("This user doesnt exist!")
            return
        if not objectName in self.matrix.getAllFiles():
            print("This file doesnt exist!")
            return
        if access > 7 or access < 0:
            print("Invalid value of access!")
            return
        self.matrix.changeCell(userName, objectName, access)

    def deleteUser(self, user:str):
        if(user == 'admin'):
            print('This user cannot deleted!')
            return
        if not user in self.matrix.getAllUsers():
            print("This user doesnt exist!")
            return
        self.matrix.delLine(user)
        self.db.deleteUser(user)
    def deleteObject(self, file):
        if not file in self.matrix.getAllFiles():
            print("This file doesnt exist!")
            return
        self.matrix.delCol(file)
        remove(file)
        del self.accesses[file]
