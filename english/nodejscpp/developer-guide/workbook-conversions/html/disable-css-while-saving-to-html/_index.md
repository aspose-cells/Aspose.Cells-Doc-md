---
title: Disable CSS while saving to HTML with Node.js via C++
linktitle: Disable CSS while saving to HTML
type: docs
weight: 320
url: /nodejs-cpp/disable-css-while-saving-to-html/
description: Learn how to disable CSS while saving Excel files to HTML using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you save your Excel file to a single‑page HTML, the CSS elements are usually embedded within the HTML file and located in the **HEAD** section. If you attach this file as the content/body of an email, most email clients will strip out the CSS elements, resulting in improper rendering. The 24.12 version of Aspose.Cells introduces an option that allows you to optionally disable CSS, enabling styles to be applied directly within the HTML elements themselves. If you want to set the HTML as the content/body of the email, please use the [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) property and set it to **true**.

## **Disable CSS while saving to HTML**

The following sample code shows how to use the [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) property.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
