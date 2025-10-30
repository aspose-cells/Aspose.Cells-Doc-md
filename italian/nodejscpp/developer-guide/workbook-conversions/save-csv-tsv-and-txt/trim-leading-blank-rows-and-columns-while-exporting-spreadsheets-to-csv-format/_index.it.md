---
title: Ritagliare le righe e le colonne vuote all inizio durante l esportazione di fogli di calcolo in formato CSV con Node.js tramite C++
linktitle: Tagliare le righe e le colonne vuote iniziali durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 100
url: /it/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Impara come ritagliare le righe e le colonne vuote all inizio durante l esportazione di fogli di calcolo in formato CSV usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

A volte, il tuo file Excel o CSV contiene colonne o righe iniziali vuote. Ad esempio, considera questa riga

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Qui le prime tre celle o colonne sono vuote. Quando apri un file CSV del genere in Microsoft Excel, allora Microsoft Excel scarta queste righe e colonne vuote iniziali.

Per impostazione predefinita, Aspose.Cells for Node.js via C++ non elimina le colonne e le righe vuote all'inizio al salvataggio, ma se vuoi rimuoverle come fa Microsoft Excel, Aspose.Cells offre la proprietà [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--). Impostala su **true** e tutte le righe e colonne vuote all'inizio verranno eliminate al salvataggio.

{{% alert color="primary" %}}

Prima del rilascio di Aspose.Cells for Node.js via C++ 20.4, il valore predefinito di [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) era **false**. Dalla versione 20.4, il valore predefinito di [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) è **true.**

{{% /alert %}}

## **Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV**

Il seguente esempio di codice carica il [file Excel di origine](sampleTrimBlankColumns.xlsx) che ha due colonne vuote all'inizio. Prima salva il file Excel in formato CSV senza modifiche e poi imposta la proprietà [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) su **true** e lo salva di nuovo. Lo screenshot mostra il [file Excel di origine](sampleTrimBlankColumns.xlsx), il [file CSV di output senza ritaglio](outputWithoutTrimBlankColumns.csv) e il [file CSV di output con ritaglio](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
