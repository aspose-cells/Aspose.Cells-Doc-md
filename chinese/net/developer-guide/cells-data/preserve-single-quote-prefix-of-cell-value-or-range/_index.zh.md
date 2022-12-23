---
title: 保留 Cell 值或范围的单引号前缀
type: docs
weight: 310
url: /zh/net/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **可能的使用场景**

当您在具有前导撇号或单引号的单元格内放置一些值时，Microsoft Excel 会将其隐藏，但当您选择该单元格时，它会在公式栏中显示前导撇号或单引号，如以下屏幕截图所示。

![待办事项：图片_替代_文本](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells 也像 Microsoft Excel 一样隐藏了前导撇号或单引号，但它设置了[**样式.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)作为**真的**对于那个细胞。如果您设置单元格的空样式，则[**样式.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)成为**错误的**再次。为了处理这个问题，Aspose.Cells提供[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)属性，当它被设置时**错误的**， 然后[**样式.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)根本不更新，它的旧值被保留。这意味着如果旧值[**样式.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)财产是**真的** , 它将保留**真的**如果旧值是**错误的** , 它将保留**错误的**.

## **保留 Cell 值或范围的单引号前缀**

下面的示例代码解释了[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)属性如前所述。请阅读代码中的注释并查看下面给出的代码的控制台输出以获得更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **控制台输出**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
