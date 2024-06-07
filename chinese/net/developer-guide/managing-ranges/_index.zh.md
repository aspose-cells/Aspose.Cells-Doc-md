---
title: 管理范围
linktitle: 范围
type: docs
weight: 105
url: /zh/net/managing-ranges/
---

## **介绍**

在Excel中，您可以使用鼠标框选多个单元格，所选的单元格集称为"范围"。

例如，您可以在Excel的单元格"A1"中单击鼠标左键，然后拖动到单元格"C4"。您选择的矩形区域也可以通过Aspose.Cells轻松创建为对象。

以下是如何创建范围、放置值、设置样式及对"范围"对象执行更多操作。

## **使用Aspose.Cells管理范围**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 表示Microsoft Excel文件。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了一个 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合。

### **创建范围**

当您想要创建一个覆盖A1:C4的矩形区域时，您可以使用以下代码：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **将值放入范围的单元格中**

假设您有一个覆盖A1:C4的单元格范围。该矩阵创建了4 * 3 = 12个单元格。单个范围单元格按顺序排列：Range[0,0]，Range[0,1]，Range[0,2]，Range[1,0]，Range[1,1]，Range[1,2]，Range[2,0]，Range[2,1]，Range[2,2]，Range[3,0]，Range[3,1]，Range[3,2]。

以下示例展示了如何将一些值输入到范围的单元格中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **设置范围单元格的样式**

以下示例展示了如何设置范围单元格的样式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **获取范围的CurrentRegion**

CurrentRegion是一个返回表示当前区域的范围对象的属性。 

当前区域是由空白行和空白列的任何组合限定的范围。只读。

在Excel中，您可以通过以下步骤获取当前区域：
1. 用鼠标框选一个区域（range1）。
2. 点击"开始 - 编辑 - 查找和选择 - 特殊跳转 - 当前区域"，或者使用"Ctrl+Shift+*"，您将看到Excel会自动帮您选中一个区域（range2），这样您就完成了，range2 就是 range1 的当前区域。

使用Aspose.Cells，您可以使用"Range.CurrentRegion"属性执行相同的功能。

请下载以下测试文件，在Excel中打开它，用鼠标框选"A1:D7"区域，然后点击"Ctrl+Shift+*"，你将看到区域"A1:C3" 被选中。

[current_region.xlsx](current_region.xlsx)

现在请运行以下示例，看看在Aspose.Cells中如何工作：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **高级主题**
- [Excel文件的自动填充范围](/cells/zh/net/autofill-ranges/)
- [复制Excel的区域](/cells/zh/net/copy-ranges-of-Excel/)
- [仅复制区域数据](/cells/zh/net/copy-range-data-only/)
- [复制带样式的区域数据](/cells/zh/net/copy-range-data-with-style/)
- [仅复制区域样式](/cells/zh/net/copy-range-style-only/)
- [创建联合范围](/cells/zh/net/create-union-range/)
- [剪切和粘贴区域](/cells/zh/net/cut-and-paste-cells/)
- [删除区域](/cells/zh/net/delete-ranges-from-Excel/)
- [获取范围的地址、单元格计数、偏移、整列和整行](/cells/zh/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [插入区域](/cells/zh/net/insert-ranges-to-Excel/)
- [合并或拆分单元格区域](/cells/zh/net/merge-or-unmerge-range-of-cells/)
- [在工作表中移动单元格范围](/cells/zh/net/move-range-of-cells-in-a-worksheet/)
- [创建工作薄和工作表范围命名区域](/cells/zh/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [在区域中查找和替换数据](/cells/zh/net/search-and-replace-data-in-a-range/)
