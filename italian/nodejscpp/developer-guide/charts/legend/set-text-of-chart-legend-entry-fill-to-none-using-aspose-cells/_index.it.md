---
title: Imposta il testo dell ingresso della legenda del grafico su nessuno usando Aspose.Cells for Node.js via C++
linktitle: Imposta il testo dell elemento legenda del grafico su nessuno utilizzando Aspose.Cells
description: Impara come usare Aspose.Cells for Node.js via C++ per impostare il testo dell ingresso della legenda del grafico su nessuno. Questa guida dimostrerà come modificare il colore di riempimento degli ingressi della legenda in grafici di Microsoft Excel per una migliore visualizzazione e personalizzazione.
keywords: Aspose.Cells for Node.js via C++, Riempimento dell Ingresso della Legenda del Grafico, Microsoft Excel, Visualizzazione, Personalizzazione.
type: docs
weight: 320
url: /it/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Se desideri impostare il testo del riempimento dell'ingresso della legenda del grafico su nessuno in modo che non venga visualizzato all’interno della leggenda del grafico, imposta [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--) su **true**.

{{% /alert %}}

Il codice di esempio seguente imposta il testo del secondo riempimento dell'elemento legenda del grafico su nessuno. Scarica il [file Excel di esempio](5115219.xlsx) utilizzato in questo codice e il [file Excel di output](5115217.xlsx) generato da esso per ulteriori informazioni.

screenshoot seguente evidenzia l'effetto di questo codice sul [file Excel di esempio](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
