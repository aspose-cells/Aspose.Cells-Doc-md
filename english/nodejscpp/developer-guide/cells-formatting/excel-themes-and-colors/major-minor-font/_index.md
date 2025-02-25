---
title: Headings And Body Theme Font with Node.js via C++
linktitle: Headings And Body Theme Font
description: Aspose.Cells is a Node.js library for working with spreadsheet files. It supports setting heading and body theme fonts in Excel documents, enabling users to customize the appearance and style of the document. This article will introduce how to use the Aspose.Cells library to work with heading and body theme fonts in Excel documents.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style, Node.js via C++
type: docs
weight: 120
url: /nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

The default font will automatically change when the region setting is changed.

If the default font is changed, the row height and column width is also changed, and it may even mess up the page layout.

What caused the default font to change?

If Excel theme font is set, Excel will automatically switch between different fonts based on the current language environment.

{{% /alert %}}

## **Headings And Body Theme Font In Excel**

In Excel, select Home tab, click on the font dropdown box, you will see "Theme Fonts" with two theme fonts: Calibri Light (Headings) and Calibri (Body) on the top with English region setting.

**![Theme Fonts](Theme-Fonts.png)**

If Theme Font is selected, the font name will display differently in different regions. If you do not want the font to automatically change in different regions, don't select the two Theme Fonts.

## **Changing Headings And Body Font Programmatically**
With Aspose.Cells for Node.js via C++, we can check whether the default font is a theme font or set the theme font with [**Font.SchemeType**](https://reference.aspose.com/cells/nodejs-cpp/font/#schemetype) property.

The following sample code shows how to manipulate the theme font.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);
let defaultStyle = workbook.getDefaultStyle();

let schemeType = defaultStyle.getFont().getSchemeType();
if (schemeType === AsposeCells.FontSchemeType.Major || schemeType === AsposeCells.FontSchemeType.Minor) {
    console.log("It's theme font");
}

// Change theme font to normal font
defaultStyle.getFont().setSchemeType(AsposeCells.FontSchemeType.None);

workbook.setDefaultStyle(defaultStyle);
```

## **Dynamically Gets Local Theme Font Programmatically**
Sometimes, our servers and users' machines are not in the same region. How can we obtain the same font that users want for file processing?

We have to set the system regional settings before loading the file with [**LoadOptions.Region**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#region) property.

The following sample code shows how to get local theme font.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new LoadOptions.
const options = new AsposeCells.LoadOptions();
// Sets the customer's region 
options.setRegion(AsposeCells.CountryCode.Japan);
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath, options);
const defaultStyle = workbook.getDefaultStyle();

// Gets customer's local font.
const localFontName = defaultStyle.getFont().getName();
```
