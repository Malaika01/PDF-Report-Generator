import pandas as pd

class CSV_Reader:
    def __init__(self,file_name):
        self.file_name = file_name
        self.data = None

    def load_excel(self):
        df = pd.read_excel(self.file_name)
        self.data = df

    def load_sheet_excel(self,sheet_name):
        df = pd.read_excel(self.file_name,sheet_name=sheet_name)
        self.data = df
