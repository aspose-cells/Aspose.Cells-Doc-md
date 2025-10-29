---  
title: Работа с эффектом свечения формы или диаграммы с помощью Node.js через C++  
linktitle: Работа с эффектом свечения формы или диаграммы  
type: docs  
weight: 240  
url: /ru/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Узнайте, как работать с эффектом свечения форм или диаграмм в Node.js, используя Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  
Aspose.Cells предоставляет свойство [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) вместе с классом [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) для работы с эффектом свечения формы или диаграммы. Класс [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) содержит следующие свойства, которые можно установить для достижения различных результатов в соответствии с требованиями приложения.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **Работа с эффектом свечения формы или диаграммы**  
Следующий пример кода загружает [исходный Excel-файл](5115407.xlsx), получает первый фигуру на первом листе и задает подпараметры свойства [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) и затем сохраняет рабочую книгу в [выходной Excel-файл](5115414.xlsx).  

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
