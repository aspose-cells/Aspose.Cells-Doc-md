---
title: 从工作表中删除数据透视表
type: docs
weight: 60
url: /zh/net/delete-pivot-table-from-a-worksheet/
description: 用于在Excel工作表中删除数据透视表的C#代码
keywords: c#删除工作表中的数据透视表，c#删除Excel中的数据透视表，如何使用c#删除数据透视表，删除Excel数据透视表的c#，c#删除数据透视表，c#移除数据透视表，移除数据透视表，删除数据透视表，如何删除数据透视表
---

{{% alert color="primary" %}}

Aspose.Cells提供了一个功能，用于删除或移除工作表中的数据透视表。您可以使用数据透视表对象或数据透视表位置来删除数据透视表。请使用[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove)方法使用数据透视表对象来删除数据透视表，使用其位置在数据透视表集合内[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)方法删除数据透视表对象。

{{% /alert %}}

以下示例代码从工作表中删除了两个数据透视表。首先使用[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove)方法移除数据透视表，然后使用[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)方法移除数据透视表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
