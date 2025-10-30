---
title: Hur man konverterar HTML till PDF med Node.js via C++
linktitle: Hur man konverterar HTML till PDF
type: docs
weight: 80
url: /sv/nodejs-cpp/convert-html-to-pdf/
description: Denna guide visar hur du konverterar HTML till PDF och MHTML till PDF med Aspose.Cells for Node.js via C++.
keywords: Node.js konverterar HTML till PDF och MHTML till PDF via C++. 
---

## **Översikt**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>konvertera HTML till PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML till PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Konvertera HTML till PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Hur konverterar man HTML till PDF</a></li>
</ul>

## **HTML till PDF-konvertering i Node.js**
Hur konverterar man HTML till PDF? Med [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/)-biblioteket kan du enkelt konvertera HTML till PDF programmässigt med några få kodrader. Aspose.Cells for Node.js via C++ är kapabel att bygga plattformsöverskridande applikationer med möjlighet att generera, modifiera, konvertera, rendera och skriva ut alla Excel-filer.

## **JavaScript Konvertera HTML till PDF**
Följande JavaScript-kod exempel visar hur man konverterar ett HTML-dokument till PDF med [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/).

1. Skapa en instans av [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/) klassen.
1. Initiera [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) objekt.
1. Spara utdata PDF-dokument genom att anropa Workbook.save() metoden.

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

## **Försök att konvertera HTML till PDF online**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML till PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="nodejs-cpp" >}}
