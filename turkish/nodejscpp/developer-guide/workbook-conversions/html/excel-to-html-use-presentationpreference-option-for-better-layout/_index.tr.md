---
title: Excel den HTML ye  Node.js kullanarak Node.js via C++ ile daha iyi düzen için PresentationPreference Seçeneği kullanımı
linktitle: Excel den HTML ye  Daha İyi Düzen İçin Presentasyon Tercihi Seçeneğini Kullanın
type: docs
weight: 220
url: /tr/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel dosyasını HTML veya MHT formatına kaydederken daha iyi düzen sağlayan görünüm tercihi özelliği olan HtmlSaveOptions.presentationPreference'ı geliştiricilere sunar. Özelliğin varsayılan değeri yanlıştır. Daha çekici bir Sunum almak için bu özelliği **true** yapmanızı öneririz.

{{% /alert %}} 

Aşağıdaki örnek kod, PresentationPreference açıkken bir Excel raporundan HTML dosyası nasıl render edileceğini gösterir.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
