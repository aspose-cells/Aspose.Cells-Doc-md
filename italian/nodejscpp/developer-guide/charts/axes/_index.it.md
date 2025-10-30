---  
title: Gestisci assi di grafici Excel con Node.js via C++  
description: Impara come configurare gli assi dei grafici in Aspose.Cells for Node.js via C++. La nostra guida ti mostrerà come regolare gli assi primari e secondari, impostare i loro intervalli e modificare le loro proprietà per migliorare i tuoi grafici.  
keywords: Aspose.Cells for Node.js via C++, assi grafico, configurazione, assi primari, assi secondari, intervallo, proprietà.  
linktitle: Assi  
type: docs  
weight: 50  
url: /it/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

Nei grafici Excel, ci sono 3 tipi di assi:  
1. Asse Orizzontale (Categoria): Asse X  
1. Asse verticale (valore): asse Y  
1. Asse di profondità (serie): asse Z  

{{% /alert %}}  

## **Opzioni dell'asse**  
Aspose.Cells for Node.js via C++ ti consente anche di gestire gli assi del grafico a runtime. Con l'oggetto [Axis](https://reference.aspose.com/cells/nodejs-cpp/axis/), puoi modificare tutte le opzioni dell'asse come si fa in Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Gestisci gli assi X e Y**  
 Nel grafico di Excel, gli assi orizzontale e verticale sono i due assi più popolari da usare.  

Il seguente esempio di codice dimostra come impostare le opzioni degli assi X e Y.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **Argomenti avanzati**  
- [Cambia la direzione delle etichette di graduazione](/cells/it/nodejs-cpp/change-tick-label-direction/)  
- [Determina quali assi esistono nel grafico.](/cells/it/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [Gestire le unità automatiche dell'asse del grafico come Microsoft Excel](/cells/it/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Leggere le etichette dell'asse dopo il calcolo del grafico](/cells/it/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Come impostare l'asse delle categorie nel grafico Excel](/cells/it/nodejs-cpp/how-to-set-category-axis/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
