---
title: Setting Page Options in Jython
type: docs
weight: 130
url: /java/setting-page-options-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Setting Page Options**
To set page options using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

{{< highlight java >}}
from aspose-cells import Settings
from com.aspose.cells import Workbook
from com.aspose.cells import PageOrientationType
from java.io import FileInputStream

class SettingPageOptions:
    def __init__(self):
        self.page_orientation()
        self.scaling()

    def page_orientation(dataDir):
        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SettingPageOptions/'
        # Instantiating a Workbook object by an Excel file path
        workbook = Workbook()
        # Accessing the first worksheet in the Excel file
        worksheets = workbook.getWorksheets()
        sheet_index = worksheets.add()
        sheet = worksheets.get(sheet_index)
        # Setting the orientation to Portrait
        page_setup = sheet.getPageSetup()
        page_orientation_type = PageOrientationType
        page_setup.setOrientation(page_orientation_type.PORTRAIT)
        # Saving the modified Excel file in default (that is Excel 2003) format
        workbook.save(dataDir + "Page Orientation.xls")
        print "Set page orientation, please check the output file."

    def scaling(dataDir):
        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SettingPageOptions/'
        # Instantiating a Workbook object by an Excel file path
        workbook = Workbook(dataDir + 'Book1.xls')
        # Accessing the first worksheet in the Excel file
        worksheets = workbook.getWorksheets()
        sheet_index = worksheets.add()
        sheet = worksheets.get(sheet_index)
        # Setting the scaling factor to 100
        page_setup = sheet.getPageSetup()
        page_setup.setZoom(100)
        # Saving the modified Excel file in default (that is Excel 2003) format
        workbook.save(dataDir + "Scaling.xls")
        print "Set scaling, please check the output file."

if __name__ == '__main__':
    SettingPageOptions()
{{< /highlight >}}

## **Download Running Code**
Download **Setting Page Options (Aspose.Cells)** from any of the below‑mentioned source code repositories:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SettingPageOptions.py)
