---
title: Display Hide Gridlines in Jython
type: docs
weight: 30
url: /java/display-hide-gridlines-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display/Hide Gridlines**
To display and hide gridlines using **Aspose.Cells for Java with Jython**, see the example code below.

**Jython Code**

{{< highlight java >}}

from aspose-cells import Settings
from com.aspose.cells import Workbook

class DisplayHideGridlines:
    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideGridlines/'

        workbook = Workbook(dataDir + "Book1.xls")

        # Accessing the first worksheet in the Excel file
        worksheets = workbook.getWorksheets()
        worksheet = worksheets.get(0)

        # Hiding the grid lines of the first worksheet
        worksheet.setGridlinesVisible(False)

        # Saving the modified Excel file in the default (Excel 2000) format
        workbook.save(dataDir + "output.xls")

        # Print message
        print "Grid lines are now hidden on sheet 1, please check the output document."

if __name__ == '__main__':
    DisplayHideGridlines()

{{< /highlight >}}

## **Download Running Code**
Download **Display Hide Gridlines (Aspose.Cells)** from any of the below‑listed social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideGridlines.py)
