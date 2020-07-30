---
title : "Hide Unhide Worksheet in Jython" 
description : "" 
weight : 20811 
toc : false
type: docs
url: /java/plugins/jython/guide/worksheets/hide+unhide+worksheet+in+jython/
---

# Aspose.Cells for Java : Hide Unhide Worksheet in Jython


## Aspose.Cells - Hide Unhide Worksheet

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass HideUnhideWorksheet:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/HideUnhideWorksheet/'             workbook = Workbook(dataDir + "Book1.xls")                #Accessing the first worksheet in the Excel file        worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        #Hiding the first worksheet of the Excel file        worksheet.setVisible(False)        #Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "output.xls")        # Print message        print "Worksheet 1 is now hidden, please check the output document."if \_\_name\_\_ == '\_\_main\_\_':            HideUnhideWorksheet()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/HideUnhideWorksheet.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/HideUnhideWorksheet.py)

