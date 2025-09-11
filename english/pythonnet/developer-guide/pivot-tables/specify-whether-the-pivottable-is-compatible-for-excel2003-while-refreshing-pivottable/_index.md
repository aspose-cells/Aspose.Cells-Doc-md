---
title: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
type: docs
weight: 80
url: /python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: This article shows how to specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET provides the [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) property which you can use to specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable. If true, a string must be less than or equal to 255 characters, so if the string is greater than 255 characters, it will be truncated. If **false**, a string will not have the aforementioned restriction. The default value is **true**.

{{% /alert %}}

## **How to Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable**

The following sample code explains the usage of [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) property. The original string is 383 characters long. But when [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) property is set **true** and pivot table is refreshed, the data of cell B5 of the pivot table is truncated and it becomes 255 characters long. However, when [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) property is set **false** and pivot table is again refreshed, the data of cell B5 of the pivot table is not truncated and remains 383 characters long. Please read the comments inside the code for better understanding of this property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
{{< app/cells/assistant language="python-net" >}}