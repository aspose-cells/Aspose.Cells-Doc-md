---
title: Setting Headers and Footers with Node.js via C++
linktitle: Setting Headers and Footers
type: docs
weight: 30
url: /nodejs-cpp/setting-headers-and-footers/
description: This article explains how to programmatically insert an image in the header and footer of Excel worksheets using Aspose.Cells for Node.js via C++.
keywords: insert image in excel header footer Node.js via C++, set excel header footer script commands Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Headers and footers are the lines of text displayed below the top margin or above the bottom margin, respectively. It's possible to add headers and footers to worksheets as well. Headers and footers can be used to display useful information like page number, author name, topic name, or date and time. Headers and footers are managed using the page‑setup settings.

{{% /alert %}}

## **Setting Headers and Footers**

Aspose.Cells for Node.js via C++ allows you to add headers and footers to worksheets at runtime, but we recommend setting headers and footers manually in a pre‑designed file for printing. You can use Microsoft Excel as a GUI tool to set headers and footers, saving effort and development time. Aspose.Cells can import the file and preserve the settings.

To add headers and footers at runtime, Aspose.Cells provides special API calls and script commands to format headers and footers.

### **Script Commands**

Script commands are special commands that allow you to set header and footer formatting.

| **Script Commands** | **Description** |
| :- | :- |
| &P | The current page number |
| &G | A picture |
| &N | The total number of pages |
| &D | The current date |
| &T | The current time |
| &A | The worksheet name |
| &F | The file name without its path |
| &&Text | Shows &Text. For example: &&WO will be displayed as &WO |
| &"<FontName>" | Represents a font name. For example: &"Arial" |
| &"<FontName>, <FontStyle>" | Represents a font name with style. For example: &"Arial,Bold" |
| &<FontSize> | Represents font size. For example: “&14abc”. However, if this command is followed by a plain number to be printed in the header, the number should be separated from the font size by a space character. For example: “&14 123”. |

### **Set Headers and Footers**

The [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) class provides two methods, [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) and [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-), used to add a header and a footer to a worksheet. These methods take only two parameters:

- **Section** – the section where the header or footer should be placed. There are three sections: left, center, and right, represented by 0, 1, and 2 respectively.
- **Script** – the script to be used for the header or footer. This script contains script commands to format headers or footers.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting the page count at the right section of the footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **Insert an Image into a Header or Footer**

The [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) class has two additional methods, [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) and [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-), used to add pictures into the header and footer. These methods take the following parameters:

- **Section** – the header or footer section where the picture will be placed. There are three sections, left, center, and right, represented by the values 0, 1, and 2 respectively.
- **Byte array** – the graphical data (the binary data should be written into the buffer of a byte array).

After executing the code below and opening the file, check the header of the worksheet by:

1. On the **File** menu, select **Page Setup**. A dialog will be displayed.  
2. Select the **Header/Footer** tab.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the URL of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
