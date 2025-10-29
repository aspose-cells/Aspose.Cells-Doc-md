---
title: 使用 C++ 和 Golang 删除工作表中的数据透视表
linktitle: 删除数据透视表
type: docs
weight: 60
url: /zh/go-cpp/delete-pivot-table-from-a-worksheet/
description: 使用 Aspose.Cells 的 C++ 代码删除 Excel 工作表中的数据透视表。
keywords: C++ 从工作表中删除数据透视表，C++ 删除 Excel 数据透视表，如何用 C++ 删除数据透视表，删除数据透视表，删除 Excel 中的数据透视表，C++ 删除数据透视表，C++ 移除数据透视表，移除数据透视表，删除数据透视表，如何删除数据透视表
---

{{% alert color="primary" %}}

Aspose.Cells提供了一个功能，用于删除或移除工作表中的数据透视表。您可以使用数据透视表对象或数据透视表位置来删除数据透视表。请使用[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/)方法使用数据透视表对象来删除数据透视表，使用其位置在数据透视表集合内[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/)方法删除数据透视表对象。

{{% /alert %}}

以下示例代码从工作表中删除两个数据透视表。首先，它使用 [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) 方法移除数据透视表，然后使用 [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) 方法继续移除。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}
