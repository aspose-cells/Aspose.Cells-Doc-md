---
title: Setting Print Options with Node.js via C++
linktitle: Setting Print Options
type: docs
weight: 40
url: /nodejs-cpp/setting-print-options/
description: This article demonstrates how to programmatically set the Print Options of the Excel Worksheet Page Setup feature using the Node.js API and C++ Library. You can set the Print Area, Print Titles, and Page Order.
keywords: set excel print area Node.js via C++, set excel print titles Node.js via C++, set excel page order Node.js via C++
---

{{% alert color="primary" %}}

Microsoft Excel's page setup settings provide several print options (also referred to as sheet options) that allow users to control how worksheet pages are printed.

{{% /alert %}}

## **Setting Print Options**

These print options allow users to:

- Select a specific print area on a worksheet.
- Print titles.
- Print gridlines.
- Print row/column headings.
- Achieve draft quality.
- Print comments.
- Print cell errors.
- Define page ordering.

Aspose.Cells for Node.js via C++ supports all the print options offered by Microsoft Excel and developers can easily configure these options for worksheets using the properties offered by the [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) class. How these properties are used is discussed below in more detail.

### **Set Print Area**

By default, the print area incorporates all areas of the worksheet that contain data. Developers can establish a specific print area of the worksheet.

To select a specific print area, use the [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) class' [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) property. Assign a cell range that defines the print area to this property.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **Set Print Titles**

Aspose.Cells allows you to designate row and column headers to repeat on all pages of a printed worksheet. To do so, use the [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) class' [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) and [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) properties.

The rows or columns that will be repeated are defined by passing their row or column numbers. For example, rows are defined as $1:$2 and columns are defined as $A:$B.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **Set Other Print Options**

The [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) class also provides several other properties to set general print options as follows:

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): a Boolean property that defines whether to print gridlines or not print.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): a Boolean property that defines whether to print row and column headings or not.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): a Boolean property that defines whether to print the worksheet in black and white mode or not.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): defines whether to display the print comments on the worksheet or at the end of the worksheet.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): a boolean property that defines whether to print the sheet without graphics.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): defines whether to print cell errors as displayed, blank, dash or N/A.

To set the [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) and [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) properties, Aspose.Cells for Node.js via C++ also provides two enumerations, [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) and [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) that contain pre-defined values to be assigned to the [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) and [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) properties respectively.

The pre-defined values in the [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) enumeration are listed below with their descriptions.

|**Print Comments Types**|**Description**|
| :- | :- |
|PrintInPlace|Specifies to print comments as displayed on the worksheet.|
|PrintNoComments|Specifies not to print comments.|
|PrintSheetEnd|Specifies to print comments at the end of the worksheet.|

The pre-defined values of [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) enumeration are listed below with their descriptions.

|**Print Errors Types**|**Description**|
| :- | :- |
|PrintErrorsBlank|Specifies not to print errors.|
|PrintErrorsDash|Specifies to print errors as "--".|
|PrintErrorsDisplayed|Specifies to print errors as displayed.|
|PrintErrorsNA|Specifies to print errors as "#N/A".|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **Set Page Order**

The [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) class provides the [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--) property that is used to order multiple pages of your worksheet to be printed. There are two possibilities to order the pages as follows.

- **Down then over:** prints all the pages down before printing any pages to the right.
- **Over then down:** prints pages left to right before printing the pages below.

Aspose.Cells provides an enumeration, [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) that contains all pre-defined order types.

The pre-defined values of the [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) enumeration are listed below.

|**Print Order Types**|**Description**|
| :- | :- |
|DownThenOver|Represents printing order as down then over.|
|OverThenDown|Represents printing order as over then down.|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}