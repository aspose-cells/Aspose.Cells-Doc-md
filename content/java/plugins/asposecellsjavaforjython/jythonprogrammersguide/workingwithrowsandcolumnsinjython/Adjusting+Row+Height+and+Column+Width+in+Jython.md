+++
title = "Adjusting Row Height and Column Width in Jython" 
description = "" 
weight = 20798 
+++

Aspose.Cells for Java : Adjusting Row Height and Column Width in Jython  

# Aspose.Cells for Java : Adjusting Row Height and Column Width in Jython


## Aspose.Cells - Adjusting Row Height and Column Width

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass RowsAndColumns:    def \_\_init\_\_(self):                dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'                # Setting the Row Height        self.set\_row\_height()        # Setting the Width of a Column        self.set\_column\_width()        def set\_row\_height(dataDir):        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'            # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Book1.xls')        # Accessing the first worksheet in the Excel file        worksheet = workbook.getWorksheets().get(0)        cells = worksheet.getCells()        # Setting the height of the second row to 13        cells.setRowHeight(1, 13)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Set Row Height.xls")        print "Set Row Height Successfully."         def set\_column\_width(dataDir):        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'            # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Book1.xls')        # Accessing the first worksheet in the Excel file        worksheet = workbook.getWorksheets().get(0)        cells = worksheet.getCells()        # Setting the width of the second column to 17.5        cells.setColumnWidth(1, 17.5)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Set Column Width.xls")        print "Set Column Width Successfully." if \_\_name\_\_ == '\_\_main\_\_':            RowsAndColumns()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)

