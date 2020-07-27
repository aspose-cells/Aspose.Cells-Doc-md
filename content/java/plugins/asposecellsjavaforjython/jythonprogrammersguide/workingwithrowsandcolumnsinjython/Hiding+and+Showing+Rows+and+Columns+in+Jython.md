+++
title = "Hiding and Showing Rows and Columns in Jython" 
description = "" 
weight = 20802 
+++

Aspose.Cells for Java : Hiding and Showing Rows and Columns in Jython  

# Aspose.Cells for Java : Hiding and Showing Rows and Columns in Jython


## Aspose.Cells - Hiding and Showing Rows and Columns

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass RowsAndColumns:    def \_\_init\_\_(self):                dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'                # Hiding Rows and Columns        self.hide\_rows\_columns()        # Showing Rows and Columns        self.unhide\_rows\_columns()                def hide\_rows\_columns(dataDir):        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'            # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Book1.xls')        # Accessing the first worksheet in the Excel file        worksheet = workbook.getWorksheets().get(0)        cells = worksheet.getCells()        # Hiding the 3rd row of the worksheet        cells.hideRow(2)        # Hiding the 2nd column of the worksheet        cells.hideColumn(1)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Hide Rows And Columns.xls")        print "Hide Rows And Columns Successfully."         def unhide\_rows\_columns(dataDir):        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'            # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Book1.xls')        # Accessing the first worksheet in the Excel file        worksheet = workbook.getWorksheets().get(0)        cells = worksheet.getCells()        # Unhiding the 3rd row and setting its height to 13.5        cells.unhideRow(2,13.5)        # Unhiding the 2nd column and setting its width to 8.5        cells.unhideColumn(1,8.5)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Unhide Rows And Columns.xls")        print "Unhide Rows And Columns Successfully." if \_\_name\_\_ == '\_\_main\_\_':            RowsAndColumns()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)

