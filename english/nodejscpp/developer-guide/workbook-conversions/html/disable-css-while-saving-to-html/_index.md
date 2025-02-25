---
title: Disable CSS while saving to HTML with Node.js via C++
linktitle: Disable CSS while saving to HTML
type: docs
weight: 320
url: /nodejs-cpp/disable-css-while-saving-to-html/
description: Learn how to disable CSS while saving Excel files to HTML using Aspose.Cells for Node.js via C++. 
---

## **Possible Usage Scenarios**

When you save your Excel file to a single page HTML, usually the CSS elements will be embedded within the HTML file and will be located in the HEAD section. If you attach this file as content/body of an email, the CSS elements will be stripped out by most email clients, resulting in improper rendering. The 24.12 version of Aspose.Cells introduces an option which allows you to optionally disable CSS, allowing styles to be directly applied within the HTML elements themselves. If you want to set the HTML as the content/body of the email please use the [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#disableCss-boolean-) property and set it to **true**.

## **Disable CSS while saving to HTML**

The following sample code shows the usage of [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#disableCss-boolean-) property. 

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
