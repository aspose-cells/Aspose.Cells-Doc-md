+++
title = "Grouping and Ungrouping Rows and Columns in Jython" 
description = "" 
weight = 20801 
+++

Aspose.Cells for Java : Grouping and Ungrouping Rows and Columns in Jython  

# Aspose.Cells for Java : Grouping and Ungrouping Rows and Columns in Jython


## Aspose.Cells - Grouping and Ungrouping Rows and Columns

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass RowsAndColumns:    def \_\_init\_\_(self):                dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'                # Grouping Rows & Columns        self.group\_rows\_columns()        # Ungrouping Rows & Columns        self.ungroup\_rows\_columns()                def group\_rows\_columns(dataDir):        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'            # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Book1.xls')        # Accessing the first worksheet in the Excel file        worksheet = workbook.getWorksheets().get(0)        cells = worksheet.getCells()        # Grouping first six rows (from 0 to 5) and making them hidden by passing true        cells.groupRows(0,5,True)        # Grouping first three columns (from 0 to 2) and making them hidden by passing true        cells.groupColumns(0,2,True)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Group Rows And Columns.xls")        print "Group Rows And Columns Successfully."         def ungroup\_rows\_columns(dataDir):        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'            # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Group Rows And Columns.xls')        # Accessing the first worksheet in the Excel file        worksheet = workbook.getWorksheets().get(0)        cells = worksheet.getCells()        # Ungrouping first six rows (from 0 to 5)        cells.ungroupRows(0,5)        # Ungrouping first three columns (from 0 to 2)        cells.ungroupColumns(0,2)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Ungroup Rows And Columns.xls")        print "Ungroup Rows And Columns Successfully."        if \_\_name\_\_ == '\_\_main\_\_':            RowsAndColumns()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)

