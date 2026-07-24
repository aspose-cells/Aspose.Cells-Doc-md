---
title: 根据数据透视表的PivotField显示名称获取单元格对象
type: docs
weight: 70
url: /zh/python-net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: 如何通过Aspose.Cells for Python via .NET获取数据透视表的PivotField的DisplayName的Cell对象。
keywords: 使用Aspose.Cells for Python Excel库，获取数据透视表的PivotField的DisplayName的Cell对象。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET提供了[**PivotTable.get_cell_by_display_name(display_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_cell_by_display_name/#str)方法，您可以使用它来访问数据透视表的显示字段的单元格对象。当您想要突出显示或格式化数据透视表的字段标题时，这种方法非常有用。本文解释了如何通过显示数据字段的名称检索单元格对象，然后对其应用格式。

{{% /alert %}}

## **如何通过数据透视表的PivotField的DisplayName获取Cell对象**

以下代码访问工作表的第一个透视表，然后通过透视表的第二个数据字段的显示名称获取单元格。然后将单元格的填充颜色和字体颜色分别更改为浅蓝色和黑色。下面的屏幕截图显示了代码执行之前和之后透视表的外观。

|**透视表 - 在之前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.py" >}}

|**透视表 - 在之后**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="python-net" >}}
