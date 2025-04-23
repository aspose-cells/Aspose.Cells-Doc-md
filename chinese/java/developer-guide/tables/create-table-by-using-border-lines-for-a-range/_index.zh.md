---
title: 使用边框线创建范围的表格
type: docs
weight: 50
url: /zh/java/create-table-by-using-border-lines-for-a-range/
description: 如何通过使用边框线创建范围的表。Aspose.Cells for Java 提供了一个简单易用的 API，可用于向范围添加边框。
keywords: 创建表格，范围转表格，范围转表格excel，excel范围转表格，带边框的范围转表格，如何从范围创建表格，转换范围为表格，excel转换范围为表格，excel创建表格，范围转表格java 
---

{{% alert color="primary" %}}

有时，您希望根据您拥有的单元格地址为**Range**/**CellArea**添加边框线创建表。您可以使用[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-)方法创建一系列单元格。[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-)方法返回一个[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)对象。您可以创建一个[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象，并据此规定上、左、下、右的边框选项。稍后，您可以获取[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)的单元格，并对单元格应用您期望的格式。

{{% /alert %}}

以下示例演示如何创建一个[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)并为范围单元格指定边框线。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

运行以上代码后，我们可以得到包含格式化表格的生成的Excel文件；以下是文件的屏幕截图。

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
{{< app/cells/assistant language="java" >}}
