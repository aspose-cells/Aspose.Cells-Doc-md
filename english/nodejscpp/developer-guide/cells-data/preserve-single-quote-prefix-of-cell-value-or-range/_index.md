---
title: Preserve Single Quote Prefix of Cell Value or Range with Node.js via C++
linktitle: Preserve Single Quote Prefix of Cell Value or Range
type: docs
weight: 310
url: /nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Learn how to Preserve Single Quote Prefix of Cell Value or Range through the Aspose.Cells for Node.js via C++ API.
keywords: Preserve Single Quote Prefix of Cell Value or Range Node.js via C++, Hide leading apostrophe or single quote mark Node.js via C++, Show leading apostrophe or single quote mark Node.js via C++
---

## **Possible Usage Scenarios**

When you put some value inside the cell that has a leading apostrophe or single quote mark, Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in a formula bar as shown in the following screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells also hides the leading apostrophe or single quote like Microsoft Excel but it sets the [**Style.QuotePrefix**](https://reference.aspose.com/cells/nodejs-cpp/style/#QuotePrefix) as **true** for that cell. If you set an empty style of the cell, then [**Style.QuotePrefix**](https://reference.aspose.com/cells/nodejs-cpp/style/#QuotePrefix) becomes **false** again. In order to deal with this issue, Aspose.Cells provides [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#QuotePrefix) property, when it is set **false**, then [**Style.QuotePrefix**](https://reference.aspose.com/cells/nodejs-cpp/style/#QuotePrefix) is not updated at all and its old value is preserved. It means if the old value of [**Style.QuotePrefix**](https://reference.aspose.com/cells/nodejs-cpp/style/#QuotePrefix) property was **true**, it will remain **true** and if the old value was **false**, it will remain **false**.

## **Preserve Single Quote Prefix of Cell Value or Range**

The following sample code explains the usage of [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#QuotePrefix) property as described previously. Please read the comments inside the code and see the console output of the code given below for more help.

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell A1
const cell = ws.getCells().get("A1");

// Put some text in cell, it does not have Single Quote at the beginning
cell.putValue("Text");

// Access style of cell A1
let st = cell.getStyle();

// Print the value of Style.QuotePrefix of cell A1
console.log("Quote Prefix of Cell A1: " + st.getQuotePrefix());

// Put some text in cell, it has Single Quote at the beginning
cell.putValue("'Text");

// Access style of cell A1
st = cell.getStyle();

// Print the value of Style.QuotePrefix of cell A1
console.log("Quote Prefix of Cell A1: " + st.getQuotePrefix());

// Print information about StyleFlag.QuotePrefix property
console.log();
console.log("When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.");
console.log("Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.");
console.log();

// Create an empty style
st = wb.createStyle();

// Create style flag - set StyleFlag.QuotePrefix as false
// It means, we do not want to update the Style.QuotePrefix property of cell A1's style.
let flag = new AsposeCells.StyleFlag();
flag.setQuotePrefix(false);

// Create a range consisting of single cell A1
const rng = ws.getCells().createRange("A1");

// Apply the style to the range
rng.applyStyle(st, flag);

// Access the style of cell A1
st = cell.getStyle();

// Print the value of Style.QuotePrefix of cell A1
// It will print True, because we have not updated the Style.QuotePrefix property of cell A1's style.
console.log("Quote Prefix of Cell A1: " + st.getQuotePrefix());

// Create an empty style
st = wb.createStyle();

// Create style flag - set StyleFlag.QuotePrefix as true
// It means, we want to update the Style.QuotePrefix property of cell A1's style.
flag = new AsposeCells.StyleFlag();
flag.setQuotePrefix(true);

// Apply the style to the range
rng.applyStyle(st, flag);

// Access the style of cell A1
st = cell.getStyle();

// Print the value of Style.QuotePrefix of cell A1
// It will print False, because we have updated the Style.QuotePrefix property of cell A1's style.
console.log("Quote Prefix of Cell A1: " + st.getQuotePrefix());
```

## **Console Output**

{{< highlight javascript >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
