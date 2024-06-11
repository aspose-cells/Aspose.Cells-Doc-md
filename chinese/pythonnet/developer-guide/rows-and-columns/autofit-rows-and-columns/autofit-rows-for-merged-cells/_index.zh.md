---
title: 自动调整合并单元格的行高
type: docs
weight: 120
url: /zh/python-net/autofit-rows-for-merged-cells/
description: 本文介绍了如何通过Aspose.Cells for Python via .NET API来自动调整合并单元格的行高。
keywords: Python Excel库，Python如何使用AutoFitMergedCellsType自动调整行高，Python中合并单元格的行自动调整。
---

{{% alert color="primary" %}}

Microsoft Excel提供了一个功能，可以根据内容自动调整单元格的高度。该功能称为自动调整行高。Microsoft Excel不会本机设置合并单元格的自动调整操作。有时，这项功能对于真正需要在合并单元格上实现自动调整行高的用户来说是至关重要的。

{{% /alert %}}

## **如何使用AutoFitMergedCellsType自动调整行高**
Aspose.Cells for Python via .NET通过[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/) API支持这个功能。使用这个API，可以在一个包括合并单元格的工作表中自动调整行高。以下是所有可能类型的自动调整合并单元格：

- NONE
- 第一行
- 最后一行
- 每一行

## **自动调整合并单元格的行高**

请参考下面的代码，它创建一个工作簿对象并添加多个工作表。在每个工作表中使用不同的方法进行自动调整操作。屏幕截图显示了在执行示例代码后的结果。

<br>
<img src="result.png" width=80% />

## **C# 示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
