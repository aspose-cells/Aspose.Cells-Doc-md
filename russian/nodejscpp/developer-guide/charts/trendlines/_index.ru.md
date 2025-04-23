---
title: Получить текст уравнения трендлайна диаграммы с помощью Node.js через C++.
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для получения текста уравнения трендлайна в диаграмме, созданной в Microsoft Excel. Наш гид покажет, как получить и извлечь уравнение трендлайна для дальнейшего анализа или отображения.
keywords: Aspose.Cells for Node.js via C++, Трендлайн диаграммы, Текст уравнения, Microsoft Excel, Анализ данных, Отображение.
linktitle: Трендовые линии
type: docs
weight: 110
url: /ru/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Вы можете получить текст уравнения трендлайна диаграммы, используя Aspose.Cells for Node.js via C++. Aspose.Cells предоставляет свойство [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--), которое возвращает текст уравнения трендлайна диаграммы. Для использования этого свойства сначала необходимо вызвать метод [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--).

{{% /alert %}}

Следующий скриншот показывает диаграмму с трендлайном и его текст уравнения, выделенный красным цветом. Мы получим этот текст, используя свойство [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) в следующем примере.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Код Node.js для получения текста уравнения трендлайна диаграммы

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
