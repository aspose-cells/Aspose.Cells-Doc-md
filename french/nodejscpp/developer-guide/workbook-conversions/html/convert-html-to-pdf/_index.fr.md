---
title: Comment convertir HTML en PDF avec Node.js via C++
linktitle: Comment convertir du HTML en PDF
type: docs
weight: 80
url: /fr/nodejs-cpp/convert-html-to-pdf/
description: Ce sujet vous montre comment convertir HTML en PDF et MHTML en PDF en utilisant Aspose.Cells for Node.js via C++.
keywords: Conversion de HTML et MHTML en PDF via Node.js et C++. 
---

## **Vue d'ensemble**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>convertir du HTML en PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML vers PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Convertir HTML en PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Comment convertir HTML en PDF</a></li>
</ul>

## **Conversion de HTML en PDF dans Node.js**
Comment convertir HTML en PDF ? Avec la bibliothèque [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/), vous pouvez facilement convertir HTML en PDF de manière programmatique en quelques lignes de code. Aspose.Cells for Node.js via C++ est capable de créer des applications multiplateformes avec la capacité de générer, modifier, convertir, rendre et imprimer tous les fichiers Excel.

## **JavaScript Convertir HTML en PDF**
L'extrait de code JavaScript suivant montre comment convertir un document HTML en PDF en utilisant [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/).

1. Créer une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/).
1. Initialiser l'objet [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/).
1. Enregistrer le document PDF de sortie en appelant la méthode Workbook.save().

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

## **Essayez de convertir du HTML en PDF en ligne**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML en PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="nodejs-cpp" >}}
