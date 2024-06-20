---
title: 管理范围
linktitle: 范围
type: docs
weight: 105
url: /zh/python-net/managing-ranges/
description: 本文显示了如何通过Aspose.Cells for Python via .NET API管理范围。
keywords: Python Excel库，Python管理范围，在Python中创建范围，将值放入范围的单元格中，设置范围单元格的样式，获取范围的CurrentRegion。
---

## **介绍**

在Excel中，您可以使用鼠标框选来选择多个单元格，所选的单元格集称为“范围”。

例如，您可以在Excel的单元格“ A1”中单击鼠标左键，然后拖动到单元格“ C4”。您选择的矩形区域也可以轻松地通过使用Aspose.Cells for Python via .NET创建为对象。

这里是如何创建范围、设置值、设置样式以及对“范围”对象进行更多操作。

## **使用Aspose.Cells for Python Excel库管理范围**

Aspose.Cells for Python via .NET提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合。

## **如何创建范围**

当您想创建覆盖 A1:C4 的矩形区域时，您可以使用以下代码：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **如何将值放入范围的单元格中**

假设您有一个跨越A1:C4的单元格范围。矩阵构成了4 * 3 = 12个单元格。单个范围单元格是依次排列的。

以下示例展示如何向范围单元格输入一些值。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **如何设置范围单元格的样式**

以下示例展示如何设置范围单元格的样式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **如何获取范围的CurrentRegion**

CurrentRegion 是一个返回代表当前区域的 Range 对象的属性。 

当前区域是由任意组合空行和空列所限定的范围。只读。

在Excel中，您可以通过以下方式获取当前区域：
1. 用鼠标框选一个区域（range1）。
2. 点击“开始 - 编辑 - 查找和选择 - 特殊跳转 - 当前区域”，或使用“Ctrl+Shift+*”，您会看到Excel会自动帮您选择一个区域（range2），现在您已经成功选择了range2，它就是range1的当前区域。

使用Aspose.Cells for Python via .NET，您可以使用“Range.current_region”属性执行相同的功能。

请下载以下测试文件，在Excel中打开它，使用鼠标框选一个区域“A1:D7”，然后点击“Ctrl+Shift+*”，您会看到区域“A1:C3”被选中。

[current_region.xlsx](current_region.xlsx)

现在请运行以下示例，在Aspose.Cells for Python via .NET中查看其运行方式：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **高级主题**
- [Excel文件的自动填充范围](/cells/zh/python-net/autofill-ranges/)
- [复制Excel的区域](/cells/zh/python-net/copy-ranges-of-excel/)
- [仅复制区域数据](/cells/zh/python-net/copy-range-data-only/)
- [复制具有样式的区域数据](/cells/zh/python-net/copy-range-data-with-style/)
- [仅复制区域样式](/cells/zh/python-net/copy-range-style-only/)
- [创建联合范围](/cells/zh/python-net/create-union-range/)
- [剪切和粘贴范围](/cells/zh/python-net/cut-and-paste-cells/)
- [删除区域](/cells/zh/python-net/delete-ranges-from-excel/)
- [获取区域的地址、单元格计数、偏移、整行和整列](/cells/zh/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [插入范围](/cells/zh/python-net/insert-ranges-to-excel/)
- [合并或取消合并单元格范围](/cells/zh/python-net/merge-or-unmerge-range-of-cells/)
- [在工作表中移动单元格范围](/cells/zh/python-net/move-range-of-cells-in-a-worksheet/)
- [创建工作簿和工作表范围命名](/cells/zh/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [在范围内搜索和替换数据](/cells/zh/python-net/search-and-replace-data-in-a-range/)

