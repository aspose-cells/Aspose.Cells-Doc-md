+++
title = "Removing Worksheets using Sheet Index in Jython" 
description = "" 
weight = 20815 
+++

Aspose.Cells for Java : Removing Worksheets using Sheet Index in Jython  

# Aspose.Cells for Java : Removing Worksheets using Sheet Index in Jython


## Aspose.Cells - Removing Worksheets using Sheet Index

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom java.io import FileInputStream;class RemovingWorksheetsusingSheetIndex:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex/'                  fstream=FileInputStream(dataDir + "Book1.xls");        #Instantiating a Workbook object with the stream        workbook = Workbook(fstream)        #Removing a worksheet using its sheet index        workbook.getWorksheets().removeAt(0)        #Saving the Excel file        workbook.save(dataDir + "book.out.xls")        #Closing the file stream to free all resources        fstream.close()        #Print Message        print "Sheet removed successfully."if \_\_name\_\_ == '\_\_main\_\_':            RemovingWorksheetsusingSheetIndex()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex.py)

