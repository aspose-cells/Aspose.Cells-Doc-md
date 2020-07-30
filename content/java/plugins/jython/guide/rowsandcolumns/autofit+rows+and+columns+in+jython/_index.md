---
title : "Autofit Rows and Columns in Jython" 
description : "" 
weight : 20799 
toc : false
type: docs
url: /java/plugins/jython/guide/rowsandcolumns/autofit+rows+and+columns+in+jython/
---

# Aspose.Cells for Java : Autofit Rows and Columns in Jython


## Aspose.Cells - Autofit Rows and Columns

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass RowsAndColumns:    def \_\_init\_\_(self):                dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'              # Auto Fit Row        self.autofit\_row()        # Auto Fit Column        self.autofit\_column()         def autofit\_row(dataDir):        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'        # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Book1.xls')        # Accessing the first worksheet in the Excel file        worksheet = workbook.getWorksheets().get(0)        # Auto-fitting the 3rd row of the worksheet        worksheet.autoFitRow(2)        # Auto-fitting the 3rd row of the worksheet based on the contents in a range of        # cells (from 1st to 9th column) within the row        #worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Autofit Row.xls")        print "Autofit Row Successfully."     def autofit\_column(dataDir):        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'        # Instantiating a Workbook object by excel file path        workbook = Workbook(dataDir + 'Book1.xls')        # Accessing the first worksheet in the Excel file        worksheet = workbook.getWorksheets().get(0)        # Auto-fitting the 4th column of the worksheet        worksheet.autoFitColumn(3)        # Auto-fitting the 4th column of the worksheet based on the contents in a range of        # cells (from 1st to 9th row) within the column        #worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Autofit Column.xls")        print "Autofit Column Successfully."    if \_\_name\_\_ == '\_\_main\_\_':            RowsAndColumns()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)

