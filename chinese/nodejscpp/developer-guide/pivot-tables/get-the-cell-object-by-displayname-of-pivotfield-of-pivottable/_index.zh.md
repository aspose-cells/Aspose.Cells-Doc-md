---
title: 根据数据透视表的PivotField显示名称获取单元格对象
type: docs
weight: 70
url: /zh/nodejs-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: 如何通过Aspose.Cells for Node.js via C++获取数据透视表的PivotField显示名称对应的单元格对象。
keywords: Aspose.Cells for Node.js via C++ Excel，Excel Node.js库，使用Aspose.Cells for Node.js via C++ Excel库通过数据透视表的PivotField显示名称获取单元格对象。
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++提供[**PivotTable.getCellByDisplayName(string)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getCellByDisplayName-string-)方法，可以通过显示名称访问数据透视表字段的单元格对象。当你想突出显示或格式化数据透视字段标题时，此方法非常有用。本文介绍如何通过数据字段的显示名称检索单元格对象，并对其应用格式。

{{% /alert %}}

## **如何通过数据透视表的PivotField的DisplayName获取Cell对象**

以下代码访问工作表的第一个透视表，然后通过透视表的第二个数据字段的显示名称获取单元格。然后将单元格的填充颜色和字体颜色分别更改为浅蓝色和黑色。下面的屏幕截图显示了代码执行之前和之后透视表的外观。

|**透视表 - 在之前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.js" >}}

|**透视表 - 在之后**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
