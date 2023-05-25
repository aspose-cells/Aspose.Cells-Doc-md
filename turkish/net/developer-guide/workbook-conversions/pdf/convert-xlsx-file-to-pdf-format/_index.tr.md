---
title: XLSX Dosyasını PDF Formatına Dönüştür
type: docs
weight: 30
url: /tr/net/convert-xlsx-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Taşınabilir Belge Biçimi), belgeleri, bu belgeleri oluşturmak için kullanılan yazılım, donanım ve işletim sisteminden bağımsız olarak temsil eder. Bir PDF dosyası, cihazdan ve çözünürlükten bağımsız bir şekilde herhangi bir metin, grafik ve resim kombinasyonuna sahip belgeler olabilir. PDF dosyaları genellikle sıkıştırılır, bu nedenle orijinal dosyadan daha az yer kaplarlar.

Bazen bir Microsoft Excel dosyasını PDF'e dönüştürmeniz gerekir. Bunun için, PDF belgelerini dünya çapında dağıtmanıza olanak tanıyan hızlı, güvenli, doğru ve güvenilir bir çözüme ihtiyacınız vardır. Bu görevi gerçekleştirebilecek çok sayıda dönüştürme aracı vardır. Ancak orijinal Excel belgesinin düzeninin PDF çıktı dosyasında korunduğundan emin olmalısınız. Resimler, çizelgeler, şekiller, veri biçimlendirme, yazı tipleri, nitelikler, renkler, sayfa kurulum ayarları, metin yönü, kenarlıklar, çizelgeler vb. doğru ve tam olarak oluşturulmalıdır.[Aspose.Cells](https://products.aspose.com/cells/net/) aslına uygun dönüşüm sağlar.

Bu belge, bir Microsoft Excel belgesinin (resimler, grafikler, biçimlendirme vb. içeren) PDF'e nasıl dönüştürülebileceğini kapsamlı bir şekilde anlamak için tasarlanmıştır. Bu amaçla, Visual Studio.Net'te dönüştüren basit bir konsol uygulamasının nasıl oluşturulacağı gösterilmektedir. Aspose.Cells API kullanılarak PDF'e bir Excel dosyası. Dönüştürme, yüksek düzeyde hassasiyet ve doğrulukla gerçekleştirilir.

{{% /alert %}}

##  **Excel'i PDF'e dönüştürme**

Bu örnek, şablon olarak bir Excel dosyası (SampleInput.xlsx) kullanır. Çalışma kitabı, grafikler ve resimler içeren çalışma sayfaları içerir. Her çalışma sayfası, yazı tipleri, nitelikler, renkler, gölgeleme efektleri ve kenarlıklar kullanan farklı biçim türleri içerir. İlk çalışma sayfasında bir sütun grafiği ve sonuncusunda bir resim var.

###  **Şablon Excel Dosyası**

Şablon dosyasında, grafikler ve Medya olarak resim dahil olmak üzere üç çalışma sayfası bulunur. İlk çalışma sayfasında grafikler var ve son çalışma sayfasında aşağıdaki ekran görüntülerinde gösterildiği gibi bir görüntü var.

|![yapılacaklar:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![yapılacaklar:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| İlk çalışma sayfası**(Satış tahmini)**| ikinci çalışma sayfası**(Satış raporu)**|
|![yapılacaklar:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![yapılacaklar:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Üçüncü çalışma sayfası**(Veri girişi)**| son çalışma sayfası**(Resim)**|

###  **Dönüştürme işlemi**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

 Elektronik tablo formüller içeriyorsa, aramak en iyisidir[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)yöntemi, elektronik tabloyu PDF'e dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de oluşturulmasını sağlar.

{{% /alert %}}

###  **Sonuç**

Yukarıdaki kod çalıştırıldığında, uygulama dizininizdeki Dosyalar klasöründe bir PDF dosyası oluşturulur.
Aşağıdaki ekran görüntüleri PDF sayfalarını göstermektedir. Üst bilgilerin ve alt bilgilerin de çıktı PDF dosyasında tutulduğunu unutmayın.

|![yapılacaklar:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![yapılacaklar:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| İlk çalışma sayfası**(Satış tahmini)**| ikinci çalışma sayfası**(Satış raporu)**|
|![yapılacaklar:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![yapılacaklar:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Üçüncü çalışma sayfası**(Veri girişi)**| son çalışma sayfası**(Resim)**|
