class Product:
    def __init__(self):
        self.Tags = []

product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")