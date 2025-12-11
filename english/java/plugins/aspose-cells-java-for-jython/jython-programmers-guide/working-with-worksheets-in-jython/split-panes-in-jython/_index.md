---
title: Split Panes in Jython
type: docs
weight: 140
url: /java/split-panes-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Split Panes**
To split panes using **Aspose.Cells Java for Jython**, see the example code below.

**Jython Code**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class SplitPanes:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SplitPanes/'



        saveFormat = SaveFormat;



        workbook = Workbook(dataDir + "Book1.xls")

        # Set the active cell

        workbook.getWorksheets().get(0).setActiveCell("A20");

        # Split the worksheet window

        workbook.getWorksheets().get(0).split();

        # Save the Excel file

        workbook.save(dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

        # Print message

        print "Panes split successfully."

if __name__ == '__main__':        

    SplitPanes()

{{< /highlight >}}

## **Download Running Code**
Download the Split Panes example (Aspose.Cells) from any of the below‑mentioned source code repositories:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SplitPanes.py)
