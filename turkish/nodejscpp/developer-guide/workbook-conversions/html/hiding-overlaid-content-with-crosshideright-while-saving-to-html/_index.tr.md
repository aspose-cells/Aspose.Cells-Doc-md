---
title: CrossHideRight ile Katmanlı İçeriği Gizleme ve Node.js kullanarak C++ ile HTML ye Kaydederken
linktitle: HTML ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme
type: docs
weight: 100
url: /tr/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken hücre dizileri için farklı çapraz türleri belirtebilirsiniz. Varsayılan olarak, Aspose.Cells Microsoft Excel'e göre HTML oluşturur, ancak çapraz türünü [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) olarak değiştirirseniz, hücreyle örtüşen veya üst üste binen tüm dizileri gizler.

## **HTML'ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716894.xlsx) yükler ve [**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--) değerini [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) yapar, ardından [çıktı HTML'sine](64716893.zip) kaydeder. Ekran görüntüsü, [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)'nin varsayılan çıktı üzerindeki etkisini açıklar.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
