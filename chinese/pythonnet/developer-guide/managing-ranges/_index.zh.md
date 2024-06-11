---
title: 管理范围
linktitle: 范围
type: docs
weight: 105
url: /zh/python-net/managing-ranges/
description: 本文演示如何通过带.NET API的Aspose.Cells for Python管理范围。
keywords: Python Excel Library, Python管理范围,在Python中创建范围,将值放入范围的单元格,设置范围单元格的样式,获取范围的CurrentRegion。
---

## **介绍**

在Excel中，您可以使用鼠标框选多个单元格，所选的单元格集称为"范围"。

例如，您可以在Excel的单元格"A1"中单击鼠标左键，然后拖动到单元格"C4"。您选择的矩形区域也可以通过使用Aspose.Cells for Python通过.NET轻松地创建为对象。

以下是如何创建范围、放置值、设置样式及对"范围"对象执行更多操作。

## **使用Aspose.Cells for Python Excel库管理范围**

Aspose.Cells for Python通过.NET提供一个类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 代表一个Microsoft Excel文件。 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) 集合，允许访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合。

## **如何创建范围**

当您想要创建一个覆盖A1:C4的矩形区域时，您可以使用以下代码：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **如何将值放入范围的单元格**

假设您有一个跨越A1:C4的单元格范围。该矩阵使12个单元格。单个范围单元格按顺序排列。

以下示例展示了如何将一些值输入到范围的单元格中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **如何设置范围单元格的样式**

以下示例展示了如何设置范围单元格的样式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **如何获取范围的CurrentRegion**

CurrentRegion是一个返回表示当前区域的范围对象的属性。 

当前区域是由空白行和空白列的任何组合限定的范围。只读。

在Excel中，您可以通过以下步骤获取当前区域：
1. 用鼠标框选一个区域（range1）。
2. 点击"开始 - 编辑 - 查找和选择 - 特殊跳转 - 当前区域"，或者使用"Ctrl+Shift+*"，您将看到Excel会自动帮您选中一个区域（range2），这样您就完成了，range2 就是 range1 的当前区域。

使用Aspose.Cells for Python通过.NET，您可以使用“Range.current_region”属性执行相同的功能。

请下载以下测试文件，在Excel中打开它，用鼠标框选"A1:D7"区域，然后点击"Ctrl+Shift+*"，你将看到区域"A1:C3" 被选中。

[current_region.xlsx](current_region.xlsx)

现在请运行以下示例，在Aspose.Cells for Python通过.NET中查看其工作原理:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}


