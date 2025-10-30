---  
title: XLS ve XLSX formatlarının desteklediği Maksimum Satır ve Sütun Sayısını Node.js ve C++ kullanarak bulun.  
linktitle: XLS ve XLSX formatları tarafından desteklenen maksimum satır ve sütun sayısını bulun.  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  

## **Olası Kullanım Senaryoları**  

Excel formatlarının desteklediği satır ve sütun sayıları farklıdır. Örneğin, XLS 65536 satır ve 256 sütun desteklerken, XLSX 1048576 satır ve 16384 sütun destekler. Belirli bir formatın kaç satır ve sütunu desteklediğini öğrenmek için [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) ve [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--) özelliklerini kullanabilirsiniz.  

## **XLS ve XLSX formatları tarafından desteklenen maksimum satır ve sütun sayısını bulun.**  

Aşağıdaki örnek kod, ilk olarak XLS formatında, sonra XLSX formatında bir çalışma kitabı oluşturur. Oluşturulduktan sonra, [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) ve [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--) özelliklerinin değerlerini yazdırır. Lütfen aşağıda verilen kodun konsol çıktılarına bakınız.  

## **Örnek Kod**  

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

## **Konsol Çıktısı**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
