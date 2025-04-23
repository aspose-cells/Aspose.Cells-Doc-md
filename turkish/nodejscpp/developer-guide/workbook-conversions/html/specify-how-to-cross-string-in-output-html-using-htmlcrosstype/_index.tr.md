---
title: HtmlCrossType ile Node.js kullanarak çıktı HTML sinde dizi çaprazlamanın nasıl belirtileceğini belirtin.
linktitle: Çıkış HTML sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin
type: docs
weight: 140
url: /tr/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aspose.Cells for Node.js via C++ te HTML çıktıdında dizi taşmasını nasıl kontrol edeceğinizi öğrenin ve HtmlCrossType ı belirleyin. 
---

## **Olası Kullanım Senaryoları**

Bir hücre metin veya dizi içeriyorsa ve hücrenin genişliğinden büyükse, dizi taşar; eğer bir sonraki hücre boş veya null ise. Excel dosyanızı HTML'ye kaydederken, [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) sıralaması kullanılarak çaprazlama türü belirleyerek bu taşmayı kontrol edebilirsiniz. Aşağıdaki değerlere sahiptirler:

- **HtmlCrossType.Default**: MS Excel gibi gösterir; bir sonraki hücreye bağlıdır. Eğer bir sonraki hücre null ise, dizi çaprazlar veya kısaltılır.

- **HtmlCrossType.MSExport**: Diziyi MS Excel'in HTML olarak dışa aktarması gibi görüntüle.

- **HtmlCrossType.Cross**: HTML çapraz dizisini gösterir; büyük HTML dosyaları oluşturma performansı, Default veya FitToCell ayarlarından on kat daha hızlıdır.

- **HtmlCrossType.FitToCell**: Dizeyi yalnızca hücre genişliği içinde gösterir.

## **Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin**

 Aşağıdaki örnek kod, [örnek Excel dosyasını](51740732.xlsx) yükler ve farklı [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) değerleri belirterek HTML formatında kaydeder. Lütfen bu kod ile üretilen [çıktı HTML'leri](51740734.zip) indirin. Örnek Excel dosyası, bu ekran görüntüsünde gösterildiği gibi kırmızı renkli çerçeve ile sınırlanmış bir resmi içerir ve bu ekran görüntüsü, [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) değerlerinin çıktı HTML'sine etkisini gösterir.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
