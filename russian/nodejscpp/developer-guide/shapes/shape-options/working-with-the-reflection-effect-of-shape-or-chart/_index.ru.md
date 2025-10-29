---
title: Работа с эффектом отражения формы или диаграммы с Node.js через C++
linktitle: Работа с эффектом отражения формы или диаграммы
type: docs
weight: 210
url: /ru/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Узнайте, как работать с эффектом отражения форм или диаграмм, используя Aspose.Cells for Node.js via C++. Устанавливайте различные свойства отражения для достижения желаемых результатов.
---

## **Возможные сценарии использования**
Aspose.Cells for Node.js via C++ предоставляет свойство [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) вместе с классом [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) для работы с эффектом отражения формы или диаграммы. Класс [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) содержит следующие свойства, которые можно установить для получения различных результатов в соответствии с требованиями приложения.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **Работа с эффектом отражения формы или диаграммы**
Следующий пример кода загружает исходный Excel-файл (5115424.xlsx) и обращается к первой форме на листе по умолчанию. Он устанавливает различные свойства класса [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) и сохраняет рабочую книгу в выходном Excel-файле (5115423.xlsx).

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
