---
title : "Zoom Factor in Jython" 
description : "" 
weight : 20821 
toc : false
type: docs
url: /java/plugins/jython/guide/worksheets/zoom+factor+in+jython/
---

# Aspose.Cells for Java : Zoom Factor in Jython


## Aspose.Cells - Zoom Factor

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatclass ZoomFactor:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/ZoomFactor/'             workbook = Workbook(dataDir + "Book1.xls")        #Accessing the first worksheet in the Excel file        worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        #Setting the zoom factor of the worksheet to 75        worksheet.setZoom(75)        #Saving the modified Excel file in default format        workbook.save(dataDir + "output.xls")        # Print message        print "Zoom factor set to 75% for sheet 1, please check the output document."if \_\_name\_\_ == '\_\_main\_\_':            ZoomFactor()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/ZoomFactor.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/ZoomFactor.py)

