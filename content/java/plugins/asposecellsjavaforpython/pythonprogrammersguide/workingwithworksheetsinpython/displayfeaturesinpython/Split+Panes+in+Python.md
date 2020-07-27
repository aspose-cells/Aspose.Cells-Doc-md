+++
title = "Split Panes in Python" 
description = "" 
weight = 24771 
+++

Aspose.Cells for Java : Split Panes in Python  

# Aspose.Cells for Java : Split Panes in Python


## Aspose.Cells - Split Panes

To Split Panes using **Aspose.Cells Java for Python**, simply invoke **SplitPanes** module.

**Python Code**

saveFormat = self.SaveFormat;workbook = self.Workbook(self.dataDir + "Book1.xls")#Set the active cellworkbook.getWorksheets().get(0).setActiveCell("A20");#Split the worksheet windowworkbook.getWorksheets().get(0).split();#Save the excel fileworkbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL\_97\_TO\_2003);#Print Messageprint "Panes split successfully."

## Download Running Code

Download **Split Panes (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

