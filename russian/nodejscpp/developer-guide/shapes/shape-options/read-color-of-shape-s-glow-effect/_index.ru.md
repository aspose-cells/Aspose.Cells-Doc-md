---
title: Прочитать цвет эффекта свечения формы с помощью Node.js через C++
linktitle: Чтение цвета эффекта свечения фигуры
type: docs
weight: 330
url: /ru/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Узнайте, как прочитать цвет свечения формы, использовав Aspose.Cells for Node.js via C++. 
---

## Возможные сценарии использования

Если вы хотите прочитать цвет свечения любой формы, используйте свойство [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--). Оно поможет найти различные свойства, связанные с цветом свечения формы.

## Прочитать цвет эффекта свечения формы

Пожалуйста, ознакомьтесь с следующим образцом кода и его [исходным файлом Excel](22774108.xlsx) и выводом консоли для вашего справочного значения. Ниже приведен снимок экрана эффекта свечения фигуры в исходном файле Excel, когда просматривается в Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Код Node.js для чтения цвета свечения формы

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

## Вывод в консоль

Вот вывод консоли вышеуказанного образца кода при выполнении с предоставленным [исходным файлом Excel](22774108.xlsx).

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
