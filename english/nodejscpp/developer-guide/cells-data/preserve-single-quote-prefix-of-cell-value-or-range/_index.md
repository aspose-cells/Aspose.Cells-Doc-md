---
title: Preserve Single Quote Prefix of Cell Value or Range
type: docs
weight: 310
url: /nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Learn how to Preserve Single Quote Prefix of Cell Value or Range through the Aspose.Cells for Node.js via C++ API.
keywords: Preserve Single Quote Prefix of Cell Value or Range Node.js via C++, Hide leading apostrophe or single quote mark Node.js via C++, Show leading apostrophe or single quote mark Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you put some value inside the cell that has leading apostrophe or single quote mark, then Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in a formula bar as shown in the following screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++ also hides the leading apostrophe or single quote like Microsoft Excel but it sets the [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) as **true** for that cell. If you set an empty style of the cell, then [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) becomes **false** again. In order to deal with this issue, Aspose.Cells for Node.js via C++ provides [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) method, when it is set **false**, then [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) is not updated at all and its old value is preserved. It means if the old value of [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) was **true**, it will remain **true** and if the old value was **false**, it will remain **false**.

## **Preserve Single Quote Prefix of Cell Value or Range**

The following sample code explains the usage of [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) method as described previously. Please read the comments inside the code and see the console output of the code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **Console Output**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
