##Converting Worksheet To SVG in Jython
## **Aspose.Cells - Converting Worksheet To SVG**
To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.
**Jython Code**
from aspose-cells import Settings
from com.aspose.cells import Workbook
from com.aspose.cells import ImageFormat
from com.aspose.cells import ImageOrPrintOptions
from com.aspose.cells import SheetRender
from com.aspose.cells import SaveFormat
class ConvertingWorksheetToSVG:
def __init__(self):
dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'
saveFormat = SaveFormat
workbook = Workbook(dataDir + "Book1.xls")
#Convert each worksheet into svg format in a single page.
imgOptions = ImageOrPrintOptions()
imgOptions.setSaveFormat(saveFormat.SVG)
imgOptions.setOnePagePerSheet(True)
#Convert each worksheet into svg format
sheetCount = workbook.getWorksheets().getCount()
#for(i=0; i<sheetCount; i++)
for i in range(sheetCount):
sheet = workbook.getWorksheets().get(i)
sr = SheetRender(sheet, imgOptions)
pageCount = sr.getPageCount()
#for (k = 0 k < pageCount k++)
for k in range(pageCount):
#Output the worksheet into Svg image format
sr.toImage(k, dataDir + sheet.getName() + ".out.svg")
# Print message
print "Excel to SVG conversion completed successfully."
if __name__ == '__main__':
ConvertingWorksheetToSVG()
## **Download Running Code**
Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
