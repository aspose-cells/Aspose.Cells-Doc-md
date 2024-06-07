---
title: 从工作表中删除数据透视表
type: docs
weight: 60
url: /zh/net/delete-pivot-table-from-a-worksheet/
description: 用于Excel工作表的删除PivotTable的C#代码
keywords: C#从工作表删除数据透视表，C#从Excel删除数据透视表，如何使用C#删除数据透视表，使用C#删除数据透视表，从Excel中删除数据透视表的C#，C#删除数据透视表，C#删除数据透视表，删除数据透视表，如何删除数据透视表
---

{{% alert color="primary" %}}

Aspose.Cells提供了删除或删除工作表中数据透视表的功能。您可以使用数据透视表对象或数据透视表位置来删除数据透视表。请使用[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove)方法使用数据透视表对象删除数据透视表，使用[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)方法使用其在数据透视表集合内的位置删除数据透视表对象。

{{% /alert %}}

以下示例代码从工作表中删除了两个数据透视表。首先，它使用[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove)方法删除数据透视表，然后使用[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)方法删除数据透视表

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
