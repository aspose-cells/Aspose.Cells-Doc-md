---
title: Вставка спарклайна с помощью Node.js через C++
linktitle: Sparklines
type: docs
weight: 160
url: /ru/nodejs-cpp/creating-sparklines/
description: Создайте спарклайн для Excel, используя Aspose.Cells for Node.js via C++.
---

## **Вставить спарклайн**
{{% alert color="primary" %}} 

Спарклайн — это крошечная диаграмма в ячейке листа, которая обеспечивает визуальное представление данных. Используйте спарклайны для отображения тенденций в серии значений, таких как сезонные подъёмы или спады, экономические циклы или для выделения максимальных и минимальных значений. Разместите спарклайн рядом со своими данными для максимального эффекта. Есть три типа спарклайнов: Линия, Столбец и Стек.

{{% /alert %}} 

Создать спарклайн с Aspose.Cells for Node.js via C++ очень просто — используйте приведённые ниже примеры кода:



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);

sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);

// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);

const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);

const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);

// Customize Sparklines

// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight 
group.setLineWeight(1.0);

// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```

## **Продвинутые темы**
- [Использование мерных линий и настройка 3D-формата](/cells/ru/nodejs-cpp/using-sparklines-and-settings-3d-format/)
