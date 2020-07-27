+++
title = "Protecting Worksheet in Jython" 
description = "" 
weight = 20814 
+++

Aspose.Cells for Java : Protecting Worksheet in Jython  

# Aspose.Cells for Java : Protecting Worksheet in Jython


## Aspose.Cells - Protecting Worksheet

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatclass ProtectingWorksheet:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithWorksheets/ProtectingWorksheet/'                #Instantiating a Excel object by excel file path        excel = Workbook(dataDir + "Book1.xls")        #Accessing the first worksheet in the Excel file        worksheets = excel.getWorksheets()        worksheet = worksheets.get(0)        protection = worksheet.getProtection()        #The following 3 methods are only for Excel 2000 and earlier formats        protection.setAllowEditingContent(False)        protection.setAllowEditingObject(False)        protection.setAllowEditingScenario(False)        #Protects the first worksheet with a password "1234"        protection.setPassword("1234")        #Saving the modified Excel file in default format        excel.save(dataDir + "output.xls")        #Print Message        print "Sheet protected successfully."if \_\_name\_\_ == '\_\_main\_\_':            ProtectingWorksheet()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/ProtectingWorksheet.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/ProtectingWorksheet.py)

