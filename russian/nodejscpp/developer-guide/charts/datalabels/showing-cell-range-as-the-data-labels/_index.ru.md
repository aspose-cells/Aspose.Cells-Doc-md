---  
title: Отображение диапазона ячеек в качестве меток данных с помощью Node.js через C++  
linktitle: Отображение диапазона ячеек в качестве меток данных  
description: Научитесь показывать диапазон ячеек в качестве меток данных в диаграммах с помощью Aspose.Cells for Node.js via C++. Наш гид продемонстрирует, как связать метки с источником данных и оформить их для отображения точной и значимой информации.  
keywords: Aspose.Cells for Node.js via C++, создание диаграмм, метки данных, диапазон ячеек, источник данных, форматирование, точность, информационная ценность.  
type: docs  
weight: 130  
url: /ru/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
В Microsoft Excel 2013 можно отображать диапазон ячеек для меток данных. Aspose.Cells для Node.js поддерживает эту функцию.  
{{% /alert %}}  

## **Флажок для отображения диапазона ячеек в качестве меток данных**  

Чтобы показать диапазон ячеек в качестве меток данных в Microsoft Excel:  

1. Выберите метки данных ряда и щелкните правой кнопкой мыши, чтобы открыть контекстное меню.  
1. Выберите **Формат меток данных**. Опции меток отображаются.  
1. Выберите или снимите флажок у опции **Метка содержит - значение из ячеек**.  

Пример кода ниже получает метки данных серии диаграммы и устанавливает свойство [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) в **true**, чтобы выбрать опцию **Label Contains - Value From Cells**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
