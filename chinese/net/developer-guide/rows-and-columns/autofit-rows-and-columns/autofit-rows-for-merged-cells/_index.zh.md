---
title: 用于合并的自动调整行 Cells
type: docs
weight: 120
url: /zh/net/autofit-rows-for-merged-cells/
---
{{% alert color="primary" %}}

Microsoft Excel 提供了一项功能，允许您根据单元格的内容自动调整单元格的高度。该功能称为自动调整行。 Microsoft Excel 本身不会对合并单元格设置自动调整操作。有时，对于真正需要在合并单元格上实现自动调整行的用户来说，该功能变得至关重要。

{{% /alert %}}

##  **如何使用 AutoFitMergedCellsType 自动调整行**
Aspose.Cells 通过以下方式支持此功能[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API。使用此 API，可以自动调整工作表中包括合并单元格的行。以下是自动调整合并单元格的所有可能类型的列表：

- 没有任何
- 第一行
- 最后一行
- 每行

##  **用于合并的自动调整行 Cells**

请参阅以下代码，它创建一个工作簿对象并添加多个工作表。在每个工作表中使用不同的方法进行自动调整操作。屏幕截图显示了示例代码执行后的结果。

<br>
<img src="result.png" width=80% />

##  **C# 示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
