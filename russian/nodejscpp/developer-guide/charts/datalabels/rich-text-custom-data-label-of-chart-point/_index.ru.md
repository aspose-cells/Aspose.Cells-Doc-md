---
title: Пользовательская богатая текстовая метка данных точки диаграммы с помощью Node.js через C++
description: Научитесь добавлять богатые текстовые пользовательские метки данных к точкам диаграммы в Aspose.Cells for Node.js via C++. Наш гид покажет, как форматировать метки с использованием различных шрифтов, цветов и вариантов выравнивания, чтобы улучшить внешний вид и читаемость ваших диаграмм.
keywords: Aspose.Cells for Node.js via C++, создание диаграмм, богатый текст, пользовательские метки данных, шрифты, цвета, выравнивание, внешний вид, читаемость.
type: docs
weight: 10
url: /ru/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для создания богатых пользовательских меток данных для точек диаграммы. Aspose.Cells предоставляет метод [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-), который возвращает объект [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting), который можно использовать для установки свойств шрифта текста, таких как цвет, жирность и т. д.

{{% /alert %}}

## Многострочная пользовательская подпись данных точки диаграммы

Следующий код получает первую точку диаграммы первой серии, устанавливает ее текст и затем задает шрифт первых 10 символов, задавая их цвет красным и делая их жирными — **true**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
