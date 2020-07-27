+++
title = "Page Break Preview in Jython" 
description = "" 
weight = 20813 
+++

Aspose.Cells for Java : Page Break Preview in Jython  

# Aspose.Cells for Java : Page Break Preview in Jython


## Aspose.Cells - Page Break Preview

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookclass PageBreakPreview:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/PageBreakPreview/'             workbook = Workbook(dataDir + "Book1.xls")                #Adding a new worksheet to the Workbook object        worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        #Displaying the worksheet in page break preview        worksheet.setPageBreakPreview(True)        #Saving the modified Excel file in default format        workbook.save(dataDir + "output.xls")        # Print message        print "Page break preview is enabled for sheet 1, please check the output document." if \_\_name\_\_ == '\_\_main\_\_':            PageBreakPreview()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/PageBreakPreview.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/PageBreakPreview.py)

