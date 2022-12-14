---
title: 管理范围
linktitle: 范围
type: docs
weight: 105
url: /zh/net/managing-ranges/
---
## **介绍**

在 Excel 中，您可以使用鼠标框选择多个单元格，所选单元格的集合称为“范围”。

例如，可以在Cell Excel的“A1”中单击鼠标左键，然后拖动到“C4”单元格。您选择的矩形区域也可以使用 Aspose.Cells 轻松创建为对象。

下面介绍如何创建范围、放置值、设置样式以及对“范围”对象进行更多操作。

## **使用 Aspose.Cells 管理范围**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。

### **创建范围**

当你想创建一个延伸到 A1:C4 的矩形区域时，你可以使用下面的代码：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **将值放入Range的Cells**

假设您有一系列单元格延伸到 A1:C4。该矩阵有 4 * 3 = 12 个单元格。各个范围单元格按顺序排列：Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、范围[2,0]、范围[2,1]、范围[2,2]、范围[3,0]、范围[3,1]、范围[3,2]。

以下示例显示如何将一些值输入到范围的单元格中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Range的Cells的设置样式**

以下示例显示如何设置 Range 单元格的样式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **获取范围的当前区域**

CurrentRegion 是一个返回表示当前区域的 Range 对象的属性。

当前区域是由空白行和空白列的任意组合界定的范围。只读。

在 excel 中，您可以通过以下方式获取 CurrentRegion 区域：
1. 用鼠标框选择一个区域（range1）。
2. 点击“Home - Editing - Find & Select - Go To Special - Currect region”，或者使用“Ctrl+Shift+*”，你会看到excel自动帮你选择一个区域（range2），现在你做到了，range2是range1 的 CurrentRegion。

使用 Aspose.Cells，您可以使用“Range.CurrentRegion”属性来执行相同的功能。

请下载以下测试文件，用excel打开，用鼠标框选“A1:D7”区域，然后按“Ctrl+Shift+*”，即可看到“A1:C3”区域被选中。

[当前区域.xlsx](current_region.xlsx)

现在请运行以下示例，在 Aspose.Cells 中查看它是如何工作的：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **推进主题**
- [Excel 文件的自动填充范围](/cells/zh/net/autofill-ranges/)
- [复制Excel的范围](/cells/zh/net/copy-ranges-of-Excel/)
- [仅复制范围数据](/cells/zh/net/copy-range-data-only/)
- [使用样式复制范围数据](/cells/zh/net/copy-range-data-with-style/)
- [仅复制范围样式](/cells/zh/net/copy-range-style-only/)
- [创建联合范围](/cells/zh/net/create-union-range/)
- [剪切和粘贴范围](/cells/zh/net/cut-and-paste-cells/)
- [删除范围](/cells/zh/net/delete-ranges-from-Excel/)
- [获取地址 Cell Count Offset 整列和整行的范围](/cells/zh/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [插入范围](/cells/zh/net/insert-ranges-to-Excel/)
- [合并或取消合并范围 Cells](/cells/zh/net/merge-or-unmerge-range-of-cells/)
- [在工作表中移动范围 Cells](/cells/zh/net/move-range-of-cells-in-a-worksheet/)
- [创建工作簿和工作表范围命名范围](/cells/zh/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [搜索和替换范围内的数据](/cells/zh/net/search-and-replace-data-in-a-range/)
