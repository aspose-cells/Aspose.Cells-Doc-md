---
title: Golang ve C++ kullanarak XLSX Dosyasını PDF Formatına dönüştür
linktitle: XLSX Dosyasını PDF Biçimine Dönüştür
type: docs
weight: 30
url: /tr/go-cpp/convert-xlsx-file-to-pdf-format/
description: Aspose.Cells for C++ ile Excel dosyalarını yüksek hassasiyet ve doğrulukla PDF formatına nasıl dönüştüreceğinizi öğrenin.
---

{{% alert color="primary" %}}

PDF (Taşınabilir Belge Formatı), belgeleri belgeyi oluşturan yazılım, donanım ve işletim sisteminden bağımsız hale getirir. Bir PDF dosyası, metin, grafik ve görüntüleri cihazdan bağımsız ve çözünürlükten bağımsız olarak içerebilir. PDF'ler genellikle sıkıştırılır, bu da onları orijinal dosyadan daha az yer kaplar.

Bazen, bir Microsoft Excel dosyasını PDF'ye dönüştürmeniz gerekir. Bunun için hızlı, güvenli, doğru ve güvenilir bir çözüme ihtiyacınız vardır ki dünya çapında PDF belgelerini dağıtmanıza olanak sağlar. Bu görevi yapabilecek birçok dönüşüm aracı mevcuttur. Ama orijinal Excel belgesinin düzeninin çıktı PDF dosyasında korunmasını sağlamalısınız. Resimler, grafikler, şekiller, veri biçimlendirme, yazı tipleri, öznitelikler, renkler, sayfa ayarları, metin yönü, sınırlar, grafikler vb. doğru ve kesin şekilde render edilmelidir. [Aspose.Cells](https://products.aspose.com/cells/go-cpp/) yüksek doğrulukta dönüşümü garanti eder.

Bu belge, bir Microsoft Excel belgesinin (resimler, grafikler, biçimlendirme vb. içeren) PDF'ye nasıl dönüştürüleceğine dair kapsamlı bir anlayış sağlamayı amaçlamaktadır. Bunun için, Aspose.Cells API kullanarak Excel dosyasını PDF'ye dönüştüren basit bir C++ konsol uygulaması nasıl oluşturulacağını gösterir. Dönüştürme, yüksek hassasiyet ve doğrulukla gerçekleştirilir.

{{% /alert %}}

## **Excel'i PDF'ye Dönüştürme**

Bu örnekte, şablon olarak bir Excel dosyası (SampleInput.xlsx) kullanılmıştır. Çalışma kitabında grafikler ve resimler bulunan çalışma sayfaları bulunmaktadır. Her çalışma sayfası, fontlar, özellikler, renkler, gölgeleme efektleri ve kenarlıklar kullanılarak farklı biçimlendirme türleri içermektedir. İlk çalışma sayfasında bir sütun grafiği ve son sayfada bir resim bulunmaktadır.

### **Şablon Excel Dosyası**

Şablon dosyası üç çalışma sayfası içermektedir; bunlar Medya olarak grafikler ve resimler içerir. İlk çalışma sayfasında grafikler, son çalışma sayfasında ise bir resim bulunmaktadır; aşağıdaki ekran görüntülerinde gösterildiği gibi.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|

### **Dönüşüm Süreci**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsxFileToPdfFormat.go" >}}
{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF'ye dönmeden hemen önce [Workbook.CalculateFormula](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) metodunu çağırmak en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve doğru değerlerin PDF'de görüntülenmesini sağlar.

{{% /alert %}}

### **Sonuç**

Yukarıdaki kod çalıştırıldığında, bir PDF dosyası uygulama dizinindeki Dosyalar klasöründe oluşturulur.
Aşağıdaki ekran görüntüleri, PDF sayfalarını göstermektedir. Başlık ve altbilgilerin çıktı PDF dosyasında da korunduğuna dikkat edin.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|
