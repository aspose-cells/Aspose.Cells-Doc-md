---
title: Refresh and Calculate Pivot Table having Calculated Items
type: docs
weight: 130
url: /java/refresh-and-calculate-pivot-table-having-calculated-items/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells now supports refreshing and calculating a pivot table having calculated items. Please use [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) and [**PivotTable.calculateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) as usual to perform this function.

{{% /alert %}}

## **Refresh and Calculate Pivot Table having Calculated Items**

The following sample code loads the [source Excel file](5473428.xlsx) which contains a pivot table having three calculated items such as "add", "div", and "div2". We first change the value of cell D2 to 20, and then refresh and calculate the pivot table using Aspose.Cells APIs, and save the workbook in PDF format. The results in the [output PDF](5473431.pdf) show that Aspose.Cells refreshed and calculated the pivot table having calculated items successfully. You can verify it using Microsoft Excel by manually setting the value 20 in cell D2 and then refreshing the pivot table via the Alt+F5 shortcut key or by clicking the Refresh button on the pivot table.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
{{< app/cells/assistant language="java" >}}
