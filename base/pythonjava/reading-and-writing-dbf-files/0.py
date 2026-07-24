import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat

dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")

loadOptions = LoadOptions(LoadFormat.Dbf)

workbook = Workbook(filePath, loadOptions)

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

sb = []

maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()

for i in range(maxRow + 1):
    for j in range(maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|" + "\n")

print("".join(sb))

outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.Xlsx)

print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)

jpype.shutdownJVM()