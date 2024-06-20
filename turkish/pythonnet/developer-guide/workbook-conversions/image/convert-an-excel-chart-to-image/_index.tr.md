---
title: Bir Excel Grafikini Görüntüye Dönüştür
type: docs
weight: 20
url: /tr/python-net/convert-an-excel-chart-to-image/
description: Aspose.Cells for Python via .NET API sını kullanarak bir Excel Grafik İçeri Aktar.
keywords: Python da Bir Excel Grafik İçeri Aktar, Python da Bir Excel Grafik İhracatı via NET, Python da Bir Excel Grafik İhracatı.
---

{{% alert color="primary" %}}

Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, desenleri ve trendleri görmesini kolaylaştırır. Örneğin, çalışsayfa numaralarını analiz etmek yerine, bir grafik, satışların düşüp düşmediğini veya yükseldiğini veya gerçek satışların projeksiyonlanmış satışlarla nasıl karşılaştırıldığını hemen gösterir. İnsanlar genellikle istatistiksel ve grafiksel bilgileri anlaşılması ve bakımı kolay bir şekilde sunmaları istenir. Bir resim yardımcı olur.

Bazen, grafikler bir uygulamada veya web sayfalarında gereklidir. Veya bir Word belgesi, PDF dosyası, bir PowerPoint sunumu veya başka bir uygulama için gereklilik olabilir. Her durumda, grafiği başka bir yerde kullanabilmek için görüntü olarak render etmek istersiniz.

{{% /alert %}}

## **Grafikleri Görüntüye Dönüştürme**

Bu örneklerde, bir dilim grafiği ve bir sütun grafiği görüntüye dönüştürülür.

### **Bir Dilim Grafiğini Bir Görüntü Dosyasına Dönüştürme**

İlk olarak, Microsoft Excel'de bir pasta grafiği oluşturun ve daha sonra Aspose.Cells for Python via .NET ile onu bir görüntü dosyasına dönüştürün. Bu örnekteki kod, şablon Microsoft Excel dosyasındaki pasta grafiğine dayalı bir EMF görüntüsü oluşturur.

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

Python paketlerimizi PyPi depolarında barındırıyoruz. 

Aspose.Cells for Python'ı pypi'dan kurun, komutu şu şekilde kullanın: $ pip install aspose-cells-python.

Ve ayrıca"Aspose.Cells for Python via .NET" nasıl kurulacağına dair adım adım talimatları takip edebilirsiniz.
1. Aspose.Cells for Python via .NET'yi indirin ve kurun:
   1. [pypi](https://pypi.org/project/aspose-cells-python/) üzerinden Aspose.Cells for Python via .NET'yi yükleyin, komutu şu şekilde kullanabilirsiniz: $ pip install aspose-cells-python.
   1. Ve geliştirme ortamınıza"Aspose.Cells for Python via .NET" nasıl kurulacağına dair [adım adım talimatları](https://docs.aspose.com/cells/python-net/getting-started/) takip edebilirsiniz.

Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun bir süresi yoktur ve yalnızca çıktı belgelerine filigran yerleştirir.

1. Bir proje oluşturun:
   1. Visual Studio'yu başlatın.
   1. Python projenize bir kütüphane referansı ekleyin (kütüphaneyi içe aktarın).
   1. Grafikleri bulan ve dönüştüren kodu yazın. Aşağıdaki kod, görevi gerçekleştirmek için bileşen tarafından kullanılan kod örneğidir. Çok az kod satırı kullanılmıştır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
