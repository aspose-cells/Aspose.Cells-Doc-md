---
title: 保留单引号前缀的单元格值或范围
type: docs
weight: 310
url: /zh/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: 通过Aspose.Cells为Python通过.NET API学习如何保留单元格值或范围的单引号前缀。
keywords: Python Excel库，保留单元格值或范围的单引号前缀，隐藏前导撇号或单引号标记，显示前导撇号或单引号标记
---

## **可能的使用场景**

当您将一些值放入具有前导撇号或单引号标记的单元格中时，Microsoft Excel会隐藏它，但是当您选择该单元格时，在公式栏中会显示前导撇号或单引号，如下面的截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells为Python通过.NET还隐藏前导撇号或单引号，类似于Microsoft Excel，但它将[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)设置为true。 如果您设置单元格的空样式，那么[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)再次变为false。为了处理此问题，Aspose.Cells为Python通过.NET提供了[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)属性，当它设置为false时，[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)根本不会更新，其旧值将被保留。这意味着如果[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)属性的旧值是true，则其将保持为true，如果旧值是false，则其将保持为false。

## **保留单引号前缀的单元格值或范围**

以下示例代码解释了如前所述的[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)属性的用法。请阅读代码内的注释，并查看下面给出的代码的控制台输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **控制台输出**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
