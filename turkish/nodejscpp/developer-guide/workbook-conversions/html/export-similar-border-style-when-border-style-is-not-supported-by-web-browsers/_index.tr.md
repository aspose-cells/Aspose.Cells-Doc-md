---  
title: Tarz Desteklenmeyen Kenarlık Stiliyle Benzer Kenarlık Stili Dışa Aktarma Node.js kullanarak C++ ile  
linktitle: Web Tarayıcıları tarafından Desteklenmeyen Kenar Stili Benzeri Kenar Stilini Dışa Aktar  
type: docs  
weight: 70  
url: /tr/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Web Tarayıcılarının desteklemediği kenarlıkları dışa aktarmanın yollarını öğrenin, Excel dosyalarını HTML ye dönüştürürken Aspose.Cells for Node.js via C++ kullanarak.  
---  

## **Olası Kullanım Senaryoları**  

Microsoft Excel, Web Tarayıcıların desteklemediği bazı kesikli sınır türlerini destekler. Bu tür sınırlar, Aspose.Cells for Node.js via C++ kullanılarak böyle bir Excel dosyası HTML'ye dönüştürülürken kaldırılır. Ancak, Aspose.Cells bu tür sınırların görüntülenmesini `[**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--)` özelliği ile de destekler. Lütfen değerini **true** olarak ayarlayın, ve desteklenmeyen sınırlar da HTML dosyasına aktarılır.  

## **CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle**  

Aşağıdaki örnek kod, aşağıdaki ekran görüntüsünde gösterildiği gibi bazı desteklenmeyen sınırları içeren örnek Excel dosyasını (64716806.xlsx) yükler. Ekran görüntüsü ayrıca [çıktı HTML](64716804.zip) içindeki [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) özelliğinin etkisini gösterir.  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

