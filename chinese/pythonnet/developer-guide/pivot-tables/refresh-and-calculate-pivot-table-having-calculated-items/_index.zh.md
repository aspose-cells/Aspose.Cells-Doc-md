---
title: 刷新和计算包含计算项的数据透视表
type: docs
weight: 40
url: /zh/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: 本文展示了如何使用Aspose.Cells for Python via .NET刷新和计算具有计算项的数据透视表。
keywords: Aspose.Cells for Python Excel，Excel Python库，刷新和计算具有计算项的数据透视表
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET现在支持刷新和计算具有计算项的数据透视表。请像往常一样使用[**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#)和[**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#)执行此功能。

{{% /alert %}}

## **刷新和计算包含计算项的数据透视表**

以下示例代码加载了包含三个计算项（例如“add”、“div”、“div2”）的数据透视表的[源Excel文件](5115238.xlsx)。我们首先将单元格D2的值更改为20，然后使用Aspose.Cells for Python via .NET的API刷新和计算数据透视表，并将工作簿保存为PDF格式。[输出PDF](5115229.pdf)中的结果显示，Aspose.Cells for Python via .NET成功地刷新和计算了具有计算项的数据透视表。您可以使用Microsoft Excel手动将值20放入单元格D2，然后通过Alt+F5快捷键或单击数据透视表的刷新按钮来验证它。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
