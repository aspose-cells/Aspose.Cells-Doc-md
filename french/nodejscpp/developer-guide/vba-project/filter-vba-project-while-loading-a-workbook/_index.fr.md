---
title: Filtrer le projet VBA lors du chargement d un classeur avec Node.js via C++
linktitle: Filtrer le projet VBA lors du chargement d un classeur
type: docs
weight: 140
url: /fr/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: Découvrez comment filtrer les projets VBA lors du chargement de classeurs Excel en utilisant Aspose.Cells for Node.js via C++.
---

## **Filtrer le projet VBA lors du chargement d'un classeur Excel dans Node.js via C++**

Certains fichiers .xlsm/.xslb contiennent une quantité extrêmement grande de macros (ou des macros très longues). Aspose.Cells for Node.js via C++ chargera inconditionnellement ces données (métadonnées) lors de l'ouverture de tels classeurs. Vous pouvez avoir besoin de contrôler cela [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) lorsque vous souhaitez uniquement extraire les noms de feuilles pour un grand nombre de classeurs, en évitant ainsi le contenu inutile. Ce filtre est fourni par l'introduction d'une nouvelle option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions).

## **Code d'exemple**

Le code d'exemple suivant charge un classeur de telle sorte que seul le VBA est filtré. Un fichier exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
