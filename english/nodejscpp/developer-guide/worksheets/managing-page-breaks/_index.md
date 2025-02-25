---
title: Managing Page Breaks with Node.js via C++
linktitle: Managing Page Breaks
type: docs
weight: 30
url: /nodejs-cpp/managing-page-breaks/
description: This article provides sample code and explains how to add, clear, or delete specific page breaks in Excel worksheets programmatically using Aspose.Cells for Node.js via C++.
keywords: page breaks Node.js via C++, excel page breaks Node.js via C++, clear page break Node.js via C++, delete specific page break Node.js via C++
---

{{% alert color="primary" %}}

According to the definition, a page break is a place in a flow of text where one page ends and the next begins. Microsoft Excel lets users add page breaks into any selected cell of a worksheet.

The location of the cell where the page break is added, the page is ended and the rest of the data after the page break is printed on the next page while printing. In simple words, page breaks divide your worksheet into multiple pages according to your specifications. You can also add page breaks to your worksheets at runtime using Aspose.Cells. Aspose.Cells allows developers to add two kinds of page breaks:

- Horizontal page break
- Vertical page break

In the rest of the discussion, we will describe how can you add horizontal or vertical page breaks into your worksheets using Aspose.Cells.

{{% /alert %}}

## **Page Breaks**

Aspose.Cells provides a [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods used to manage a worksheet.

To add the page breaks, use the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class' [**horizontalPageBreaks**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#horizontalPageBreaks) and [**verticalPageBreaks**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#verticalPageBreaks) properties.

The [**horizontalPageBreaks**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#horizontalPageBreaks) and [**verticalPageBreaks**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#verticalPageBreaks) properties are collections that may contain several page breaks. Each collection contains several methods for managing horizontal and vertical page breaks.

### **Adding Page Breaks**

To add a page break in a worksheet, insert vertical and horizontal page breaks at the specified cell by calling the [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/methods/add) and [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/methods/add) methods. Each **add** method takes the name of the cell where the break should be added.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

In page break preview or print preview modes, you can see how these page breaks work.

{{% /alert %}}

### **Clearing All Page Breaks**

To clear all page breaks in a worksheet, call the [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection) and [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection) collections' [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/methods/clear) methods.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Clearing all page breaks
workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear();
workbook.getWorksheets().get(0).getVerticalPageBreaks().clear();

// Save the Excel file.
workbook.save(path.join(dataDir, "ClearAllPageBreaks_out.xls"));
```

### **Removing Specific Page Break**

To remove a specific page break, call the [**HorizontalPageBreakCollection.removeAt()**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/methods/removeAt) and [**VerticalPageBreakCollection.removeAt()**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/methods/removeAt) methods. Each **removeAt** method takes the index of the page break about to be removed.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **Important to know**

When you set **fitToPages** properties (that is [**fitToPagesTall**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#fitToPagesTall) and [**fitToPagesWide**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#fitToPagesWide)) in page setup settings, the page break settings are affected, so, if you print the worksheet, the page break settings are not considered although they are still set.
