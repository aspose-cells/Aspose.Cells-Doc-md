---  
title: Uso de la clase ChartGlobalizationSettings para establecer diferentes idiomas para el componente del gráfico con Node.js mediante C++  
linktitle: Usar la clase ChartGlobalizationSettings para establecer un idioma diferente para el componente del gráfico  
description: Aprende cómo usar la clase ChartGlobalizationSettings en Aspose.Cells for Node.js via C++ para establecer diferentes idiomas para los componentes del gráfico. Nuestra guía te ayudará a entender cómo localizar los elementos, etiquetas y leyendas del gráfico.  
keywords: Aspose.Cells for Node.js via C++, gráficos, globalización de gráficos, idiomas, localización, ChartGlobalizationSettings, elementos, etiquetas, leyendas.  
type: docs  
weight: 2200  
url: /es/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **Escenarios de uso posibles**  

Las API de Aspose.Cells han expuesto la clase [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) para tratar escenarios donde el usuario desea establecer componentes del gráfico en diferentes idiomas y etiquetas personalizadas para los subtotales en una hoja de cálculo.  

## **Introducción a la clase ChartGlobalizationSettings**  

La clase [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) actualmente ofrece los siguientes 8 métodos que pueden ser anulados en una clase personalizada para traducir, como el nombre del Título del Eje, la Unidad del Eje, el Título del Gráfico, etc., a diferentes idiomas.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--): Obtiene el nombre del Título para el Eje.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-): Obtiene el nombre de la Unidad del Eje.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--): Obtiene el nombre del Título del Gráfico.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--): Obtiene el nombre de Disminución para la Leyenda.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): Obtiene el nombre de Incremento para la leyenda.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--): Obtiene el nombre de Total para la Leyenda.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--): Obtiene el nombre de las etiquetas "Otro" para el Gráfico.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--): Obtiene el nombre de la Serie en el Gráfico.  

### **Traducción personalizada de idioma**  
Aquí, crearemos un gráfico de cascada basado en los siguientes datos. Los nombres de los componentes del gráfico se mostrarán en inglés en el gráfico. Utilizaremos un ejemplo en idioma turco para mostrar cómo mostrar el Título del Gráfico, los nombres de Aumento/Disminución de la Leyenda, el nombre de Total y el Título del Eje en turco.  

![todo:image_alt_text](sample.png)  

## **Código de muestra**  
El siguiente código de ejemplo carga el [archivo de Excel de muestra](waterfall.xlsx).  

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

Resultado generado por el código de ejemplo  

Este es el resultado de consola del código de ejemplo anterior.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
