---
title: 合并单元格的行自动调整大小
type: docs
weight: 120
url: /zh/python-net/autofit-rows-for-merged-cells/
description: 本文展示了如何通过 Aspose.Cells for Python 的 .NET API 自动调整合并单元格的行高。
keywords: Python Excel 库，Python 如何用 AutoFitMergedCellsType 自动调整行高，Python 合并单元格自动适应行高。
---

{{% alert color="primary" %}}

Microsoft Excel提供了一个功能，允许您根据内容自动调整单元格的高度。该功能称为自动调整行高。Microsoft Excel本身不会在合并单元格上设置自动调整操作。有时，用户确实需要在合并单元格上实现自动调整行的用户对此功能非常重要。

{{% /alert %}}

## **如何使用AutoFitMergedCellsType自动调整行高**
通过 [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/) API，Aspose.Cells for Python 的 .NET 版本支持此功能。使用此 API，可以自动调整工作表中的行高，包括合并单元格。以下是所有可能的合并单元格自动调整行高的类型列表：

- NONE
- FIRST_LINE
- LAST_LINE
- EACH_LINE

## **自动调整合并单元格的行**

请参阅以下代码，它创建一个工作簿对象并添加多个工作表。在每个工作表中使用不同方法进行自动调整操作。屏幕截图显示了执行示例代码后的结果。

<br>
<img src="result.png" width=80% />

## **C# 示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
