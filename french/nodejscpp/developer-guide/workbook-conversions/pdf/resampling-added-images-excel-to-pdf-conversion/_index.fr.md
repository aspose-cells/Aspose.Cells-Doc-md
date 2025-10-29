---
title: Resampling des images ajoutées  Conversion Excel en PDF avec Node.js via C++
linktitle: Ajout d images échantillonnées
type: docs
weight: 150
url: /fr/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Apprenez à compresser les images ajoutées dans les fichiers Excel pour réduire la taille du PDF et améliorer la performance de conversion en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Lors de la manipulation de grands fichiers Microsoft Excel contenant beaucoup d'images, vous pourriez avoir besoin de compresser les images ajoutées pour réduire la taille du fichier PDF généré et améliorer la performance globale de la conversion. Aspose.Cells for Node.js via C++ supporte le resampling des images ajoutées pour réduire la taille du PDF de sortie et améliorer la performance dans une moindre mesure.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant qui décrit comment effectuer la tâche à l'aide de l'API Aspose.Cells. L'exemple convertit un fichier Microsoft Excel en un fichier PDF tout en compressant les images dans le fichier.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

L'option [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) minimise la taille du PDF de sortie, mais cela peut affecter un peu la qualité de l'image.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
