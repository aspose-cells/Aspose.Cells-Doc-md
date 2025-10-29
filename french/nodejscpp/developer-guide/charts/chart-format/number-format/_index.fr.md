---
title: Définir le code de format des valeurs des séries de graphique avec Node.js via C++
description: Apprenez comment définir le code de format des valeurs des séries de graphique dans Aspose.Cells for Node.js via C++. Ce guide vous aidera à comprendre comment formater les données de votre série de graphique en utilisant le code de format approprié, vous permettant de présenter vos données de manière précise et professionnelle.
keywords: Aspose.Cells pour Node.js, séries de graphique, code de format des valeurs, formatage, présentation des données, précision, professionnalisme.
linktitle: Format numérique
type: docs
weight: 100
url: /fr/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir le code de format des valeurs des séries de graphique en utilisant la propriété [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--). Cette propriété est non seulement utile pour les séries basées sur la plage dans la feuille de calcul, mais aussi pour celles créées avec un tableau de valeurs.

## **Définir le code de format des valeurs de la série du graphique**
Le code d’exemple suivant ajoute une série dans un graphique vide qui n’avait aucune série auparavant. Il ajoute la série en utilisant un tableau de valeurs. Une fois la série ajoutée, il la formate avec le code $#,##0 en utilisant la propriété [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) et le nombre 10000 devient $10,000. La capture d'écran montre l’effet du code sur le [fichier Excel d’exemple](51740712.xlsx) et le [fichier Excel de sortie](51740713.xlsx) après exécution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Code d'exemple**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
