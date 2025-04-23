---
title: Dışa aktarırken Yorumlar, Excel dosyasını HTML ye kaydetme sırasında, Yorumlar dışa aktarılmaz. Ancak, Aspose.Cells for Node.js via C++ bu özelliği {0} özelliği kullanarak sağlar. Eğer  true  olarak ayarlarsanız, HTML dosyası içinde Excel dosyanızdaki yorumlar da gösterilir.
linktitle: Excel Dosyasını HTML ye Kaydederken Yorumları Dışa Aktar
type: docs
weight: 40
url: /tr/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken, yorumlar dışa aktarılmaz. Ancak, Aspose.Cells for Node.js via C++ bu özelliği `[**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/)` özelliği ile sağlar. Eğer onu **true** olarak ayarlarsanız, HTML ayrıca Excel dosyanızda bulunan yorumları da gösterecektir.

## **Excel Dosyasını HTML'ye Kaydederken Yorumları Dışa Aktar**

Aşağıdaki örnek kod, [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/) özelliğinin kullanımını açıklar. Ekran görüntüsü, bu kodun **true** olarak ayarlandığında HTML üzerindeki etkisini göstermektedir. Referans için lütfen [örnek Excel dosyasını](50528260.xlsx) ve [oluşturulan HTML'i](5052826.txt) indirin.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
