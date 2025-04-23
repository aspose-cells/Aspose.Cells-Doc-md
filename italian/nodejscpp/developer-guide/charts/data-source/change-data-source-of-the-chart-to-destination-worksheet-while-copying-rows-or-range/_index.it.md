---
title: Cambia la fonte dati del grafico alla diapositiva di destinazione durante la copia di righe o intervalli con Node.js tramite C++
linktitle: Cambia origine dati del grafico al foglio di lavoro di destinazione durante la copia di righe o intervalli
description: Impara come cambiare la fonte dei dati di un grafico a un foglio di lavoro di destinazione durante la copia di righe o di un intervallo in Aspose.Cells for Node.js via C++. Questa guida mostra come aggiornare l intervallo di dati del grafico e collegarlo al foglio di lavoro di destinazione.
keywords: Aspose.Cells for Node.js via C++, creazione di grafici, fonte di dati, foglio di lavoro di destinazione, righe, intervallo, copia, aggiornamento, intervallo di dati, collegamento.
type: docs
weight: 440
url: /it/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Possibili Scenari di Utilizzo**

Quando si copiano righe o intervalli contenenti grafici in un nuovo foglio di lavoro, la fonte dei dati del grafico non cambia. Ad esempio, se la fonte dei dati del grafico è `=Sheet1!$A$1:$B$4`, dopo aver copiato righe o intervallo in un nuovo foglio di lavoro, la fonte dei dati rimarrà uguale, cioè `=Sheet1!$A$1:$B$4`. Si riferisce ancora al vecchio foglio di lavoro, ovvero Sheet1. Questo è anche il comportamento in Microsoft Excel. Ma se si desidera che si riferisca al nuovo foglio di lavoro di destinazione, utilizzare la proprietà [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) e impostarla su **true** durante la chiamata del metodo [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-). Ora, se il foglio di lavoro di destinazione è DestSheet, la fonte dei dati del grafico cambierà da `=Sheet1!$A$1:$B$4` a `=DestSheet!$A$1:$B$4`.

## **Modifica dell'origine dei dati del grafico al foglio di lavoro di destinazione durante la copia delle righe o dell'intervallo**

Il seguente esempio di codice spiega come utilizzare la proprietà [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) durante la copia di righe o intervalli contenenti grafici in un nuovo worksheet. Il codice utilizza il [file Excel di esempio](5113699.xlsx) e genera il [file Excel di output](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
