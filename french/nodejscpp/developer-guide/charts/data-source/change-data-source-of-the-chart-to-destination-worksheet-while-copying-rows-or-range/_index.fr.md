---
title: Modifier la source de données du graphique vers la feuille de destination lors de la copie de lignes ou de plages avec Node.js via C++
linktitle: Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage
description: Apprenez comment changer la source de données d un graphique vers une feuille de destination tout en copiant des lignes ou une plage dans Aspose.Cells for Node.js via C++. Ce guide montre comment mettre à jour la plage de données du graphique et la lier à la feuille de destination.
keywords: Aspose.Cells for Node.js via C++, création de graphiques, source de données, feuille de destination, lignes, plage, copie, mise à jour, plage de données, liaison.
type: docs
weight: 440
url: /fr/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Scénarios d'utilisation possibles**

Lorsque vous copiez des lignes ou une plage contenant des graphiques vers une nouvelle feuille, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est `=Sheet1!$A$1:$B$4`, alors après la copie, la source de données restera la même, c’est-à-dire `=Sheet1!$A$1:$B$4`. Elle continue de faire référence à l’ancienne feuille, c'est-à-dire Sheet1. Ce comportement est également celui de Microsoft Excel. Mais si vous souhaitez qu’elle fasse référence à la nouvelle feuille de destination, utilisez la propriété [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) et définissez-la sur **true** lors de l’appel de la méthode [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-). Maintenant, si votre feuille de destination est DestSheet, la source de données de votre graphique passera de `=Sheet1!$A$1:$B$4` à `=DestSheet!$A$1:$B$4`.

## **Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage**

Le code d'exemple suivant explique l'utilisation de la propriété [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) lors de la copie de lignes ou de plages contenant des graphiques vers une nouvelle feuille. Le code utilise le [fichier Excel d'exemple](5113699.xlsx) et génère le [fichier Excel de sortie](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
