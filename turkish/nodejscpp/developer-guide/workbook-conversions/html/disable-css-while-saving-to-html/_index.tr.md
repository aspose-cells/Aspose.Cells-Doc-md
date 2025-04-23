---
title: Node.js ve C++ kullanarak HTML ye kaydederken CSS yi devre dışı bırakın
linktitle: HTML yi kaydederken CSS yi devre dışı bırak
type: docs
weight: 320
url: /tr/nodejs-cpp/disable-css-while-saving-to-html/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarını HTML ye kaydederken CSS yi nasıl devre dışı bırakacağınızı öğrenin. 
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı tek sayfa HTML'ye kaydettiğinizde, genellikle CSS öğeleri HTML dosyasına gömülü olur ve HEAD bölümünde bulunur. Bu dosyayı e-posta içeriği/gövdesi olarak eklediğinizde, CSS öğeleri çoğu e-posta istemcisi tarafından kaldırılır ve düzgün görüntüleme sağlanmaz. Aspose.Cells'in 24.12 sürümü, CSS'yi isteğe bağlı olarak devre dışı bırakmanıza olanak tanıyan bir seçenek sunar, böylece stiller doğrudan HTML öğeleri içinde uygulanabilir. E-posta içeriği/gövdesi olarak HTML ayarlamak istiyorsanız, lütfen [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) özelliğini kullanın ve **true** olarak ayarlayın.

## **CSS'yi devre dışı bırakırken HTML'ye kaydetme**

 Aşağıdaki örnek kod, [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) özelliğinin kullanımını gösterir. 

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
