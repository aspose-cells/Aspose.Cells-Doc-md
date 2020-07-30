---
title : "Freeze Panes in Jython" 
description : "" 
weight : 20810 
toc : false
type: docs
url: /java/plugins/jython/guide/worksheets/freeze+panes+in+jython/
---

# Aspose.Cells for Java : Freeze Panes in Jython


## Aspose.Cells - Freeze Panes

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass FreezePanes:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/FreezePanes/'             workbook = Workbook(dataDir + "Book1.xls")                #Accessing the first worksheet in the Excel file        worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        #Applying freeze panes settings        worksheet.freezePanes(3,2,3,2)        #Saving the modified Excel file in default format        workbook.save(dataDir + "book.out.xls")        #Print Message        print "Panes freeze successfull."if \_\_name\_\_ == '\_\_main\_\_':            FreezePanes()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/FreezePanes.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/FreezePanes.py)

