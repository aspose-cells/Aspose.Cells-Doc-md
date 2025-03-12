---
title: Setting Margins with Node.js via C++
linktitle: Setting Margins
type: docs
weight: 20
url: /nodejs-cpp/setting-margins/
description: In this article, you will learn how to set the margins of an Excel worksheet using sample code. Also learn how to programmatically set margins for page center, header, and footer using the Node.js API via C++.
keywords: set excel worksheet margin to center Node.js via C++, set worksheet header and footer margin Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells fully supports Microsoft Excel's page setup options. Developers may need to configure page setup settings for worksheets to control the printing process. This topic discusses how to use Aspose.Cells to configure page margins.

{{% /alert %}}

## **Setting Margins**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains the [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class.

The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides the [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) property used to set the page setup options for a worksheet. The [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) attribute is an object of the [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) class that enables developers to set different page layout options for a printed worksheet. The [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) class provides various properties and methods used to set page setup options.

### **Page Margins**

Set page margins (left, right, top, bottom) using [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) class members. A few of the methods are listed below which are used to specify page margins:

- [**PageSetup.getLeftMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getLeftMargin--)
- [**PageSetup.getRightMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getRightMargin--)
- [**PageSetup.getTopMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getTopMargin--)
- [**PageSetup.getBottomMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBottomMargin--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Set bottom, left, right and top page margins
pageSetup.setBottomMargin(2);
pageSetup.setLeftMargin(1);
pageSetup.setRightMargin(1);
pageSetup.setTopMargin(3);

// Save the Workbook.
workbook.save(path.join(dataDir, "SetMargins_out.xls"));
```

### **Center on Page**

It is possible to center something on a page horizontally and vertically. For this, there are some useful members of the [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) class, [**PageSetup.getCenterHorizontally()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterHorizontally--) and [**PageSetup.getCenterVertically()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterVertically--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Center on page Horizontally and Vertically
pageSetup.setCenterHorizontally(true);
pageSetup.setCenterVertically(true);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```

### **Header and Footer Margins**

Set header and footer margins with the [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) class members such as [**PageSetup.getHeaderMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeaderMargin--) and [**PageSetup.getFooterMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooterMargin--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Header / Footer margins
pageSetup.setHeaderMargin(2);
pageSetup.setFooterMargin(2);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```
