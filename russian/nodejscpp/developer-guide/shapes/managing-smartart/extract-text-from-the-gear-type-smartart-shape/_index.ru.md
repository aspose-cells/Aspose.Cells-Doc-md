---
title: Извлечение текста из фигуры SmartArt типа Gear с помощью Node.js через C++
linktitle: Извлечение текста из формы SmartArt типа Gear
type: docs
weight: 500
url: /ru/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Узнайте, как извлечь текст из фигуры SmartArt типа Gear с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Aspose.Cells может извлечь текст из фигуры Smart Art типа Gear. Для этого сначала преобразуйте фигуру Smart Art в группу форм с помощью метода [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). Затем получите массив всех отдельных фигур, составляющих группу, с помощью метода [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--). В конце можете перебрать все отдельные фигуры по очереди и извлечь их текст, используя свойство [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).

## **Извлечение текста из формы SmartArt с шестеренчатым типом**

В следующем примере кода загружается [образец файла Excel](67338483.xlsx), содержащий умную форму Gear Type Smart Art. Затем извлекается текст из ее индивидуальных форм, как обсуждалось выше. Пожалуйста, ознакомьтесь с выводом консоли в приведенном ниже примере кода в качестве примера.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **Вывод в консоль**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
