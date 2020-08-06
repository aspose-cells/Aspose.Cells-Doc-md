---
title : "Preserve Single Quote Prefix of Cell Value or Range" 
description : "" 
weight : 12182 
toc : false
type: docs
url: /java/developerguide/data/preserve+single+quote+prefix+of+cell+value+or+range/
---

# Aspose.Cells for Java : Preserve Single Quote Prefix of Cell Value or Range


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Preserve Single Quote Prefix of Cell Value or Range](#preserve-single-quote-prefix-of-cell-value-or-range)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

When you put some value inside the cell that has leading apostrophe or single quote mark, then Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in a formula bar as shown in the following screenshot.

![image](64716824.png)

Aspose.Cells also hides the leading apostrophe or single quote like Microsoft Excel but it sets the [Style.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/style#QuotePrefix) as **true** for that cell. If you set an empty style of the cell, then [Style.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/style#QuotePrefix) becomes **false** again. In order to deal with this issue, Aspose.Cells provides [StyleFlag.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/styleflag#QuotePrefix) property, when it is set **false**, then [StyleFlag.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/styleflag#QuotePrefix) is not updated at all and its old value is preserved. It means if the old value of [Style.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/style#QuotePrefix) property was **true**, it will remain true and if the old value was false, it will remain false.

## Preserve Single Quote Prefix of Cell Value or Range

The following sample code explains the usage of [StyleFlag.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/styleflag#QuotePrefix) property as described previously. Please read the comments inside the code and see the console output of the code given below for more help.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Quote Prefix of Cell A1: false
Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.
Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true
Quote Prefix of Cell A1: false
{{< /code >}}

