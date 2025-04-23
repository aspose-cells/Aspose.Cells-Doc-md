---
title: 检测空工作表
type: docs
weight: 410
url: /zh/net/detecting-empty-worksheets/
description: 本文向您展示了如何使用C# API和.NET库以编程方式检测Excel工作簿的空工作表的代码。
keywords: 检测空工作表C#，查找空的Excel工作表C#
---

## **检查已填充的单元格**

工作表中可以填充一个或多个单元格的值，其中值可以是简单的（文本、数字、日期/时间）或公式或基于公式的值。在这种情况下，很容易检测给定工作表是否为空。我们只需检查[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)或[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)属性。如果上述属性返回零或正值，那么表示一个或多个单元格已被填充，但如果其中任何一个属性返回-1，那就表示给定工作表中没有填充任何单元格。

{{% alert color="primary" %}}

行和列的集合具有从零开始的索引，因此行0和列0的单元格表示工作表中的第一个单元格，即A1。

{{% /alert %}}

## **检测空初始化单元格**

所有具有值的单元格都会自动初始化，但有可能工作表只有应用了格式的单元格。在这种情况下，[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)或[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)属性将返回-1，表示没有填充任何值，但由于单元格格式化而初始化的单元格无法使用此方法进行检测。为了检查工作表是否有已初始化的空单元格，建议在从[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合中获取的枚举器上使用IEnumerator.MoveNext方法。如果IEnumerator.MoveNext方法返回true，那么表示给定工作表中有一个或多个已初始化的单元格。

## **检查形状**

可能存在一个工作表中没有填充的单元格，但它可能包含形状和对象，如控件、图表、图像等。如果我们需要检查一个工作表是否包含任何形状，可以通过检查[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)属性来实现。任何正值都表示在工作表中存在形状。

## **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
