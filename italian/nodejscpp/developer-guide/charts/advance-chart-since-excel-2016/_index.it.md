---  
title: Leggi e manipola grafici Excel 2016 con Node.js via C++  
linktitle: Lettura e manipolazione dei grafici di Excel 2016  
description: Impara come leggere e manipolare grafici Excel 2016 usando Aspose.Cells for Node.js via C++. Questa guida mostrerà come accedere e modificare varie proprietà del grafico.  
keywords: Aspose.Cells per Node.js, grafici Excel 2016, leggere, manipolare, etichette dati, colori serie, layout, grafici gerarchici, grafici circolari.  
type: docs  
weight: 48  
url: /it/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **Possibili Scenari di Utilizzo**  
Aspose.Cells supporta ora la lettura e la manipolazione dei grafici di Microsoft Excel 2016 che non sono presenti in Microsoft Excel 2013 o nelle versioni precedenti.  
## **Lettura e manipolazione dei grafici di Excel 2016**  
Il seguente esempio di codice carica il [file excel sorgente](22774101.xlsx) che contiene grafici Excel 2016 nel primo foglio di lavoro. Legge tutti i grafici uno ad uno e cambia il suo titolo in base al tipo di grafico. Lo screenshot seguente mostra il file excel di origine prima dell'esecuzione del codice. Come puoi vedere, il titolo del grafico è lo stesso per tutti.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

La seguente schermata mostra il [file excel di output](22774104.xlsx) dopo l'esecuzione del codice. Come puoi vedere, il titolo del grafico è stato cambiato in base al tipo di grafico.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Codice di Esempio**  
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
## **Output della console**  
Ecco l'output della console del codice di esempio sopra quando eseguito con il [file excel di origine fornito](22774101.xlsx).

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Argomenti avanzati**  
- [Creazione del grafico a cascata](/cells/it/nodejs-cpp/creating-waterfall-chart/)  
- [Creazione del grafico Mappa a blocchi](/cells/it/nodejs-cpp/creating-treemap-chart/)  
- [Creazione del grafico Radiali](/cells/it/nodejs-cpp/creating-sunburst-chart/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
