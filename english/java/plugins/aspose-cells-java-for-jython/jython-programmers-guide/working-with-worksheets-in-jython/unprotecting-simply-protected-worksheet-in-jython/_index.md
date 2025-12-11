---
title: Unprotecting Simply Protected Worksheet in Jython
type: docs
weight: 160
url: /java/unprotecting-simply-protected-worksheet-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Unprotecting Simply Protected Worksheet**
This example demonstrates how to unprotect a worksheet using **Aspose.Cells for Java with Jython**. Below you can see the sample code.

**Jython Code**

{{< highlight java >}}
from aspose-cells import Settings
from com.aspose.cells import Workbook
from com.aspose.cells import SaveFormat
from com.aspose.cells import FileFormatType

class UnprotectingSimplyProtectedWorksheet:
    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet/'

        filesFormatType = FileFormatType

        # Instantiating a Workbook object
        workbook = Workbook(dataDir + "Book1.xls")
        worksheets = workbook.getWorksheets()
        worksheet = worksheets.get(0)
        protection = worksheet.getProtection()

        # The following 3 methods are only for Excel 2000 and earlier formats
        protection.setAllowEditingContent(False)
        protection.setAllowEditingObject(False)
        protection.setAllowEditingScenario(False)

        # Unprotecting the worksheet
        worksheet.unprotect()

        # Save the Excel file.
        workbook.save(dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

        # Print message
        print "Worksheet unprotected successfully."

if __name__ == '__main__':
    UnprotectingSimplyProtectedWorksheet()
{{< /highlight >}}

## **Download Running Code**
Download **Unprotecting Simply Protected Worksheet (Aspose.Cells)** from any of the below-mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet.py)
