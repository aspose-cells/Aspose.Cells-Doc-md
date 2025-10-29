---
title: 管理Excel文件的数据
linktitle: 单元格数据
type: docs
weight: 110
url: /zh/nodejs-cpp/view-and-edit-excel-data/
description: 本文介绍如何通过C++使用Aspose.Cells库查看和编辑Excel文件的数据
keywords: Aspose.Cells Node.js via C++ 管理Excel文件的数据，向Excel添加数据，从Excel获取数据，如何提高添加数据的效率，管理单元格数据，更新单元格数据，获取单元格数据，插入单元格数据
---

{{% alert color="primary" %}}

在[访问工作表的单元格](/cells/zh/nodejs-cpp/accessing-cells-of-a-worksheet/)中，我们讨论了访问工作表中单元格的基本方法。本文使用其中一种方法向单元格添加不同类型的数据。

{{% /alert %}}

## **如何向单元格添加数据**

Aspose.Cells for Node.js via C++提供一个类，[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，用于表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，可以访问文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供一个[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合，[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合中的每个项目代表[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的对象。

Aspose.Cells允许开发者通过调用[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的[**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)方法向工作表中的单元格添加数据。Aspose.Cells提供了[**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)方法的重载版本，允许开发者向单元格添加不同类型的数据。使用这些重载版本的[**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)方法，可以向单元格添加布尔值、字符串、双精度、整数或日期/时间等值。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **如何提高效率**

如果你使用[**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)方法将大量数据放入工作表，应该先按行、再按列向单元格添加值。这种方法极大地提高了应用程序的效率。

## **如何从单元格中检索数据**

Aspose.Cells for Node.js via C++提供一个类，[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，用于表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，可以访问文件中的工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供一个[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合，[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合中的每个项目代表[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的对象。

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类提供了多个属性，允许开发者根据数据类型从单元格中检索值。这些属性包括：

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)：返回单元格的字符串值。
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--)：返回单元格的双精度值。
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--)：返回单元格的布尔值。
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--)：返回单元格的日期/时间值。
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--)：返回单元格的浮点值。
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--)：返回单元格的整数值。

当字段未填充时，[**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--)或[**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--)的单元格会抛出异常。

还可以通过使用[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的[**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--)方法检查单元格中包含的数据类型。实际上，[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的[**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--)方法基于以下列出的一组预定义值的[**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype)枚举：

|**单元格值类型**|**描述**|
| :- | :- |
|IsBool|指定单元格值为布尔类型。|
|IsDateTime|指定单元格值为日期/时间类型。|
|IsNull|表示空白单元格。|
|IsNumeric|指定单元格值为数值类型。|
|IsString|指定单元格值为字符串类型。|
|IsUnknown|指定单元格值为未知类型。|

您还可以使用上述预定义的单元格值类型与每个单元格中存在的数据类型进行比较。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

在操作工作表时，用户可能在单元格中添加不同类型的数据。这些数据类型可能包括布尔值、整数、浮点数、文本或日期/时间值。使用Aspose.Cells，可以根据数据类型获取相应的单元格值。

{{% /alert %}}

## **高级主题**
- [访问工作表的单元格](/cells/zh/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [将文本数值数据转换为数字](/cells/zh/nodejs-cpp/convert-text-numeric-data-to-number/)
- [创建小计](/cells/zh/nodejs-cpp/creating-subtotals/)
- [数据筛选](/cells/zh/nodejs-cpp/data-filtering/)
- [数据排序](/cells/zh/nodejs-cpp/sort-data-of-excel/)
- [数据有效性](/cells/zh/nodejs-cpp/data-validation/)
- [查找或搜索数据](/cells/zh/nodejs-cpp/find-or-search-data/)
- [获取有格式和无格式的单元格字符串值](/cells/zh/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [在单元格内添加HTML富文本](/cells/zh/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [在Excel或OpenOffice中插入超链接](/cells/zh/nodejs-cpp/insert-hyperlinks-to-excel/)
- [如何在何处使用枚举器](/cells/zh/nodejs-cpp/how-and-where-to-use-enumerators/)
- [以像素为单位测量单元格值的宽度和高度](/cells/zh/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [同时读取多个线程中的单元格值](/cells/zh/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [单元格名称和行/列索引之间的转换](/cells/zh/nodejs-cpp/names-and-indices/)
- [首先按行，然后按列填充数据](/cells/zh/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [保留单引号前缀的单元格值或范围](/cells/zh/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [访问和更新单元格的富文本部分](/cells/zh/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="nodejs-cpp" >}}
