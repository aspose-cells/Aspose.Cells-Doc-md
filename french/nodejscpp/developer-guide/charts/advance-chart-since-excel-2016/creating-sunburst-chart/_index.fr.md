---
title: Comment créer un graphique Sunburst avec Node.js via C++
linktitle: Comment créer un diagramme en cercles emboîtés
description: Apprenez comment créer un graphique en rayon de soleil en Aspose.Cells for Node.js via C++, un graphique qui présente des données dans un cercle. Notre guide vous aidera à configurer diverses propriétés et formats de votre graphique, y compris les étiquettes de données, les légendes, les couleurs et plus encore.
keywords: Aspose.Cells for Node.js via C++, graphique en rayon de soleil, créer, définir propriétés, étiquettes de données, légende, format, couleur, cercle, rendu des données.
type: docs
weight: 162
url: /fr/nodejs-cpp/creating-sunburst-chart/
---

## **Scénarios d'utilisation possibles**
Les graphiques en treemap sont efficaces pour comparer les proportions au sein de la hiérarchie ; cependant, les graphiques en treemap ne sont pas idéaux pour montrer les niveaux hiérarchiques entre les plus grandes catégories et chaque point de données. Un graphique en rayon de soleil est beaucoup plus adapté pour cela. Le graphique en rayon de soleil est idéal pour afficher des données hiérarchiques. Chaque niveau de la hiérarchie est représenté par un anneau ou un cercle, le cercle le plus intérieur étant le sommet de la hiérarchie. Un graphique en rayon de soleil sans données hiérarchiques (un seul niveau de catégories) ressemble à un graphique en anneau. Cependant, un graphique en rayon de soleil avec plusieurs niveaux de catégories montre comment les anneaux extérieurs se rapportent aux anneaux intérieurs. Le graphique en rayon de soleil est le plus efficace pour montrer comment un anneau est divisé en ses parties contributives, alors qu'un autre type de graphique hiérarchique, le graphique en treemap, est idéal pour comparer les tailles relatives.

![todo:image_alt_text](sample.png)
## **Diagramme sunburst**
Après avoir exécuté le code ci-dessous, vous verrez le diagramme sunburst comme indiqué ci-dessous.

![todo:image_alt_text](result.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](sunburst.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
