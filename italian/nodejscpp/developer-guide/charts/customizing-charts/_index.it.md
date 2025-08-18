---  
title: Personalizzazione dei Grafici con Node.js tramite C++  
linktitle: Personalizzazione dei grafici  
description: Impara come personalizzare i grafici in Aspose.Cells for Node.js via C++. La nostra guida mostrerà come modificare layout dei grafici, aggiungere e formattare le serie di dati, regolare gli assi e applicare varie opzioni di formattazione per migliorare l aspetto e l usabilità dei tuoi grafici.  
keywords: Aspose.Cells for Node.js via C++, grafici, personalizzazione, layout, serie di dati, assi, formattazione, aspetto, usabilità.  
type: docs  
weight: 40  
url: /it/nodejs-cpp/customizing-charts/  
---  


## **Creazione di grafici personalizzati**  

Finora, quando abbiamo discusso di grafici, abbiamo considerato i grafici standard con le loro impostazioni di formattazione standard. Definiamo solo la sorgente dati, impostiamo alcune proprietà, e il grafico viene creato con le impostazioni di formato predefinite. Ma le API di Aspose.Cells supportano anche la creazione di grafici personalizzati che permettono agli sviluppatori di creare grafici con le proprie impostazioni di formato.  

Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando Aspose.Cells.  

Un grafico è composto da una serie di dati. Ogni serie di dati in Aspose.Cells è rappresentata da un oggetto [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) mentre l'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) funge da collezione di oggetti [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series). Quando si crea un grafico personalizzato, gli sviluppatori hanno libertà di usare diversi tipi di grafici per diverse serie di dati (raccolte nell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)).  

Il codice di esempio di seguito dimostra come creare grafici personalizzati. In questo esempio, utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

Attualmente, Aspose.Cells supporta solo grafici personalizzati che combinano grafici a torta, linee, colonne e colonne impilate, ma altri grafici saranno supportati in future versioni.  

{{% /alert %}}  

