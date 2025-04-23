---  
title: Utilizzo della classe ChartGlobalizationSettings per impostare lingue differenti per il componente grafico con Node.js tramite C++  
linktitle: Utilizzare la classe ChartGlobalizationSettings per impostare una lingua diversa per il componente del grafico  
description: Impara come usare la classe ChartGlobalizationSettings in Aspose.Cells for Node.js via C++ per impostare lingue diverse per i componenti del grafico. La nostra guida ti aiuterà a capire come localizzare gli elementi del grafico, le etichette e le legende.  
keywords: Aspose.Cells for Node.js via C++, grafici, globalizzazione dei grafici, lingue, localizzazione, ChartGlobalizationSettings, elementi, etichette, legende.  
type: docs  
weight: 2200  
url: /it/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **Possibili Scenari di Utilizzo**  

Le API di Aspose.Cells hanno esposto la classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) per gestire gli scenari in cui l'utente desidera impostare componenti del grafico in lingue diverse e etichette personalizzate per i subtotali in un foglio di calcolo.  

## **Introduzione alla classe ChartGlobalizationSettings**  

La classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) attualmente offre i seguenti 8 metodi che possono essere sovrascritti in una classe personalizzata per tradurre nomi come AxisTitle, AxisUnit, ChartTitle e altri in diverse lingue.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--): Ottiene il nome del Titolo per l'Asse.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-): Ottiene il Nome dell'Unità di Asse.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--): Ottiene il nome del Titolo del Grafico.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--): Ottiene il nome di Diminuzione per la Leggenda.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): Ottiene il nome di Increase per la legenda.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--): Ottiene il nome di Totale per la Leggenda.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--): Ottiene il nome delle etichette "Altro" per il Grafico.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--): Ottiene il nome di Serie nel Grafico.  

### **Traduzione personalizzata**  
Qui, creeremo un grafico a barre basato sui seguenti dati. I nomi dei componenti del grafico verranno visualizzati in inglese nel grafico. Useremo un esempio in lingua turca per mostrare come visualizzare il Titolo del Grafico, i nomi di Aumento/Diminuzione della Leggenda, il nome Totale e il Titolo dell'Asse in turco.  

![todo:image_alt_text](sample.png)  

## **Codice di Esempio**  
Il seguente codice di esempio carica il [file Excel di esempio](waterfall.xlsx).  

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

## Output generato dal codice di esempio  

Questo è l'output console del codice di esempio precedente.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

