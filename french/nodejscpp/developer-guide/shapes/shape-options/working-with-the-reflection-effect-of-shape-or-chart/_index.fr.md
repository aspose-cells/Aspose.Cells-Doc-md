---
title: Travailler avec l effet de réflexion de la forme ou du graphique avec Node.js via C++
linktitle: Travailler avec l effet de réflexion de la forme ou du graphique
type: docs
weight: 210
url: /fr/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Apprenez comment travailler avec l effet de réflexion des formes ou des graphiques en utilisant Aspose.Cells for Node.js via C++. Définissez diverses propriétés de réflexion pour obtenir les résultats souhaités.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells for Node.js via C++ fournit la propriété [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) ainsi que la classe [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) pour travailler avec l'effet de réflexion d'une forme ou d'un graphique. La classe [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) contient les propriétés suivantes qui peuvent être réglées pour obtenir différents résultats selon les besoins de l'application.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **Travailler avec l'effet de réflexion de la forme ou du graphique**
Le code exemple suivant charge le [fichier excel source](5115424.xlsx) et accède à la première forme dans la feuille par défaut. Il définit différentes propriétés de la classe [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) puis enregistre le classeur dans le [fichier excel de sortie](5115423.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
const reflectionEffect = shape.getReflection();
reflectionEffect.setBlur(30);
reflectionEffect.setSize(90);
reflectionEffect.setTransparency(0);
reflectionEffect.setDistance(80);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
