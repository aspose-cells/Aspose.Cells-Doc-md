---  
title: Preserve Single Quote Prefix of Cell Value or Range with Golang via C++  
linktitle: Preserve Single Quote Prefix of Cell Value or Range  
type: docs  
weight: 310  
url: /go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/  
description: Learn how to preserve single quote prefix of cell value or range through the Aspose.Cells for C++ API.  
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark  
---  

## **Possible Usage Scenarios**  

When you put a value inside a cell that has a leading apostrophe or single‑quote mark, Microsoft Excel hides it; however, when you select the cell, the leading apostrophe appears in the formula bar, as shown in the following screenshot.  

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)  

Aspose.Cells also hides the leading apostrophe or single quote like Microsoft Excel, but it sets the [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) property to **true** for that cell. If you apply an empty style to the cell, then **Style.GetQuotePrefix()** becomes **false** again. To address this behavior, Aspose.Cells provides the [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) property. When it is set to **false**, **Style.GetQuotePrefix()** is not updated at all and its previous value is preserved. This means that if the old value of **Style.GetQuotePrefix()** was **true**, it will remain **true**; if it was **false**, it will remain **false**.  

## **Preserve Single Quote Prefix of Cell Value or Range**  

The following sample code explains the usage of the [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/) property as described above. Please read the comments inside the code and see the console output of the code given below for more help.  

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