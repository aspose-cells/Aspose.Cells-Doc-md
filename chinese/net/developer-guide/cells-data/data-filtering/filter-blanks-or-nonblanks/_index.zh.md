---
title: 如何筛选空白或非空白
type: docs
weight: 85
url: /zh/net/how-to-filter-blanks-and-non-blanks/
description: 通过使用Aspose.Cells for .NET API了解如何筛选空白和非空白。
keywords: 筛选空白、筛选非空白、工作表中的筛选空白、工作表中的筛选非空白、Excel中的筛选空白、Excel中的筛选非空白、Excel中的筛选空白和非空白
---

## **可能的使用场景**
在Excel中进行数据筛选是一项有价值的工具，通过根据标准聚焦于数据的特定子集，以增强数据分析、探索和展示，使整体数据处理和解释过程更加高效和有效。

## **如何在Excel中筛选空白或非空白**
在Excel中，您可以使用筛选选项轻松筛选空白或非空格。 以下是操作方法：

### **如何在Excel中筛选空白**
1. 选择范围：单击列标题的字母以选择整列或选择要筛选空白的范围。
1. 打开筛选菜单：转到功能区中的“数据”选项卡。
<br>
<image src="1.png" width="70%" />
1. 筛选选项：单击“筛选”按钮。 这将向所选范围添加筛选箭头。
1. 筛选空白：单击要筛选空白的列中的筛选箭头。 取消选择除“空白”之外的所有选项，然后单击“确定”。 这将仅显示该列中的空白单元格。
<br>
<image src="2.png" width="70%" />
1. 结果如下:
<br>
<image src="3.png" width="70%" />

### **如何在Excel中筛选非空白**
1. 选择范围：单击列标题的字母以选择整列或选择要筛选非空白的范围。
1. 打开筛选菜单：转到功能区中的“数据”选项卡。
<br>
<image src="1.png" width="70%" />
1. 筛选选项：单击“筛选”按钮。 这将向所选范围添加筛选箭头。
1. 筛选非空白：单击要筛选非空白的列中的筛选箭头。 取消选择除“非空白”或“自定义”之外的所有选项，并根据条件进行设置。 单击“确定”。 这将仅显示该列中不为空的单元格。
<br>
<image src="4.png" width="70%" />
1. 结果如下:
<br>
<image src="5.png" width="70%" />

## **如何使用Aspose.Cells过滤空白**
如果一列包含文本，以致其中有几个单元格为空白，并且需要筛选只选择那些存在空白单元格的行，则可以使用[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/)和[AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/)方法，如下所演示的那样。 

请查看以下加载包含一些虚拟数据的[示例Excel文件](sample.xlsx)的样本代码。该示例代码使用三种方法来过滤空白。然后将工作簿保存为[输出Excel文件](FilteredBlanks.xlsx)。 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

## **如何使用Aspose.Cells过滤非空白**

请查看以下加载包含一些虚拟数据的[示例Excel文件](sample.xlsx)的样本代码。加载文件后，调用[AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/)函数来过滤非空白数据，最后将工作簿保存为[输出Excel文件](FilteredNonBlanks.xlsx)。 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

