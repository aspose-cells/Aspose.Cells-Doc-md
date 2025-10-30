---
title: Node.js ve C++ kullanarak Çalışma Sayfasını Ölçeklendirme
linktitle: Sayfa Çalışma Sayfasını Nasıl Ölçeklendirilir
type: docs
weight: 130
url: /tr/nodejs-cpp/how-to-scale-a-worksheet/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak nasıl çalışma sayfasını ölçeklendireceğinizi gösteriyor.
keywords: Node.js ile çalışma sayfasını ölçeklendirme, Node.js kullanarak çalışma sayfasını nasıl ölçeklendirebilirsiniz, Node.js ve C++ kullanarak çalışma sayfasını ölçeklendirme.
---

## **Olası Kullanım Senaryoları**
Çalışma sayfasını ölçeklendirmek, çalıştığınız bağlama bağlı olarak çeşitli yarar sağlayabilir. İşte birkaç yaygın neden:
1. Sayfaya Sığdır: Yazdırırken tüm içeriğin tek bir sayfaya veya belirli sayıda sayfaya sığmasını sağlamak, böylece okumayı ve yönetimi kolaylaştırmak, çok sayfalı sayfaları çevirmeye gerek kalmadan.

1. Sunum: Çalışma sayfasını daha düzenli ve profesyonel görünmesini sağlamak, özellikle toplantılarda veya raporlarda başkalarıyla paylaşıldığında.

1. Okunabilirlik: Metin ve diğer öğelerin boyutunu daha iyi okunabilirlik için ayarlamak, özellikle küçük fontları okumakta zorluk çeken kişiler için.

1. Alan Yönetimi: Çalışma sayfasında alan kullanımını optimize etmek, gereksiz boş alanın olmamasını ve tüm önemli bilgilerin görünür olmasını sağlamak, aşırı kaydırmadan.

1. Veri Görselleştirme: Çizelge ve grafiklerde, uygun alanı doldurmak için boyut ayarlaması yaparak onları daha anlaşılır hale getirmeye yardımcı olabilir.

1. Tutarlılık: Birden fazla çalışma sayfası veya belge arasında tutarlı görünüm ve his sağlamak, özellikle profesyonel ve eğitimsel ortamlar için önemlidir.

## **Excel'de Çalışma Sayfasını Nasıl Ölçeklendirilir**
Excel’de çalışma sayfasını ölçeklendirmek, içeriğinizi yazdırırken tek bir sayfaya veya belirli sayfa sayısına sığdırmaya yardımcı olabilir. İşte çalışma sayfasını ölçeklendirme adımları:

1. Çalışma Sayfanızı Açın: Ölçeklendirmek istediğiniz Excel çalışma sayfasını açın.

1. Sayfa Düzeni Sekmesine Gidin: Ribbon'da Sayfa Düzeni sekmesine tıklayın.

1. Ölçekleme Gruplarına Göz Atma: Sayfa Düzeni sekmesinde, Ölçekleyecek Gruplarını bulun. Burada ölçeklendirme ayarlarını yapabilirsiniz. Genişlik: Yazdırılan çalışma sayfasının kaç sayfa genişliğinde olacağını belirlemenizi sağlar. Yükseklik: Yazdırılan çalışma sayfasının kaç sayfa yüksekliğinde olacağını belirlemenizi sağlar. Ölçek: Burada özel bir ölçek yüzdesi de ayarlayabilirsiniz.
<br>
<img src="1.png" width=60% />

1. Genişlik ve Yükseklik Ayarları: Genişlik ve yüksekliği istediğiniz sayfa sayısına ayarlayın. Örneğin, çalışma sayfasını tek sayfaya sığdırmak istiyorsanız her ikisini de 1 sayfa yapın.

1. Ölçekleme Yüzdesini (gerekirse) Ayarlayın: Belirli bir ölçek yüzdesi ayarlamak istiyorsanız, Ölçek kutusunu ayarlayın. Örneğin, %50 olarak ayarlarsanız, her şey yarı boyutuna gelir.


## **Node.js ve C++ kullanarak Çalışma Sayfasını Ölçeklendirme**
Aspose.Cells for Node.js via C++, Excel dosyalarıyla programatik olarak çalışmak için güçlü bir kütüphanedir. Aspose.Cells kullanarak bir çalışma sayfasını ölçeklemek için şu adımları izlemelisiniz: [örnek dosyayı](sample.xlsx) yükleyin ve içeriğin istenilen sayfa sayısına veya orijinal boyutun belirli bir yüzdesine uyacak şekilde yazdırma ayarlarını ayarlayın.

### **Örnek: Sayfaya Sığdır**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the worksheet to fit to 1 page wide and 1 page tall
pageSetup.setFitToPagesWide(1);
pageSetup.setFitToPagesTall(1);

// Save the modified workbook
workbook.save("output_fit_to_page.xlsx");
```
<br>
<img src="3.png" width=60% />

### **Örnek: Yüzdeye Ölçekle**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the scaling to a specific percentage (e.g., 75%)
pageSetup.setZoom(75);

// Save the modified workbook
workbook.save("output_scaled_percentage.xlsx");
```
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
