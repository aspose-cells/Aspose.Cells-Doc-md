---  
title: Arbeiten mit dem Schatteneffekt von Form oder Diagramm mit Node.js über C++  
linktitle: Arbeiten mit dem Schatten Effekt von Form oder Diagramm  
type: docs  
weight: 220  
url: /de/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Erfahren Sie, wie Sie mit dem Schatteneffekt von Formen oder Diagrammen mit Aspose.Cells for Node.js via C++ arbeiten.  
---  

## **Mögliche Verwendungsszenarien**  
Aspose.Cells for Node.js via C++ bietet die [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) Eigenschaft zusammen mit der [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) Klasse, um mit dem Schatteneffekt von Form oder Diagramm zu arbeiten. Die [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) Klasse enthält die folgenden Eigenschaften, die je nach Anwendungsanforderung eingestellt werden können, um unterschiedliche Ergebnisse zu erzielen.  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **Arbeiten mit dem Schatten-Effekt von Form oder Diagramm**  
Der folgende Beispielcode lädt die [Quelldatei Excel](5115425.xlsx) und greift auf die erste Form im ersten Arbeitsblatt zu. Er setzt die Untereigenschaften der [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) Eigenschaft und speichert dann die Arbeitsmappe in der [Ausgabedatei Excel](5115411.xlsx).  

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

// Set the shadow effect of the shape, set its Angle, Blur, Distance and Transparency properties
const shadowEffect = shape.getShadowEffect();
shadowEffect.setAngle(150);
shadowEffect.setBlur(4);
shadowEffect.setDistance(45);
shadowEffect.setTransparency(0.3);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

