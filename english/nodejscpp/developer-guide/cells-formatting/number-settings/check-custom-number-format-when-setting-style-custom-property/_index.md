---
title: Check Custom Number Format when Setting Style.Custom Property with Node.js via C++
linktitle: Check Custom Number Format when Setting Style.Custom Property
description: Aspose.Cells is a Node.js library for working with spreadsheet files, which supports checking custom number formats when styling. This article will show you how to use the Aspose.Cells library to check custom number formats to ensure that the styling is correct.
keywords: Aspose.Cells, Node.js libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Possible Usage Scenarios**

If you assign an invalid custom number format to [**Style.custom**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/custom) property, then Aspose.Cells for Node.js via C++ will not throw any exception. But if you want Aspose.Cells to check if the assigned custom number format is valid or not, then please set the [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/checkcustomnumberformat) property to **true**.

## **Check Custom Number Format when setting Style.Custom property**

The following sample code assigns an invalid custom number format to [**Style.custom**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/custom) property. Since we have already set the [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/checkcustomnumberformat) property to **true**, it throws an exception, e.g., Invalid number format. Please read the comments inside the code for more help.

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Setting this property to true will make Aspose.Cells to throw exception
// when invalid custom number format is assigned to Style.Custom property
book.getSettings().setCheckCustomNumberFormat(true);

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Access cell A1 and put some number to it
const cell = sheet.getCells().get("A1");
cell.putValue(2347);

// Access cell's style and set its Style.Custom property
const style = cell.getStyle();

// This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
style.setCustom("ggg @ fff"); //Invalid custom number format
``` 
