---
title : "Display or Hide Gridlines in Python" 
description : "" 
weight : 24765 
toc : false
type: docs
url: /java/plugins/python/guide/worksheets/display/display+or+hide+gridlines+in+python/
---

# Aspose.Cells for Java : Display or Hide Gridlines in Python


## Aspose.Cells - Display Hide Gridlines

##### Hiding Gridlines

To hide worksheet using **Aspose.Cells Java for Ruby**, call **displayhidegridlines** module.

**Python Code**

workbook = self.Workbook(self.dataDir + "Book1.xls")#Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()worksheet = worksheets.get(0)#Hiding the grid lines of the first worksheet of the Excel fileworksheet.setGridlinesVisible(False)#Saving the modified Excel file in default (that is Excel 2000) formatworkbook.save(self.dataDir + "output.xls")# Print messageprint "Grid lines are now hidden on sheet 1, please check the output document."

##### Making Gridlines Visible

To make gridlines visible, use the the`Worksheet`class'`setGridlinesVisible(true)`method.

**Python Code**

\# Displaying the gridlines of the worksheetworksheet.setGridlinesVisible(True)

## Download Running Code

Download **DisplayHideGridlines (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

