---  
title: Node.js kullanarak C++ ile Yazdırma Başlıklarını Nasıl Ayarlarsınız?  
linktitle: Yazdırma Başlıklarını Nasıl Ayarlarsınız  
type: docs  
weight: 200  
url: /tr/nodejs-cpp/how-to-set-print-titles/  
description: Bu makale, Node.js için Aspose.Cells kütüphanesini kullanarak Yazdırma başlıklarını nasıl ayarlayacağınızı gösterir.  
keywords: Satır ve sütunları tekrar tekrar yazdırın, Node.js Yazdırma Başlıklarını Nasıl Ayarlarsınız, Node.js kullanarak Yazdırma Başlıklarını ayarlayın ve temizleyin, Node.js kullanarak Yazdırma Başlıklarını nasıl temizlersiniz, Node.js kullanarak yazdırma başlıkları ekleyin, Node.js kullanarak yazdırma başlıklarını kaldırın, Excel de Yazdırma Başlıklarını Nasıl Ayarlarsınız, Excel de Yazdırma Başlıklarını Nasıl Temizlersiniz.  
---  

## **Olası Kullanım Senaryoları**  

Excel'de yazdırma başlıklarını ayarlamak, belirli satır veya kolonların her yazdırılan sayfada tekrarlanmasını sağlar, bu özellik büyük elektronik tablolar için özellikle faydalıdır. İşte birkaç neden:  

1. Artırılmış Okunabilirlik: Yazdırma başlıkları, başlıkları tüm sayfalarda görünür tutarak veriyi anlamaya yardımcı olur, böylece her seferinde ilk sayfaya dönmeden bilgileri yorumlamak daha kolay hale gelir.  

1. Profesyonel Sunum: Her sayfada tutarlı bir şekilde başlıklar veya etiketler göstermek, yazdırılmış belgeler için daha düzgün ve profesyonel bir görünüm sağlar.  

1. Gelişmiş Navigasyon: Geniş veriler içeren belgelerde, her sayfada başlıkların tekrarlanması, daha hızlı gezinme ve referans sağlar, böylece sayfalar arasında geri dönüp gitme ihtiyacını azaltır.  

1. Hata Azaltma: Her sayfada başlıklar olduğunda, yanlış anlamalar veya veri giriş hataları minimize edilir, kullanıcılar verilerin bağlamını kolayca görebilir.  

1. Tutarlılık: Kolon başlıkları veya satır etiketleri gibi önemli bilgilerin her zaman görünür olması, belge genelinde tutarlılık ve açıklık sağlar.  

## **Excel’de Yazdırma Başlıklarını Nasıl Ayarlarsınız**  

Excel’de yazdırma başlıklarını ayarlamak için şu adımları izleyin:  

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.  
1. Yazdırma Başlıklarına Erişin: "Sayfa Ayarı" grubunda "Yazdırma Başlıkları"na tıklayın.  
1. Satırları Tekrarlamak İçin Ayarlayın: "Sayfa Ayarı" iletişim kutusunda, "Sayfa" sekmesine gidin. "Yazdırma başlıkları" bölümünde, "Üstte tekrarlanacak satırlar" kutusuna tıklayın ve tekrarlanmasını istediğiniz satırları seçin.  
1. Kolonları Tekrarlamak İçin Ayarlayın (gerekirse): Aynı şekilde, "Sol tarafta tekrarlanacak kolonlar" kutusuna tıklayın ve tekrarlanmasını istediğiniz kolonları seçin.  
<br>  
<img src="3.png" width=60% />  

1. Onaylayın ve Yazdırın: "Tamam"a tıklayarak ayarları uygulayın. Çalışma sayfasını yazdırdığınızda, belirttiğiniz satırlar veya kolonlar her sayfada görünecektir.  

## **Excel’de Yazdırma Başlıklarını Nasıl Temizlersiniz**  

Excel’de yazdırma başlıklarını temizlemek için, her yazdırılan sayfada tekrarlanan satır veya kolonları kaldırmanız gerekir. İşte nasıl yapılır:  

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.  
1. Yazdırma Başlıklarına Erişin: "Sayfa Ayarı" grubunda "Yazdırma Başlıkları"na tıklayın.  
1. Yazdırma Başlıklarını Temizle: "Sayfa Ayarı" iletişim kutusunda, "Sayfa" sekmesine gidin. "Üstte tekrarlanacak satırlar" ve "Sol tarafta tekrarlanacak kolonlar" metin kutularını temizleyin ve içlerindeki içerikleri silin.  
<br>  
<img src="4.png" width=60% />  

1. Onaylayın ve Kapatın: Değişiklikleri uygulamak için "Tamam"a tıklayın.  

## **Aspose.Cells for Node.js via C++ Kullanarak Yazdırma Başlıklarını Nasıl Ayarlarsınız**  

Belirtilmiş bir çalışma sayfasında yazdırma başlıklarını ayarlamak için: İlk olarak, [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) ve [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) özelliklerini [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) nesnesinde değiştirmeniz gerekir. Bu özellikleri bir aralık dizesine ayarlamak, yazdırma başlıklarını belirler.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.getPageSetup().setPrintTitleRows("$1:$2");

// Set columns to repeat at the left (e.g., columns A and B)
worksheet.getPageSetup().setPrintTitleColumns("$A:$B");

// Save the workbook
workbook.save("set_print_titles.pdf");
```  

Çıktı sonucu:  
<br>  
<img src="1.png" width=60% />  

## **Aspose.Cells for Node.js via C++ Kullanarak Yazdırma Başlıklarını Nasıl Temizlersiniz**  

Belirli bir çalışma sayfasında yazdırma başlıklarını temizlemek için: İlk olarak, [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) ve [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) özelliklerini [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) nesnesinde değiştirin. Bu özellikleri boş bir dizgeye ayarlamak, yazdırma başlıklarını temizler.  

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

// Clear the rows and columns set to repeat
worksheet.getPageSetup().setPrintTitleRows("");
worksheet.getPageSetup().setPrintTitleColumns("");

// Save the workbook
workbook.save("clear_print_titles.pdf");
```  

Çıktı sonucu:  
<br>  
<img src="2.png" width=60% />  

