---
title: Измените направление меток на осях с помощью Node.js через C++
linktitle: Изменение направления меток делений
description: Узнайте, как изменить направление меток осей в Aspose.Cells для Node.js. Наше руководство поможет вам понять, как настроить ориентацию меток на осях, включая горизонтальные, вертикальные и наклонные ориентации.
keywords: Aspose.Cells для Node.js, метки осей, направление, ориентация, оси, горизонтальные, вертикальные, наклонные.
type: docs
weight: 170
url: /ru/nodejs-cpp/change-tick-label-direction/
---

## **Изменение направления меток делений**

Aspose.Cells позволяет изменять направление меток осей, используя свойство [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--). Свойство [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) принимает значение перечисления [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype). Перечисление [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) включает следующие члены:

- Горизонтальное
- Вертикальное
- Повернуть90
- Повернуть270
- Стековое

На следующем изображении приведено сравнение исходного и выходного файлов

### **Изображение исходного файла**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Изображение выходного файла**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Следующий фрагмент кода изменяет направление меток делений с Повернуть90 на Горизонтальное.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

Исходные и выходные файлы можно загрузить по следующим ссылкам.

[Исходный файл](105480221.xlsx)

[Выходной файл](105480223.xlsx)
{{< app/cells/assistant language="nodejs-cpp" >}}
