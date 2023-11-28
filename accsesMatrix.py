import pandas as pd
import csv
class AccessMatrix:

    def __init__(self, fileName: str):
        self.file = fileName
        self.data = pd.read_csv(self.file)
    def addCol(self, col: list):
        self.data[col[0]] = col[1:]
        self.data.to_csv(self.file, index=False)

    def addLine(self, line: list):
        newRow = pd.Series(line, index=self.data.columns)
        self.data = self.data._append(newRow, ignore_index=True)
        self.data.to_csv(self.file, index=False)
    def changeCell(self, user, file, newAccess):
        self.data.loc[self.data["users"] == user, file] = newAccess
        self.data.to_csv(self.file, index=False)
    def getCell(self, user, file):
        return self.data.loc[self.data["users"] == user, file].values[0]

    def getAllFiles(self):
        with open(self.file, newline='') as f:
            reader = csv.reader(f)
            row = next(reader)
            return row[1:]
    def getAllUsers(self):
        save = self.data.iloc[:, 0]
        return [i for i in save]
    def delCol(self, col):
       self.data = self.data.drop(col, axis=1)
       self.data.to_csv(self.file, index=False)

    def delLine(self, line):
        self.data = self.data[self.data["users"].str.contains(line) == False]
        self.data.to_csv(self.file, index=False)


