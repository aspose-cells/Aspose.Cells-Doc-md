---  
title: Excel i Tooltip ile HTML e Dönüştürmek Node.js ve C++ kullanarak  
linktitle: Excel i HTML e dönüştür ve açıklama metni ekleyin  
type: docs  
weight: 200  
url: /tr/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarını tooltip ile HTML formatına nasıl dönüştüreceğinizi öğrenin.  
---  

## **Excel'i HTML'e dönüştür ve açıklama metni ekleyin**

Üretilen HTML'de metin kesildiğinde, tamamını göstermek ve üzerine gelindiğinde tooltip olarak göstermek isteyebilirsiniz. Aspose.Cells for Node.js via C++, bunu destekler ve [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) özelliği ile sağlar. [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) özelliğini **true** yaparsanız, tamamını tooltip olarak ekler.

Aşağıdaki resim, oluşturulan HTML dosyasındaki açıklama metnini göstermektedir.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Aşağıdaki kod örneği, [kaynak excel dosyasını](98107416.xlsx) yükler ve [çıktı HTML dosyasını](98107417.zip) araç ipucu ile oluşturur.

Örnek Kod

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

