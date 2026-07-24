class Order:
    def __init__(self, items):
        self._items = items

    @property
    def Items(self):
        return self._items

    @Items.setter
    def Items(self, value):
        self._items = value

order = Order(["Apple", "Banana", "Cherry", "Date"])

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Section 1: Default Smart Marker - values spread horizontally across cells
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# Bind the data source and process Smart Markers
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# Save the resulting workbook
workbook.save("output_comparison.xlsx")