---  
title: Работа с эффектом тени формы или диаграммы с Node.js через C++  
linktitle: Работа с эффектом тени формы или диаграммы  
type: docs  
weight: 220  
url: /ru/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Узнайте, как работать с эффектом тени форм или диаграмм, используя Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  
Aspose.Cells for Node.js via C++ предоставляет свойство [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) вместе с классом [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) для работы с эффектом тени формы или диаграммы. Класс [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) содержит следующие свойства, которые можно установить для получения различных результатов в соответствии с требованиями приложения.  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **Работа с теневым эффектом формы или диаграммы**  
Следующий пример кода загружает исходный Excel-файл (5115425.xlsx) и обращается к первой форме на первом листе, устанавливает под-свойства свойства [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) и сохраняет рабочую книгу в выходном Excel-файле (5115411.xlsx).  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
