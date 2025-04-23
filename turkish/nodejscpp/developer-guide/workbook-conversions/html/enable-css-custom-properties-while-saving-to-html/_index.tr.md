---
title: Node.js ve C++ kullanarak HTML ye kaydederken CSS Özelleştirilmiş Özellikleri etkinleştirin
linktitle: HTML ye Kaydederken CSS Özel Özelliklerini Etkinleştir
type: docs
weight: 320
url: /tr/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarını HTML ye kaydederken CSS özel özelliklerini nasıl etkinleştireceğinizi öğrenin. 
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken, tek bir temel64 resmi için birden fazla tekrar varsa, özel özellik ile resim verileri yalnızca bir kez kaydedilmelidir, böylece ortaya çıkan HTML'nin performansı artırılabilir. Lütfen [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) özelliğini kullanın ve kaydederken **true** olarak ayarlayın.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## ** HTML'ye Kaydederken CSS Özel Özelliklerini Etkinleştir**

Aşağıdaki örnek kod, [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) özelliğinin kullanımını gösterir. Ekran görüntüsü, bu özelliğin **true** olarak ayarlanmadığında etkisini gösterir. Lütfen bu kodda kullanılan [örnek Excel dosyasını](50528260.xlsx) ve onun tarafından oluşturulan [çıktı HTML'sini](50528261.zip) indirin ve referans alın.



## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
