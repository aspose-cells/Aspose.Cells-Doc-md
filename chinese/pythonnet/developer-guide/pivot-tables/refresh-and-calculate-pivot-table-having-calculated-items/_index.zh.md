---
title: 刷新并计算具有计算项目的数据透视表
type: docs
weight: 40
url: /zh/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: 本文介绍如何刷新和计算具有 Aspose.Cells for Python via .NET 计算项目的数据透视表。
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET 现在支持刷新和计算具有计算项的数据透视表。请使用[**数据透视表.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#)和[**数据透视表.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#)像往常一样执行此功能。

{{% /alert %}}

##  **刷新并计算具有计算项目的数据透视表**

以下示例代码加载[源 Excel 文件](5115238.xlsx)其中包含一个数据透视表，该数据透视表具有三个计算项，例如“add”、“div”、“div2”。我们首先将单元格 D2 的值更改为 20，然后使用 Aspose.Cells for Python via .NET API 刷新和计算数据透视表，并将工作簿保存为 PDF 格式。结果在[输出PDF](5115229.pdf)显示 Aspose.Cells for Python via .NET 刷新并计算了已成功计算项目的数据透视表。您可以使用 Microsoft Excel 进行验证，方法是手动将值 20 放入单元格 D2 中，然后通过 Alt+F5 快捷键刷新数据透视表或单击数据透视表刷新按钮。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
