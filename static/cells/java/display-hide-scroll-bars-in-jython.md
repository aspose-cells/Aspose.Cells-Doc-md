##Display Hide Scroll Bars in Jython
## **Aspose.Cells - Display Hide Scroll Bars**
To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.
**Jython Code**
from aspose-cells import Settings
from com.aspose.cells import Workbook
class DisplayHideScrollBars:
def __init__(self):
dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideScrollBars/'
workbook = Workbook(dataDir + "Book1.xls")
#Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setVScrollBarVisible(False)
#Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setHScrollBarVisible(False)
#Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(dataDir + "output.xls")
# Print message
print "Scroll bars are now hidden, please check the output document."
if __name__ == '__main__':
DisplayHideScrollBars()
## **Download Running Code**
Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideScrollBars.py)
