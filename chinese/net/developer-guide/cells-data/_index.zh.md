---
title: 管理Excel文件的数据
linktitle: 单元格数据
type: docs
weight: 110
url: /zh/net/view-and-edit-excel-data/
description: 本文介绍了如何使用Aspose.Cells库查看和编辑Excel文件的数据。
keywords: Aspose.Cells C#管理Excel文件的数据，向Excel文件添加数据，从Excel文件获取数据，如何提高添加数据的效率，管理单元格数据，更新单元格数据，获取单元格数据，插入单元格数据
---

{{% alert color="primary" %}}

在 [访问工作表的单元格](/cells/zh/net/accessing-cells-of-a-worksheet/) 中，我们讨论了访问工作表中单元格的基本方法。本文使用这些方法之一来向单元格添加不同类型的数据。

{{% /alert %}}

## **如何向单元格添加数据**

Aspose.Cells提供了一个表示Microsoft Excel文件的 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合。 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合中的每个项目都表示 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的对象。

Aspose.Cells允许开发人员通过调用 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的 [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 方法向工作表中的单元格添加数据。Aspose.Cells提供 [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 方法的重载版本，使开发人员可以向单元格添加不同类型的数据。使用 [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 方法的这些重载版本，可以将布尔值、字符串、双精度、整数或日期/时间等值添加到单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **如何提高效率**

如果您使用[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法向工作表添加大量数据，应先按行然后按列添加值到单元格。这种方法极大地提高了应用程序的效率。

## **如何从单元格中检索数据**

Aspose.Cells提供一个代表Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问文件中的工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合中的每个项代表[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供了几个属性，允许开发人员根据其数据类型从单元格中检索值。这些属性包括：

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue)：返回单元格的字符串值。
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue)：返回单元格的双精度值。
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue)：返回单元格的布尔值。
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue)：返回单元格的日期/时间值。
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)：返回单元格的浮点值。
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)：返回单元格的整数值。

当字段未填写时，具有[**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) 或[**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) 的单元格会引发异常。

还可以通过使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的[**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) 属性来检查单元格中包含的数据类型。 实际上，[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的[**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) 属性基于[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype) 枚举，其预定义值如下：

|**单元格值类型**|**描述**|
| :- | :- |
|IsBool|指定单元格值为布尔类型。|
|IsDateTime|指定单元格值为日期/时间类型。|
|IsNull|表示空白单元格。|
|IsNumeric|指定单元格值为数值类型。|
|IsString|指定单元格值为字符串类型。|
|IsUnknown|指定单元格值为未知类型。|

您还可以使用上述预定义的单元格值类型与每个单元格中存在的数据类型进行比较。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

在处理工作表时，用户可能在单元格中添加不同类型的数据。这些数据类型可能包括布尔值、整数、浮点、文本或日期/时间值。使用Aspose.Cells，您可以根据它们的数据类型从单元格中获取适当的值。

{{% /alert %}}

## **高级主题**
- [访问工作表的单元格](/cells/zh/net/accessing-cells-of-a-worksheet/)
- [将文本数值数据转换为数字](/cells/zh/net/convert-text-numeric-data-to-number/)
- [创建小计](/cells/zh/net/creating-subtotals/)
- [数据筛选](/cells/zh/net/data-filtering/)
- [数据排序](/cells/zh/net/sort-data-of-excel/)
- [数据有效性](/cells/zh/net/data-validation/)
- [从工作表导出数据](/cells/zh/net/export-data-from-worksheet/)
- [查找或搜索数据](/cells/zh/net/find-or-search-data/)
- [获取有格式和无格式的单元格字符串值](/cells/zh/net/get-cell-string-value-with-and-without-formatting/)
- [在单元格内添加HTML富文本](/cells/zh/net/adding-html-rich-text-inside-the-cell/)
- [在Excel或OpenOffice中插入超链接](/cells/zh/net/insert-hyperlinks-to-excel/)
- [将数据导入工作表](/cells/zh/net/import-data-into-worksheet/)
- [如何在何处使用枚举器](/cells/zh/net/how-and-where-to-use-enumerators/)
- [以像素为单位测量单元格值的宽度和高度](/cells/zh/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [同时读取多个线程中的单元格值](/cells/zh/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [单元格名称和行/列索引之间的转换](/cells/zh/net/names-and-indices/)
- [首先按行，然后按列填充数据](/cells/zh/net/populate-data-first-by-row-then-by-column/)
- [保留单引号前缀的单元格值或范围](/cells/zh/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [访问和更新单元格的富文本部分](/cells/zh/net/access-and-update-the-portions-of-rich-text-of-cell/)



{{< app/cells/assistant language="csharp" >}}
