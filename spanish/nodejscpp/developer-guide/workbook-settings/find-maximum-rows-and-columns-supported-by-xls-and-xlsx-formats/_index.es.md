---  
title: Encontrar el número máximo de filas y columnas soportadas por los formatos XLS y XLSX con Node.js a través de C++  
linktitle: Encontrar el número máximo de filas y columnas admitidas por los formatos XLS y XLSX  
type: docs  
weight: 20  
url: /es/nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  

## **Escenarios de uso posibles**  

Hay diferentes números de filas y columnas soportadas por los formatos de Excel. Por ejemplo, XLS soporta 65536 filas y 256 columnas mientras que XLSX soporta 1048576 filas y 16384 columnas. Si deseas saber cuántas filas y columnas soporta un formato dado, puedes usar las propiedades [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) y [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--).  

## **Encontrar el número máximo de filas y columnas admitidas por los formatos XLS y XLSX**  

El siguiente código de ejemplo crea un libro de trabajo primero en formato XLS y luego en XLSX. Después de la creación, imprime los valores de las propiedades [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) y [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--). Por favor, consulta la salida de la consola del código a continuación para tu referencia.  

## **Código de muestra**  

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

## **Salida de la consola**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
