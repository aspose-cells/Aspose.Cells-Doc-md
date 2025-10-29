---
title: 保留单元格值或范围的单引号前缀，使用Golang通过C++
linktitle: 保留单引号前缀的单元格值或范围
type: docs
weight: 310
url: /zh/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: 学习如何通过Aspose.Cells for C++ API保持单元格值或范围的单引号前缀。
keywords: 保留单元值或范围的前导单引号，隐藏行首撇号或单引号，显示行首撇号或单引号
---

## **可能的使用场景**

当你在单元格中放入带前导撇号或单引号的值时，Excel会隐藏它，但在选中该单元格时，公式栏会显示出前导撇号或单引号，如下截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells 同样会像Excel一样隐藏前导撇号，但会将[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)设置为**true**以示该单元格已保存此属性。如果将单元格设置为空样式，则[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)变为**false**。为处理此问题，Aspose.Cells提供了[**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/)属性。当它设为**false**时，[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)不会被更新，原有值会被保留。这意味着，如果[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)属性的旧值为**true**，它会保持为**true**；如果旧值为**false**，则保持不变。

## **保留单引号前缀的单元格值或范围**

下面的示例代码演示了前面描述的[**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/)属性的用法。请阅读代码中的注释，并查看以下代码的控制台输出以获得更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **控制台输出**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
