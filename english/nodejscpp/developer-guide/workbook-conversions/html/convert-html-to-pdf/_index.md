---
title: How to Convert HTML to PDF with Node.js via C++
linktitle: How to Convert HTML to PDF
type: docs
weight: 80
url: /nodejs-cpp/convert-html-to-pdf/
description: This topic shows you how to convert HTML to PDF and MHTML to PDF using Aspose.Cells for Node.js via C++.
keywords: Node.js convert HTML to PDF and MHTML to PDF via C++. 
---

## **Overview**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>convert HTML to PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML to PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Convert HTML to PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript How to convert HTML to PDF</a></li>
</ul>

## **HTML to PDF Conversion in Node.js**
How to convert HTML to PDF? With [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) library, you can easily convert HTML to PDF programmatically with a few lines of code. Aspose.Cells for Node.js via C++ is capable of building cross-platform applications with the ability to generate, modify, convert, render and print all Excel files.

## **JavaScript Convert HTML to PDF**
The following JavaScript code sample shows how to convert an HTML document to a PDF using [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/).

1. Create an instance of the [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/) class.
1. Initialize [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) object.
1. Save output PDF document by calling Workbook.save() method.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.html");

// Loads the workbook which contains hidden external links
const options = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
const book = new AsposeCells.Workbook(filePath, options);
book.save("out.pdf");
```

## **Try to convert HTML to PDF online**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML to PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
