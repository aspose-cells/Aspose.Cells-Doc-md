---  
title: Conversione di grafico in immagine in formato SVG con Node.js tramite C++  
linktitle: Conversione del grafico in un immagine nel formato SVG  
type: docs  
weight: 240  
url: /it/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Impara come convertire un grafico in immagine nel formato SVG usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Scalable Vector Graphics (SVG) è un formato di immagine vettoriale basato su XML per grafica bidimensionale che supporta anche l'interattività e l'animazione. La specifica SVG è uno standard aperto sviluppato dal World Wide Web Consortium (W3C) dal 1999.  

Le immagini SVG e i loro comportamenti sono definiti in file di testo XML. Ciò significa che possono essere cercati, indicizzati, scriptati e compressi. Come file XML, le immagini SVG possono essere create e modificate con qualsiasi editor di testo, ma vengono più spesso create con software di disegno.  

Aspose.Cells può salvare grafici in immagini in vari formati come BMP, JPEG, PNG, GIF, SVG, ecc. Questo articolo spiega come salvare un grafico in formato SVG.  

{{% /alert %}}  

Nel seguente codice di esempio viene spiegato come utilizzare Aspose.Cells per convertire un grafico in un'immagine nel formato SVG. Il codice carica il file Microsoft Excel di origine e poi salva il primo grafico trovato nel primo foglio di lavoro in SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
