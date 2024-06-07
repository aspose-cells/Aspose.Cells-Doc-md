---
title: 保留单引号前缀的单元格值或范围
type: docs
weight: 310
url: /zh/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: 通过Aspose.Cells for .NET API学习如何保留单元格值或范围的单引号前缀。
keywords: 保留单引号前缀的单元格值或范围，隐藏前导撇号或单引号标记，显示前导撇号或单引号标记
---

## **可能的使用场景**

当您将一些值放入具有前导撇号或单引号标记的单元格中时，Microsoft Excel会隐藏它，但是当您选择该单元格时，在公式栏中会显示前导撇号或单引号，如下面的截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells也会隐藏前导撇号或单引号，但它会为该单元格设置[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)为true。如果您设置单元格的空样式，则[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)再次变为false。为了解决这个问题，Aspose.Cells提供了一个[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)属性，当它设置为false时，[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)根本不会更新，它的旧值被保留。这意味着如果[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)属性的旧值为true，则它将保持不变，并且如果旧值为false，则它将保持不变。

## **保留单引号前缀的单元格值或范围**

以下示例代码解释了如前所述的[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)属性的用法。请阅读代码内的注释，并查看下面给出的代码的控制台输出以获取更多帮助。

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
