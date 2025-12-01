---
title: Setting Different Headers and Footers For Different Pages with Node.js via C++
linktitle: Setting Different Headers and Footers For Different Pages
type: docs
weight: 35
url: /nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: This article provides sample code that shows how to programmatically set headers and footers of Excel worksheet Page Setup using Aspose.Cells for Node.js via C++. Set headers and footers for first, odd, and even pages.
keywords: set excel header footer first page Node.js via C++, set excel header footer odd pages Node.js via C++, set excel header footer even pages Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

MS Excel supports setting different headers and footers for the first page, odd pages, and even pages since Excel 2007.
Aspose.Cells for Node.js via C++ supports the same feature.

{{% /alert %}}

## **Setting Different Headers and Footers in MS Excel**

**![Setting Different Headers and Footers](difpage.png)**

1. Click **page Layout > Print Titles > Header/Footer**.
1. Check **Different Odd and Even Pages** or **Different first page**.
1. Enter different headers and footers.

## **Setting Different Headers and Footers with Aspose.Cells for Node.js via C++**

Aspose.Cells behaves the same as Excel.
1. Sets the flags [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) and [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. Enter different headers and footers.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
