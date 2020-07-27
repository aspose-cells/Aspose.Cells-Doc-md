+++
title = "Freeze Panes in Python" 
description = "" 
weight = 24768 
+++

Aspose.Cells for Java : Freeze Panes in Python  

# Aspose.Cells for Java : Freeze Panes in Python


## Aspose.Cells - Freeze Panes

To Freeze Panes in the Spreadsheet Document using **Aspose.Cells Java for Python**, simply invoke **FreezePanes** module.

**Python Code**

workbook = self.Workbook(self.dataDir + "Book1.xls")#Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()worksheet = worksheets.get(0)#Applying freeze panes settingsworksheet.freezePanes(3,2,3,2)#Saving the modified Excel file in default formatworkbook.save(self.dataDir + "book.out.xls")#Print Messageprint "Panes freeze successfull."

## Download Running Code

Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

