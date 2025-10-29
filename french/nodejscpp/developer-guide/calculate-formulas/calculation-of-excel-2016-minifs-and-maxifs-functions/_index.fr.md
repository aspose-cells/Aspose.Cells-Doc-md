---
title: Calcul des fonctions MINIFS et MAXIFS d’Excel 2016 avec Node.js via C++
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer les fonctions MINIFS et MAXIFS dans Microsoft Excel 2016 en utilisant Node.js via C++. Chargez un fichier Excel existant ou créez en un nouveau, puis utilisez les méthodes Aspose.Cells pour calculer ces fonctions et enregistrer les résultats sur le disque.
keywords: Aspose.Cells, Excel, 2016, fonction MINIFS, fonction MAXIFS, calcul Node.js via C++
type: docs
weight: 300
url: /fr/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Scénarios d'utilisation possibles**
Microsoft Excel 2016 supporte les fonctions MINIFS et MAXIFS. Ces fonctions ne sont pas prises en charge dans Excel 2013 ou les versions antérieures. Aspose.Cells for Node.js via C++ supporte également le calcul de ces fonctions. La capture d'écran suivante illustre l'utilisation de ces fonctions. Veuillez lire les commentaires en rouge dans la capture d'écran pour comprendre leur fonctionnement.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcul des fonctions MINIFS et MAXIFS d'Excel 2016**
Le code d'exemple suivant charge le [fichier Excel d'exemple](5115149.xlsx) et appelle la méthode [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) pour effectuer le calcul de la formule via Aspose.Cells for Node.js via C++, puis enregistre les résultats dans le [PDF de sortie](5115154.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
