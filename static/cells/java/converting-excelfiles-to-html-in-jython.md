##Converting ExcelFiles To Html in Jython
## **Aspose.Cells - Converting ExcelFiles To Html**
To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.
**Jython Code**
from aspose-cells import Settings
from com.aspose.cells import Workbook
from com.aspose.cells import SaveFormat
class ConvertingExcelFilesToHtml:
def __init__(self):
dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingExcelFilesToHtml/'
saveFormat = SaveFormat
workbook = Workbook(dataDir + "Book1.xls")
#Save the document in PDF format
workbook.save(dataDir + "OutBook1.html", saveFormat.HTML)
# Print message
print "\n Excel to HTML conversion performed successfully."
if __name__ == '__main__':
ConvertingExcelFilesToHtml()
## **Download Running Code**
Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingExcelFilesToHtml.py)
