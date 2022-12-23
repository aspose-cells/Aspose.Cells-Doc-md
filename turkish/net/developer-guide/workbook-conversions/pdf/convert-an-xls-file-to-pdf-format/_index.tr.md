---
title: XLS Dosyasını PDF Formatına Dönüştür
type: docs
weight: 30
url: /tr/net/convert-an-xls-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Taşınabilir Belge Biçimi), belgeleri, bu belgeleri oluşturmak için kullanılan yazılım, donanım ve işletim sisteminden bağımsız olarak temsil eder. Bir PDF dosyası, cihazdan ve çözünürlükten bağımsız bir şekilde herhangi bir metin, grafik ve resim kombinasyonuna sahip belgeler olabilir. PDF dosyaları genellikle sıkıştırılır, bu nedenle orijinal dosyadan daha az yer kaplarlar.

 Bazen bir Microsoft Excel dosyasını PDF'e dönüştürmeniz gerekir. Bunun için, PDF belgelerini dünya çapında dağıtmanıza olanak tanıyan hızlı, güvenli, doğru ve güvenilir bir çözüme ihtiyacınız vardır. Bu görevi gerçekleştirebilecek çok sayıda dönüştürme aracı vardır. Ancak orijinal Excel belgesinin düzeninin PDF çıktı dosyasında korunduğundan emin olmalısınız. Görüntüler, veri biçimlendirme, yazı tipleri, nitelikler, renkler, sayfa kurulum ayarları, metin yönü, kenarlıklar, çizelgeler vb. doğru ve hassas bir şekilde oluşturulmalıdır.[Aspose.Cells](https://products.aspose.com/cells/net/) aslına uygun dönüşüm sağlar.

Bu belge, bir Microsoft Excel belgesinin (resimler, grafikler, biçimlendirme vb. içeren) PDF'e nasıl dönüştürülebileceğini kapsamlı bir şekilde anlamak için tasarlanmıştır. Bu amaçla, Visual Studio.Net'te dönüştüren basit bir konsol uygulamasının nasıl oluşturulacağı gösterilmektedir. Aspose.Cells API kullanılarak PDF'e bir Excel dosyası. Dönüştürme, yüksek düzeyde hassasiyet ve doğrulukla gerçekleştirilir.

{{% /alert %}}

## **Excel'i PDF'e dönüştürme**

Bu örnek, şablon olarak bir Excel dosyası (SampleInput.xlsx) kullanır. Çalışma kitabı, grafikler ve resimler içeren çalışma sayfaları içerir. Her çalışma sayfası, yazı tipleri, nitelikler, renkler, gölgeleme efektleri ve kenarlıklar kullanan farklı biçim türleri içerir. İlk çalışma sayfasında bir sütun grafiği ve sonuncusunda bir resim var.

### **Şablon Excel Dosyası**

Şablon dosyasında, grafikler ve Medya olarak resim dahil olmak üzere üç çalışma sayfası bulunur. İlk çalışma sayfasında grafikler var ve son çalışma sayfasında aşağıdaki ekran görüntülerinde gösterildiği gibi bir görüntü var.

|![yapılacaklar:resim_alternatif_metin](Convert_an_XLS_File_to_PDF_Sheet1.png)|![yapılacaklar:resim_alternatif_metin](Convert_an_XLS_File_to_PDF_Sheet2.png)|
|:- |:- |
| İlk çalışma sayfası**(Satış tahmini)**| ikinci çalışma sayfası**(Satış raporu)**|
|![yapılacaklar:resim_alternatif_metin](Convert_an_XLS_File_to_PDF_Sheet3.png)|![yapılacaklar:resim_alternatif_metin](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Üçüncü çalışma sayfası**(Veri girişi)**| son çalışma sayfası**(Resim)**|

### **Dönüştürme işlemi**

1. Aspose.Cells'i indirin ve yükleyin:
 1. İndir Aspose.Cells for .NET.
 1. Geliştirme bilgisayarınıza kurun.
1. Bir proje oluşturun ve referanslar ekleyin:
 1. Visual Studio.Net'i başlatın.
 1. Yeni bir konsol uygulaması oluşturun.
 1. …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll dosyasına bir başvuru ekleyin
1. Dönüşüm kodunu projeye ekleyin:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}}

Elektronik tablo formüller içeriyorsa, elektronik tabloyu PDF'e dönüştürmeden hemen önce Workbook.CalculateFormula() öğesini çağırmak en iyisidir. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de işlenmesini sağlar.

{{% /alert %}}

### **Sonuç**

yukarıdaki kod çalıştırıldığında, uygulama dizininizdeki Dosyalar klasöründe bir PDF dosyası oluşturulur.
Aşağıdaki ekran görüntüleri PDF sayfalarını göstermektedir. Üst bilgilerin ve alt bilgilerin de çıktı PDF dosyasında tutulduğunu unutmayın.

|![yapılacaklar:resim_alternatif_metin](Convert_an_XLS_File_to_PDF_Converted1.png)|![yapılacaklar:resim_alternatif_metin](Convert_an_XLS_File_to_PDF_Converted2.png)|
|:- |:- |
| İlk çalışma sayfası**(Satış tahmini)**| ikinci çalışma sayfası**(Satış raporu)**|
|![yapılacaklar:resim_alternatif_metin](Convert_an_XLS_File_to_PDF_Converted3.png)|![yapılacaklar:resim_alternatif_metin](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Üçüncü çalışma sayfası**(Veri girişi)**| son çalışma sayfası**(Resim)**|
