---
title: Refresh and Calculate Pivot Table having Calculated Items
type: docs
weight: 130
url: /java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}} 

Aspose.Cells now supports refreshing and calculating pivot table having calculated items. Please use [PivotTable.refreshData()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#refreshData\(\)) and [PivotTable.caclulateData()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#calculateData\(\)) as usual to perform this function.

{{% /alert %}} 
#### **Refresh and Calculate Pivot Table having Calculated Items**
The following sample code loads the [source excel file](5473428.xlsx) which contains a pivot table having three calculated items such as "add", "div", "div2". We first change the value of cell D2 to 20 and then refresh and calculate pivot table using Aspose.Cells APIs and save the workbook in PDF format. The results in the [output PDF](5473431.pdf) shows that Aspose.Cells refreshed and calculated the pivot table having calculated items successfully. You can verify it using Microsoft Excel by manually putting the value 20 in cell D2 and then refreshing the pivot table via Alt+F5 shortcut key or clicking the pivot table Refresh button.



{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
