---  
title: Определите, по какой оси размещена диаграмма с помощью Node.js через C++  
linktitle: Определите, какая ось существует в диаграмме  
description: Узнайте, как определить, по какой оси расположена созданная с помощью Aspose.Cells for Node.js via C++ диаграмма. Наше руководство поможет вам идентифицировать и получить доступ к различным осям диаграммы, включая категорийные, значений и вторичные оси.  
keywords: Aspose.Cells для Node.js, диаграмма, ося, существование, категория, значение, вторичная.  
type: docs  
weight: 140  
url: /ru/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
Иногда пользователю нужно знать, существует ли конкретная ось в Диаграмме. Например, он хочет узнать, существует ли Вторая Значительная Ось внутри диаграммы или нет. Некоторые диаграммы, такие как Круговая, Взрывная круговая, Пирог, Бар-Пирог, 3D-Пирог, 3D-взрывной Пирог, Бублик, Взрывной бублик и т.д., не имеют оси.  

В следующем образце кода демонстрируется использование [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) для определения, имеет ли образецная диаграмма основную и вторичную категориальные и числовые оси.  
{{% /alert %}}  

Следующий пример кода демонстрирует использование [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) для определения наличия в образцовой диаграмме Первичной и Вторичной Категориальной и Значительной Оси.  

## Код Node.js для определения, какая ось есть в диаграмме  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
// Create workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Check if there are any charts before accessing
const charts = worksheet.getCharts();
if (charts.getCount() === 0) {
console.log("No charts found in the worksheet.");
return;
}

// Access the chart
const chart = charts.get(0);

// Determine which axis exists in chart
let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
console.log("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
console.log("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
console.log("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
console.log("Has Secondary Value Axis: " + ret);
```  

## Консольный вывод, сгенерированный образцовым кодом  

Вывод консоли этого кода показан ниже, он показывает true для Первичной Категориальной и Значительной Оси и false для Вторичной Категориальной и Значительной Оси.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
