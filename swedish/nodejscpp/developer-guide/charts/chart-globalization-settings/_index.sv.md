---  
title: Använda ChartGlobalizationSettings klassen för att ställa in olika språk för diagramkomponenten med Node.js via C++  
linktitle: Utvecklare kan inte bara kontrollera synligheten av stora rutnätlinjer utan också andra egenskaper inklusive dess färg osv.  
description: Lär dig hur du använder ChartGlobalizationSettings klassen i Aspose.Cells for Node.js via C++ för att ställa in olika språk för diagramkomponenter. Vår guide hjälper dig att förstå hur du lokaliserar diagram element, etiketter och legender.  
keywords: Aspose.Cells for Node.js via C++, diagram, diagramglobalisering, språk, lokalisering, ChartGlobalizationSettings, element, etiketter, legender.  
type: docs  
weight: 2200  
url: /sv/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **Möjliga användningsscenario**  

Aspose.Cells API:er har exponerat [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)-klassen för att hantera scenarier där användaren vill ställa in diagramkomponenter till olika språk och anpassade etiketter för deltotaler i ett kalkylblad.  

## **Introduktion till ChartGlobalizationSettings-klassen**  

Klass [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) erbjuder för närvarande följande 8 metoder som kan åsidosättas i en anpassad klass för att översätta till exempel AxisTitle-namn, AxisUnit-namn, ChartTitle-namn och så vidare till olika språk.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--): Hämtar namnet på titeln för axeln.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-): Hämtar namnet på axelenhet.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--): Hämtar namnet på diagramtiteln.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--): Hämtar namnet på minskningen för förklaringen.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): Hämtar namnet på Increase för Legend.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--): Hämtar namnet på totalen för förklaringen.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--): Hämtar namnet på "Annan" etiketter för diagrammet.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--): Hämtar namnet på serier i diagrammet.  

### **Anpassad språköversättning**  
Här kommer vi att skapa en stapeldiagram baserat på följande data. Namnen på diagramkomponenterna kommer att visas på engelska i diagrammet. Vi kommer att använda ett turkiskt språkexempel för att visa hur man visar diagramtitel, förklarings-ökning/minskning, totalt namn och axelns titel på turkiska.  

![todo:image_alt_text](sample.png)  

## **Exempelkod**  
Följande exempelkod laddar [prov Excel-filen](vattenfall.xlsx).  

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

## Utdata genererad av provkoden  

Detta är konsoloutputen för ovanstående exempelkod.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

