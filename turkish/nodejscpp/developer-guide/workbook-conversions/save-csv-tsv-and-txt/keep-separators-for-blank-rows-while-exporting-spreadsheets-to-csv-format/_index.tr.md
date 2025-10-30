---  
title: Boş Satırlarda Ayırıcıları Koru ve Node.js/C++ kullanarak CSV ye Dışa Aktarma  
linktitle: CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla  
type: docs  
weight: 160  
url: /tr/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla**  

Aspose.Cells, çalışma sayfalarını CSV'ye dönüştürürken satır ayırıcılarını koruma yeteneği sağlar. Bu amaçla, [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/)nin [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) özelliğini kullanabilirsiniz. [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) boolean bir özelliktir. Excel dosyasını CSV'ye dönüştürürken boş satırların ayırıcılarını korumak için, [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) özelliğini **true** olarak ayarlayın.  

Aşağıdaki örnek kod, [kaynak Excel dosyasını](84378743.xlsx) yükler. [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) özelliğini **true** yapar ve [çıktı.csv](84378744.csv) olarak kaydeder. Ekran görüntüsü, kaynak Excel dosyası, varsayılan CSV'ye dönüştürme ve [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) ayarlamasıyla üretilen çıktı arasındaki karşılaştırmayı gösterir.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Örnek Kod**  

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
