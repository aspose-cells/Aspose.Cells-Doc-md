##Adding Worksheets to New Excel File in Jython
## **Aspose.Cells - Adding Worksheets to New Excel**
To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.
**Jython Code**
from aspose-cells import Settings
from com.aspose.cells import Workbook
from com.aspose.cells import SaveFormat
class AddingWorksheetstoNewExcelFile:
def __init__(self):
dataDir = Settings.dataDir + 'WorkingWithWorksheets/AddingWorksheetstoNewExcelFile/'
workbook = Workbook(dataDir + "Book1.xls")
#Adding a new worksheet to the Workbook object
worksheets = workbook.getWorksheets()
sheetIndex = worksheets.add()
worksheet = worksheets.get(sheetIndex)
#Setting the name of the newly added worksheet
worksheet.setName("My Worksheet")
#Saving the Excel file
workbook.save(dataDir + "book.out.xls")
#Print Message
print "Sheet added successfully."
if __name__ == '__main__':
AddingWorksheetstoNewExcelFile()
## **Download Running Code**
Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)
