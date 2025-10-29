---
title: Obtenir la largeur et la hauteur du papier dans la mise en page de la feuille avec Node.js via C++
linktitle: Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul
type: docs
weight: 50
url: /fr/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Découvrez comment obtenir la largeur et la hauteur du papier de la mise en page d’une feuille Excel en utilisant Node.js via C++ de manière programmatique.
keywords: largeur du papier de la mise en page Excel Node.js via C++, hauteur du papier de la mise en page Excel Node.js via C++
---

## **Scénarios d'utilisation possibles**

Parfois, vous devez connaître la largeur et la hauteur du papier tel qu’il a été défini dans la mise en page de la feuille de calcul. Veuillez utiliser les propriétés [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) et [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) à cette fin.

## **Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul**

Le code d’échantillon suivant explique l’utilisation des propriétés [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) et [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--). Il change d’abord la taille du papier en *A2*, puis trouve la largeur et la hauteur du papier, puis le change en *A3*, *A4*, *Letter* et trouve respectivement la largeur et la hauteur du papier.

### **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
