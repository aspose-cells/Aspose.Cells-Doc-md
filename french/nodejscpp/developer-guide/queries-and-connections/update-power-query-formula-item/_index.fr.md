---
title: Mettre à jour l’élément de formule Power Query avec Node.js via C++
linktitle: Mettre à jour l élément de formule Power Query
type: docs
weight: 120
url: /fr/nodejs-cpp/update-power-query-formula-item/
description: Apprenez comment mettre à jour la source de données de l’élément de formule Power Query dans un fichier Excel en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénario d'utilisation**

Il peut arriver que les fichiers source de données soient déplacés et que le fichier Excel ne puisse pas localiser le fichier. Dans ce cas, l’API Aspose.Cells offre l’option de mettre à jour l’élément de formule Power Query en utilisant la classe [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) pour mettre à jour l’emplacement du fichier source.

## **Mise à jour de l'élément de formule Power Query**

L’API Aspose.Cells permet de mettre à jour les éléments de formule Power Query. Le code suivant illustre la mise à jour de l’emplacement du fichier source des données dans le fichier Excel en utilisant la propriété [**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--). Les fichiers source et de sortie sont joints pour votre référence.

- [Fichier source 1](106364953.xlsx)
- [Fichier source 2](106364954.xlsx)
- [Fichier de sortie](106364955.xlsx)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Working directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SamplePowerQueryFormula.xlsx"));
const mashupData = workbook.getDataMashup();

const powerQueryFormulas = mashupData.getPowerQueryFormulas();
const count = powerQueryFormulas.getCount();
for (let i = 0; i < count; i++) 
{
const formula = powerQueryFormulas.get(i);
const items = formula.getPowerQueryFormulaItems();
const itemsCount = items.getCount();
for (let j = 0; j < itemsCount; j++) 
{
const item = items.get(j);
if (item.getName() === "Source") 
{
item.setValue(`Excel.Workbook(File.Contents("${path.join(sourceDir, "SamplePowerQueryFormulaSource.xlsx")}", null, true)`);
}
}
}

// Save the output workbook.
workbook.save(outputDir + "SamplePowerQueryFormula_out.xlsx");
```
