---
title: Add PDF Bookmarks with Node.js via C++
linktitle: Add PDF Bookmarks
type: docs
weight: 10
url: /nodejs-cpp/add-pdf-bookmarks/
description: Learn how to insert PDF bookmarks when converting a spreadsheet to PDF using Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

This article provides information on how to insert PDF bookmarks when converting a spreadsheet to PDF.

Aspose.Cells for Node.js via C++ allows you to add bookmarks on the fly. PDF bookmarks can drastically improve the navigability of long documents. When adding bookmark links to a PDF document, you can have precise control over the exact view you want; you're not limited to linking to a page. You can set up the precise view by positioning the target page and then create the bookmark.

{{% /alert %}}

Please see the following sample code to find out how to add PDF bookmarks. The code generates a simple workbook, specifies PDF bookmarks with destination locations, and generates the PDF file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiate a new workbook
const workbook = new AsposeCells.Workbook();
// Get the cells in the first(default) worksheet
let cells = workbook.getWorksheets().get(0).getCells();
// Get the A1 cell
let p = cells.get("A1");
// Enter a value
p.putValue("Preface");
// Get the A10 cell
let A = cells.get("A10");
// Enter a value.
A.putValue("page1");
// Get the H15 cell
let D = cells.get("H15");
// Enter a value
D.putValue("page1(H15)");
// Add a new worksheet to the workbook
workbook.getWorksheets().add();
// Get the cells in the second sheet
cells = workbook.getWorksheets().get(1).getCells();
// Get the B10 cell in the second sheet
let B = cells.get("B10");
// Enter a value
B.putValue("page2");
// Add a new worksheet to the workbook
workbook.getWorksheets().add();
// Get the cells in the third sheet
cells = workbook.getWorksheets().get(2).getCells();
// Get the C10 cell in the third sheet
let C = cells.get("C10");
// Enter a value
C.putValue("page3");

// Create a main PDF Bookmark entry object
let pbeRoot = new AsposeCells.Rendering.PdfBookmarkEntry();
// Specify its text
pbeRoot.setText("Sections");
// Set the destination cell/location
pbeRoot.setDestination(p);

// Set its sub entry array list
pbeRoot.setSubEntry([]);

// Create a sub PDF Bookmark entry object
let subPbe1 = new AsposeCells.Rendering.PdfBookmarkEntry();
// Specify its text
subPbe1.setText("Section 1");
// Set its destination cell
subPbe1.setDestination(A);
// Define/Create a sub Bookmark entry object of "Section A"
let ssubPbe = new AsposeCells.Rendering.PdfBookmarkEntry();
// Specify its text
ssubPbe.setText("Section 1.1");
// Set its destination
ssubPbe.setDestination(D);
// Create/Set its sub entry array list object
subPbe1.setSubEntry([]);
// Add the object to "Section 1"
subPbe1.getSubEntry().push(ssubPbe);
// Add the object to the main PDF root object
pbeRoot.getSubEntry().push(subPbe1);

// Create a sub PDF Bookmark entry object
let subPbe2 = new AsposeCells.Rendering.PdfBookmarkEntry();
// Specify its text
subPbe2.setText("Section 2");
// Set its destination
subPbe2.setDestination(B);
// Add the object to the main PDF root object
pbeRoot.getSubEntry().push(subPbe2);

// Create a sub PDF Bookmark entry object
let subPbe3 = new AsposeCells.Rendering.PdfBookmarkEntry();
// Specify its text
subPbe3.setText("Section 3");
// Set its destination
subPbe3.setDestination(C);
// Add the object to the main PDF root object
pbeRoot.getSubEntry().push(subPbe3);

// Create an instance of PdfSaveOptions
let pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set the PDF Bookmark root object
pdfSaveOptions.setBookmark(pbeRoot);

const outputFilePath = path.join(dataDir, "PDFBookmarks_test.out.pdf");
// Save the pdf file
workbook.save(outputFilePath, pdfSaveOptions);
```

{{% alert color="primary" %}}

If your spreadsheet has formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are refreshed & rendered correctly in PDF.

{{% /alert %}}

