---
title: 刷新和计算包含计算项的数据透视表
type: docs
weight: 40
url: /zh/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells现在支持刷新和计算包含计算项的数据透视表。请像往常一样使用[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata)和[**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata)执行此功能。

{{% /alert %}}

## **刷新和计算包含计算项的数据透视表**

以下示例代码加载包含三个计算项（如"add"、"div"、"div2"）的数据透视表的源Excel文件。我们首先将单元格D2的值更改为20，然后使用Aspose.Cells API刷新和计算数据透视表，并以PDF格式保存工作簿。在[输出PDF](5115229.pdf)中的结果显示Aspose.Cells成功刷新和计算了包含计算项的数据透视表。您可以通过在单元格D2中手动输入值20，然后通过Alt+F5快捷键或单击数据透视表刷新按钮来验证它。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
