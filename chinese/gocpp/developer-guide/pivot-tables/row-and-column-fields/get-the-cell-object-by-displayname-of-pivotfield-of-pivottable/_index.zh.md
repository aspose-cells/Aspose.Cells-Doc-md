---
title: 使用 C++ 和 Golang 根据显示名称获取数据透视表中的单元格对象
linktitle: 通过数据透视表的 PivotField 的显示名称获取单元格对象
type: docs
weight: 70
url: /zh/go-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: 学习如何通过数据透视字段的显示名称检索单元格对象并应用格式，使用 Aspose.Cells for C++。
---

{{% alert color="primary" %}}

Aspose.Cells 提供了 [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/go-cpp/pivottable/getcellbydisplayname/) 方法，可以通过数据透视字段的显示名称访问单元格对象。此方法在需要突出显示或格式化数据透视表标题时非常有用。本文详细介绍了如何通过数据字段的显示名称检索单元格对象，然后进行格式化。

{{% /alert %}}

## **用 C++ 通过数据透视表的 PivotField 的显示名称获取单元格对象**

以下代码访问工作表的第一个数据透视表，并根据数据透视表的第二个数据字段的显示名称检索单元格。然后，将单元格的填充颜色设为浅蓝色，字体颜色设为黑色。以下为执行前后数据透视表的效果截图。

|**透视表 - 在之前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetTheCellObjectByDisplaynameOfPivotfieldOfPivottable.go" >}}
|**透视表 - 在之后**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
