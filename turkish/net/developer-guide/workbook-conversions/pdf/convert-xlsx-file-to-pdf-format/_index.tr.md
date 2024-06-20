---
title: XLSX Dosyasını PDF Biçimine Dönüştür
type: docs
weight: 30
url: /tr/net/convert-xlsx-file-to-pdf-format/
---

{{% alert color="primary" %}}

PDF (Taşınabilir Belge Biçimi), bu belgeleri oluşturmak için kullanılan yazılım, donanım ve işletim sisteminden bağımsız olarak belgeleri temsil eder. Bir PDF dosyası, aygıt bağımsız ve çözünürlük bağımsız bir şekilde metin, grafik ve resimlerin herhangi bir kombinasyonunu içerebilir. PDF dosyaları genellikle sıkıştırılır, bu nedenle orijinal dosyadan daha az yer kaplar.

Bazı durumlarda, bir Microsoft Excel dosyasını PDF'ye dönüştürmeniz gerekebilir. Bunun için dünya çapında PDF belgeleri dağıtmanıza olanak tanıyan hızlı, güvenli, kesin ve güvenilir bir çözüme ihtiyacınız vardır. Bu görevi yerine getirebilecek birçok dönüştürme aracı bulunmaktadır. Ancak orijinal Excel belgesinin düzeninin çıktı PDF dosyasında korunduğundan emin olmanız gerekir. Resimler, grafikler, şekiller, veri biçimlendirme, yazı tipleri, öznitelikler, renkler, sayfa ayarlama ayarları, metin yönlendirmesi, sınırlar, grafikler vb. kesin ve doğru bir şekilde oluşturulmalıdır. [Aspose.Cells](https://products.aspose.com/cells/net/), yüksek sadakatli dönüşümü garanti altına alır.

Bu belge, bir Microsoft Excel belgesinin (resimler, grafikler, biçimlendirme vb. içeren) nasıl PDF'ye dönüştürüleceğinin kapsamlı bir anlayışını sağlamak üzere tasarlanmıştır. Bu amaçla, Aspose.Cells API'sını kullanarak bir Excel dosyasının nasıl PDF'ye dönüştürüleceğini gösteren Visual Studio.Net'te basit bir konsol uygulamasının nasıl oluşturulacağını gösterir. Dönüşüm, yüksek derecede hassasiyet ve doğrulukla gerçekleştirilir.

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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, elektronik tabloyu PDF'ye dönüştürmeden önce [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) yöntemini çağırmak en iyisidir. Böylece formül bağımlı değerlerin tekrar hesaplanmasını sağlar ve doğru değerler PDF'de görüntülenir.

{{% /alert %}}

### **Sonuç**

Yukarıdaki kod çalıştırıldığında, bir PDF dosyası uygulama dizinindeki Dosyalar klasöründe oluşturulur.
Aşağıdaki ekran görüntüleri, PDF sayfalarını göstermektedir. Başlık ve altbilgilerin çıktı PDF dosyasında da korunduğuna dikkat edin.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|İlk çalışma sayfası **(Satış Tahmini)**|İkinci çalışma sayfası **(Satış Raporu)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Üçüncü çalışma sayfası **(Veri Girişi)**|Son çalışma sayfası **(Resim)**|
