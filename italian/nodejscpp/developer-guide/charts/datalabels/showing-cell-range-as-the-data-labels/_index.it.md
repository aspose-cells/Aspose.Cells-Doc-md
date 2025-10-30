---  
title: Mostra l intervallo di celle come etichette dei dati con Node.js via C++  
linktitle: Mostrare l intervallo di celle come etichette dati  
description: Impara come mostrare un intervallo di celle come etichette dei dati nei grafici utilizzando Aspose.Cells for Node.js via C++. La nostra guida dimostrerà come collegare le etichette alla tua fonte di dati e formattarle per fornire informazioni precise e significative nei tuoi grafici.  
keywords: Aspose.Cells for Node.js via C++, creazione di grafici, etichette dati, intervallo di celle, fonte di dati, formattazione, accuratezza, informazioni significative.  
type: docs  
weight: 130  
url: /it/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
In Microsoft Excel 2013, puoi visualizzare un intervallo di celle per le etichette dei dati. Aspose.Cells per Node.js supporta questa funzione.  
{{% /alert %}}  

## **Casella di controllo per mostrare l'intervallo di celle come etichette dati**  

Per mostrare l'intervallo di celle come etichette dati in Microsoft Excel:  

1. Seleziona le etichette dati della serie e fai clic con il tasto destro per aprire il menu contestuale.  
1. Seleziona **Formatta etichette dati**. Le opzioni di etichettatura vengono visualizzate.  
1. Seleziona o deseleziona l'opzione **L'etichetta contiene - Valore dalle celle**.  

Il codice di esempio di seguito accede alle etichette dei dati di una serie di grafico e imposta la proprietà [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) su **true** per selezionare l'opzione **Etichetta Contiene - Valore Da Celle**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
