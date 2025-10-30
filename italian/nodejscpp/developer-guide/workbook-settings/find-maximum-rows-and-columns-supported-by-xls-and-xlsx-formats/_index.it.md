---  
title: Trova il massimo numero di righe e colonne supportate dai formati XLS e XLSX con Node.js tramite C++  
linktitle: Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX  
type: docs  
weight: 20  
url: /it/nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  

## **Possibili Scenari di Utilizzo**  

Ci sono diversi numeri di righe e colonne supportati dai formati Excel. Per esempio, XLS supporta 65536 righe e 256 colonne mentre XLSX supporta 1048576 righe e 16384 colonne. Se vuoi sapere quante righe e colonne sono supportate da un determinato formato, puoi usare le proprietà [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) e [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--).  

## **Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX**  

Il codice di esempio seguente crea prima un workbook in formato XLS e poi in formato XLSX. Dopo la creazione, stampa i valori delle proprietà [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) e [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--). Guarda l'output della console del codice sotto per riferimento.  

## **Codice di Esempio**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Print message about XLS format.
console.log("Maximum Rows and Columns supported by XLS format.");

// Create workbook in XLS format.
let wb = new AsposeCells.Workbook(AsposeCells.FileFormatType.Excel97To2003);

// Print the maximum rows and columns supported by XLS format.
let maxRows = wb.getSettings().getMaxRow() + 1;
let maxCols = wb.getSettings().getMaxColumn() + 1;
console.log("Maximum Rows: " + maxRows);
console.log("Maximum Columns: " + maxCols);
console.log();

// Print message about XLSX format.
console.log("Maximum Rows and Columns supported by XLSX format.");

// Create workbook in XLSX format.
wb = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Print the maximum rows and columns supported by XLSX format.
maxRows = wb.getSettings().getMaxRow() + 1;
maxCols = wb.getSettings().getMaxColumn() + 1;
console.log("Maximum Rows: " + maxRows);
console.log("Maximum Columns: " + maxCols);
```  

## **Output della console**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
