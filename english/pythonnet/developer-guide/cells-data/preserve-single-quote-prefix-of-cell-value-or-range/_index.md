---
title: Preserve Single Quote Prefix of Cell Value or Range
type: docs
weight: 310
url: /python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Learn how to Preserve Single Quote Prefix of Cell Value or Range through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Preserve Single Quote Prefix of Cell Value or Range, Python Hide leading apostrophe or single quote mark, Python Show leading apostrophe or single quote mark
---

## **Possible Usage Scenarios**

When you put some value inside the cell that has leading apostrophe or single quote mark, then Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in a formula bar as shown in the following screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Python via .NET also hides the leading apostrophe or single quote like Microsoft Excel but it sets the [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) as **true** for that cell. If you set an empty style of the cell, then [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) becomes **false** again. In order to deal with this issue, Aspose.Cells for Python via .NET provides [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) property, when it is set **false**, then [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) is not updated at all and its old value is preserved. It means if the old value of [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) property was **true**, it will remain **true** and if the old value was **false**, it will remain **false**.

## **Preserve Single Quote Prefix of Cell Value or Range**

The following sample code explains the usage of [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) property as described previously. Please read the comments inside the code and see the console output of the code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Console Output**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}