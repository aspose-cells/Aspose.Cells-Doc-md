---
title: 合并单元格的行自动调整大小
type: docs
weight: 120
url: /zh/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel提供了一个功能，允许您根据内容自动调整单元格的高度。该功能称为自动调整行高。Microsoft Excel本身不会在合并单元格上设置自动调整操作。有时，用户确实需要在合并单元格上实现自动调整行的用户对此功能非常重要。

{{% /alert %}}

## **如何使用AutoFitMergedCellsType自动调整行高**
Aspose.Cells通过[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/) API支持这一功能。使用此API，可以自动调整工作表中包括合并单元格的行。以下是所有可能的合并单元格自动调整类型列表:

- 无
- 第一行
- 最后一行
- 每一行

## **自动调整合并单元格的行**

请参阅以下代码，它创建一个工作簿对象并添加多个工作表。在每个工作表中使用不同方法进行自动调整操作。屏幕截图显示了执行示例代码后的结果。

<br>
<img src="result.png" width=80% />

## **C# 示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
