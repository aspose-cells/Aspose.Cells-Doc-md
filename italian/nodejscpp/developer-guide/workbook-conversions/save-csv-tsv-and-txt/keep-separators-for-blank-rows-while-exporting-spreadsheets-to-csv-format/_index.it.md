---  
title: Mantieni i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV con Node.js tramite C++  
linktitle: Mantieni i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV  
type: docs  
weight: 160  
url: /it/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV**  

Aspose.Cells offre la possibilità di mantenere i separatori di linea durante la conversione dei fogli di calcolo in formato CSV. Per questo, puoi usare la proprietà [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) di [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/). [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) è una proprietà booleana. Per mantenere i separatori per le righe vuote durante la conversione del file Excel in CSV, imposta la proprietà [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) su **true**.  

Il seguente esempio di codice carica il [file Excel di origine](84378743.xlsx). Imposta la proprietà [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) su **true** e lo salva come [output.csv](84378744.csv). Lo screenshot mostra il confronto tra il file Excel sorgente, l'output predefinito generato durante la conversione in CSV e l'output generato impostando [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) su **true**.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Set KeepSeparatorsForBlankRow to true to show separators in blank rows
options.setKeepSeparatorsForBlankRow(true);

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
