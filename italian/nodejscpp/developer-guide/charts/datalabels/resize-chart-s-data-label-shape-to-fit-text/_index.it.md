---  
title: Ridimensiona il forma dell etichetta dei dati del grafico per adattarla al testo con Node.js via C++  
linktitle: Ridimensionare la forma dell etichetta dati del grafico per adattare il testo  
description: Impara come ridimensionare la forma dell etichetta dei dati in un grafico per adattarla al testo in Aspose.Cells for Node.js via C++. La nostra guida ti mostrerà come regolare la dimensione e la forma del contenitore dell etichetta per garantire che il testo venga visualizzato correttamente senza troncature o sovrapposizioni.  
keywords: Aspose.Cells for Node.js via C++, creazione grafici, etichette dei dati, ridimensionamento forma, adattamento testo, troncature, sovrapposizioni.  
type: docs  
weight: 220  
url: /it/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
L'applicazione Excel fornisce l'opzione **Ridimensiona forma per adattare il testo** per le etichette dati del grafico al fine di aumentare le dimensioni della forma in modo che il testo vi entri.  
{{% /alert %}}  

## **Come Ridimensionare la Forma della etichetta dati del grafico per Adattare il Testo in Microsoft Excel**  

Questa opzione può essere accessibile sull'interfaccia Excel selezionando qualsiasi etichetta dei dati sul grafico. Fai clic con il tasto destro e seleziona il menu **Formato etichette dati**. Nella scheda **Dimensione e proprietà**, espandi **Allineamento** per rivelare le proprietà correlate, inclusa l'opzione **Ridimensiona forma per adattare il testo**.  

## **Come ridimensionare la forma dell'etichetta dei dati del grafico per adattarla al testo usando Aspose.Cells for Node.js via C++**  

Per imitare la funzione di Excel di ridimensionare le forme delle etichette dei dati per adattarsi al testo, le API Aspose.Cells hanno esposto la proprietà di tipo Boolean [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--). Il seguente esempio di codice mostra uno scenario di utilizzo semplice della proprietà [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

