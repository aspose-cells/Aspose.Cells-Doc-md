---  
title: Aggiungi filigrana WordArt al grafico con Node.js tramite C++  
linktitle: Aggiungere WordArt come Filigrana al Grafico  
description: Impara a usare Aspose.Cells for Node.js via C++ per aggiungere una filigrana WordArt a un grafico in Microsoft Excel. La nostra guida dimostrerà come creare e posizionare una filigrana WordArt per migliorare l attrattiva visiva e l unicità del tuo grafico.  
keywords: Aspose.Cells per Node.js, Filigrana WordArt, Filigrana del Grafico, Microsoft Excel, Attrattiva Visiva, Unicità del Grafico.  
type: docs  
weight: 50  
url: /it/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

Puoi usare WordArt per aggiungere effetti speciali al testo nei fogli di calcolo. Ad esempio, estendere un titolo, decorare il testo, far si che il testo si adatti a una forma predefinita o applicare il testo interessato all'area di tracciamento di un grafico come filigrana. Il WordArt diventa un oggetto che puoi spostare o posizionare nei tuoi fogli di calcolo per aggiungere decorazioni.  

L'esempio seguente mostra come aggiungere una forma WordArt come filigrana per l'area di tracciamento del grafico.  

{{% /alert %}}  

L'esempio seguente mostra come aggiungere una forma WordArt come watermark all'area di trama di un grafico esistente.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Open the existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add a WordArt watermark (shape) to the chart's plot area.
const wordart = chart.getShapes().addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

// Get the shape's fill format.
const wordArtFormat = wordart.getFill();

// Set the transparency.
wordArtFormat.setTransparency(0.9);

// Get the line format.
const lineFormat = wordart.getLine();

// Set Line format to invisible.
lineFormat.setWeight(0.0);

// Save the excel file.
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

