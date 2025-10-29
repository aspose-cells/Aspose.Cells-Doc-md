---
title: Définir le texte de l entrée de la légende du graphique en remplissant à none en utilisant Aspose.Cells for Node.js via C++
linktitle: Définir le texte de la légende du graphique sans remplissage en utilisant Aspose.Cells
description: Apprenez comment utiliser Aspose.Cells for Node.js via C++ pour définir le texte d une entrée de légende du graphique en remplissant à none. Ce guide démontrera comment modifier la couleur de remplissage des entrées de légende dans les graphiques Microsoft Excel pour une meilleure visualisation et personnalisation.
keywords: Aspose.Cells for Node.js via C++, Remplissage de l’entrée de la légende du graphique, Microsoft Excel, Visualisation, Personnalisation.
type: docs
weight: 320
url: /fr/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Si vous souhaitez définir le texte de l'entrée de la légende du graphique en aucun pour qu'il ne s'affiche pas dans la légende du graphique, veuillez définir [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--) sur **true**.

{{% /alert %}}

Le code d'exemple suivant définit le texte du remplissage de la deuxième entrée de légende du graphique sur aucun. Veuillez télécharger le [fichier Excel d'exemple](5115219.xlsx) utilisé dans ce code et le [fichier Excel de sortie](5115217.xlsx) généré par celui-ci pour votre référence.

La capture d'écran suivante met en évidence l'effet de ce code sur le fichier Excel d'exemple (5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
