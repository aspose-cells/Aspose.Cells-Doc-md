---
title: Preserve Single Quote Prefix of Cell Value or Range
type: docs
weight: 310
url: /python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Learn how to preserve the single‑quote prefix of a cell value or range using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Preserve Single Quote Prefix of Cell Value or Range, Python Hide leading apostrophe or single quote mark, Python Show leading apostrophe or single quote mark
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you put a value inside a cell that has a leading apostrophe or single‑quote mark, Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in the formula bar, as shown in the following screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Python via .NET also hides the leading apostrophe or single quote like Microsoft Excel, but it sets the [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) property to **true** for that cell. If you apply an empty style to the cell, then [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) becomes **false** again. To address this, Aspose.Cells for Python via .NET provides the [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) property; when it is set to **false**, the property is not updated and its previous value is preserved. That means if the previous value of [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) was **true**, it will remain **true**, and if it was **false**, it will remain **false**.

## **Preserve Single Quote Prefix of Cell Value or Range**

The following sample code explains the usage of the [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) property as described previously. Please read the comments inside the code and see the console output below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Console Output**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
