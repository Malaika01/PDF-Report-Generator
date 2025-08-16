from CSV_Reader import CSV_Reader
from Report_generator import ReportGenerator
from Summary_generator import Summary_generator

def main():
    csv_reader = CSV_Reader(r"C:\Users\Admin\Desktop\Malaika\PDF-Report-Generator\SampleData\SampleData.xlsx")
    csv_reader.load_sheet_excel("SalesOrders")
    print("Excel file read")
    df = csv_reader.data
    get_summary = Summary_generator()
    heading, stats = get_summary.extract_data(df,"SalesOrders")
    print("Stats Calculated")
    report_gen = ReportGenerator()
    report_gen.save_report(heading,stats)


if __name__ == "__main__":
    main()