---
title: 刷新和计算包含计算项的数据透视表
type: docs
weight: 130
url: /zh/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells现在支持刷新和计算具有计算项的数据透视表。请使用[**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData()和[**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()来执行此功能。

{{% /alert %}}

## **刷新和计算包含计算项的数据透视表**

以下示例代码加载了包含三个计算项（如"add"、"div"、"div2"）的数据透视表的[源Excel文件](5473428.xlsx)。我们首先将单元格D2的值更改为20，然后使用Aspose.Cells API刷新和计算数据透视表，并将工作簿保存为PDF格式。在[输出PDF](5473431.pdf)中的结果显示，Aspose.Cells成功刷新和计算了具有计算项的数据透视表。您可以通过在单元格D2手动放置值20，然后通过Alt+F5快捷键刷新数据透视表或单击数据透视表刷新按钮来验证它。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
