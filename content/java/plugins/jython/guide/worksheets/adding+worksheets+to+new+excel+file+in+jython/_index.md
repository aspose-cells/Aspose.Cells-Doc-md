---
title : "Adding Worksheets to New Excel File in Jython" 
description : "" 
weight : 20805 
toc : false
type: docs
url: /java/plugins/jython/guide/worksheets/adding+worksheets+to+new+excel+file+in+jython/
---

# Aspose.Cells for Java : Adding Worksheets to New Excel File in Jython


## Aspose.Cells - Adding Worksheets to New Excel

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatclass AddingWorksheetstoNewExcelFile:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/AddingWorksheetstoNewExcelFile/'             workbook = Workbook(dataDir + "Book1.xls")        #Adding a new worksheet to the Workbook object        worksheets = workbook.getWorksheets()        sheetIndex = worksheets.add()        worksheet = worksheets.get(sheetIndex)        #Setting the name of the newly added worksheet        worksheet.setName("My Worksheet")        #Saving the Excel file        workbook.save(dataDir + "book.out.xls")        #Print Message        print "Sheet added successfully."if \_\_name\_\_ == '\_\_main\_\_':            AddingWorksheetstoNewExcelFile()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)

