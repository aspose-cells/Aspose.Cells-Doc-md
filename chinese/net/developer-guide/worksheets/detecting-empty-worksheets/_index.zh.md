---
title: 检测空工作表
type: docs
weight: 410
url: /zh/net/detecting-empty-worksheets/
---
## **检查填充 Cells**

工作表可以有一个或多个单元格填充值，其中值可以是简单的（文本、数字、日期/时间）或公式或基于公式的值。在这种情况下，很容易检测到给定工作表是否为空。我们只需要检查[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)要么[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)特性。如果上述属性返回零值或正值，这意味着一个或多个单元格已被填充，但是，如果这些属性中的任何一个返回 -1，则表示给定工作表中没有任何单元格被填充。

{{% alert color="primary" %}}

行和列集合具有从零开始的索引，因此第 0 行和第 0 列的单元格表示工作表中的第一个单元格，即 A1。

{{% /alert %}}

## **检查空初始化 Cells**

所有具有值的单元格都会自动初始化，但是，工作表中的单元格可能只应用了格式。在这种情况下，[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)要么[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) properties 将返回 -1，表示没有任何填充值，但使用此方法无法检测到由于单元格格式而初始化的单元格。为了检查工作表是否有空的初始化单元格，建议对从中获取的枚举器使用 IEnumerator.MoveNext 方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。如果 IEnumerator.MoveNext 方法返回**真的**这意味着给定工作表中有一个或多个已初始化的单元格。

## **检查形状**

给定的工作表可能没有任何填充的单元格，但是，它可能包含形状和对象，例如控件、图表、图像等。如果我们需要检查工作表是否包含任何形状，我们可以通过检查[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)财产。任何正值表示工作表中存在形状。

## **编程范例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
