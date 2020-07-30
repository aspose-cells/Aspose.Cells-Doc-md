---
title : "Display Hide Gridlines in Jython" 
description : "" 
weight : 20807 
toc : false
type: docs
url: /java/plugins/jython/guide/worksheets/display+hide+gridlines+in+jython/
---

# Aspose.Cells for Java : Display Hide Gridlines in Jython


## Aspose.Cells - Display Hide Gridlines

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass DisplayHideGridlines:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideGridlines/'             workbook = Workbook(dataDir + "Book1.xls")                #Accessing the first worksheet in the Excel file        worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        #Hiding the grid lines of the first worksheet of the Excel file        worksheet.setGridlinesVisible(False)        #Saving the modified Excel file in default (that is Excel 2000) format        workbook.save(dataDir + "output.xls")        # Print message        print "Grid lines are now hidden on sheet 1, please check the output document." if \_\_name\_\_ == '\_\_main\_\_':            DisplayHideGridlines()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/DisplayHideGridlines.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideGridlines.py)

