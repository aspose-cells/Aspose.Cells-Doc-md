---
title: 将Excel表转换为数据范围
type: docs
weight: 10
url: /zh/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

有时您在Microsoft Excel中创建表格，但不希望继续使用它带来的表格功能。 相反，您希望类似表格的东西。为了保留表格中的数据而不丢失格式，将表格转换为常规数据范围。

Aspose.Cells 确实支持表格和列表对象的此 Microsoft Excel 功能。

{{% /alert %}}

## **使用Microsoft Excel**

使用 **转换为范围** 功能快速将表格转换为范围，而不会丢失格式。在Microsoft Excel 2007/2010中：

1. 单击表格中的任何位置，确保活动单元格位于表格列中。

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. 在 **设计** 标签中，单击 **工具** 组中的 **转换为范围**。

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

表格转换为范围后，表格功能将不再可用。例如，行标题不再包括排序和过滤箭头，以及在公式中使用的结构引用（使用表名的引用）将变为常规单元格引用。

{{% /alert %}}

## **使用Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **将表格转换为范围并提供选项**

Aspose.Cells 通过 [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) 类提供将表格转换为数据范围的其他选项。 [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) 类提供 [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow) 属性，允许您设置表格行的最后索引。 表格格式将保留到指定的行索引，并且其余的格式将被移除。

以下示例代码演示了如何使用[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)类。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
