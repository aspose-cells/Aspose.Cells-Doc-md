---
title: Работа с ThreeDFormat формы или диаграммы с Node.js через C++
linktitle: Работа с ThreeDFormat формы или диаграммы
type: docs
weight: 250
url: /ru/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Возможные сценарии использования**
Aspose.Cells for Node.js via C++ предоставляет свойство [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) вместе с классом [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) для работы с 3D-форматом формы или диаграммы. Класс [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) содержит различные свойства, которые можно установить для достижения различных результатов в соответствии с требованиями приложения.

## **Работа с ThreeDFormat формы или диаграммы**
Следующий пример кода загружает исходный Excel-файл (5115419.xlsx) и обращается к первой форме на листе, устанавливает под-свойства [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) и сохраняет рабочую книгу в выходном Excel-файле (5115410.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
