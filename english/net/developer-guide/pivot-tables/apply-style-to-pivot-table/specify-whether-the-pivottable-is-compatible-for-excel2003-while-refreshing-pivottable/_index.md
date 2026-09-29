---
title: Specify whether the PivotTable is compatible with Excel 2003 while refreshing the PivotTable
type: docs
weight: 80
url: /net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides the [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) property, which you can use to specify whether the PivotTable is compatible with Excel 2003 while refreshing the PivotTable. If **true**, a string must be less than or equal to 255 characters; therefore, if the string exceeds 255 characters, it will be truncated. If **false**, a string will not be subject to the aforementioned restriction. The default value is **true**.

{{% /alert %}}

## **Specify whether the PivotTable is compatible with Excel 2003 while refreshing the PivotTable**

The following sample code demonstrates the usage of the [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) property. The original string is 383 characters long. When the **PivotTable.IsExcel2003Compatible** property is set to **true** and the pivot table is refreshed, the data in cell B5 of the pivot table is truncated to 255 characters. However, when the property is set to **false** and the pivot table is refreshed again, the data in cell B5 is not truncated and remains 383 characters long. Please read the comments inside the code for a better understanding of this property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
