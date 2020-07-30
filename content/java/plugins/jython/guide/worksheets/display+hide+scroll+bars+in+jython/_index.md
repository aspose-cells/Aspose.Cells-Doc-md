---
title : "Display Hide Scroll Bars in Jython" 
description : "" 
weight : 20808 
toc : false
type: docs
url: /java/plugins/jython/guide/worksheets/display+hide+scroll+bars+in+jython/
---

# Aspose.Cells for Java : Display Hide Scroll Bars in Jython


## Aspose.Cells - Display Hide Scroll Bars

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass DisplayHideScrollBars:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideScrollBars/'             workbook = Workbook(dataDir + "Book1.xls")                #Hiding the vertical scroll bar of the Excel file        workbook.getSettings().setVScrollBarVisible(False)        #Hiding the horizontal scroll bar of the Excel file        workbook.getSettings().setHScrollBarVisible(False)        #Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "output.xls")        # Print message        print "Scroll bars are now hidden, please check the output document." if \_\_name\_\_ == '\_\_main\_\_':            DisplayHideScrollBars()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/DisplayHideScrollBars.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideScrollBars.py)

