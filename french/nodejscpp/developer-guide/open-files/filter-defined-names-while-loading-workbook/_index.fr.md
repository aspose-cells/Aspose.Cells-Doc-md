---
title: Filtrer les noms définis lors du chargement du classeur avec Node.js via C++
linktitle: Filtrer les noms définis lors du chargement du classeur
type: docs
weight: 50
url: /fr/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells permet de filtrer ou de supprimer les noms définis présents dans le classeur. Veuillez utiliser [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) pour charger les noms définis et [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) pour les supprimer lors du chargement du classeur. À noter, en supprimant les noms définis, les formules dans le classeur pourraient ne plus fonctionner.

## **Filtrer les noms définis lors du chargement du classeur**

Le code d’exemple suivant charge le [fichier Excel exemple](61767860.xlsx) qui contient une formule en cellule **C1** incluant des noms définis, c’est-à-dire *=SUM(MyName1, MyName2)*. Comme nous utilisons [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) pour supprimer les noms définis lors du chargement du classeur, la formule en cellule C1 dans le [fichier Excel de sortie](61767861.xlsx) est cassée et affiche *#NAME?*. Voir la capture d’écran suivante illustrant l’effet du code sur le fichier Excel d’exemple.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
