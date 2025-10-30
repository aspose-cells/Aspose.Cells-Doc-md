---  
title: Gestire le unità automatiche dell asse del grafico come Microsoft Excel con Node.js tramite C++  
linktitle: Gestire le unità automatiche dell asse del grafico come Microsoft Excel  
description: Impara come gestire le unità automatiche sugli assi del grafico in Aspose.Cells for Node.js via C++. La nostra guida ti mostrerà come configurare e personalizzare le unità automatiche su un asse del grafico, inclusa la visualizzazione in notazione scientifica e la regolazione della scala.  
keywords: Aspose.Cells for Node.js via C++, assi del grafico, unità automatiche, Microsoft Excel, configurazione, personalizzazione, notazione scientifica, scalatura.  
type: docs  
weight: 120  
url: /it/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **Possibili Scenari di Utilizzo**  
Le versioni precedenti di Aspose.Cells for Node.js via C++ non erano in grado di gestire correttamente le unità automatiche dell'asse del grafico quando il grafico veniva reso in immagine o PDF. Ora, Aspose.Cells for Node.js via C++ supporta la gestione delle unità automatiche dell'asse del grafico. Non c'è stato alcun cambiamento nel codice. Basta convertire il tuo grafico in immagine o PDF e verrà renderizzato come in Microsoft Excel.  

## **Gestire le unità automatiche dell'asse del grafico come Microsoft Excel**  
Il seguente esempio di codice carica il [file Excel di esempio](61767755.xlsx) e genera il [grafico PDF in output](61767752.pdf). Lo screenshot mostra le unità automatiche dell'asse del grafico evidenziate da rettangoli rossi e confronta anche il grafico del file Excel di esempio con il grafico PDF in output. Entrambi sono esattamente simili.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Codice di Esempio**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
