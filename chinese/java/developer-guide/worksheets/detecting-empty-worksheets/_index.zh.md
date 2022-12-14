---
title: 检测空工作表
type: docs
weight: 710
url: /zh/java/detecting-empty-worksheets/
---
## **检查填充 Cells**
工作表可以有一个或多个单元格填充值，其中值可以是简单的（文本、数字、日期/时间）或公式或基于公式的值。在这种情况下，很容易检测到给定工作表是否为空。我们只需要检查[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow)或者[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)特性。如果上述属性返回零值或正值，则表示已填充一个或多个单元格，但是，如果这些属性中的任何一个返回 -1，则表示给定工作表中未填充任何单元格。

{{% alert color="primary" %}} 

行和列集合具有从零开始的索引，因此，第 0 行和第 0 列的单元格表示工作表中的第一个单元格，即 A1。

{{% /alert %}} 
## **检查空初始化 Cells**
所有具有值的单元格都会自动初始化，但是，工作表中的单元格可能只应用了格式。在这种情况下，[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow)或者[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)properties 将返回 -1，表示没有任何填充值，但使用此方法无法检测到由于单元格格式而初始化的单元格。为了检查工作表是否有空的初始化单元格，建议使用*迭代器.hasNext*从 Cells 集合获取的迭代器上的方法。如果*迭代器.hasNext*方法返回 true 那么这意味着在给定的工作表中有一个或多个已初始化的单元格。

{{% alert color="primary" %}} 

有许多方法可以获取细胞枚举器，详见[如何以及在何处使用迭代器](/cells/zh/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **检查形状**
给定的工作表可能没有任何填充的单元格，但是，它可能包含形状和对象，例如控件、图表、图像等。如果我们需要检查工作表是否包含任何形状，我们可以通过检查[ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count)财产。任何正值表示工作表中存在形状。
## **编程范例**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
