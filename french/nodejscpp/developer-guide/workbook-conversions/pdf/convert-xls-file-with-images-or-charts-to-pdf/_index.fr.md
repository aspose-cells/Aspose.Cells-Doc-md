---
title: Convertir un fichier XLS avec images ou graphiques en PDF avec Node.js via C++
linktitle: Convertir un fichier XLS avec des images ou des graphiques en PDF
type: docs
weight: 50
url: /fr/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells supporte la conversion de fichiers XLS contenant des images et des graphiques en documents PDF. Aspose.Cells for Node.js via C++ peut fonctionner de manière indépendante pour convertir une feuille de calcul en PDF : Aspose.PDF pour Node.js via C++ n'est pas nécessaire pour la conversion. Le processus peut être effectué en mémoire car il ne dépend pas de fichiers XML temporaires ou intermédiaires. Cela signifie que de grands fichiers Excel, par exemple contenant des images, des graphiques et d'autres objets de dessin, peuvent être convertis rapidement et efficacement.

{{% /alert %}} 
## **Code d'exemple**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

 Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) juste avant de rendre en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et que les bonnes valeurs sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
