---
title: Hiding and Showing Rows and Columns in Jython
type: docs
weight: 50
url: /java/hiding-and-showing-rows-and-columns-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Hiding and Showing Rows and Columns**
This example demonstrates how to hide and show rows and columns using **Aspose.Cells for Java with Jython**. Here you can see the sample code.

**Jython Code**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

class RowsAndColumns:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'

        # Hiding rows and columns
        self.hide_rows_columns()
        # Showing rows and columns
        self.unhide_rows_columns()

    def hide_rows_columns(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    
        # Instantiating a Workbook object by an Excel file path
        workbook = Workbook(dataDir + 'Book1.xls')
        # Accessing the first worksheet in the Excel file
        worksheet = workbook.getWorksheets().get(0)
        cells = worksheet.getCells()
        # Hiding the 3rd row of the worksheet
        cells.hideRow(2)
        # Hiding the 2nd column of the worksheet
        cells.hideColumn(1)
        # Saving the modified Excel file in the default (that is Excel 2003) format
        workbook.save(dataDir + "Hide Rows And Columns.xls")
        print "Hide Rows And Columns Successfully." 

    def unhide_rows_columns(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    
        # Instantiating a Workbook object by an Excel file path
        workbook = Workbook(dataDir + 'Book1.xls')
        # Accessing the first worksheet in the Excel file
        worksheet = workbook.getWorksheets().get(0)
        cells = worksheet.getCells()
        # Unhiding the 3rd row and setting its height to 13.5
        cells.unhideRow(2,13.5)
        # Unhiding the 2nd column and setting its width to 8.5
        cells.unhideColumn(1,8.5)
        # Saving the modified Excel file in the default (that is Excel 2003) format
        workbook.save(dataDir + "Unhide Rows And Columns.xls")
        print "Unhide Rows And Columns Successfully." 

if __name__ == '__main__':        
    RowsAndColumns()

{{< /highlight >}}
## **Download Running Code**
Download the Append Documents (Aspose.Cells) example from any of the social coding sites listed below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
