import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()