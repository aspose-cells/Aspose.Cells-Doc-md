---
title: 保留单引号前缀的单元格值或范围
type: docs
weight: 1900
url: /zh/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **可能的使用场景**

当您在单元格中放入具有前导撇号或单引号标记的值时，Microsoft Excel会隐藏它，但当您选择单元格时，它会在公式栏中显示前导撇号或单引号，如下面的屏幕截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells也会隐藏前导撇号或单引号，但它将**[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)**设置为**true**，以表示该单元格。如果您设置单元格的空样式，则**[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)**再次变为**false**。为了解决此问题，Aspose.Cells提供了**[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)**属性，当其设置为**false**时，**[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)**根本不会更新，其旧值将被保留。这意味着**[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)**属性的旧值如果为**true**，它将保持不变；如果旧值为false，它将保持不变。

## **保留单引号前缀的单元格值或范围**

以下示例代码解释了之前所描述的**[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)**属性的用法。请阅读代码中的注释，并查看下面给出的代码的控制台输出，以获取更多帮助。

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
{{< app/cells/assistant language="java" >}}
