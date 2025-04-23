---  
title: Читать подписи осей после расчета диаграммы с помощью Node.js через C++  
linktitle: Чтение меток оси после вычисления диаграммы  
description: Узнайте, как читать подписи осей в Aspose.Cells for Node.js via C++ после расчета диаграммы. Наше руководство покажет вам, как получить доступ и извлечь подписи осей, включая их форматирование и расположение.  
keywords: Aspose.Cells для Node.js, диаграмма, подписи осей, расчет, чтение, доступ, извлечение, форматирование, расположение, Node.js через C++  
type: docs  
weight: 90  
url: /ru/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **Возможные сценарии использования**

Вы можете прочитать подписи осей вашей диаграммы после расчетов с помощью метода [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--). Для этого используйте метод [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--), который вернет список подписей осей.

## **Чтение меток оси после вычисления диаграммы**

Пожалуйста, см. следующий образец кода, который загружает [образец файла Excel](ReadAxisLabels.xlsx) и читает подписи осей категорий диаграммы на первом листе. Затем выводятся значения подписей осей на консоль. См. пример вывода на консоль приведенный ниже в качестве справки.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **Вывод в консоль**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  

