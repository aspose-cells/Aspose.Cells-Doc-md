---
title: Limiter le nombre de pages générées  Conversion Excel en PDF avec Node.js via C++
linktitle: Limitez le nombre de pages générées  Conversion Excel en PDF
type: docs
weight: 180
url: /fr/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Apprenez comment limiter le nombre de pages générées lors de la conversion d une feuille de calcul Excel en PDF en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Parfois, vous souhaitez imprimer une plage de pages dans un fichier PDF de sortie. Aspose.Cells for Node.js via C++ a la capacité de limiter le nombre de pages générées lors de la conversion d'une feuille de calcul Excel en format PDF.

{{% /alert %}}

## **Limitez le nombre de pages générées**

L'exemple suivant montre comment restituer une plage de pages (3 et 4) dans un fichier Microsoft Excel au format PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Instantiate the PdfSaveOption
const options = new AsposeCells.PdfSaveOptions();

// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.setPageIndex(3);
// Number of pages to be printed
options.setPageCount(2);

// Save the PDF file
workbook.save(path.join(dataDir, "outPDF1.out.pdf"), options);
```

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) juste avant de l'exporter en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et que les bonnes valeurs sont affichées dans le fichier de sortie.

{{% /alert %}}
