---
title: So konvertieren Sie HTML mit Node.js über C++ in PDF
linktitle: Wie konvertiere ich HTML in PDF
type: docs
weight: 80
url: /de/nodejs-cpp/convert-html-to-pdf/
description: Dieses Thema zeigt, wie Sie HTML in PDF und MHTML in PDF mit Aspose.Cells for Node.js via C++ konvertieren.
keywords: Node.js konvertiert HTML zu PDF und MHTML zu PDF über C++. 
---

## **Übersicht**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>konvertieren Sie HTML in das PDF-Saveformat</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML zu PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML in PDF konvertieren</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Wie konvertiert man HTML in PDF</a></li>
</ul>

## **HTML-zu-PDF-Konvertierung in Node.js**
Wie konvertiert man HTML in PDF? Mit der [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) Bibliothek können Sie HTML einfach programmatisch in PDF umwandeln, mit nur wenigen Codezeilen. Aspose.Cells for Node.js via C++ ist in der Lage, plattformübergreifende Anwendungen zu erstellen, die alle Excel-Dateien generieren, modifizieren, konvertieren, rendern und drucken können.

## **JavaScript HTML in PDF konvertieren**
Das folgende JavaScript-Codebeispiel zeigt, wie man ein HTML-Dokument mit [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) in eine PDF umwandelt.

1. Erstellen Sie eine Instanz der Klasse [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/).
1. Initialisieren Sie das [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) Objekt.
1. Speichern Sie das Ausgabedokument als PDF, indem Sie die Methode Workbook.save() aufrufen.

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

## **Versuchen Sie, HTML online in PDF zu konvertieren**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">„HTML in PDF“</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="nodejs-cpp" >}}
