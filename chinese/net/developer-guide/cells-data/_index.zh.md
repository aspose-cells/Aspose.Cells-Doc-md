---
title: 管理Excel文件的数据
linktitle: Cells 数据
type: docs
weight: 110
url: /zh/net/view-and-edit-excel-data/
description: 本文介绍如何使用Aspose.Cells库查看和编辑Excel文件的数据。
keywords: Aspose.Cells C# Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---
{{% alert color="primary" %}}

在[访问工作表的 Cells](/cells/zh/net/accessing-cells-of-a-worksheet/)，我们讨论了访问工作表中的单元格的基本方法。本文使用其中一种方法向单元格添加不同类型的数据。

{{% /alert %}}

##  **如何向Cells添加数据**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

 Aspose.Cells 允许开发人员通过调用向工作表中的单元格添加数据[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**看跌期权**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。 Aspose.Cells 提供了重载版本[**看跌期权**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)允许开发人员将不同类型的数据添加到单元格的方法。使用这些重载版本[**看跌期权**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法，可以向单元格添加布尔值、字符串、双精度、整数或日期/时间等值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

##  **如何提高效率**

如果你使用[**看跌期权**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法将大量数据放入工作表中，您应该将值添加到单元格中，首先按行，然后按列。这种方法极大地提高了应用程序的效率。

##  **如何从 Cells 检索数据**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)代表 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问文件中的工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

这[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供了多个属性，允许开发人员根据单元格的数据类型检索值。这些属性包括：

- [**字符串值**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue)：返回单元格的字符串值。
- [**双值**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue)：返回单元格的双精度值。
- [**布尔值**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue)：返回单元格的布尔值。
- [**日期时间值**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue)：返回单元格的日期/时间值。
- [**浮点值**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)：返回单元格的浮点值。
- [**整数值**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)：返回单元格的整数值。

当字段未填充时，单元格带有[**双值**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue)或者[**浮点值**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)抛出异常。

还可以使用以下命令检查单元格中包含的数据类型[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**类型**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type)财产。事实上，[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**类型**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type)属性是基于[**单元格值类型**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)下面列出了其预定义值的枚举：

|**Cell 值类型**|**描述**|
| :- | :- |
|为布尔值|指定单元格值为布尔值。|
|是日期时间|指定单元格值为日期/时间。|
|一片空白|代表一个空白单元格。|
|是数字|指定单元格值为数字。|
|是字符串|指定单元格值是字符串。|
|未知|指定单元格值未知。|

您还可以使用上述预定义的单元格值类型与每个单元格中存在的数据类型进行比较。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

在处理工作表时，用户可以在单元格中添加不同类型的数据。这些数据类型可能包括布尔值、整数、浮点值、文本或日期/时间值。使用 Aspose.Cells，您可以根据单元格的数据类型从单元格中获取适当的值。

{{% /alert %}}

##  **高级主题**
- [访问工作表的 Cells](/cells/zh/net/accessing-cells-of-a-worksheet/)
- [将文本数字数据转换为数字](/cells/zh/net/convert-text-numeric-data-to-number/)
- [创建小计](/cells/zh/net/creating-subtotals/)
- [数据过滤](/cells/zh/net/data-filtering/)
- [数据排序](/cells/zh/net/sort-data-of-excel/)
- [数据验证](/cells/zh/net/data-validation/)
- [从工作表导出数据](/cells/zh/net/export-data-from-worksheet/)
- [查找或搜索数据](/cells/zh/net/find-or-search-data/)
- [获取带格式和不带格式的 Cell 字符串值](/cells/zh/net/get-cell-string-value-with-and-without-formatting/)
- [在 Cell 内添加 HTML 富文本](/cells/zh/net/adding-html-rich-text-inside-the-cell/)
- [将超链接插入 Excel 或 OpenOffice](/cells/zh/net/insert-hyperlinks-to-excel/)
- [将数据导入工作表](/cells/zh/net/import-data-into-worksheet/)
- [如何以及在何处使用枚举器](/cells/zh/net/how-and-where-to-use-enumerators/)
- [以像素为单位测量 Cell 值的宽度和高度](/cells/zh/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [同时读取多个线程中的 Cell 值](/cells/zh/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [单元格名称与行/列索引之间的转换](/cells/zh/net/names-and-indices/)
- [先按行填充数据，然后按列填充数据](/cells/zh/net/populate-data-first-by-row-then-by-column/)
- [保留 Cell 值或范围的单引号前缀](/cells/zh/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [访问并更新Cell的富文本部分](/cells/zh/net/access-and-update-the-portions-of-rich-text-of-cell/)



