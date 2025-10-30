---  
title: Arbeiten mit dem Glüheffekt eines Shapes oder Diagramms mit Node.js via C++  
linktitle: Arbeiten mit dem Leuchteffekt von Shape oder Diagramm  
type: docs  
weight: 240  
url: /de/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Erfahren Sie, wie Sie mit dem Glüheffekt von Shapes oder Diagrammen in Node.js mit Aspose.Cells for Node.js via C++ arbeiten.  
---  

## **Mögliche Verwendungsszenarien**  
Aspose.Cells bietet die Eigenschaft [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) zusammen mit der Klasse [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/), um mit dem Glüheffekt von Shape oder Diagramm zu arbeiten. Die Klasse [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) enthält die folgenden Eigenschaften, die je nach Anwendungsanforderungen eingestellt werden können.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **Arbeiten mit dem Leuchteffekt von Form oder Diagramm**  
Das folgende Beispiel lädt die [Quellexcel-Datei](5115407.xlsx), greift auf die erste Shape im ersten Arbeitsblatt zu, setzt die Untereigenschaften der Eigenschaft [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) und speichert anschließend die Arbeitsmappe in der [Ausgabedatei](5115414.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
