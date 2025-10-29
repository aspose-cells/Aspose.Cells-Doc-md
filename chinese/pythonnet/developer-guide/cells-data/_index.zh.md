---
title: 管理Excel文件的数据
linktitle: 单元格数据
type: docs
weight: 110
url: /zh/python-net/view-and-edit-excel-data/
description: 本文介绍了如何使用Aspose.Cells for Python via .NET库查看和编辑Excel文件的数据。
keywords: Python Excel库，Aspose.Cells for Python管理Excel文件的数据，Python向Excel文件添加数据，Python从Excel文件获取数据，Python如何提高添加数据的效率，Python管理单元格数据，Python更新单元格数据，Python获取单元格数据，Python插入单元格数据。
---

{{% alert color="primary" %}}

在[访问工作表的单元格](/cells/zh/python-net/accessing-cells-of-a-worksheet/)中，我们讨论了访问工作表中单元格的基本方法。本文使用其中一种方法向单元格中添加不同类型的数据。

{{% /alert %}}

## **如何向单元格添加数据**

Aspose.Cells for Python via .NET提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)集合，用于访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)集合。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)集合中的每个项目表示[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的对象。

Aspose.Cells for Python via .NET允许开发人员通过调用[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool)方法向工作表中的单元格添加数据。Aspose.Cells for Python via .NET提供了[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)方法的重载版本，让开发人员可以向单元格添加不同类型的数据。使用[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)方法的这些重载版本，可以向单元格添加布尔值、字符串、双精度、整数或日期/时间等值。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **如何提高效率**

如果您使用[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)方法向工作表添加大量数据，应先按行然后按列添加值到单元格。这种方法极大地提高了应用程序的效率。

## **如何从单元格中检索数据**

Aspose.Cells for Python via .NET提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，该类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)集合，允许访问文件中的工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了一个[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)集合。该集合中的每个项目表示[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的对象。

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类提供了几个属性，允许开发人员根据其数据类型从单元格中检索值。这些属性包括：

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/)：返回单元格的字符串值。
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/)：返回单元格的双精度值。
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/)：返回单元格的布尔值。
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/)：返回单元格的日期/时间值。
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/)：返回单元格的浮点值。
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/)：返回单元格的整数值。

当字段未填写时，具有[**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) 或[**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) 的单元格会引发异常。

还可以通过使用[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类的[**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) 属性来检查单元格中包含的数据类型。 实际上，[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类的[**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) 属性基于[**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype) 枚举，其预定义值如下：

|**单元格值类型**|**描述**|
| :- | :- |
|IS_BOOL|指定单元格值为布尔值。
|IS_DATE_TIME|指定单元格值为日期/时间。
|IS_NULL|表示空白单元格。
|IS_NUMERIC|指定单元格值为数字。
|IS_STRING|指定单元格值为字符串。
|IS_ERROR|指定单元格值为错误值。
|IS_UNKNOWN|指定单元格值为未知。

您还可以使用上述预定义的单元格值类型与每个单元格中存在的数据类型进行比较。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

在处理工作表时，用户可能在单元格中添加不同类型的数据。 这些数据类型可能包括布尔值，整数，浮点数，文本或日期/时间值。 使用Aspose.Cells for Python via .NET，您可以根据其数据类型从单元格中获取相应的值。

{{% /alert %}}

## **高级主题**
- [访问工作表的单元格](/cells/zh/python-net/accessing-cells-of-a-worksheet/)
- [将文本数值数据转换为数字](/cells/zh/python-net/convert-text-numeric-data-to-number/)
- [创建小计](/cells/zh/python-net/creating-subtotals/)
- [数据筛选](/cells/zh/python-net/data-filtering/)
- [数据排序](/cells/zh/python-net/sort-data-of-excel/)
- [数据有效性](/cells/zh/python-net/data-validation/)
- [获取有格式和无格式的单元格字符串值](/cells/zh/python-net/get-cell-string-value-with-format-strategy/)
- [在单元格内添加HTML富文本](/cells/zh/python-net/adding-html-rich-text-inside-the-cell/)
- [查找或搜索数据](/cells/zh/python-net/find-or-search-data/)
- [在Excel或OpenOffice中插入超链接](/cells/zh/python-net/insert-hyperlinks-to-excel/)
- [以像素为单位测量单元格值的宽度和高度](/cells/zh/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [单元格名称和行/列索引之间的转换](/cells/zh/python-net/names-and-indices/)
- [首先按行，然后按列填充数据](/cells/zh/python-net/populate-data-first-by-row-then-by-column/)
- [保留单引号前缀的单元格值或范围](/cells/zh/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [访问和更新单元格的富文本部分](/cells/zh/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="python-net" >}}
