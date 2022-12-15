---
title: 将 Excel 表转换为数据范围
type: docs
weight: 10
url: /zh/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

有时您在 Microsoft Excel 中创建了一个表格，并且不想继续使用它附带的表格功能。相反，您想要看起来像桌子的东西。要在不丢失格式的情况下保留表格中的数据，请将表格转换为常规范围的数据。

Aspose.Cells 不支持表和列表对象的 Microsoft Excel 的此功能。

{{% /alert %}}

## **使用 Microsoft Excel**

使用**转换为范围**在不丢失格式的情况下快速将表格转换为范围的功能。在 Microsoft Excel 2007/2010 中：

1. 单击表格中的任意位置以确保活动单元格位于表格列中。

![待办事项：图像_替代_文本](convert-an-excel-table-to-a-range-of-data_1.gif)

1. 在**设计**选项卡，在**工具**分组，点击**转换为范围**.

![待办事项：图像_替代_文本](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

表格转换为区域后，表格功能将不再可用。例如，行标题不再包含排序和筛选箭头，公式中使用的结构化引用（使用表名的引用）变成了常规单元格引用。

{{% /alert %}}

## **使用 Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **使用选项将表转换为范围**

Aspose.Cells 在通过 Table 转换为 Range 时提供了额外的选项[**TableToRange选项**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)班级。这[**TableToRange选项**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)类提供[**最后一行**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)允许您设置表行的最后一个索引的属性。表格格式将保留到指定的行索引，其余格式将被删除。

下面给出的示例代码演示了使用[**TableToRange选项**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)班级。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
