---
title: 刷新和计算包含计算项的数据透视表
type: docs
weight: 130
url: /zh/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells现在支持刷新和计算具有计算项的数据透视表。请像往常一样使用[**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--)和[**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--)执行此函数。

{{% /alert %}}

## **刷新和计算包含计算项的数据透视表**

以下示例代码加载了[源Excel文件](5473428.xlsx)，其中包含一个具有“add”、“div”、“div2”等三个计算项的数据透视表。我们首先将单元格 D2 的值更改为 20，然后使用Aspose.Cells API刷新和计算数据透视表，并将工作簿保存为PDF格式。[输出PDF](5473431.pdf)中的结果显示Aspose.Cells已成功刷新和计算具有计算项的数据透视表。您可以使用Microsoft Excel手动将值20放入单元格D2，然后通过Alt+F5快捷键或点击数据透视表刷新按钮来验证。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
