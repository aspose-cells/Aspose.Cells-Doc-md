---
title: Adapter toutes les colonnes de la feuille sur une seule page PDF avec Node.js via C++
linktitle: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 160
url: /fr/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Parfois, vous voulez générer un fichier PDF qui adapte toutes les colonnes d'une feuille de calcul sur une seule page. La propriété [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) offre cette fonctionnalité de manière très facile à utiliser. Les calculs complexes tels que la hauteur et la largeur du PDF de sortie sont gérés en interne et sont basés sur les données de la feuille de calcul.

{{% /alert %}}

## **Adapter les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) assure que toutes les colonnes d'une feuille sont rendues sur une seule page PDF, même si les lignes peuvent s'étendre sur plusieurs pages en fonction des données de la feuille.

Le code d'exemple ci-dessous montre comment utiliser la propriété [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) pour afficher une grande feuille de calcul de 100 colonnes.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée comporte de nombreuses colonnes, le fichier PDF généré peut afficher le contenu dans une taille très petite. Il reste lisible lorsqu'il est agrandi dans une application de visualisation telle que Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
