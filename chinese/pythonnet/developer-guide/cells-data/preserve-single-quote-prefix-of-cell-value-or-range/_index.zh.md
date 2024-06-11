---
title: 保留单引号前缀的单元格值或范围
type: docs
weight: 310
url: /zh/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: 学习如何通过Aspose.Cells for Python via .NET API保存单引号前缀的单元格值或范围。
keywords: Python Excel库，Python保存单引号前缀的单元格值或范围，Python隐藏前导撇号或单引号标记，Python显示前导撇号或单引号标记
---

## **可能的使用场景**

当您在单元格中放入具有前导撇号或单引号标记的值时，Microsoft Excel会隐藏它，但当您选择单元格时，它会在公式栏中显示前导撇号或单引号，如下面的屏幕截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Python via .NET也隐藏前导撇号或单引号，就像Microsoft Excel一样，但它将[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)设置为**true**以用于该单元格。如果您设置一个空的单元格样式，则[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)再次变为**false**。为了解决这个问题，Aspose.Cells for Python via .NET提供了[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)属性，当它设置为**false**时，[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)根本不被更新，它的旧值被保留。这意味着如果[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)属性的旧值为**true**，它将保持为**true**，如果旧值为**false**，它将保持为**false**。

## **保留单引号前缀的单元格值或范围**

以下示例代码解释了如何使用先前描述的[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)属性。请阅读代码中的注释，并查看下面给定的代码的控制台输出以获取更多帮助。

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
