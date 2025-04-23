---  
title: Использование класса ChartGlobalizationSettings для установления различных языков для компонента графика с Node.js через C++  
linktitle: Используя класс ChartGlobalizationSettings для установки другого языка для компонента диаграммы  
description: Узнайте, как использовать класс ChartGlobalizationSettings в Aspose.Cells for Node.js via C++, чтобы установить разные языки для элементов графика. Наше руководство поможет вам понять, как локализовать элементы графика, метки и легенды.  
keywords: Aspose.Cells for Node.js via C++, построение графиков, глобализация графика, языки, локализация, ChartGlobalizationSettings, элементы, метки, легенды.  
type: docs  
weight: 2200  
url: /ru/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **Возможные сценарии использования**  

API Aspose.Cells предоставили класс [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) для сценариев, когда пользователь желает установить язык элементов графика и пользовательские метки для промежуточных итогов в электронной таблице.  

## **Введение в класс ChartGlobalizationSettings**  

Класс [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) в настоящее время предлагает 8 методов, которые можно переопределить в пользовательском классе для перевода таких элементов, как название AxisTitle, название AxisUnit, название ChartTitle и т. д. на разные языки.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--): Получает название заголовка для оси.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-): Получает название единицы оси.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--): Получает название заголовка диаграммы.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--): Получает название уменьшения для легенды.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): Получает название Increase для легенды.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--): Получает название итога для легенды.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--): Получает название меток "Другие" для диаграммы.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--): Получает название серии в диаграмме.  

### **Пользовательский перевод языка**  
Здесь мы создадим водопадную диаграмму на основе следующих данных. Названия компонентов диаграммы будут отображаться на английском языке. Мы воспользуемся турецким примером, чтобы показать, как отображать заголовок диаграммы, наименования увеличения/уменьшения в легенде, общее наименование и заголовок оси на турецком языке.  

![todo:image_alt_text](sample.png)  

## **Образец кода**  
В следующем образце кода загружается [образец файла Excel](waterfall.xlsx).  

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TurkeyChartGlobalizationSettings extends AsposeCells.ChartGlobalizationSettings {
getChartTitleName() {
return "Grafik Başlığı"; // Chart Title
}
getLegendIncreaseName() {
return "Artış"; // Increase
}
getLegendDecreaseName() {
return "Düşüş"; // Decrease
}
getLegendTotalName() {
return "Toplam"; // Total
}
getAxisTitleName() {
return "Eksen Başlığı"; // Axis Title
}
}

async function chartGlobalizationSettingsTest() {
// Create an instance of existing Workbook
const dataDir = path.join(__dirname, "data");
const pathName = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(pathName);

// Set custom chartGlobalizationSettings, here is TurkeyChartGlobalizationSettings
workbook.getSettings().getGlobalizationSettings().setChartSettings(new TurkeyChartGlobalizationSettings());

// Get the worksheet 
const worksheet = workbook.getWorksheets().get(0);
const chartCollection = worksheet.getCharts();

// Load the chart from source worksheet
const chart = chartCollection.get(0);

// Chart Calculate
chart.calculate();

// Get the chart title
const title = chart.getTitle();
console.log("\nWorkbook chart title: " + title.getText());

const legendEntriesLabels = chart.getLegend().getLegendLabels();

// Output the name of the Legend 
legendEntriesLabels.forEach(label => {
console.log("\nWorkbook chart legend: " + label);
```  

## Вывод, созданный образцовым кодом  

Это вывод консоли вышеуказанного образца кода.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

