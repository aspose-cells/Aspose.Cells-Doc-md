---
title: Node.js kullanarak XLSX Dosyasını PDF Formatına Dönüştürmek için C++
linktitle: XLSX Dosyasını PDF Biçimine Dönüştür
type: docs
weight: 30
url: /tr/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: Bu rehber, bir Excel dosyasını (XLSX) Aspose.Cells for Node.js via C++ kullanarak PDF formatına nasıl dönüştüreceğinizi açıklar. 
---

{{% alert color="primary" %}}

PDF (Taşınabilir Belge Biçimi), bu belgeleri oluşturmak için kullanılan yazılım, donanım ve işletim sisteminden bağımsız olarak belgeleri temsil eder. Bir PDF dosyası, aygıt bağımsız ve çözünürlük bağımsız bir şekilde metin, grafik ve resimlerin herhangi bir kombinasyonunu içerebilir. PDF dosyaları genellikle sıkıştırılır, bu nedenle orijinal dosyadan daha az yer kaplar.

Bazen, bir Microsoft Excel dosyasını PDF'ye dönüştürmeniz gerekir. Bunun için, dünyaya PDF belgeleri dağıtmanıza izin verecek hızlı, güvenli, doğru ve güvenilir bir çözüme ihtiyacınız vardır. Bu işi yapabilen çeşitli dönüştürme araçları mevcuttur. Ancak, orijinal Excel belge düzeninin çıktı PDF dosyasında korunmasını sağlamalısınız. Resimler, grafikler, şekiller, veri biçimlendirme, fontlar, özellikler, renkler, sayfa ayarları, metin yönü, kenarlıklar, grafikler vb. doğru ve kesin şekilde gösterilmelidir. [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/) yüksek doğrulukta dönüşüm sağlar.

Bu belge, Microsoft Excel belgesinin (resimler, grafikler, biçimlendirme vb. içeren) PDF'ye nasıl dönüştürüleceğine ilişkin kapsamlı anlayış sağlamayı amaçlamaktadır. Bu doğrultuda, Aspose.Cells API kullanarak bir Excel dosyasını PDF'ye dönüştüren basit bir komut satırı uygulaması nasıl oluşturulacağını gösterir. Dönüştürme yüksek hassasiyet ve doğrulukla gerçekleştirilir.

{{% /alert %}}

## **Excel'i PDF'ye Dönüştürme**

Bu örnekte, şablon olarak bir Excel dosyası (SampleInput.xlsx) kullanılmıştır. Çalışma kitabında grafikler ve resimler bulunan çalışma sayfaları bulunmaktadır. Her çalışma sayfası, fontlar, özellikler, renkler, gölgeleme efektleri ve kenarlıklar kullanılarak farklı biçimlendirme türleri içermektedir. İlk çalışma sayfasında bir sütun grafiği ve son sayfada bir resim bulunmaktadır.

### **Şablon Excel Dosyası**

Şablon dosyasında grafikler ve medya olarak resimler içeren üç çalışma sayfası bulunmaktadır. İlk çalışma sayfasında grafikler, son sayfada ise aşağıdaki ekran görüntülerinde gösterildiği gibi bir resim yer alır.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|

### **Dönüşüm Süreci**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) metodunu çağırmak en iyisidir. Bu, formüle bağlı değerlerin tekrar hesaplanmasını ve PDF'de doğru değerlerin gösterilmesini sağlar.

{{% /alert %}}

### **Sonuç**

Yukarıdaki kod çalıştırıldığında, bir PDF dosyası uygulama dizinindeki Dosyalar klasöründe oluşturulur.
Aşağıdaki ekran görüntüleri, PDF sayfalarını göstermektedir. Başlık ve altbilgilerin çıktı PDF dosyasında da korunduğuna dikkat edin.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|
