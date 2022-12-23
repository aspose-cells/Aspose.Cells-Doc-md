---
title: 刷新并计算具有计算项的数据透视表
type: docs
weight: 40
url: /zh/net/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells 现在支持刷新和计算具有计算项的数据透视表。请使用[**数据透视表.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata)和[**数据透视表.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata)像往常一样执行此功能。

{{% /alert %}}

## **刷新并计算具有计算项的数据透视表**

下面的示例代码加载[源文件](5115238.xlsx)其中包含一个数据透视表，其中包含三个计算项，例如“add”、“div”、“div2”。我们首先将单元格 D2 的值更改为 20，然后使用 Aspose.Cells API 刷新和计算数据透视表，并将工作簿保存为 PDF 格式。结果在[输出 PDF](5115229.pdf)显示Aspose.Cells刷新计算数据透视表计算项成功。您可以使用 Microsoft Excel 验证它，方法是手动将值 20 放入单元格 D2，然后通过 Alt+F5 快捷键或单击数据透视表刷新按钮刷新数据透视表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
