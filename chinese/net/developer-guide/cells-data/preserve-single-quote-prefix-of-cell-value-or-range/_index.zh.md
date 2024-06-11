---
title: 保留单引号前缀的单元格值或范围
type: docs
weight: 310
url: /zh/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: 通过 Aspose.Cells for .NET API 学习如何保留单元格值或范围的单引号前缀。
keywords: 保留单元值或范围的前导单引号，隐藏行首撇号或单引号，显示行首撇号或单引号
---

## **可能的使用场景**

当您在单元格中放入具有前导撇号或单引号标记的值时，Microsoft Excel会隐藏它，但当您选择单元格时，它会在公式栏中显示前导撇号或单引号，如下面的屏幕截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells也隐藏行首撇号或单引号，类似于Microsoft Excel，但它将[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)设置为true。如果设置单元格的空样式，则[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)再次变为false。为了解决这个问题，Aspose.Cells提供了[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)属性，当将其设置为false时，[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)根本不更新，其旧值将被保留。这意味着如果[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)属性的旧值为true，它将保持为true，如果旧值为false，它将保持为false。

## **保留单引号前缀的单元格值或范围**

以下示例代码解释了如何使用先前描述的[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)属性。请阅读代码中的注释，并查看下面给定的代码的控制台输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **控制台输出**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
