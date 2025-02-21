---
title: Get HTML5 string from Cell with Node.js via C++
type: docs
weight: 90
url: /nodejs-cpp/get-html5-string-from-cell/
description: Learn how to get HTML5 string from Cell through the Aspose.Cells for Node.js via C++ API.
keywords: Get HTML5 string from Cell Node.js via C++, Obtain HTML5 string from Cell Node.js via C++, Manage HTML5 string of Cell Node.js via C++
---

## **Possible Usage Scenarios**

Aspose.Cells returns the HTML string of the cell using the [**getHtmlString**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-string-) method which accepts a boolean parameter. If you pass **false** as a parameter, it will return Normal HTML but if you pass **true** as a parameter, it will return HTML5 string.

## **Get HTML5 string from Cell**

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [**getHtmlString**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-string-) method and prints them on the console.

## **Sample Code**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A1 and put some text inside it.
const cell = ws.getCells().get("A1");
cell.putValue("This is some text.");

// Get the Normal and Html5 strings.
const strNormal = cell.getHtmlString(false);
const strHtml5 = cell.getHtmlString(true);

// Print the Normal and Html5 strings on console.
console.log("Normal:\r\n" + strNormal);
console.log();
console.log("Html5:\r\n" + strHtml5);
```

## **Console Output**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
