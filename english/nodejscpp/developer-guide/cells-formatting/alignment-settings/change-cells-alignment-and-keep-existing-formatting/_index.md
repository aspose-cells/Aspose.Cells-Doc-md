---
title: Change Cells Alignment and Keep Existing Formatting with Node.js via C++
linktitle: Change Cells Alignment and Keep Existing Formatting
description: Use the Aspose.Cells library to change cell alignment and preserve existing formatting in Node.js via C++
keywords: Aspose.Cells, Node.js via C++, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Possible Usage Scenarios**

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells for Node.js via C++ allows you to do it using the [**StyleFlag.Alignments**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#alignments) property. If you will set it **true**, changes in alignment will take place otherwise not. Please note, [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) object is passed as a parameter to the [**Range.applyStyle()**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-styles-styleflag-) method which actually applies the formatting to a range of cells.

## **Change Cells Alignment and Keep Existing Formatting**

The following sample code loads the [sample Excel file](67338585.xlsx), creates the range and center aligns it horizontally and vertically and keeps the existing formatting intact. The following screenshot compares the sample Excel file and [output Excel file](67338586.xlsx) and shows that all existing formatting of the cells is the same except that cells are now center aligned horizontally and vertically.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing cells with formatting.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Create cells range.
const range = worksheet.getCells().createRange("B2:D7");

// Create style object.
const style = workbook.createStyle();

// Set the horizontal and vertical alignment to center.
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Create style flag object.
const flag = new AsposeCells.StyleFlag();
flag.setAlignments(true); // Set style flag alignments true. It is most crucial statement.

// Apply style to range of cells.
range.applyStyle(style, flag);

// Save the workbook in XLSX format.
workbook.save(path.join(outputDir, "outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
