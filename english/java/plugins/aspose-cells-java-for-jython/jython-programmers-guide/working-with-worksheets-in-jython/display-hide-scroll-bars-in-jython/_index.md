---
title: Display Hide Scroll Bars in Jython
type: docs
weight: 40
url: /java/display-hide-scroll-bars-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells – Display/Hide Scroll Bars**

To display or hide scroll bars using **Aspose.Cells Java for Jython**, see the example code below.

**Jython Code**

{{< highlight java >}}
from aspose-cells import Settings
from com.aspose.cells import Workbook


class DisplayHideScrollBars:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideScrollBars/'

        workbook = Workbook(dataDir + "Book1.xls")

        # Hide the vertical scroll bar of the Excel file
        workbook.getSettings().setVScrollBarVisible(False)

        # Hide the horizontal scroll bar of the Excel file
        workbook.getSettings().setHScrollBarVisible(False)

        # Save the modified Excel file in the default (Excel 2003) format
        workbook.save(dataDir + "output.xls")

        # Print message
        print "Scroll bars are now hidden, please check the output document."


if __name__ == '__main__':
    DisplayHideScrollBars()
{{< /highlight >}}

## **Download Running Code**

Download **Display/Hide Scroll Bars (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideScrollBars.py)
