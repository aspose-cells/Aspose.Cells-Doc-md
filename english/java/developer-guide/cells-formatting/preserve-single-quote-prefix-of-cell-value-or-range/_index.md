---
title: Preserve Single Quote Prefix of Cell Value or Range
type: docs
weight: 1900
url: /java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **Possible Usage Scenarios**

When you put some value inside the cell that has leading apostrophe or single quote mark, then Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in a formula bar as shown in the following screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells also hides the leading apostrophe or single quote like Microsoft Excel but it sets the [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) as **true** for that cell. If you set an empty style of the cell, then [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) becomes **false** again. In order to deal with this issue, Aspose.Cells provides [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) property, when it is set **false**, then [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) is not updated at all and its old value is preserved. It means if the old value of [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) property was **true**, it will remain true and if the old value was false, it will remain false.

## **Preserve Single Quote Prefix of Cell Value or Range**

The following sample code explains the usage of [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) property as described previously. Please read the comments inside the code and see the console output of the code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Console Output**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}