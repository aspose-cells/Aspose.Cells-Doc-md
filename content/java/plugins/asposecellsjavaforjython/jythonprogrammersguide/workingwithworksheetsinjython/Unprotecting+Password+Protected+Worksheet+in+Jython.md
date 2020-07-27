+++
title = "Unprotecting Password Protected Worksheet in Jython" 
description = "" 
weight = 20819 
+++

Aspose.Cells for Java : Unprotecting Password Protected Worksheet in Jython  

# Aspose.Cells for Java : Unprotecting Password Protected Worksheet in Jython


## Aspose.Cells - Append Documents

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatfrom com.aspose.cells import FileFormatType;class UnprotectingPasswordProtectedWorksheet:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet/'                filesFormatType = FileFormatType        #Instantiating a Workbook object        workbook = Workbook(dataDir + "book1.xls")        worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        protection = worksheet.getProtection()        #Unprotecting the worksheet with a password        worksheet.unprotect("aspose")        # Save the excel file.        workbook.save(dataDir + "output.xls", filesFormatType.EXCEL\_97\_TO\_2003)        #Print Message        print "Worksheet unprotected successfully."if \_\_name\_\_ == '\_\_main\_\_':            UnprotectingPasswordProtectedWorksheet()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet.py)

