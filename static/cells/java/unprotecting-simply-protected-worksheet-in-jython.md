##Unprotecting Simply Protected Worksheet in Jython
## **Aspose.Cells - Unprotecting Simply Protected Worksheet**
To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.
**Jython Code**
from aspose-cells import Settings
from com.aspose.cells import Workbook
from com.aspose.cells import SaveFormat
from com.aspose.cells import FileFormatType
class UnprotectingSimplyProtectedWorksheet:
def __init__(self):
dataDir = Settings.dataDir + 'WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet/'
filesFormatType = FileFormatType
#Instantiating a Workbook object
workbook = Workbook(dataDir + "Book1.xls")
worksheets = workbook.getWorksheets()
worksheet = worksheets.get(0)
protection = worksheet.getProtection()
#The following 3 methods are only for Excel 2000 and earlier formats
protection.setAllowEditingContent(False)
protection.setAllowEditingObject(False)
protection.setAllowEditingScenario(False)
#Unprotecting the worksheet
worksheet.unprotect()
# Save the excel file.
workbook.save(dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)
#Print Message
print "Worksheet unprotected successfully."
if __name__ == '__main__':
UnprotectingSimplyProtectedWorksheet()
## **Download Running Code**
Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet.py)
