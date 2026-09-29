---
title: Specify whether the PivotTable is compatible with Excel 2003 while refreshing the PivotTable
type: docs
weight: 80
url: /nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ provides the [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) property which you can use to specify whether the PivotTable is compatible with Excel 2003 while refreshing the PivotTable. If **true**, a string must be 255 characters or fewer; strings longer than 255 characters will be truncated. If **false**, the string will not be subject to that restriction. The default value is **true**.

{{% /alert %}}

## **Specify whether the PivotTable is compatible with Excel 2003 while refreshing the PivotTable**

The following sample code explains the usage of the [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) property. The original string is 383 characters long. However, when the property is set **true** and the PivotTable is refreshed, the data in cell B5 is truncated to 255 characters. When the property is set **false** and the PivotTable is refreshed again, the data in cell B5 is not truncated and remains 383 characters long. Please read the comments inside the code for a better understanding of this property.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
