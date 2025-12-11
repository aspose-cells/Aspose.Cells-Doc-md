---
title: Getting Headers or Footers with Node.js via C++
linktitle: Getting Headers or Footers
type: docs
weight: 30
url: /nodejs-cpp/get-headers-or-footers/
description: This article explains how to programmatically get headers and footers from Excel or OpenOffice files using the Node.js via C++ API.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Headers and footers are displayed only in Page Layout view, Print Preview, and on printed pages. 

You can also use the Page Setup dialog box if you want to view headers or footers for more than one worksheet at a time. 

For other sheet types, such as chart sheets or charts, you can insert headers and footers only by using the Page Setup dialog box.

{{% /alert %}}

## **Getting Headers and Footers in MS Excel**
1. Click the worksheet where you want to view or change headers or footers.
2. On the View tab, in the Workbook Views group, click Page Layout.  
   Excel displays the worksheet in Page Layout view.
3. To view or edit a header or footer, click the left, center, or right header or footer text box at the top or the bottom of the worksheet page (under Header or above Footer).

## **Getting Headers and Footers using Aspose.Cells for Node.js via C++**
With [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) and [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-) methods, Node.js developers can simply get headers or footers from the file.

1. Construct a Workbook to open the file.
2. Get the worksheet where you want to get headers or footers.
3. Get the header or footer with a specific section ID.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **Parse Headers and Footers into a Command List**
The header or footer text can contain special commands, for example, a placeholder for the page number, current date, or text formatting attributes.

Special commands are represented by a single letter with a leading ampersand ("&").

The header and footer strings are constructed using ABNF grammar. It is not easy to understand without a viewer.

Aspose.Cells for Node.js via C++ provides [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) method to parse headers and footers as a command list.

The following code shows how to parse the header or footer as a command list and process commands:

```javascript
try {
    const AsposeCells = require("aspose.cells.node");
    const path = require("path");

    // The path to the documents directory.
    const dataDir = path.join(__dirname, "data");
    const filePath = path.join(dataDir, "HeaderFooter.xlsx");

    // Instantiate a new Workbook.
    const workbook = new AsposeCells.Workbook(filePath);
    const sheet = workbook.getWorksheets().get(0);

    // Gets left section of header
    const headerSection = sheet.getPageSetup().getHeader(0);
    const commands = sheet.getPageSetup().getCommands(headerSection) || [];

    commands.forEach(c => {
        switch (c.getType()) {
            case AsposeCells.HeaderFooterCommandType.SheetName:
                // embeds the name of the sheet in the header or footer
                break;
        }
    });
}
{{< app/cells/assistant language="nodejs-cpp" >}}
