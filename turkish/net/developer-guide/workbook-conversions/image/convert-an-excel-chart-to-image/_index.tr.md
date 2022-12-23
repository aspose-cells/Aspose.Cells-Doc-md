---
title: Bir Excel Grafiğini Görüntüye Dönüştür
type: docs
weight: 20
url: /tr/net/convert-an-excel-chart-to-image/
---
{{% alert color="primary" %}}

Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, kalıpları ve eğilimleri görmesini kolaylaştırır. Örneğin, çalışma sayfası numaralarının sütunlarını analiz etmek yerine, bir grafik bir bakışta satışların düşüp yükselmediğini veya gerçek satışların öngörülen satışlarla karşılaştırmasını gösterir. İnsanlardan sık sık istatistiksel ve grafik bilgileri anlaşılması kolay ve bakımı kolay bir şekilde sunmaları istenir. Bir resim yardımcı olur.

Bazen bir uygulamada veya web sayfalarında grafiklere ihtiyaç duyulur. Veya bir Word belgesi, PDF dosyası, PowerPoint sunumu veya başka bir uygulama için gerekli olabilir. Her durumda, grafiği başka bir yerde kullanabilmek için bir görüntü olarak işlemek istersiniz.

{{% /alert %}}

## **Grafikleri Görüntülere Dönüştürme**

Buradaki örneklerde, bir pasta grafiği ve bir sütun karakteri görüntülere dönüştürülmüştür.

### **Pasta Grafiği Görüntü Dosyasına Dönüştürme**

Önce Microsoft Excel'de bir pasta grafik oluşturun ve ardından bunu Aspose.Cells ile bir görüntü dosyasına dönüştürün. Bu örnekteki kod, şablon Microsoft Excel dosyasındaki pasta grafiği temel alarak bir EMF görüntüsü oluşturur.

|**Çıktı: pasta grafiği resmi**|
|:- |
|![yapılacaklar:resim_alternatif_metin](convert-an-excel-chart-to-image_1.png)|

1. Microsoft Excel'de bir pasta grafiği oluşturun:
 1. Microsoft Excel'de yeni bir çalışma kitabı açtı.
 1. Bir çalışma sayfasına bazı veriler girin.
 1. Verilere dayalı bir pasta grafiği oluşturdu.
 1. Dosyayı kaydedin.

|**Giriş dosyası.**|
|:- |
|![yapılacaklar:resim_alternatif_metin](convert-an-excel-chart-to-image_2.png)|

1. Aspose.Cells'i indirin ve yükleyin:
   1. [İndir Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Geliştirme bilgisayarınıza kurun.

 Herşey[Aspose](http://www.aspose.com/) bileşenler ilk kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve çıktı belgelerine yalnızca filigran ekler.

1. Bir proje oluşturun:
 1. Visual Studio.Net'i başlatın.
 1. Yeni bir konsol uygulaması oluşturun. Bu örnek, bir C# konsol uygulamasını kullanır, ancak VB.NET'i de kullanabilirsiniz.
 1. Bir referans ekleyin. Bu proje Aspose.Cells'i kullanıyor, dolayısıyla Aspose.Cells'e bir referans ekleyin, örneğin ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Grafiği bulan ve dönüştüren kodu yazın. Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıdadır. Çok az kod satırı kullanılmıştır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Sütun Grafiğini Görüntü Dosyasına Dönüştürme**

Önce Microsoft Excel'de bir sütun grafiği oluşturun ve yukarıdaki gibi bir görüntü dosyasına dönüştürün. Örnek kodu çalıştırdıktan sonra, şablon Excel dosyasındaki sütun grafiğine göre bir JPEG dosyası oluşturulur.

|**Çıktı dosyası: bir sütun grafiği görüntüsü.**|
|:- |
|![yapılacaklar:resim_alternatif_metin](convert-an-excel-chart-to-image_3.png)|

1. Microsoft Excel'de bir sütun grafiği oluşturun:
 1. Microsoft Excel'de yeni bir çalışma kitabı açın.
 1. Bir çalışma sayfasına bazı veriler girin.
 1. Verilere dayalı bir sütun grafiği oluşturun.
 1. Dosyayı kaydedin.

|**Giriş dosyası.**|
|:- |
|![yapılacaklar:resim_alternatif_metin](convert-an-excel-chart-to-image_4.png)|

1. Yukarıda açıklandığı gibi referanslarla bir proje oluşturun.
1. Grafiği dinamik olarak bir görüntüye dönüştürün. Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıdadır. Kod bir öncekine benzer:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
