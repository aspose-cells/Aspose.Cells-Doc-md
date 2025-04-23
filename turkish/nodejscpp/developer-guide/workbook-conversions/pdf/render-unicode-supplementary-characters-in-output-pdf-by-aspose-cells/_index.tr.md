---
title: Aspose.Cells for Node.js via C++ kullanarak Unicode Destekleyici karakterleri çıktı PDF sinde Yansıtın
linktitle: Aspose.Cells ile çıktı PDF de Unicode Ek Sayısal karakterlerin oluşturulması
type: docs
weight: 350
url: /tr/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aspose.Cells for Node.js via C++ kullanarak Unicode Destekleyici karakterleri çıktı PDF sinde nasıl yansıtılacağını öğrenin. 
---

{{% alert color="primary" %}}

Normal Unicode karakterleri 2 bayt uzunluğunda iken Unicode Ek Sayısal karakterleri 4 bayt uzunluğundadır. Aspose.Cells şimdi bu 4 bayt Unicode karakterlerin oluşturulmasını destekliyor.

Unicode Karakter Standartında, Ek Sayısal Karakterler U+10000'den U+10FFFF'e kadar olan kod noktalarına atanmış karakterlerdir. Diğer bir deyişle, bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 takyeyi (16 bit birimler) gerektirir.

{{% /alert %}}

## Aspose.Cells for Node.js via C++ ile çıktı PDF'sinde Unicode Destekleyici karakterleri yansıtın

Aşağıdaki ekran görüntüsü, Aspose.Cells'in [kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'sine](5115564.pdf) nasıl dönüştürdüğünü gösteriyor. Gördüğünüz gibi, tüm üç Unicode Destekleyici karakter Microsoft Excel tarafından yapıldığı gibi tam olarak render edilmiştir.

![todo:image_alt_text](output.png)

## Örnek Kod

[Kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'ye](5115564.pdf) dönüştürmek için bu örnek kodu kullanabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));

// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
