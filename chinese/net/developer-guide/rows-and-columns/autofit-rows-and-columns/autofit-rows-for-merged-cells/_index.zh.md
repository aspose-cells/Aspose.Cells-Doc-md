---
title: 自动调整合并单元格的行高
type: docs
weight: 120
url: /zh/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel提供了一个功能，可以根据内容自动调整单元格的高度。该功能称为自动调整行高。Microsoft Excel不会本机设置合并单元格的自动调整操作。有时，这项功能对于真正需要在合并单元格上实现自动调整行高的用户来说是至关重要的。

{{% /alert %}}

## **如何使用AutoFitMergedCellsType自动调整行高**
Aspose.Cells支持通过[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API实现此功能。使用此API，可以自动调整工作表中合并的单元格的行。

- 无
- 首行
- 末行
- 每行

## **自动调整合并单元格的行高**

请参考下面的代码，它创建一个工作簿对象并添加多个工作表。在每个工作表中使用不同的方法进行自动调整操作。屏幕截图显示了在执行示例代码后的结果。

<br>
<img src="result.png" width=80% />

## **C# 示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
