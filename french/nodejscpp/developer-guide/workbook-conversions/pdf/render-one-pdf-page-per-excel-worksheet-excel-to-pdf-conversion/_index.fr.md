---  
title: Rendre une page PDF par feuille de calcul Excel  Conversion Excel en PDF avec Node.js via C++  
linktitle: Rendre une page PDF par feuille de calcul Excel  Conversion Excel en PDF  
type: docs  
weight: 100  
url: /fr/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

Lors de la manipulation de grands fichiers Excel (par exemple, un classeur comprenant plusieurs feuilles, chacune avec 50 colonnes et 300 lignes ou plus), vous pouvez vouloir que la sortie PDF affiche une page par feuille, quelle que soit la taille de la feuille. Cela signifierait que chaque page pourrait avoir une taille très différente. Cela peut être réalisé en utilisant Aspose.Cells for Node.js via C++.  

{{% /alert %}}  

Veuillez consulter le code d'exemple suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

Si l'option [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) est activée à **true**, tout le contenu de la feuille sera rendu sur une seule page PDF.  

{{% /alert %}} {{% alert color="primary" %}}  

Si votre feuille contient des formules, il est préférable d'appeler [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) juste avant de la rendre en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont affichées dans le PDF.  

{{% /alert %}}  

