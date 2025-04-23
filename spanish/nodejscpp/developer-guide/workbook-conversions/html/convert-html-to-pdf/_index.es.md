---
title: Cómo convertir HTML a PDF con Node.js mediante C++
linktitle: Cómo convertir HTML a PDF
type: docs
weight: 80
url: /es/nodejs-cpp/convert-html-to-pdf/
description: Este tema te muestra cómo convertir HTML a PDF y MHTML a PDF usando Aspose.Cells for Node.js via C++.
keywords: Node.js convierte HTML a PDF y MHTML a PDF mediante C++. 
---

## **Visión general**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>convertir HTML a PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">HTML JavaScript a PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Convierte HTML a PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Cómo convertir HTML a PDF</a></li>
</ul>

## **Conversión de HTML a PDF en Node.js**
¿Cómo convertir HTML a PDF? Con la biblioteca [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) puedes convertir fácilmente HTML a PDF programáticamente con unas pocas líneas de código. Aspose.Cells for Node.js via C++ es capaz de construir aplicaciones multiplataforma con la capacidad de generar, modificar, convertir, renderizar e imprimir todos los archivos de Excel.

## **JavaScript Convierte HTML a PDF**
El siguiente ejemplo de código JavaScript muestra cómo convertir un documento HTML a PDF usando [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/).

1. Crea una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/).
1. Inicializa un objeto [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/).
1. Guarde el documento PDF de salida llamando al método Workbook.save().

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

## **Intenta convertir HTML a PDF en línea**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML a PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
