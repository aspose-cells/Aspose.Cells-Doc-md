---  
title: Trouver le nombre maximum de lignes et de colonnes pris en charge par les formats XLS et XLSX avec Node.js via C++  
linktitle: Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  

## **Scénarios d'utilisation possibles**  

Il y a différentes quantités de lignes et de colonnes supportées par les formats Excel. Par exemple, XLS supporte 65536 lignes et 256 colonnes tandis que XLSX supporte 1048576 lignes et 16384 colonnes. Si vous souhaitez connaître le nombre de lignes et de colonnes supportées par un format donné, vous pouvez utiliser les propriétés [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) et [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--).  

## **Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX**  

Le code d'exemple suivant crée d'abord un classeur au format XLS puis en XLSX. Après la création, il affiche les valeurs des propriétés [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) et [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--). Veuillez consulter la sortie console du code ci-dessous pour référence.  

## **Code d'exemple**  

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

## **Sortie console**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}  

