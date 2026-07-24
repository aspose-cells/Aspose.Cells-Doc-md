import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat
import java.time as _jt
import java.util as _ju

outputDir = "C:\\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Column headers
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Department")
cells.get(0, 3).putValue("Salary")
cells.get(0, 4).putValue("HireDate")

# Data row 1
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Engineering")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(_jt.LocalDate.of(2020, 3, 15))

# Data row 2
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(_jt.LocalDate.of(2019, 7, 22))

# Data row 3
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finance")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(_jt.LocalDate.of(2021, 1, 10))

# Data row 4
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Human Resources")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(_jt.LocalDate.of(2018, 11, 5))

# Data row 5
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Operations")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(_jt.LocalDate.of(2022, 5, 30))

# Set column widths for better readability
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)

workbook.save(filePath, SaveFormat.DBf)

jpype.shutdownJVM()