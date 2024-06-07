---
title: 表格和范围
type: docs
weight: 50
url: /zh/net/tables-and-ranges/
---

## **介绍**

有时您在Microsoft Excel中创建表格，但不希望继续使用它带来的表格功能。 相反，您希望类似表格的东西。为了保留表格中的数据而不丢失格式，将表格转换为常规数据范围。
Aspose.Cells确实支持Microsoft Excel的表格和列表对象的此功能。

## **使用Microsoft Excel**

使用 **转换为范围** 功能快速将表格转换为范围，而不会丢失格式。在Microsoft Excel 2007/2010中：

1. 单击表格中的任何位置，确保活动单元格位于表格列中。
1. 在 **设计** 标签中，单击 **工具** 组中的 **转换为范围**。

## **使用Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

表格转换为范围后，表格功能将不再可用。例如，行标题不再包括排序和过滤箭头，以及在公式中使用的结构引用（使用表名的引用）将变为常规单元格引用。

{{% /alert %}}

## **将表格转换为范围并提供选项**

Aspose.Cells通过[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)类提供了转换表格为范围时的附加选项。 [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)类提供了[**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow)属性，允许您设置表格行的最后索引。 表格格式将保留到指定行索引，其余格式将被删除。

以下示例代码演示了如何使用[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
