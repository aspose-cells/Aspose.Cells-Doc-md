---
title: 使用 Golang 通过 C++ 操作数据透视表中 DataField 的显示格式。
linktitle: 操作数据透视表中的数据字段显示格式
type: docs
weight: 140
url: /zh/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: 学习如何使用Aspose.Cells for C++操作数据透视表中数据字段的显示格式。
---

{{% alert color="primary" %}}

Aspose.Cells支持数据透视表中所有数据字段的数据显示格式。

{{% /alert %}}

## **“从最小到最大排名”和“从最大到最小排名”显示格式选项**

Aspose.Cells提供设置数据透视字段显示格式的能力。API提供了 [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) 属性，要将排名从最大到最小设置，可以将 [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) 属性设置为 [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/)。以下代码片段演示了如何设置显示格式选项。

可从此处下载示例源文件和输出文件以测试示例代码:

【源 Excel 文件】（101089332.xlsx）

【输出 Excel 文件】（101089333.xlsx）

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
