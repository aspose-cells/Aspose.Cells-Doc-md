---
title: Travailler avec le format 3D (ThreeDFormat) de la forme ou du graphique avec Node.js via C++
linktitle: Travailler avec le ThreeDFormat de la forme ou du graphique
type: docs
weight: 250
url: /fr/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells for Node.js via C++ fournit la propriété [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) ainsi que la classe [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) pour travailler avec le format 3D d'une forme ou d'un graphique. La classe [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) contient différentes propriétés pouvant être réglées pour obtenir différents résultats selon les besoins de l'application.

## **Travailler avec le ThreeDFormat de la forme ou du graphique**
Le code exemple suivant charge le [fichier excel source](5115419.xlsx) et accède à la première forme dans la première feuille, en réglant les sous-propriétés de [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) puis en enregistrant le classeur dans le [fichier excel de sortie](5115410.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
