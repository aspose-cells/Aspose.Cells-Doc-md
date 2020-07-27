+++
title = "Unprotecting Simply Protected Worksheet in Jython" 
description = "" 
weight = 20820 
+++

Aspose.Cells for Java : Unprotecting Simply Protected Worksheet in Jython  

# Aspose.Cells for Java : Unprotecting Simply Protected Worksheet in Jython


## Aspose.Cells - Unprotecting Simply Protected Worksheet

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatfrom com.aspose.cells import FileFormatTypeclass UnprotectingSimplyProtectedWorksheet:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet/'                filesFormatType = FileFormatType        #Instantiating a Workbook object        workbook = Workbook(dataDir + "Book1.xls")        worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        protection = worksheet.getProtection()        #The following 3 methods are only for Excel 2000 and earlier formats        protection.setAllowEditingContent(False)        protection.setAllowEditingObject(False)        protection.setAllowEditingScenario(False)        #Unprotecting the worksheet        worksheet.unprotect()        # Save the excel file.        workbook.save(dataDir + "output.xls", filesFormatType.EXCEL\_97\_TO\_2003)        #Print Message        print "Worksheet unprotected successfully."if \_\_name\_\_ == '\_\_main\_\_':            UnprotectingSimplyProtectedWorksheet()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet.py)

