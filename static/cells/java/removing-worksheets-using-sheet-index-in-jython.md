##Removing Worksheets using Sheet Index in Jython
## **Aspose.Cells - Removing Worksheets using Sheet Index**
To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.
**Jython Code**
from aspose-cells import Settings
from com.aspose.cells import Workbook
from java.io import FileInputStream;
class RemovingWorksheetsusingSheetIndex:
def __init__(self):
dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex/'
fstream=FileInputStream(dataDir + "Book1.xls");
#Instantiating a Workbook object with the stream
workbook = Workbook(fstream)
#Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0)
#Saving the Excel file
workbook.save(dataDir + "book.out.xls")
#Closing the file stream to free all resources
fstream.close()
#Print Message
print "Sheet removed successfully."
if __name__ == '__main__':
RemovingWorksheetsusingSheetIndex()
## **Download Running Code**
Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex.py)
