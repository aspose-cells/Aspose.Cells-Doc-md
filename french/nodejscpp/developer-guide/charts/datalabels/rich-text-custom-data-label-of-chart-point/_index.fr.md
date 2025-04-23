---
title: Étiquette de donnée personnalisée en texte enrichi pour un point de graphique avec Node.js via C++
description: Apprenez comment ajouter des étiquettes de données personnalisées en texte enrichi aux points du graphique dans Aspose.Cells for Node.js via C++. Notre guide montrera comment formater les étiquettes avec différentes polices, couleurs et options d alignement pour améliorer l apparence et la lisibilité de vos graphiques.
keywords: Aspose.Cells for Node.js via C++, programmation de graphiques, texte enrichi, étiquettes de données personnalisées, polices, couleurs, alignement, apparence, lisibilité.
type: docs
weight: 10
url: /fr/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour créer des étiquettes de données personnalisées en texte enrichi pour les points du graphique. Aspose.Cells propose la méthode [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-) pour retourner l'objet [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) qui peut être utilisé pour définir les propriétés de police du texte comme sa couleur, sa graisse, etc.

{{% /alert %}}

## Étiquette de données personnalisée en texte enrichi du point du graphique

Le code suivant accède au premier point du graphique de la première série, définit son texte, puis définit la police des 10 premiers caractères en réglant leur couleur en rouge et leur graisse à **true**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
