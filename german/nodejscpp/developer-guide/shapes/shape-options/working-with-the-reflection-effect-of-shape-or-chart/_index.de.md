---
title: Arbeiten mit dem Reflexionseffekt von Form oder Diagramm mit Node.js über C++
linktitle: Arbeiten mit dem Spiegeleffekt von Form oder Diagramm
type: docs
weight: 210
url: /de/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Erfahren Sie, wie Sie mit dem Reflexionseffekt von Formen oder Diagrammen mit Aspose.Cells for Node.js via C++ arbeiten. Stellen Sie verschiedene Reflexioneigenschaften ein, um gewünschte Ergebnisse zu erzielen.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells for Node.js via C++ bietet die [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) Eigenschaft zusammen mit der [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) Klasse, um mit dem Reflexionseffekt von Form oder Diagramm zu arbeiten. Die [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) Klasse enthält die folgenden Eigenschaften, die je nach Anwendungsanforderung eingestellt werden können, um unterschiedliche Ergebnisse zu erzielen.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **Arbeiten mit dem Spiegeleffekt von Form oder Diagramm**
Der folgende Beispielcode lädt die [Quelldatei Excel](5115424.xlsx) und greift auf die erste Form im Standardarbeitsblatt zu. Er setzt verschiedene Eigenschaften der [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) Klasse und speichert dann die Arbeitsmappe in der [Ausgabedatei Excel](5115423.xlsx).

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
