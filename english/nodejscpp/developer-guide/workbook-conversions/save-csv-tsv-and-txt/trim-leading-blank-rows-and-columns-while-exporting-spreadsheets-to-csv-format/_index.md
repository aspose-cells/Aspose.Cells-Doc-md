---
title: Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format with Node.js via C++
linktitle: Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format
type: docs
weight: 100
url: /nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Learn how to trim leading blank rows and columns when exporting spreadsheets to CSV format using Aspose.Cells for Node.js via C++.
---

## **Possible Usage Scenarios**

Sometimes, your Excel or CSV file has leading blank columns or rows. For example, consider this line

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Here the first three cells or columns are blank. When you open such a CSV file in Microsoft Excel, then Microsoft Excel discards these leading blank rows and columns.

By default, Aspose.Cells for Node.js via C++ does not discard leading blank columns and rows on saving but if you want to remove them just like Microsoft Excel does, then Aspose.Cells provides [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn-boolean-) property. Please set it to **true** and then all the leading blank rows and columns will be discarded on saving.

{{% alert color="primary" %}}

Prior to the release of Aspose.Cells for Node.js via C++ 20.4, the default value of [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn-boolean-) was **false**. Since the 20.4 release, the default value of [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn-boolean-) is **true.**

{{% /alert %}}

## **Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format**

The following sample code loads the [source excel file](sampleTrimBlankColumns.xlsx) which has two leading blank columns. It first saves the excel file in CSV format without any changes and then it sets [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn-boolean-) property to **true** and saves it again. The screenshot shows the [source excel file](sampleTrimBlankColumns.xlsx), [output CSV file without trimming](outputWithoutTrimBlankColumns.csv), and the [output CSV file with trimming](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
