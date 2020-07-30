---
title : "Removing Worksheets using Sheet Name in Jython" 
description : "" 
weight : 20816 
toc : false
type: docs
url: /java/plugins/jython/guide/worksheets/removing+worksheets+using+sheet+name+in+jython/
---

# Aspose.Cells for Java : Removing Worksheets using Sheet Name in Jython


## Aspose.Cells - Removing Worksheets using Sheet Name

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom java.io import FileInputStream;class RemovingWorksheetsusingSheetName:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetName/'                  #Creating a file stream containing the Excel file to be opened        fstream = FileInputStream(dataDir + "Book1.xls");        #Instantiating a Workbook object with the stream        workbook = Workbook(fstream);        #Removing a worksheet using its sheet name        workbook.getWorksheets().removeAt("Sheet1");        #Saving the Excel file        workbook.save(dataDir + "book.out.xls");        #Closing the file stream to free all resources        fstream.close();        #Print Message        print "Sheet removed successfully.";if \_\_name\_\_ == '\_\_main\_\_':            RemovingWorksheetsusingSheetName()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetName.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetName.py)

