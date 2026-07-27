---
title: 刷新并计算具有计算项的数据透视表，使用 Golang 通过 C++。
linktitle: 刷新和计算包含计算项的数据透视表
type: docs
weight: 40
url: /zh/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: 使用 Aspose.Cells 通过 C++ 和 Golang 刷新和计算带有计算项的数据透视表。
---

{{% alert color="primary" %}}

Aspose.Cells现在支持刷新和计算包含计算项的数据透视表。请像往常一样使用[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/)和[**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)执行此功能。

{{% /alert %}}

## **刷新和计算包含计算项的数据透视表**

以下示例代码加载了包含三个计算项（如“add”、“div”、“div2”）的[源 Excel 文件](5115238.xlsx)，首先将单元格 D2 的值修改为 20，然后使用 Aspose.Cells API 刷新并计算数据透视表，并将工作簿保存为 PDF 格式。生成的 [输出 PDF](5115229.pdf) 证明 Aspose.Cells 成功刷新和计算了包含计算项的数据透视表。可以通过手动在 D2 输入 20 并用 Alt+F5 快捷键或点击数据透视表的刷新按钮，使用 Microsoft Excel 进行验证。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}
