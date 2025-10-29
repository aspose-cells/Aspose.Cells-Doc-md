---  
title: Enregistrer chaque feuille de travail dans un fichier PDF séparé avec Node.js via C++  
linktitle: Enregistrer chaque feuille de calcul dans un fichier PDF différent  
type: docs  
weight: 130  
url: /fr/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cells supporte la conversion de fichiers XLS (contenant des images, graphiques, etc.) en documents PDF. Aspose.Cells for Node.js via C++ peut fonctionner indépendamment pour convertir une feuille de calcul en PDF, sans avoir besoin d'utiliser Aspose.PDF pour Node.js via C++ pour la conversion. La conversion n'exige pas la création ou l'utilisation de fichiers temporaires car tout le processus peut être effectué en mémoire.  
{{% /alert %}}  

## **Sauvegarder chaque feuille de calcul dans un fichier PDF différent**  
Si vous avez besoin d'enregistrer chaque feuille de votre modèle Excel pour générer différents fichiers PDF, vous pouvez facilement le faire. Essayez de définir un indice de feuille à l'option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) à la fois pour rendre en PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
