---
title: Получить лист графика с помощью Node.js через C++
linktitle: Получить рабочий лист диаграммы
description: Научитесь получать связанный с графиком лист Excel с помощью Aspose.Cells for Node.js via C++. Эффективно получайте доступ и управляйте базовыми данными графика.
keywords: Aspose.Cells для Node.js, графики Excel, листы, манипуляции с данными, базовые данные, операции, Node.js через C++
type: docs
weight: 1000
url: /ru/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Иногда вам нужно получить доступ к листу рабочей книги из ссылки на диаграмму. Aspose.Cells предоставляет свойство [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--), которое возвращает ссылку на лист рабочей книги, содержащий диаграмму.

{{% /alert %}}

Следующий пример показывает, как использовать свойство [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--). Сначала код выводит название листа, затем обращается к первому графику на листе. После этого снова выводит название листа, используя свойство [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

Ниже приведен вывод консоли, который получается в результате примера. Как видно, он дважды выводит одно и то же имя листа.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
