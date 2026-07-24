import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# Define the data source as a dictionary (equivalent to the Order class)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Section 1: Default Smart Marker - values spread horizontally across cells
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# Bind the data source and process Smart Markers
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# Save the resulting workbook
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()