---
title: 保留单引号前缀的单元格值或范围
type: docs
weight: 1900
url: /zh/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **可能的使用场景**

当您将一些值放入具有前导撇号或单引号标记的单元格中时，Microsoft Excel会隐藏它，但是当您选择该单元格时，在公式栏中会显示前导撇号或单引号，如下面的截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells 还隐藏前导撇号或单引号，类似于 Microsoft Excel，但设置为 [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) 为 **true**。如果设置单元格的空样式，则 [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) 再次变为 **false**。为了解决这个问题，Aspose.Cells 提供了 [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) 属性，当它设置为 **false** 时， [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) 就完全不更新，它的旧值会被保留。这意味着如果 [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) 属性的旧值为 **true**，它将保持为 true，如果旧值为 false，则将保持为 false。

## **保留单引号前缀的单元格值或范围**

下面的示例代码解释了之前描述的 [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) 属性的用法。请阅读代码内的注释，并查看下面给出的代码的控制台输出，以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **控制台输出**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
