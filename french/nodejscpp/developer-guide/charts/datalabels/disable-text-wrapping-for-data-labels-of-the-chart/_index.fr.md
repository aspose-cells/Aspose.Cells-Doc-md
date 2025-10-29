---
title: Désactiver le saut de ligne pour les étiquettes de données du graphique avec Node.js via C++
description: Apprenez comment désactiver le saut de ligne pour les étiquettes de données dans les graphiques en utilisant Aspose.Cells for Node.js via C++. Notre guide vous montrera comment empêcher les longues étiquettes de se chevaucher et offrir des affichages de graphiques plus lisibles et clairs.
keywords: Aspose.Cells for Node.js via C++, graphique, étiquettes de données, retour à la ligne du texte, chevauchement, lisibilité, affichages.
type: docs
weight: 70
url: /fr/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 permet aux utilisateurs de mettre en forme ou de défaire le retour à la ligne à l'intérieur des étiquettes de données du graphique. Par défaut, le texte à l'intérieur des étiquettes de données du graphique est à l'état de retour à la ligne.

Aspose.Cells fournit une propriété [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--) que vous pouvez définir sur vrai ou faux pour activer ou désactiver respectivement le retour à la ligne du texte des étiquettes de données.

{{% /alert %}}

L'exemple de code ci-dessous montre comment désactiver le retour à la ligne pour les étiquettes de données du graphique.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
