---
title: 检测空工作表
type: docs
weight: 710
url: /zh/java/detecting-empty-worksheets/
---

## **检查已填充的单元格**
工作表可以具有一个或多个填充值的单元格，其中值可以是简单的（文本、数字、日期/时间）或公式或基于公式的值。在这种情况下，很容易检测给定工作表是否为空。我们需要检查的是 [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) 或 [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) 属性。如果上述属性返回零或正值，则意味着一个或多个单元格已填充，但是，如果其中任何一个属性返回-1，则表明给定工作表中没有填充单元格。

{{% alert color="primary" %}} 

行和列集合具有从零开始的索引，因此，行为 0 列为 0 意味着工作表中的第一个单元格，即 A1。

{{% /alert %}} 
## **检测空初始化单元格**
所有具有值的单元格都会自动初始化，但是有可能工作表只有应用格式的单元格。在这种情况下，[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) 或 [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) 属性将返回-1，表明没有填充值，但由于单元格格式化而初始化的单元格无法使用此方法检测。为了检查工作表是否有空初始化的单元格，建议使用从 Cells 集合获取的迭代器的 *Iterator.hasNext* 方法。如果 *iterator.hasNext* 方法返回 true，则意味着给定工作表中有一个或多个初始化的单元格。

{{% alert color="primary" %}} 

有多种方式可以获得单元格枚举器，详见[如何和何地使用迭代器](/cells/zh/java/how-and-where-to-use-iterators/)。

{{% /alert %}} 
## **检查形状**
可能某个给定的工作表没有填充单元格，但是它可能包含形状和对象，如控件、图表、图像等。如果我们需要检查工作表是否包含任何形状，可以通过检查 [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count) 属性来进行。任何正值表示工作表中存在形状。
## **编程示例**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}
