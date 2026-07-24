---
title: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
type: docs
weight: 80
url: /python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: This article shows how to specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET provides the [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) property which you can use to specify whether the PivotTable is compatible with Excel 2003 while refreshing the PivotTable. If **true**, a string must be less than or equal to 255 characters, so if the string is greater than 255 characters, it will be truncated. If **false**, a string will not have the aforementioned restriction. The default value is **true**.

{{% /alert %}}

## **How to Specify whether the PivotTable is compatible with Excel2003 while refreshing the PivotTable**

The following sample code demonstrates the usage of the [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) property. The original string is 383 characters long. When the property is set **true** and the pivot table is refreshed, the data in cell B5 of the pivot table is truncated to 255 characters. However, when the property is set **false** and the pivot table is refreshed again, the data in cell B5 is not truncated and remains 383 characters long. Please read the comments inside the code for a better understanding of this property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
