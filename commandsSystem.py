import cmd

import accsesMatrix
import admin
import usersBase
from user import User
class CommandsSystems(cmd.Cmd):
    prompt = 'admin' + '>'
    def __init__(self):
        cmd.Cmd.__init__(self)
        db = usersBase.UsersDataBase()
        mat = accsesMatrix.AccessMatrix('matrix.csv')
        self.admin = admin.Admin(db, mat)
        self.currentUser = self.admin
    def do_write(self, line):
        self.currentUser.write(line)
    def do_read(self, line):
        self.currentUser.read(line)
    def do_cns(self, line):
        if(self.currentUser == self.admin):
            self.admin.createNewUser(line)
        else:
            print("For this command you mast have administrator rights")
    def do_cno(self, line):
        if (self.currentUser == self.admin):
            self.admin.createNewObject(line)
        else:
            print("For this command you mast have administrator rights")
    def do_cua(self, line):
        args = line.split()
        self.admin.changeUsersAccess(args[0], args[1], int(args[2]))
    def do_delu(self, line):
        if (self.currentUser == self.admin):
            self.admin.deleteUser(line)
        else:
            print("For this command you mast have administrator rights")

    def do_delo(self, line):
        if (self.currentUser == self.admin):
            self.admin.deleteObject(line)
        else:
            print("For this command you mast have administrator rights")

    def do_chng(self, line):
        user = input("Name:")
        password = input("Password:")
        if not self.admin.db.autentification(user, password):
            print("Inccorect username of password!")
        else:
            if user == 'admin':
                self.currentUser = self.admin
                return
            files = self.admin.matrix.getAllFiles()
            accesses = [int(self.admin.matrix.getCell(user, f)) for f in files]
            self.currentUser = User(user, files, accesses)
            promp = user + '>'
    def do_exit(self, line):
        exit()
        return