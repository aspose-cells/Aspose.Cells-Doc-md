---
title: Node.js üzerinden C++ kullanarak 1904 Tarih Sistemi Uygula
description: Aspose.Cells, spreadsheet dosyalarıyla çalışmak için kullanılan Node.js kütüphanesidir. 1904 tarih sistemi uygulamasını destekler, kullanıcıların 1 Ocak 1904 tarihine göre hesaplama ve biçimlendirme yapmasına olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak 1904 tarih sisteminin nasıl uygulanacağını anlatmaktadır.
keywords: Aspose.Cells, 1904 tarih sistemi, elektronik tablo, hesaplama, biçimlendirme, Node.js üzerinden C++
type: docs
weight: 7000
url: /tr/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel iki tarih sistemi destekler: 1900 tarih sistemi (Windows için Excel'de varsayılan tarih sistemi) ve 1904 tarih sistemi. 1904 tarih sistemi genellikle Macintosh Excel dosyalarıyla uyumluluk sağlamak amacıyla kullanılır ve Macromce Excel kullanıyorsanız varsayılan sistemdir. Excel dosyalarında 1904 tarih sistemi ayarlamak için Aspose.Cells for Node.js via C++ kullanılabilir. 

{{% /alert %}} 

Microsoft Excel'de (örneğin, Microsoft Excel 2003) 1904 tarih sistemini uygulamak için:

1. **Araçlar** menüsünden **Seçenekler**'i seçin ve **Hesaplama** sekmesini seçin.
1. **1904 tarih sistemi** seçeneğini belirleyin.
1. **Tamam**'a tıklayın.

|**Microsoft Excel'de 1904 tarih sistemini seçme**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Bunu, Aspose.Cells API'lerini kullanarak nasıl başarılır gösteren örnek kodu görün.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
