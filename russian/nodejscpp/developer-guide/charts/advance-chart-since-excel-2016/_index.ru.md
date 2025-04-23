---  
title: Чтение и управление графиками Excel 2016 с помощью Node.js через C++  
linktitle: Чтение и манипулирование диаграммами Excel 2016  
description: Узнайте, как читать и управлять графиками Excel 2016 с помощью Aspose.Cells for Node.js via C++. В этом руководстве показано, как получать доступ и изменять различные свойства графика.  
keywords: Aspose.Cells для Node.js, графики Excel 2016, чтение, управление, метки данных, цвета серий, макеты, иерархическая диаграмма, круговая диаграмма.  
type: docs  
weight: 48  
url: /ru/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **Возможные сценарии использования**  
Aspose.Cells теперь поддерживает чтение и изменение диаграмм Microsoft Excel 2016, которые отсутствуют в Microsoft Excel 2013 и более ранних версиях.  
## **Чтение и манипулирование диаграммами Excel 2016**  
Следующий пример кода загружает [исходный файл Excel](22774101.xlsx), содержащий графики Excel 2016 на первом листе. Он по очереди читает все графики и изменяет их заголовки в соответствии с типом графика. На следующем скриншоте показан исходный файл Excel до выполнения кода. Как видно, заголовок графика одинаков для всех графиков.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Ниже показан скриншот [выходного файла Excel](22774104.xlsx) после выполнения кода. Как видно, заголовок диаграммы изменен в соответствии с их типом диаграммы.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Образец кода**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "excel2016Charts.xlsx");

// Load source excel file containing excel 2016 charts
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet which contains the charts
const sheet = workbook.getWorksheets().get(0);

// Access all charts one by one and read their types
for (let i = 0; i < sheet.getCharts().getCount(); i++) {
// Access the chart
const ch = sheet.getCharts().get(i);

// Print chart type
console.log(ch.getType());

// Change the title of the charts as per their types
ch.getTitle().setText("Chart Type is " + ch.getType().toString());
}

// Save the workbook
workbook.save(path.join(dataDir, "out_excel2016Charts.xlsx"));
```  
## **Вывод в консоль**  
Вот вывод консоли из приведенного выше образца кода при выполнении с предоставленным [исходным файлом Excel](22774101.xlsx).

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Продвинутые темы**  
- [Создание водопадной диаграммы](/cells/ru/nodejs-cpp/creating-waterfall-chart/)  
- [Создание диаграммы дерева](/cells/ru/nodejs-cpp/creating-treemap-chart/)  
- [Создание диаграммы Sunburst](/cells/ru/nodejs-cpp/creating-sunburst-chart/)  

