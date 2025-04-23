---
title: Yazdırma alanını Node.js ve C++ kullanarak nasıl ayarlayacağınızı gösteren yöntem
linktitle: Yazdırma Alanı Nasıl Ayarlanır
type: docs
weight: 200
url: /tr/nodejs-cpp/how-to-set-print-area/
description: Bu makale, Node.js ve C++ kullanarak Aspose.Cells kütüphanesi ile yazdırma alanını nasıl ayarlayacağınızı gösteren kodlar sağlar.
keywords: Yazdırma aralığını sınırlama, Yazdırma Aralığını Ayarla, Yazdırma Aralığını Temizle, Node.js ve C++ kullanarak Yazdırma Aralığını ayarla ve temizle, Node.js ve C++ ile Yazdırma Aralığını Nasıl Ayarlarsınız, Node.js ve C++ kullanarak Yazdırma Alanını Temizle, Excel de Yazdırma Alanını Nasıl Ayarlarsınız, Excel de Yazdırma Alanını Nasıl Temizlersiniz.
---

## **Olası Kullanım Senaryoları**

Bir belge, örneğin bir Excel sayfası, içinde yer alan içeriği kontrol etmek için yazdırma alanı ayarlamak faydalıdır. İşte yazdırma alanı ayarlamanın bazı nedenleri:

1. Belirli Verilere Odaklanma: Sadece en önemli bölümleri yazdırabilir, gereksiz içeriği engelleyebilirsiniz.
1. Gelişmiş Düzen: İçeriğin düzenlenmesine ve düzgün şekilde sığdırılmasına yardımcı olur, bölünmeleri veya istenmeyen sayfa sonlarını önler.
1. Kaynak Tasarrufu: Yazdırma alanını sınırlandırarak kağıt ve mürekkep kullanımını azaltabilirsiniz.
1. Profesyonel Sunum: Yalnızca verilerin düzgün ve son halini yazdırdığınızdan emin olur, bu özellikle raporlar veya sunumlar için önemlidir.
1. Tutarlılık: Aynı belgeyi birden fazla kez yazdırırken, belirli bir yazdırma alanı kullanmak, çıktıdaki tutarlılığı sağlar.

<br>
Yazdırma alanı ayarlamak, özellikle büyük belgelerde, yalnızca bir kısmının paylaşılması veya yazdırılmak üzere gözden geçirilmesi gerektiğinde çok kullanışlıdır.

## **Excel'de Yazdırma Alanı Nasıl Ayarlanır**

Excel'de yazdırma alanı belirlemek için şu adımları izleyin:

1. Hücreleri Seçin: Yazdırma alanı olarak ayarlamak istediğiniz hücre aralığını tıklayıp sürükleyerek seçin.
1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki şeritteki "Sayfa Düzeni" sekmesine gidin.
1. Yazdırma Alanını Ayarla: "Sayfa Kurulum" grubunda, "Yazdırma Alanı"na tıklayın. Açılan menüden "Yazdırma Alanını Ayarla"yı seçin.
<br>
<img src="3.png" width=60% />

1. Yazdırma Alanına Ekleyin: Mevcut yazdırma alanına başka hücreler ekmek istiyorsanız, ek hücreleri seçin, "Sayfa Düzeni" sekmesinde "Yazdırma Alanı"na gidin ve "Yazdırma Alanına Ekle"yi seçin.

<br>
Bu işlem, seçilen hücreleri yazdırma alanı olarak tanımlar. Çalışma sayfasını yazdırdığınızda, yalnızca bu tanımlı alan yazdırılır.

## **Excel'de Yazdırma Alanını Temizle Nasıl Yapılır**

Excel'de yazdırma alanını temizlemek için şu adımları izleyin:

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.
1. Yazdırma Alanını Temizle: "Sayfa Kurulum" grubunda, "Yazdırma Alanı"na tıklayın. Açılan menüden "Yazdırma Alanını Temizle"yi seçin.
<br>
<img src="4.png" width=60% />

<br>
Bu işlem, önceden ayarlanmış yazdırma alanını kaldırır ve tüm çalışma sayfasının yazdırılmasına izin verir.

## **Yazdırma Alanını Temizledikten Sonra Neler Olur**

Excel gibi elektronik tablo uygulamasında Aspose.Cells kullanarak yazdırma alanını temizlemek, belgenin tamamını yazdırmak anlamına gelir. Yazdırma alanı ayarlandıysa, yalnızca belirli hücre aralığı yazdırılır. Yazdırma alanı temizlendiğinde, herhangi bir belirli aralık tanımlanmaz ve varsayılan yazdırma davranışı devreye girer, bu da tüm sayfayı içerir.

1. Varsayılan Yazdırma Davranışı: Tüm çalışma sayfası yazdırılmak üzere değerlendirilir. Bu, tüm hücrelerin verileri veya biçimlendirmeleri kabul eder.
1. Yazdırma Alanı Sınırları Kalmadı: Önceden belirlenmiş yazdırma alanı sınırları kaldırılır. Önceden belirlenen satır ve sütunlar artık bu sınırlar içinde kalmaz.
1. Tüm İçeriğin Yazdırılması: Başlıklar, altbilgiler ve çalışma sayfasındaki diğer tüm veriler yazdırma işlemine dahil edilir.

## **Aspose.Cells for Node.js via C++ Kullanarak Yazdırma Alanını Ayarlama**

Belirli bir çalışma sayfasında yazdırma alanını ayarlamak için: İlk olarak, [örnek dosyayı](input.xlsx) yükleyin ve daha sonra [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) nesnesinin [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) özelliğini istediğiniz çalışma sayfası için değiştirin. Bu özelliği bir aralık dizisi olarak ayarlamak, yazdırma alanını belirler.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area - specify the range you want to print
worksheet.getPageSetup().setPrintArea("A1:D10");

// Save the workbook
workbook.save("set_print_area.pdf");
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Aspose.Cells for Node.js via C++ Kullanarak Yazdırma Alanını Temizleme**

Belirtilmiş bir çalışma sayfasında yazdırma alanını temizlemek için: Önce [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) nesnesinin [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) özelliğini değiştirmeniz gerekir. Bu özelliği boş bir dize olarak ayarlamak yazdırma alanını temizler.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the print area
worksheet.getPageSetup().setPrintArea("");

// Save the workbook
workbook.save("clear_print_area.pdf");
```

Çıktı sonucu:
<br>
<img src="2.png" width=60% />
