---
title: Node.js ile C++ üzerinden Başlıklar veya Altbilgiler Alma
linktitle: Başlık veya Altlık Alınması
type: docs
weight: 30
url: /tr/nodejs-cpp/get-headers-or-footers/
description: Bu makale, Node.js üzerinden C++ API kullanarak Excel veya OpenOffice dosyalarından programatik olarak başlıklar ve altbilgiler nasıl alınacağını açıklar.
---

{{% alert color="primary" %}}

Başlıklar ve altlıklar yalnızca Sayfa Düzeni görünümünde, Baskı Önizleme'de ve yazdırılan sayfalarda gösterilir. 

Ayrıca, birden fazla çalışma sayfasında başlıkları veya altlıkları görüntülemek istiyorsanız, Sayfa Düzeni iletişim kutusunu da kullanabilirsiniz. 

Grafik sayfaları veya grafikler gibi diğer sayfa türleri için, başlık ve altyazıları yalnızca Sayfa Düzeni iletişim kutusunu kullanarak ekleyebilirsiniz.

{{% /alert %}}

## **MS Excel'de Başlık ve Altlıkların Alınması**
1. Başlık veya altyazıları görüntülemek veya değiştirmek istediğiniz çalışma sayfasına tıklayın.
2. Görünüm sekmesinde, Çalışma Kitabı Görünümleri grubunda, Sayfa Düzeni'ne tıklayın.
   Excel, çalışma sayfasını Sayfa Düzeni görünümünde gösterir.
3. Bir başlık veya altlık görüntülemek veya düzenlemek için, çalışma sayfasının üstünde veya altında (Üstbilgi altında) sol, orta veya sağ başlık veya altlık metin kutusuna tıklayın.


## **Aspose.Cells for Node.js via C++ kullanarak Başlıklar ve Altbilgiler Alma**
[**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) ve [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-) yöntemleri ile Node.js geliştiricileri dosyadan başlık veya altbilgileri kolayca alabilir.

1. Dosyayı açmak için Bir Çalışma Kitabı oluşturun.
2. Başlık veya altbilgiyi almak istediğiniz çalışma sayfasını alın.
3. Belirli bir bölüm kimliği ile başlık veya altbilgiyi alın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **Başlık ve Altlıkları Komut Listesine Ayrıştır**
Başlık veya altbilgi metni, sayfa numarası, geçerli tarih veya metin biçimlendirme özellikleri gibi özel komutlar içerebilir.

Özel komutlar, önünde ampersand ("&") ile gösterilen tek harf ile temsil edilir.

Başlık ve altbilgi dizeleri, ABNF grameri kullanılarak oluşturulur. Bir görüntüleyici olmadan anlaması kolay değildir.

Aspose.Cells for Node.js via C++, başlıkları ve altbilgileri komut listesi olarak ayrıştırmak için [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) yöntemi sağlar.

Aşağıdaki kodlar, başlık veya altbilgiyi komut listesi olarak ayrıştırma ve komutları işleme nasıl gösterileceğini gözler önüne serer:

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
