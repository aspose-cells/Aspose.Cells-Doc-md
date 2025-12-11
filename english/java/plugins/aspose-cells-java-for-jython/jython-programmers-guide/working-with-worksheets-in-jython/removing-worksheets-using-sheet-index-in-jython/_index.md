---
title: Removing Worksheets using Sheet Index in Jython
type: docs
weight: 110
url: /java/removing-worksheets-using-sheet-index-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Removing Worksheets using Sheet Index**
To remove worksheets using **Aspose.Cells Java for Jython**, see the example code below.

**Jython Code**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from java.io import FileInputStream;


class RemovingWorksheetsUsingSheetIndex:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex/'



        fstream=FileInputStream(dataDir + "Book1.xls");

        # Instantiating a Workbook object with the stream

        workbook = Workbook(fstream)

        # Removing a worksheet using its sheet index

        workbook.getWorksheets().removeAt(0)

        # Saving the Excel file

        workbook.save(dataDir + "book.out.xls")

        # Closing the file stream to free all resources

        fstream.close()


        # Print Message

        print "Sheet removed successfully."

if __name__ == '__main__':        

    RemovingWorksheetsUsingSheetIndex()

{{< /highlight >}}
## **Download Running Code**
Download the example code from any of the social coding sites listed below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex.py)
