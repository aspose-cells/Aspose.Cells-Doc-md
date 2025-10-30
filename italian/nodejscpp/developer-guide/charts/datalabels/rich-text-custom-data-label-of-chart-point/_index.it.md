---
title: Etichetta dati personalizzata in formato Rich Text di un punto di grafico con Node.js via C++
description: Impara come aggiungere etichette dati personalizzate in formato Rich Text ai punti del grafico in Aspose.Cells for Node.js via C++. La nostra guida ti mostrerà come formattare le etichette con diversi font, colori e opzioni di allineamento per migliorare l aspetto e la leggibilità dei tuoi grafici.
keywords: Aspose.Cells for Node.js via C++, creazione di grafici, testo ricco, etichette dati personalizzate, font, colori, allineamento, aspetto, leggibilità.
type: docs
weight: 10
url: /it/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells per creare etichette dati personalizzate in formato Rich Text per i punti del grafico. Aspose.Cells fornisce il metodo [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-) per restituire l'oggetto [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) che può essere usato per impostare le proprietà del font del testo come il colore, il grassetto, ecc.

{{% /alert %}}

## Etichetta dati personalizzata di testo ricco del punto del grafico

Il seguente codice accede al primo punto del grafico della prima serie, imposta il suo testo e poi imposta il font dei primi 10 caratteri impostando il colore su rosso e il grassetto su **true**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
