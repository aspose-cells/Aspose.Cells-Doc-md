---
title: 使用范围的边界线创建表
type: docs
weight: 50
url: /zh/java/create-table-by-using-border-lines-for-a-range/
description: 如何使用边框线创建具有范围的表格。 Aspose.Cells for Java 提供了一个简单易用的 API，可用于向范围添加边框。
keywords: create table, range to table, range to table excel, excel range to table, range to table with borders, how to create table from range, convert range to table, excel convert range to table, excel create table, range to table java 
---
{{% alert color="primary" %}}

有时，您想通过为**范围**/**单元格区域**根据您拥有的单元格的地址。您可以使用[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) 方法来创建一系列单元格。这[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) 方法返回一个[**范围**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)目的。您可以创建一个[**风格**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象并相应地指定边框（上、左、下、右）选项。稍后，您可能会得到[**范围**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)并将所需的格式应用于单元格。

{{% /alert %}}

下面的例子展示了如何创建一个[**范围**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)并指定范围单元格的边界线。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

运行上述代码后，我们可以生成包含格式化表格的excel文件；这是文件的屏幕截图。

![待办事项：图像_替代_文本](create-table-by-using-border-lines-for-a-range_1.png)
