---
title : "Saving Files in Jython" 
description : "" 
weight : 20795 
toc : false
type: docs
url: /java/plugins/jython/guide/files/saving+files+in+jython/
---

# Aspose.Cells for Java : Saving Files in Jython


## Aspose.Cells - Saving Files

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import FileFormatTypeclass SavingFiles:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithFiles/SavingFiles/'                fileFormatType = FileFormatType                        #Creating an Workbook object with an Excel file path        workbook = Workbook(dataDir + "Book1.xls")        #Save in default (Excel2003) format        workbook.save(dataDir + "book.default.out.xls")        #Save in Excel2003 format        workbook.save(dataDir + "book.out.xls", fileFormatType.EXCEL\_97\_TO\_2003)        #Save in Excel2007 xlsx format        workbook.save(dataDir + "book.out.xlsx", fileFormatType.XLSX)        #Save in SpreadsheetML format        workbook.save(dataDir + "book.out.xml", fileFormatType.EXCEL\_2003\_XML)                #Print Message        print("<BR>")        print("Worksheets are saved successfully.")                if \_\_name\_\_ == '\_\_main\_\_':            SavingFiles()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithFiles/SavingFiles.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/SavingFiles.py)

