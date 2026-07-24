import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# Create a new workbook and access the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Populate sample data in cells A1:E1
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Add a Line sparkline group anchored at F1 (column 5, row 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# Add a Column sparkline group anchored at G1 (column 6, row 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# Configure image options for PNG output
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# Convert the Line sparkline to image and embed it in cell F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# Convert the Column sparkline to image and embed it in cell G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# Convert the Win/Loss sparkline to image and embed it in cell H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# Save the workbook to disk
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()