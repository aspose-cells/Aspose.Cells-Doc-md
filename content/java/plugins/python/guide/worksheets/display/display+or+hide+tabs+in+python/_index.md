---
title : "Display or Hide Tabs in Python" 
description : "" 
weight : 24767 
toc : false
type: docs
url: /java/plugins/python/guide/worksheets/display/display+or+hide+tabs+in+python/
---

# Aspose.Cells for Java : Display or Hide Tabs in Python


## Aspose.Cells - Display Hide Tabs

##### Hiding Tabs

To hide tabs using **Aspose.Cells Java for Ruby**, call **displayhidetabs** module.

**Python Code**

workbook = self.Workbook(self.dataDir + "Book1.xls")#Hiding the tabs of the Excel fileworkbook.getSettings().setShowTabs(False)#Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(self.dataDir + "output.xls")# Print messageprint "Tabs are now hidden, please check the output file."

##### Making Tabs Visible

Make tabs visible with the`Workbook`class'`setSheetTabBarHidden(false)`method.

**Python Code**

\# Displaying the tabs of the Excel fileworkbook.getSettings().setSowTabs(true)

## Download Running Code

Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

