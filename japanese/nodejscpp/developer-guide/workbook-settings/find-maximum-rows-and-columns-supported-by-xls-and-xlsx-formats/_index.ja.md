---  
title: Node.jsとC++を使用してXLSおよびXLSXフォーマットでサポートされる最大行数と列数を検索する。  
linktitle: XLSおよびXLSX形式がサポートする最大行数および列数を検索する  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  

## **可能な使用シナリオ**  

Excelフォーマットでは、サポートされる行数と列数が異なります。例えば、XLSは65536行と256列をサポートし、XLSXは1048576行と16384列をサポートします。特定のフォーマットでサポートされる行数と列数を知りたい場合は、[**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--)と[**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--)プロパティを使用します。  

## **XLSおよびXLSX形式がサポートする最大行数および列数を検索する**  

次のサンプルコードは、最初にXLS形式でワークブックを作成し、その後XLSX形式で作成します。作成後、[**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--)と[**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--)の値を出力します。以下のコードのコンソール出力をご参照ください。  

## **サンプルコード**  

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

## **コンソール出力**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
