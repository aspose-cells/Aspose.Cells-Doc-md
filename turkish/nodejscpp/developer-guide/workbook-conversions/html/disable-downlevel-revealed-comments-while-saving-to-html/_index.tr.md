---
title: Node.js ve C++ kullanarak HTML ye kaydederken Downlevel Revealed Comments i devre dışı bırakın
linktitle: HTML ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak
type: docs
weight: 20
url: /tr/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyasını HTML ye kaydederken alttaki görünür yorumları devre dışı bırakmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydettiğinizde, Aspose.Cells Downlevel Conditional Comments'ı gösterir. Bu koşullu yorumlar çoğunlukla eski Internet Explorer sürümleriyle ilgilidir ve modern web tarayıcılar için anlamlı değildir. Ayrıntılı bilgi için aşağıdaki bağlantıya bakabilirsiniz.

- [Koşullu yorum - Downlevel-açıklanan koşullu yorum](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++, [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) özelliğini **true** olarak ayarlayarak bu Downlevel Revealed Comments'ı ortadan kaldırmanıza olanak tanır.

## **HTML'ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak**

Aşağıdaki örnek kod, [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) özelliğinin kullanımını gösterir. Bu özelliğin **true** olarak ayarlanmadığında etkisini ekran görüntüsü ile görebilirsiniz. Bu kodda kullanılan örnek Excel dosyasını ([software.xlsx](50528257.xlsx)) ve üretilen [çıktı HTML'sini](50528258.zip) indirerek referans alabilirsiniz.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
