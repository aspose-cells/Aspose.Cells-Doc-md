---
title: Asse Z con Node.js tramite C++
description: Impara come lavorare con l asse Z in Aspose.Cells for Node.js via C++. La nostra guida ti aiuterà a capire come configurare e personalizzare l asse Z, inclusi scala e etichette, per migliorare i tuoi grafici.
keywords: Aspose.Cells for Node.js via C++, asse Z, creazione di grafici, configurazione, personalizzazione, scala, etichette.
type: docs
weight: 210
url: /it/nodejs-cpp/z-axis/
---

## **Possibili Scenari di Utilizzo**
Per alcuni grafici 3D come colonne 3D, coni 3D o piramidi 3D che hanno un asse di profondità (serie), noto anche come asse Z, che puoi modificare. Puoi specificare l'intervallo tra i segni degli tick, le etichette dell'asse e altre operazioni.

## **Gestire gli assi principali e secondari come in Microsoft Excel**
Si prega di vedere il seguente esempio di codice che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro. Quindi aggiungiamo un grafico e impostiamo il tipo di grafico su Column3D, poi puoi vedere anche l'Asse Z chiamato anche Asse di profondità. 

![todo:image_alt_text](excel.png)

## **Codice di Esempio**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
