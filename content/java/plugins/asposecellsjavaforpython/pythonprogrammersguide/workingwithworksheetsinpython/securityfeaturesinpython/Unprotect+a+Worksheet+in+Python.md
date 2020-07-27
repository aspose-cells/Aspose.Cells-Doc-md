+++
title = "Unprotect a Worksheet in Python" 
description = "" 
weight = 24777 
+++

Aspose.Cells for Java : Unprotect a Worksheet in Python  

# Aspose.Cells for Java : Unprotect a Worksheet in Python


## Aspose.Cells - Unprotect a Worksheet

To protect worksheet using **Aspose.Cells Java for Python**, call **unprotect\_worksheet** method of **protection** module.

**Python Code**

filesFormatType = self.FileFormatType#Instantiating a Workbook objectworkbook = self.Workbook(self.dataDir + "Book1.xls")worksheets = workbook.getWorksheets()worksheet = worksheets.get(0)protection = worksheet.getProtection()#The following 3 methods are only for Excel 2000 and earlier formatsprotection.setAllowEditingContent(False)protection.setAllowEditingObject(False)protection.setAllowEditingScenario(False)#Unprotecting the worksheetworksheet.unprotect()# Save the excel file.workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL\_97\_TO\_2003)#Print Messageprint "Worksheet unprotected successfully."

## Download Running Code

Download **Unprotect a Worksheet (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

