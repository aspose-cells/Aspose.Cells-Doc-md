---
title: HTML den PDF ye Dönüştürme Yöntemi  Node.js ve C++
linktitle: HTML i PDF e nasıl dönüştürülür
type: docs
weight: 80
url: /tr/nodejs-cpp/convert-html-to-pdf/
description: Bu konu, HTML yi PDF ye ve MHTML yi PDF ye dönüştürme işlemlerini Aspose.Cells for Node.js via C++ kullanarak nasıl yapacağınızı gösterir.
keywords: Node.js kullanarak HTML ve MHTML yi PDF ye C++ ile dönüştürün. 
---

## **Genel Bakış**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>HTML'i PDF'e dönüştür</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML'den PDF'ye</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML'yi PDF'ye Dönüştür</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML'yi PDF'ye nasıl dönüştürülür</a></li>
</ul>

## **Node.js'de HTML'den PDF'ye Dönüşüm**
HTML'yi PDF'ye nasıl dönüştürürüz? [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) kütüphanesi ile HTML'yi birkaç kod satırıyla programatik olarak PDF'ye dönüştürebilirsiniz. Aspose.Cells for Node.js via C++, tüm Excel dosyalarını oluşturma, değiştirme, dönüştürme, görüntüleme ve yazdırma yeteneği ile çapraz platform uygulamaları geliştirebilir.

## **JavaScript HTML'yi PDF'ye Dönüştür**
Aşağıdaki JavaScript kod örneği, [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) kullanarak bir HTML belgesini PDF'ye nasıl dönüştüreceğinizi gösterir.

1. [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/) sınıfının bir örneğini oluşturun.
1. [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) nesnesini başlatın.
1. Workbook.save() yöntemini çağırarak çıktı PDF belgesini kaydedin.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.html");

// Loads the workbook which contains hidden external links
const options = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
const book = new AsposeCells.Workbook(filePath, options);
book.save("out.pdf");
```

## **HTML'i PDF'e çevirmeyi deneyin**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML'den PDF'e”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
