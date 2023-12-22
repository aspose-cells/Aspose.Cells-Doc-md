---
title: 通过数据透视表的PivotField的DisplayName获取Cell对象
type: docs
weight: 70
url: /zh/python-net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: 如何通过数据透视表的数据透视字段的 DisplayName 与 Aspose.Cells for Python via .NET 获取 Cell 对象。
keywords: Get the Cell object by DisplayName of PivotField of PivotTable.
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET 提供[**PivotTable.get_cell_by_display_name(display_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_cell_by_display_name/#str)您可以使用该方法通过数据透视字段的显示名称访问单元格对象。当您想要突出显示或格式化数据透视表字段标题时，此方法非常有用。本文介绍如何通过数据字段的显示名称检索单元格对象，然后对其应用格式设置。

{{% /alert %}}

##  **通过数据透视表的PivotField的DisplayName获取Cell对象**

以下代码访问工作表的第一个数据透视表，然后通过数据透视表的第二个数据字段的显示名称获取单元格。然后，它将单元格的填充颜色和字体颜色分别更改为浅蓝色和黑色。下面的屏幕截图显示了数据透视表在执行代码之前和之后的外观。

|**数据透视表 - 之前**|
| :- |
|![待办事项：图像_替代_文本](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.py" >}}

|**数据透视表 - 之后**|
| :- |
|![待办事项：图像_替代_文本](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
