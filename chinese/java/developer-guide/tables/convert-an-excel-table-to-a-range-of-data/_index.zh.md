---
title: 将Excel表转换为数据范围
type: docs
weight: 10
url: /zh/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

有时您在Microsoft Excel中创建一个表格，但不想继续使用它带来的表格功能。相反，您想要看起来像表格的东西。为了在不丢失格式的情况下保留表格中的数据，可以将表格转换为普通数据范围。

Aspose.Cells确实支持Microsoft Excel中的表格和列表对象的此功能。

{{% /alert %}}

## **使用Microsoft Excel**

使用**转换为范围**功能快速将表格转换为常规数据范围，而不丢失格式。在Microsoft Excel 2007/2010中：

1. 单击表中的任意位置，确保活动单元格位于表列中。

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. 在**设计**选项卡的**工具**组中，单击**转换为范围**。

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

表格在转换为范围后将不再可用其表格功能。例如，行标头不再包含排序和筛选箭头，以及在公式中使用的结构引用（使用表名称的引用）会变成常规单元格引用。

{{% /alert %}}

## **使用Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **使用选项将表格转换为范围**

Aspose.Cells在通过[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)类转换表格为数据范围时提供了额外选项。[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)类提供了[**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)属性，允许您设置表格行的最后索引。表格的格式将保留到指定的行索引，其余的格式将被移除。

以下给出的示例代码演示了[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)类的使用。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
