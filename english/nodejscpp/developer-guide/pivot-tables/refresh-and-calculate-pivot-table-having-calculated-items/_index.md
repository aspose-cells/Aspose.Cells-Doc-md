---
title: Refresh and Calculate Pivot Table having Calculated Items
type: docs
weight: 40
url: /nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ now supports refreshing and calculating a pivot table that has calculated items. Please use the [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) and [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--) as usual to perform this function.

{{% /alert %}}

## **Refresh and Calculate Pivot Table having Calculated Items**

The following sample code loads the [source Excel file](5115238.xlsx) which contains a pivot table that has three calculated items: “add”, “div”, and “div2”. We first change the value of cell D2 to 20, and then refresh and calculate the pivot table using Aspose.Cells for Node.js via C++ APIs and save the workbook in PDF format. The results in the [output PDF](5115229.pdf) show that Aspose.Cells for Node.js via C++ refreshed and calculated the pivot table with calculated items successfully. You can verify it using Microsoft Excel by manually putting the value 20 in cell D2 and then refreshing the pivot table via the Alt+F5 shortcut key or by clicking the pivot table **Refresh** button.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
