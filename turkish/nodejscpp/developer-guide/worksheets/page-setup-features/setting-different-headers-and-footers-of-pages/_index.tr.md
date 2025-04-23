---
title: Farklı Sayfalar için Başlık ve Yiyecekleri Ayarlama (Header ve Footer) Node.js ve C++ kullanımı
linktitle: Farklı Sayfalar için Farklı Üstbilgi ve Altbilgileri Ayarlama
type: docs
weight: 35
url: /tr/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Excel çalışma sayfası Sayfa Kurulumu nun başlık ve yiyeceklerini programlı olarak nasıl ayarlayacağınızı gösteren örnek kod sunar. İlk, tek ve çift sayfalar için başlık ve yiyecekleri ayarlayın.
keywords: İlk sayfa, tek sayfalar ve çift sayfalar için Excel başlık ve altbilgisi ayarlama Node.js ve C++ kullanımı
---

{{% alert color="primary" %}}

MS Excel, ilk sayfa, tekler ve çiftler sayfalar için farklı başlık ve altbilgi ayarlamayı 2007'den beri desteklemektedir.
Aspose.Cells for Node.js via C++ bu özelliği destekler.

{{% /alert %}}

## **MS Excel'de Farklı Üstbilgi ve Altbilgiler Ayarlama**

**![Farklı Üstbilgi ve Altbilgiler Ayarlama](difpage.png)**

1. **Sayfa Düzeni > Başlık ve Alt Bilgi > Üstbilgi/Altbilgi**'ye tıklayın.
1. **Farklı Tek ve Çift Sayfalar** veya **Farklı ilk sayfa** seçeneklerini kontrol edin.
1. Farklı başlık ve altbilgileri girin.

## **Aspose.Cells for Node.js via C++ ile farklı başlık ve altbilgi ayarlama**

Aspose.Cells, Excel ile aynı davranışı sergiler.
1. [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) ve [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) bayraklarını ayarlar 
1. Farklı başlık ve altbilgileri girin.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
