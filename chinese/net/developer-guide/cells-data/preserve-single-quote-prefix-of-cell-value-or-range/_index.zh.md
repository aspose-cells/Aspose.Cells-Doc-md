---
title: 保留 Cell 值或范围的单引号前缀
type: docs
weight: 310
url: /zh/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: 了解如何通过 Aspose.Cells for .NET API 保留 Cell 值或范围的单引号前缀。
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
---
##  **可能的使用场景**

当您在带有前导撇号或单引号的单元格内放入一些值时，Microsoft Excel 会隐藏它，但当您选择该单元格时，它会在公式栏中显示前导撇号或单引号，如以下屏幕截图所示。

![待办事项：图像_替代_文本](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells 还像 Microsoft Excel 一样隐藏前导撇号或单引号，但它设置[**样式.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)作为**真的**对于该单元格。如果你设置单元格的空样式，那么[**样式.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)变成**错误的**再次。为了解决这个问题，Aspose.Cells提供了[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)属性，当它被设置时**false**，则 [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) 根本不会更新，并且保留其旧值。这意味着如果 [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) 属性的旧值是 **true**，则将保持**true**如果旧值是“假”，则它将保持“假”。

##  **保留 Cell 值或范围的单引号前缀**

下面的示例代码解释了其用法[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)属性如前所述。请阅读代码内的注释并查看下面给出的代码的控制台输出以获得更多帮助。

##  **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

##  **控制台输出**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
