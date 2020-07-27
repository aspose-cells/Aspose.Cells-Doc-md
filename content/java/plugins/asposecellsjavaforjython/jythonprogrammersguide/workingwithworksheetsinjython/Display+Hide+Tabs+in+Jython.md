+++
title = "Display Hide Tabs in Jython" 
description = "" 
weight = 20809 
+++

Aspose.Cells for Java : Display Hide Tabs in Jython  

# Aspose.Cells for Java : Display Hide Tabs in Jython


## Aspose.Cells - Display Hide Tabs

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass DisplayHideTabs:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideTabs/'             workbook = Workbook(dataDir + "Book1.xls")                #Hiding the tabs of the Excel file        workbook.getSettings().setShowTabs(False)        #Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "output.xls")        # Print message        print "Tabs are now hidden, please check the output file."if \_\_name\_\_ == '\_\_main\_\_':            DisplayHideTabs()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/DisplayHideTabs.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideTabs.py)

