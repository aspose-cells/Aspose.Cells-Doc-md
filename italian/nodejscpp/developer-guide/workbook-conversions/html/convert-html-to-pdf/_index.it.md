---
title: Come convertire HTML in PDF con Node.js tramite C++
linktitle: Come convertire HTML in PDF
type: docs
weight: 80
url: /it/nodejs-cpp/convert-html-to-pdf/
description: Questo argomento mostra come convertire HTML in PDF e MHTML in PDF usando Aspose.Cells for Node.js via C++.
keywords: Converti HTML in PDF e MHTML in PDF con Node.js tramite C++. 
---

## **Panoramica**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>converti HTML in PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML in PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Converti HTML in PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Come convertire HTML in PDF</a></li>
</ul>

## **Conversione HTML in PDF in Node.js**
Come convertire HTML in PDF? Con la libreria [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) puoi facilmente convertire HTML in PDF tramite pochi righi di codice. Aspose.Cells for Node.js via C++ è in grado di creare applicazioni multipiattaforma con capacità di generare, modificare, convertire, renderizzare e stampare tutti i file Excel.

## **JavaScript Converti HTML in PDF**
Il seguente esempio di codice JavaScript mostra come convertire un documento HTML in PDF usando [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/).

1. Crea un'istanza della classe [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/).
1. Inizializza l'oggetto [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/).
1. Salvare il documento PDF di output chiamando il metodo Workbook.save().

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

## **Prova a convertire HTML in PDF online**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML to PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="nodejs-cpp" >}}
