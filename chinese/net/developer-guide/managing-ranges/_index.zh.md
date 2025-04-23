---
title: 管理范围
linktitle: 范围
type: docs
weight: 105
url: /zh/net/managing-ranges/
---

## **介绍**

在Excel中，您可以使用鼠标框选来选择多个单元格，所选的单元格集称为“范围”。

例如，您可以在Excel的“A1”单元格单击左鼠标按钮，然后拖动到“C4”单元格。您所选的矩形区域也可以通过Aspose.Cells轻松地创建为对象。

这里是如何创建范围、设置值、设置样式以及对“范围”对象进行更多操作。

## **使用Aspose.Cells管理范围**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合。

### **创建范围**

当您想创建覆盖 A1:C4 的矩形区域时，您可以使用以下代码：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **将值放入范围单元格**

假设您有一个涵盖 A1:C4 的单元格范围。该矩阵形成 4 * 3 = 12 个单元格。单个范围单元格是按顺序排列的：Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

以下示例展示如何向范围单元格输入一些值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **设置范围单元格的样式**

以下示例展示如何设置范围单元格的样式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **获取范围的当前区域**

CurrentRegion 是一个返回代表当前区域的 Range 对象的属性。 

当前区域是由任意组合空行和空列所限定的范围。只读。

在Excel中，您可以通过以下方式获取当前区域：
1. 用鼠标框选一个区域（range1）。
2. 点击“开始 - 编辑 - 查找和选择 - 特殊跳转 - 当前区域”，或使用“Ctrl+Shift+*”，您会看到Excel会自动帮您选择一个区域（range2），现在您已经成功选择了range2，它就是range1的当前区域。

使用Aspose.Cells，您可以使用"Range.CurrentRegion" 属性执行相同的功能。

请下载以下测试文件，在Excel中打开它，使用鼠标框选一个区域“A1:D7”，然后点击“Ctrl+Shift+*”，您会看到区域“A1:C3”被选中。

[current_region.xlsx](current_region.xlsx)

现在请运行以下示例，在Aspose.Cells中看看它是如何工作的：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **高级主题**
- [Excel文件的自动填充范围](/cells/zh/net/autofill-ranges/)
- [复制Excel的区域](/cells/zh/net/copy-ranges-of-Excel/)
- [仅复制区域数据](/cells/zh/net/copy-range-data-only/)
- [复制具有样式的区域数据](/cells/zh/net/copy-range-data-with-style/)
- [仅复制区域样式](/cells/zh/net/copy-range-style-only/)
- [创建联合范围](/cells/zh/net/create-union-range/)
- [剪切和粘贴范围](/cells/zh/net/cut-and-paste-cells/)
- [删除区域](/cells/zh/net/delete-ranges-from-Excel/)
- [获取区域的地址、单元格计数、偏移、整行和整列](/cells/zh/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [插入范围](/cells/zh/net/insert-ranges-to-Excel/)
- [合并或取消合并单元格范围](/cells/zh/net/merge-or-unmerge-range-of-cells/)
- [在工作表中移动单元格范围](/cells/zh/net/move-range-of-cells-in-a-worksheet/)
- [创建工作簿和工作表范围命名](/cells/zh/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [在范围内搜索和替换数据](/cells/zh/net/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="csharp" >}}
