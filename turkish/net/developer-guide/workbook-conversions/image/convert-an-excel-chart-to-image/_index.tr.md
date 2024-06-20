---
title: Bir Excel Grafikini Görüntüye Dönüştür
type: docs
weight: 20
url: /tr/net/convert-an-excel-chart-to-image/
---

{{% alert color="primary" %}}

Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, desenleri ve trendleri görmesini kolaylaştırır. Örneğin, çalışsayfa numaralarını analiz etmek yerine, bir grafik, satışların düşüp düşmediğini veya yükseldiğini veya gerçek satışların projeksiyonlanmış satışlarla nasıl karşılaştırıldığını hemen gösterir. İnsanlar genellikle istatistiksel ve grafiksel bilgileri anlaşılması ve bakımı kolay bir şekilde sunmaları istenir. Bir resim yardımcı olur.

Bazen, grafikler bir uygulamada veya web sayfalarında gereklidir. Veya bir Word belgesi, PDF dosyası, bir PowerPoint sunumu veya başka bir uygulama için gereklilik olabilir. Her durumda, grafiği başka bir yerde kullanabilmek için görüntü olarak render etmek istersiniz.

{{% /alert %}}

## **Grafikleri Görüntüye Dönüştürme**

Bu örneklerde, bir dilim grafiği ve bir sütun grafiği görüntüye dönüştürülür.

### **Bir Dilim Grafiğini Bir Görüntü Dosyasına Dönüştürme**

Öncelikle, Microsoft Excel'de bir dilim grafiği oluşturun ve ardından bu örneklerdeki kod, şablon Microsoft Excel dosyasındaki dilim grafiğine dayalı EMF bir görüntü oluşturur.

|**Çıktı: pasta dilimi grafiği resmi**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Microsoft Excel'de bir pasta dilimi grafiği oluşturun:
   1. Microsoft Excel'de yeni bir çalışma kitabı açıldı.
   1. Bir çalışsayfaya bazı veriler girin.
   1. Verilere dayalı bir pasta dilimi grafiği oluşturuldu.
   1. Dosyayı kaydedin.

|**Giriş dosyası.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells for .NET'i İndir](https://downloads.aspose.com/cells/net).
   1. Geliştirme bilgisayarınıza kurun.

Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun bir süresi yoktur ve yalnızca çıktı belgelerine filigran yerleştirir.

1. Bir proje oluşturun:
   1. Visual Studio.Net'i başlatın.
   1. Yeni bir konsol uygulaması oluşturun. Bu örnek bir C# konsol uygulaması kullanır, ancak VB.NET de kullanabilirsiniz.
   1. Bir referans ekleyin. Bu proje Aspose.Cells'i kullandığından, örneğin ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll yolunu Aspose.Cells'e bir referans olarak ekleyin.
   1. Grafikleri bulan ve dönüştüren kodu yazın. Aşağıdaki kod, görevi gerçekleştirmek için bileşen tarafından kullanılan kod örneğidir. Çok az kod satırı kullanılmıştır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Bir Sütun Grafiğini Bir Görüntü Dosyasına Dönüştürme**

Öncelikle Microsoft Excel'de bir sütun grafiği oluşturun ve yukarıdaki gibi bir görüntü dosyasına dönüştürün. Örnek kodu çalıştırdıktan sonra, şablon Excel dosyasındaki sütun grafiğine dayalı bir JPEG dosyası oluşturulur.

|**Çıktı dosyası: bir sütun grafiği görüntüsü.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Microsoft Excel'de bir sütun grafiği oluşturun:
   1. Microsoft Excel'de yeni bir çalışma kitabı açın.
   1. Bir çalışsayfaya bazı veriler girin.
   1. Verilere dayalı bir sütun grafiği oluşturun.
   1. Dosyayı kaydedin.

|**Giriş dosyası.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Yukarıda açıklandığı gibi referanslarla bir projeyi kurun.
1. Grafik dinamik olarak bir görüntü olarak dönüştürün. Bileşen tarafından görevi gerçekleştirmek için kullanılan kod aşağıda verilmiştir. Kod öncekiyle benzerdir:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
