---
title: 检测空工作表
type: docs
weight: 410
url: /zh/net/detecting-empty-worksheets/
description: 本文向您展示了如何使用C# API和.NET库以编程方式检测Excel工作簿中的空工作表的代码。
keywords: 检测空工作表C#，查找空的Excel工作表C#
---

## **检查已填充的单元格**

工作表可能有一个或多个填充有值的单元格，其中值可以是简单的（文本、数字、日期/时间）或基于公式的值。在这种情况下，很容易检测给定工作表是否为空。我们只需检查[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)或[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)属性。如果上述属性返回零或正值，这意味着一个或多个单元格已被填充，但是，如果任何属性返回-1，这表示给定工作表中没有填充任何单元格。

{{% alert color="primary" %}}

行和列集合是基于零索引的，因此行0和列0的单元格表示工作表中的第一个单元格，即A1。

{{% /alert %}}

## **检查空的初始化单元格**

所有具有值的单元格都会自动初始化，但是，有可能工作表中有仅应用了格式设置的单元格。在这种情况下，[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)或[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)属性将返回-1，表示没有任何填充的值但是已初始化的单元格。为了检查工作表是否有空的初始化单元格，建议在从[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合获取的枚举器上使用IEnumerator.MoveNext方法。如果IEnumerator.MoveNext方法返回true，则意味着给定的工作表中存在一个或多个初始化的单元格。

## **检查形状**

可能某个工作表没有任何填充的单元格，但是可能包含形状和对象，如控件、图表、图像等。如果需要检查工作表是否包含任何形状，可以通过检查[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)属性进行。任何正值表示工作表中存在形状。

## **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
