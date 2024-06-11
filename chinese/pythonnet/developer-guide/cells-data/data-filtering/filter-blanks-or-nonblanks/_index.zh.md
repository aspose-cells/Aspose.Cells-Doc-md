---
title: 如何筛选空白或非空白
type: docs
weight: 85
url: /zh/python-net/how-to-filter-blanks-and-non-blanks/
description: 通过Aspose.Cells for Python通过.NET API筛选空白和非空白。
keywords: Python Excel库，Python筛选空白，Python筛选非空白，Python工作表中的筛选空白，Python工作表中的筛选非空白，Python Excel中的筛选空白，Python Excel中的筛选非空白，Python Excel中的筛选空白和非空白。
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

## **使用Aspose.Cells for Python Excel库筛选空白的方法**
如果一列包含文本，使得有少量单元格为空白，并需要筛选出仅包含空白单元格的行，可以使用以下示例中演示的[AutoFilter.match_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_blanks/#int)和[AutoFilter.add_filter (field_index, criteria)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/add_filter/#int)函数。 

请查看以下加载包含一些虚拟数据的[示例Excel文件](sample.xlsx)的样本代码。该示例代码使用三种方法来过滤空白。然后将工作簿保存为[输出Excel文件](FilteredBlanks.xlsx)。 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-blanks.py" >}}

## **使用Aspose.Cells for Python Excel库筛选非空白的方法**

请参阅以下示例代码，加载了包含一些虚拟数据的[示例Excel文件](sample.xlsx)。在加载文件后，调用[AutoFilter.match_non_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_non_blanks/#int)函数以筛选非空白数据，并最后将工作簿保存为[输出Excel文件](FilteredNonBlanks.xlsx)。 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-non-blanks.py" >}}

