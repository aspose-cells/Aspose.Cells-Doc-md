---
title : "Refresh and Calculate Pivot Table having Calculated Items" 
description : "" 
weight : 12252 
toc : false
type: docs
url: /java/developerguide/pivottables/refresh+and+calculate+pivot+table+having+calculated+items/
---

# Aspose.Cells for Java : Refresh and Calculate Pivot Table having Calculated Items


Aspose.Cells now supports refreshing and calculating pivot table having calculated items. Please use [PivotTable.refreshData()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#refreshData()) and [PivotTable.caclulateData()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#calculateData()) as usual to perform this function.

#### Refresh and Calculate Pivot Table having Calculated Items

The following sample code loads the [source excel file](https://docs2.aspose.com/cells/java/attachments/5276034/5473428.xlsx) which contains a pivot table having three calculated items such as "add", "div", "div2". We first change the value of cell D2 to 20 and then refresh and calculate pivot table using Aspose.Cells APIs and save the workbook in PDF format. The results in the [output PDF](https://docs2.aspose.com/cells/java/attachments/5276034/5473431.pdf) shows that Aspose.Cells refreshed and calculated the pivot table having calculated items successfully. You can verify it using Microsoft Excel by manually putting the value 20 in cell D2 and then refreshing the pivot table via `Alt+F5` shortcut key or clicking the pivot table `Refresh` button.


