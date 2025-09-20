---
title: Preserve Single Quote Prefix of Cell Value or Range with Golang via C++
linktitle: Preserve Single Quote Prefix of Cell Value or Range
type: docs
weight: 310
url: /go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Learn how to Preserve Single Quote Prefix of Cell Value or Range through the Aspose.Cells for C++ API.
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
---

## **Possible Usage Scenarios**

When you put some value inside the cell that has a leading apostrophe or single quote mark, then Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in the formula bar as shown in the following screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells also hides the leading apostrophe or single quote like Microsoft Excel but it sets the [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) as **true** for that cell. If you set an empty style of the cell, then [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) becomes **false** again. In order to deal with this issue, Aspose.Cells provides [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) property, when it is set **false**, then [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) is not updated at all and its old value is preserved. It means if the old value of [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) property was **true**, it will remain **true** and if the old value was **false**, it will remain **false**.

## **Preserve Single Quote Prefix of Cell Value or Range**

The following sample code explains the usage of [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/) property as described previously. Please read the comments inside the code and see the console output of the code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **Console Output**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}