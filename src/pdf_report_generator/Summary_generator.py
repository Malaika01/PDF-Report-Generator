import pandas as pd
from datetime import date

class Summary_generator:
    def __init__(self):
        pass    

    def extract_data(self,df,sheet_name):
        title = sheet_name
        current_data = date.today()
        report_info = {}
        report_info["title"] = title
        report_info["date"] = current_data
        int_columns = df.select_dtypes(include=["int64","float64"]).columns
        stats = {}
        for col in int_columns:
            sum = df [col].sum()
            mean = df[col].mean()
            stats[col] = {}
            stats[col]["sum"] = sum
            stats [col]["mean"] = mean

        return report_info,stats
    
