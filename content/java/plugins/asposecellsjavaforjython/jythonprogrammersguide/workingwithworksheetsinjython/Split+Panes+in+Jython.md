+++
title = "Split Panes in Jython" 
description = "" 
weight = 20818 
+++

Aspose.Cells for Java : Split Panes in Jython  

# Aspose.Cells for Java : Split Panes in Jython


## Aspose.Cells - Split Panes

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatclass SplitPanes:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SplitPanes/'                saveFormat = SaveFormat;             workbook = Workbook(dataDir + "Book1.xls")        #Set the active cell        workbook.getWorksheets().get(0).setActiveCell("A20");        #Split the worksheet window        workbook.getWorksheets().get(0).split();        #Save the excel file        workbook.save(dataDir + "book.out.xls", saveFormat.EXCEL\_97\_TO\_2003);        #Print Message        print "Panes split successfully."if \_\_name\_\_ == '\_\_main\_\_':            SplitPanes()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/SplitPanes.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SplitPanes.py)

