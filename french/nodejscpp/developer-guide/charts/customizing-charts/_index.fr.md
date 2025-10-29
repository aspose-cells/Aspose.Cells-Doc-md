---  
title: Personnalisation des graphiques avec Node.js via C++  
linktitle: Personnalisation des graphiques  
description: Apprenez comment personnaliser les graphiques dans Aspose.Cells for Node.js via C++. Notre guide vous montrera comment modifier la disposition des graphiques, ajouter et formater des séries de données, ajuster les axes et appliquer diverses options de mise en forme pour améliorer l apparence et la convivialité de vos graphiques.  
keywords: Aspose.Cells for Node.js via C++, création de graphiques, personnalisation, dispositions, séries de données, axes, mise en forme, apparence, convivialité.  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/customizing-charts/  
---  


## **Création de graphiques personnalisés**  

Jusqu'à présent, lorsque nous avons parlé de graphiques, nous avons considéré les graphiques standards avec leurs paramètres de mise en forme par défaut. Nous définissons simplement la source de données, réglons quelques propriétés, et le graphique est créé avec ses paramètres par défaut. Mais les API Aspose.Cells supportent également la création de graphiques personnalisés qui permettent aux développeurs de créer des graphiques avec leurs propres paramètres de mise en forme.  

Les développeurs peuvent créer des graphiques personnalisés à l'exécution à l'aide d'Aspose.Cells.  

Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells est représentée par un objet [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) alors que l'objet [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) sert de collection d'objets [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series). Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans l'objet [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)).  

Le code d'exemple ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un graphique en colonnes pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique en colonnes, combiné à un graphique linéaire, à la feuille de calcul.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

Actuellement, Aspose.Cells ne supporte que les graphiques personnalisés combinant pie, line, column, et column stack, mais d'autres graphiques seront supportés dans les futures versions.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
