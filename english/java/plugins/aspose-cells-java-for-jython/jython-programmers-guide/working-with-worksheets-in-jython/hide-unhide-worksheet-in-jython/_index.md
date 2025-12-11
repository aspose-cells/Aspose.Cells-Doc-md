---
title: Hide Unhide Worksheet in Jython
type: docs
weight: 70
url: /java/hide-unhide-worksheet-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells – Hide/Unhide Worksheet**
To hide or unhide worksheets using **Aspose.Cells for Java with Jython**, see the example code below.

**Jython Code**

{{< highlight java >}}
from aspose-cells import Settings
from com.aspose.cells import Workbook

class HideUnhideWorksheet:
    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithWorksheets/HideUnhideWorksheet/'

        workbook = Workbook(dataDir + "Book1.xls")

        # Accessing the first worksheet in the Excel file
        worksheets = workbook.getWorksheets()
        worksheet = worksheets.get(0)

        # Hiding the first worksheet of the Excel file
        worksheet.setVisible(False)

        # Saving the modified Excel file in the default (Excel 2003) format
        workbook.save(dataDir + "output.xls")

        # Print message
        print "Worksheet 1 is now hidden; please check the output document."

if __name__ == '__main__':
    HideUnhideWorksheet()
{{< /highlight >}}

## **Download Running Code**
Download **Hide Unhide Worksheet (Aspose.Cells)** from any of the below-mentioned source code repositories:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/HideUnhideWorksheet.py)
