+++
title = "Saving Files in Python" 
description = "" 
weight = 24748 
+++

Aspose.Cells for Java : Saving Files in Python  

# Aspose.Cells for Java : Saving Files in Python


## Aspose.Cells - Saving Files

##### Saving file to some location

If developers need to save their files using **Aspose.Cells Java for Python** to some storage location then they can simply specify the file name (with its complete storage path) and desired file format (using the**FileFormatType**enumeration) while calling the**save**method of**Workbook**object.

**Python Code**

fileFormatType = self.FileFormatType#Creating an Workbook object with an Excel file pathworkbook = self.Workbook(self.dataDir + "Book1.xls")#Save in default (Excel2003) formatworkbook.save(self.dataDir + "book.default.out.xls")#Save in Excel2003 formatworkbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL\_97\_TO\_2003)#Save in Excel2007 xlsx formatworkbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)#Save in SpreadsheetML formatworkbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL\_2003\_XML)#Print Messageprint("<BR>")print("Worksheets are saved successfully.")

Download **Saving File (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

