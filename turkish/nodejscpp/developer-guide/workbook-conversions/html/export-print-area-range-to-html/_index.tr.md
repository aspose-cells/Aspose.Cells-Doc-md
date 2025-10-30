---  
title: Yazdırma alanı aralığını HTML ye dışa aktarma (Node.js kullanarak C++ ile)  
linktitle: HTML ye Baskı Alanı Aralığını Dışa Aktar  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/export-print-area-range-to/  
---  

## **Olası Kullanım Senaryoları**

Bu, yalnızca yazdırma alanı=seçili hücre aralığı, tüm sayfa yerine HTML'ye dışa aktarmamız gereken yaygın bir senaryodur. Bu özellik zaten PDF görüntüleme için mevcuttur; ancak artık bu işlemi HTML için de yapabilirsiniz. Öncelikle, sayfa ayarlarının nesnesinde yazdırma alanını ayarlayın. Daha sonra, yalnızca seçili aralığı dışa aktarmak için [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--) bayrağını kullanın.

## Örnek Kod

Aşağıdaki örnek kod, bir çalışma kitabı yükler ve daha sonra baskı alanını HTML'e dışa aktarır. Bu özelliği test etmek için örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleInlineCharts.xlsx](79527946.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleInlineCharts.xlsx");

// Load the Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access the sheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area.
worksheet.getPageSetup().setPrintArea("D2:M20");

// Initialize HtmlSaveOptions
const options = new AsposeCells.HtmlSaveOptions();

// Set flag to export print area only
options.setExportPrintAreaOnly(true);

// Save to HTML format
const outputFilePath = path.join(dataDir, "outputInlineCharts.html");
workbook.save(outputFilePath, options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
