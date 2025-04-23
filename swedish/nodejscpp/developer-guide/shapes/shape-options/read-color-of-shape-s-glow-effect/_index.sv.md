---
title: Läs färgen på shape s glödeffekt med Node.js via C++
linktitle: Läs färgen för formens glow effekt
type: docs
weight: 330
url: /sv/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Lär dig att läsa färgen på en shapes glödeffekt med Aspose.Cells for Node.js via C++. 
---

## Möjliga användningsfall

 Om du vill läsa färgen på glödeffekten för vilken shape som helst, använd då [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)-egenskapen. Den hjälper dig att hitta olika egenskaper relaterade till färgen på shape'ns glödeffekt.

## Läs färgen på glödeffekten av en form

Se följande exempelkod och dess [käll-Excelfil](22774108.xlsx) och konsoloutputen för din referens. Följande skärmbild visar ljuseffekten hos formen i käll-Excelfilen när den visas i Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Node.js-kod för att läsa färg på shape's glödeffekt

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Read the source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sourceGlowEffectColor.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the shape
const shape = sheet.getShapes().get(0);

// Read the glow effect color and its various properties
const effect = shape.getGlow();
const color = effect.getColor();
console.log("Color: " + color.getColor());
console.log("ColorIndex: " + color.getColorIndex());
console.log("IsShapeColor: " + color.isShapeColor());
console.log("Transparency: " + color.getTransparency());
console.log("Type: " + color.getType());
```

## Konsoloutput

Här är konsoloutputen av ovanstående exempelkod när den körs med den angivna [käll-Excelfilen](22774108.xlsx).

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
