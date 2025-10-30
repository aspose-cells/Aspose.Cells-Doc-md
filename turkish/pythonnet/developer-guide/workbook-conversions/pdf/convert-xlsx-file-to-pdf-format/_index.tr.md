---
title: XLSX Dosyasını PDF Biçimine Dönüştür
type: docs
weight: 30
url: /tr/python-net/convert-xlsx-file-to-pdf-format/
description: Aspose.Cells for Python via .NET API sı ile XLSX Dosyasını PDF Formatına Dönüştürme işleminin nasıl yapılacağını öğrenin.
keywords: Python XLSX Dosyasını PDF Formatına Dönüştürme, Python ile xlsx ten pdf e çevirme, Python xlsx yi pdf e kaydetme, Python da xlsx den pdf formatına dönüştürme
---

{{% alert color="primary" %}}

PDF (Taşınabilir Belge Biçimi), bu belgeleri oluşturmak için kullanılan yazılım, donanım ve işletim sisteminden bağımsız olarak belgeleri temsil eder. Bir PDF dosyası, aygıt bağımsız ve çözünürlük bağımsız bir şekilde metin, grafik ve resimlerin herhangi bir kombinasyonunu içerebilir. PDF dosyaları genellikle sıkıştırılır, bu nedenle orijinal dosyadan daha az yer kaplar.

Zaman zaman, bir Microsoft Excel dosyasını PDF'ye dönüştürmek isteyebilirsiniz. Bunun için dünya çapında PDF belgeleri dağıtmanıza izin veren hızlı, güvenli, doğru ve güvenilir bir çözüme ihtiyacınız vardır. Bu görevi gerçekleştirebilecek pek çok dönüşüm aracı bulunmaktadır. Ancak orijinal Excel belgesinin düzeninin çıktı PDF dosyasında korunduğundan emin olmalısınız. Resimler, grafikler, şekiller, veri biçimlendirme, yazı tipleri, özellikler, renkler, sayfa düzeni ayarları, metin yönü, kenar çizgileri, grafikler vb. doğru ve kesin bir şekilde render edilmelidir. [Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) yüksek sadakatli dönüşümü garanti eder.

Bu belge, bir Microsoft Excel belgesinin (resimler, grafikler, biçimlendirme v.b. içeren) nasıl PDF'ye dönüştürüleceğini kapsamlı bir şekilde anlamak için tasarlanmıştır. Bu amaçla, Visual Studio.Net'te basit bir konsol uygulaması oluşturarak Aspose.Cells for Python via .NET API kullanarak Excel dosyasını PDF'ye dönüştürmeyi gösterir. Dönüşüm, yüksek hassasiyet ve doğruluk derecesinde gerçekleştirilir.

{{% /alert %}}

## **Excel'i PDF'ye Dönüştürme**

Bu örnek, bir Excel dosyasını (SampleInput.xlsx) bir şablon olarak kullanır. Çalışma kitabı, grafikler ve resim içeren çalışma sayfalarını içerir. Her çalışma sayfası, fontlar, öznitelikler, renkler, gölgelendirme efektleri ve sınırlar kullanılarak farklı türde biçimlendirmeler içerir. İlk çalışma sayfasında bir sütun grafiği ve son çalışma sayfasında bir resim bulunmaktadır.

### **Şablon Excel Dosyası**

Şablon dosyası, grafikler ve medya olarak bir resim içeren üç çalışma sayfasını içerir. İlk çalışma sayfasında grafikler bulunur ve son çalışma sayfasında aşağıdaki ekran görüntülerinde gösterildiği gibi bir resim bulunur.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|

### **Dönüşüm Süreci**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, spreadsheet'in PDF'e render edilmeden önce [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) yönteminin çağrılması en iyisidir. Böylelikle formül bağımlı değerler yeniden hesaplanır ve doğru değerler PDF'e render edilir.

{{% /alert %}}

### **Sonuç**

Yukarıdaki kod çalıştırıldığında, bir PDF dosyası uygulama dizinindeki Dosyalar klasöründe oluşturulur.
Aşağıdaki ekran görüntüleri, PDF sayfalarını göstermektedir. Başlık ve altbilgilerin çıktı PDF dosyasında da korunduğuna dikkat edin.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|
{{< app/cells/assistant language="python-net" >}}
