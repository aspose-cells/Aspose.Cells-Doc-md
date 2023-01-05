---
title: 刷新并计算具有计算项的数据透视表
type: docs
weight: 130
url: /zh/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells 现在支持刷新和计算具有计算项的数据透视表。请用[**数据透视表.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ） 和[**数据透视表.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) 照常执行此功能。

{{% /alert %}}

## **刷新并计算具有计算项的数据透视表**

下面的示例代码加载[源文件](5473428.xlsx)其中包含一个数据透视表，其中包含三个计算项，例如“add”、“div”、“div2”。我们首先将单元格 D2 的值更改为 20，然后使用 Aspose.Cells API 刷新和计算数据透视表，并将工作簿保存为 PDF 格式。结果在[输出 PDF](5473431.pdf)显示Aspose.Cells刷新计算数据透视表计算项成功。您可以使用 Microsoft Excel 验证它，方法是手动将值 20 放入单元格 D2，然后通过 Alt+F5 快捷键或单击数据透视表刷新按钮刷新数据透视表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
