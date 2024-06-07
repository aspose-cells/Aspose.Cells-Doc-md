---
title: 管理 Excel 文件的数据
linktitle: 单元格数据
type: docs
weight: 110
url: /zh/net/view-and-edit-excel-data/
description: 本文介绍了如何使用 Aspose.Cells 库查看和编辑 Excel 文件的数据。
keywords: Aspose.Cells C# 管理 Excel 文件数据，向 Excel 文件添加数据，从 Excel 文件获取数据，如何提高添加数据的效率，管理单元格数据，更新单元格数据，获取单元格数据，插入单元格数据。
---

{{% alert color="primary" %}}

在[访问工作表的单元格](/cells/zh/net/accessing-cells-of-a-worksheet/)中，我们讨论了访问工作表单元格的基本方法。本文章使用其中一种方法将不同类型的数据添加到单元格中。

{{% /alert %}}

## **如何向单元格添加数据**

Aspose.Cells 提供了一个表示 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含了一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问 Excel 文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合中的每个项目代表了一个[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

Aspose.Cells 允许开发人员通过调用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法向工作表的单元格中添加数据。Aspose.Cells 提供了[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法的重载版本，允许开发人员向单元格添加不同类型的数据。使用[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法的这些重载版本，可以向单元格中添加布尔值、字符串、双精度浮点数、整数或日期/时间等值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **如何提高效率**

如果您使用[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法向工作表中输入大量的数据，应当首先按行然后按列向单元格中添加值。这种方法极大地提高了应用程序的效率。

## **如何从单元格检索数据**

Aspose.Cells 提供了一个表示 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含了一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问文件中的工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合中的每个项目代表了一个[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供了几个属性，允许开发人员根据其数据类型从单元格中检索值。

- 返回单元格的字符串值。
- 返回单元格的双精度值。
- 返回单元格的布尔值。
- 返回单元格的日期/时间值。
- 返回单元格的浮点值。
- 返回单元格的整数值。

当字段未填写时，带有[**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue)或[**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)的单元格会引发异常。

还可以使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type)属性检查单元格中包含的数据类型。实际上，[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type)属性基于[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)枚举，其预定义值如下：

|**单元格值类型**|**描述**|
| :- | :- |
|IsBool|指定单元格值为布尔值。|
|IsDateTime|指定单元格值为日期/时间。|
|IsNull|表示空白单元格。|
|IsNumeric|指定单元格值为数字。|
|IsString|指定单元格值为字符串。|
|IsUnknown|指定单元格值为未知。|

您还可以使用上述预定义的单元格值类型与每个单元格中存在的数据类型进行比较。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

在处理工作表时，用户可能会在单元格中添加不同类型的数据。这些数据类型可能包括布尔值、整数、浮点数、文本或日期/时间值。使用Aspose.Cells，您可以根据它们的数据类型从单元格中获取适当的值。

{{% /alert %}}

## **高级主题**
- [访问工作表的单元格](/cells/zh/net/accessing-cells-of-a-worksheet/)
- [将文本数值数据转换为数字](/cells/zh/net/convert-text-numeric-data-to-number/)
- [创建小计](/cells/zh/net/creating-subtotals/)
- [数据过滤](/cells/zh/net/data-filtering/)
- [数据排序](/cells/zh/net/sort-data-of-excel/)
- [数据验证](/cells/zh/net/data-validation/)
- [从工作表导出数据](/cells/zh/net/export-data-from-worksheet/)
- [查找或搜索数据](/cells/zh/net/find-or-search-data/)
- [获取具有和不具有格式的单元格字符串值](/cells/zh/net/get-cell-string-value-with-and-without-formatting/)
- [在单元格中添加HTML富文本](/cells/zh/net/adding-html-rich-text-inside-the-cell/)
- [将超链接插入到Excel或OpenOffice中](/cells/zh/net/insert-hyperlinks-to-excel/)
- [将数据导入工作表](/cells/zh/net/import-data-into-worksheet/)
- [如何及在何处使用枚举器](/cells/zh/net/how-and-where-to-use-enumerators/)
- [以像素为单位测量单元格值的宽度和高度](/cells/zh/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [同时在多个线程中读取单元格值](/cells/zh/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [单元格名称和行/列索引之间的转换](/cells/zh/net/names-and-indices/)
- [首先按行然后按列填充数据](/cells/zh/net/populate-data-first-by-row-then-by-column/)
- [保留单引号前缀的单元格值或范围](/cells/zh/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [访问和更新单元格中的富文本部分](/cells/zh/net/access-and-update-the-portions-of-rich-text-of-cell/)



