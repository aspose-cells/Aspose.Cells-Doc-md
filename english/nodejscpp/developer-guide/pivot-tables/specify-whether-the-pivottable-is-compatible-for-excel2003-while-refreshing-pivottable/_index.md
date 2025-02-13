---
title: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
type: docs
weight: 80
url: /nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells provides the [**PivotTable.setExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setExcel2003Compatible-boolean-) property which you can use to specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable. If true, a string must be less than or equal to 255 characters, so if the string is greater than 255 characters, it will be truncated. If **false**, a string will not have the aforementioned restriction. The default value is **true**.

{{% /alert %}}

## **Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable**

The following sample code explains the usage of [**PivotTable.setExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setExcel2003Compatible-boolean-) property. The original string is 383 characters long. But when [**PivotTable.setExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setExcel2003Compatible-boolean-) property is set **true** and pivot table is refreshed, the data of cell B5 of the pivot table is truncated and it becomes 255 characters long. However, when [**PivotTable.setExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setExcel2003Compatible-boolean-) property is set **false** and pivot table is again refreshed, the data of cell B5 of the pivot table is not truncated and remains 383 characters long. Please read the comments inside the code for better understanding of this property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
