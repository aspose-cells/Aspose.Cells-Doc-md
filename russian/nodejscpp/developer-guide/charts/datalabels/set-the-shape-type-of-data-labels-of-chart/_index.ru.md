---
title: Установить тип формы меток данных диаграммы с помощью Node.js через C++
linktitle: Установка формы меток данных диаграммы
description: Научитесь устанавливать тип формы меток данных на диаграммах с помощью Aspose.Cells for Node.js via C++. Этот гид объяснит доступные типы форм и покажет, как выбрать подходящую форму для ваших меток данных, чтобы улучшить презентацию и удобство использования.
keywords: Aspose.Cells for Node.js via C++, создание диаграмм, метки данных, типы форм, презентация, удобство использования.
type: docs
weight: 110
url: /ru/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Возможные сценарии использования**
Вы можете изменить тип формы метки данных диаграммы, используя свойство `DataLabels.shapeType`. Оно принимает значение перечисления `DataLabelShapeType` и соответственно меняет тип формы метки данных. Некоторые из его значений:

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Установка типа формы меток данных диаграммы**
Следующий пример кода изменяет тип формы меток данных диаграммы на `DataLabelShapeType.WedgeEllipseCallout`. Обратите внимание на [пример файла Excel](60489778.xlsx), используемый в этом коде, и на [сгенерированный файл Excel](60489779.xlsx). Скриншот показывает эффект от кода на примере файла Excel.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Образец кода**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
