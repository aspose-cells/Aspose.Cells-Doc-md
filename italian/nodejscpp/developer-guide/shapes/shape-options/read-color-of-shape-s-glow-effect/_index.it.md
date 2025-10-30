---
title: Leggi il colore dell’effetto bagliore di una forma con Node.js tramite C++
linktitle: Leggi il colore dell effetto di luce esterna della forma
type: docs
weight: 330
url: /it/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Impara come leggere il colore dell’effetto bagliore di una forma usando Aspose.Cells for Node.js via C++. 
---

## Possibili scenari di utilizzo

Se vuoi leggere il colore dell’effetto bagliore di una forma qualsiasi, utilizza la proprietà [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--). Ti aiuterà a trovare le varie proprietà relative al colore dell’effetto bagliore della forma.

## Leggere il colore dell'effetto di bagliore di una forma

Si prega di vedere il seguente codice di esempio e il suo [file excel di origine](22774108.xlsx) e l'output della console per il vostro riferimento. La seguente schermata mostra l'effetto di luce esterna della forma all'interno del file excel di origine quando visualizzato in Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Codice Node.js per leggere il colore dell’effetto bagliore di una forma

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

## Output della console

Ecco l'output della console del codice di esempio precedente quando eseguito con il seguente [file excel di origine](22774108.xlsx).

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
