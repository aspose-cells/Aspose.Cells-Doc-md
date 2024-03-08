---
title: 如何过滤空白或非空白
type: docs
weight: 85
url: /zh/net/how-to-filter-blanks-and-non-blanks/
description: 了解如何使用 Aspose.Cells for .NET API 过滤空白和非空白。
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---
##  **可能的使用场景**
Excel 中的数据筛选是一种很有价值的工具，它使用户能够根据自己的标准专注于特定的数据子集，从而增强数据分析、探索和演示，从而使整个数据操作和解释过程更加高效和有效。

##  **如何在 Excel 中过滤空白或非空白**
在 Excel 中，您可以使用筛选选项轻松筛选空白或非空白。您可以这样做：

###  **如何在 Excel 中过滤空白**
1. 选择范围：单击列标题的字母可选择整个列或选择要过滤空白的范围。
1. 打开过滤器菜单：转到功能区中的“数据”选项卡。
<br>
<image src="1.png" width="70%" />
1. 过滤器选项：单击“过滤器”按钮。这会将过滤器箭头添加到所选范围。
1. 过滤空白：单击要过滤空白的列中的过滤器箭头。取消选择除“空白”之外的所有选项，然后单击“确定”。这将仅显示该列中的空白单元格。
<br>
<image src="2.png" width="70%" />
1. 结果如下：
<br>
<image src="3.png" width="70%" />

###  **如何在 Excel 中过滤非空白**
1. 选择范围：单击列标题的字母可选择整个列或选择要过滤非空白的范围。
1. 打开过滤器菜单：转到功能区中的“数据”选项卡。
<br>
<image src="1.png" width="70%" />
1. 过滤器选项：单击“过滤器”按钮。这会将过滤器箭头添加到所选范围。
1. 过滤非空白：单击要过滤非空白的列中的过滤器箭头。取消选择除“非空白”或“自定义”之外的所有选项，并相应地设置条件。单击“确定”。这将仅显示该列中非空白的单元格。
<br>
<image src="4.png" width="70%" />
1. 结果如下：
<br>
<image src="5.png" width="70%" />

##  **如何使用 Aspose.Cells 过滤空白**
如果某列包含的文本中很少有单元格为空白，并且需要过滤器来仅选择存在空白单元格的行，[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/)和[AutoFilter.AddFilter(int fieldIndex, 字符串条件)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/)可以按如下所示使用函数。

请参阅以下加载示例代码[Excel 文件示例](sample.xlsx)其中包含一些虚拟数据。示例代码使用三种方法来过滤空白。然后将工作簿另存为[输出Excel文件](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

##  **如何使用 Aspose.Cells 过滤非空白**

请参阅以下加载示例代码[Excel 文件示例](sample.xlsx)其中包含一些虚拟数据。加载文件后，调用[AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/)函数过滤非空白数据，最后将工作簿另存为[输出Excel文件](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

