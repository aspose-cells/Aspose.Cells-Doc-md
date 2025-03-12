---
title: Copy Page Setup Settings from Source Worksheet into Destination Worksheet with Node.js via C++
linktitle: Copy Page Setup Settings from Source Worksheet into Destination Worksheet
type: docs
weight: 80
url: /nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: This article explains how to use the Node.js API or C++ Library sample code to copy Page Setup settings from a source Worksheet into a destination Worksheet programmatically.
keywords: copy page setup settings Node.js via C++, copy page setup settings to target worksheet Node.js via C++
---

## **Possible Usage Scenarios**

When you add a new sheet to a workbook, it contains the default *Page Setup settings*. There may be times when you need to transfer the settings ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) from one worksheet to another worksheet. This document explains how to copy Page Setup settings from one worksheet to another using Aspose.Cells for Node.js via C++ APIs.

## **Copy Page Setup Settings from Source Worksheet into Destination Worksheet**

The following sample code illustrates how to copy *Page Setup settings* from one worksheet to another using [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-) method. Please see the following sample code and its console output for a reference.

## **Sample Code**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **Console Output**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
