---  
title: Maximale unterstützte Zeilen und Spalten für XLS und XLSX Formate mit Node.js über C++ finden  
linktitle: Suchen Sie nach der maximal unterstützten Anzahl von Zeilen und Spalten in den Formaten XLS und XLSX  
type: docs  
weight: 20  
url: /de/nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  

## **Mögliche Verwendungsszenarien**  

Es gibt unterschiedliche Zeilen- und Spaltenzahlen, die von Excel-Formaten unterstützt werden. Zum Beispiel unterstützt XLS 65536 Zeilen und 256 Spalten, während XLSX 1048576 Zeilen und 16384 Spalten unterstützt. Wenn Sie wissen möchten, wie viele Zeilen und Spalten ein bestimmtes Format unterstützt, können Sie die Eigenschaften [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) und [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--) verwenden.  

## **Suchen Sie die maximale Anzahl von Zeilen und Spalten, die von den XLS- und XLSX-Formaten unterstützt werden**  

Der folgende Beispielcode erstellt zunächst eine Arbeitsmappe im XLS-Format und anschließend im XLSX-Format. Nach der Erstellung werden die Werte der Eigenschaften [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) und [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--) ausgegeben. Bitte siehe die Konsolenausgabe des unten angegebenen Codes zu Ihrer Referenz.  

## **Beispielcode**  

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

## **Konsolenausgabe**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}  

