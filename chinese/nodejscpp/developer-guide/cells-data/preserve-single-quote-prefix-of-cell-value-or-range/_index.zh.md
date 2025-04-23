---
title: 保留单引号前缀的单元格值或范围
type: docs
weight: 310
url: /zh/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: 学习如何通过Aspose.Cells for Node.js via C++ API保持单元格值或范围的单引号前缀。
keywords: 保持单元格值或范围的单引号前缀，Node.js通过C++隐藏前导撇号或单引号，Node.js通过C++显示前导撇号或单引号
---

## **可能的使用场景**

当您在单元格中放入具有前导撇号或单引号标记的值时，Microsoft Excel会隐藏它，但当您选择单元格时，它会在公式栏中显示前导撇号或单引号，如下面的屏幕截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++还可以像Microsoft Excel一样隐藏前导撇号或单引号，但会将[**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)设为**true**以应用于该单元格。如果将单元格设置为空样式，则[**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--)再次变为**false**。为了解决此问题，Aspose.Cells for Node.js via C++提供了[**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)方法，当设置为**false**时，[**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--)不会被更新，其旧值将被保留。这意味着如果[**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--)的旧值为**true**，将保持**true**，如果旧值为**false**，将保持**false**。

## **保留单引号前缀的单元格值或范围**

以下示例代码说明了此前描述的[**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)方法的用法。请阅读代码中的注释，并查看下面的示例输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **控制台输出**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

