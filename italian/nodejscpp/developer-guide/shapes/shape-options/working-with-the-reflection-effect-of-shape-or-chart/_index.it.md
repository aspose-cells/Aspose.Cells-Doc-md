---
title: Lavorare con l effetto di riflessione di forma o grafico con Node.js tramite C++
linktitle: Lavorare con l effetto Reflex della forma o del grafico
type: docs
weight: 210
url: /it/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Impara come lavorare con l effetto di riflessione di forme o grafici usando Aspose.Cells for Node.js via C++. Imposta varie proprietà di riflessione per ottenere i risultati desiderati.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells for Node.js via C++ fornisce la proprietà [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) insieme alla classe [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) per lavorare con l'effetto di riflessione di forma o grafico. La classe [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) contiene le seguenti proprietà che possono essere impostate per ottenere risultati diversi in base alle esigenze dell'applicazione.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **Lavorare con l'Effetto Riflessione di una Forma o di un Grafico**
Il seguente esempio di codice carica il [file excel di origine](5115424.xlsx) e accede alla prima forma nel foglio di lavoro predefinito. Imposta proprietà diverse della classe [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) e poi salva il workbook nel [file excel di output](5115423.xlsx).

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
