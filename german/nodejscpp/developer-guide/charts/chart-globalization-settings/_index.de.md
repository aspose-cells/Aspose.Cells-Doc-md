---  
title: Verwendung der ChartGlobalizationSettings Klasse zur Einstellung verschiedener Sprachen für Diagrammelemente mit Node.js über C++  
linktitle: Verwendung der ChartGlobalizationSettings Klasse zum Einstellen einer anderen Sprache für das Diagrammkomponente  
description: Erfahren Sie, wie Sie die ChartGlobalizationSettings Klasse in Aspose.Cells for Node.js via C++ verwenden, um verschiedene Sprachen für Diagrammelemente festzulegen. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie Diagrammelemente, Beschriftungen und Legenden lokalisieren.  
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Diagrammglobalisierung, Sprachen, Lokalisierung, ChartGlobalizationSettings, Elemente, Beschriftungen, Legenden.  
type: docs  
weight: 2200  
url: /de/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **Mögliche Verwendungsszenarien**  

Die Aspose.Cells APIs haben die [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) Klasse bereitgestellt, um Szenarien zu behandeln, in denen der Benutzer Diagrammelemente auf verschiedene Sprachen einstellen und benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabelle erstellen möchte.  

## **Einführung in die ChartGlobalizationSettings-Klasse**  

Die [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) Klasse bietet derzeit die folgenden 8 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um z. B. den AxisTitle Namen, AxisUnit Namen, ChartTitle Namen usw. in verschiedene Sprachen zu übersetzen.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--): Gibt den Titel für die Achse zurück.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-): Gibt den Namen der Achseneinheit zurück.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--): Gibt den Titel des Diagramms zurück.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--): Gibt den Namen der Abnahme für die Legende zurück.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): Holt den Namen von Increase für Legenden.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--): Gibt den Namen des Gesamtwerts für die Legende zurück.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--): Gibt den Namen der "Andere"-Beschriftungen für das Diagramm zurück.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--): Gibt den Namen der Serie im Diagramm zurück.  

### **Benutzerdefinierte Sprachübersetzung**  
Hier erstellen wir ein Wasserfalldiagramm basierend auf den folgenden Daten. Die Namen der Diagrammkomponenten werden im Diagramm auf Englisch angezeigt. Wir verwenden ein Beispiel für die türkische Sprache, um zu zeigen, wie der Diagrammtitel, die Legenden-Abnahme/Zunahme-Namen, der Gesamtwert und der Achsentitel auf Türkisch angezeigt werden.  

![todo:image_alt_text](sample.png)  

## **Beispielcode**  
Der folgende Beispielcode lädt die [Beispieldatei Excel](waterfall.xlsx).  

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

## Ausgabe, die vom Beispielcode generiert wurde  

Dies ist die Konsolenausgabe des obigen Beispiels.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

