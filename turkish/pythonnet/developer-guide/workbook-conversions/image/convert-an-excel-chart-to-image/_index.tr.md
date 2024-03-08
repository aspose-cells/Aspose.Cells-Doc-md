---
title: Excel Grafiğinin Görüntüye Dönüştürülmesi
type: docs
weight: 20
url: /tr/python-net/convert-an-excel-chart-to-image/
description: Aspose.Cells for Python via .NET API'i kullanarak bir Excel Grafiği Görüntüye dönüştürün.
keywords: Python Convert an Excel Chart to Image, Export an Excel Chart to Image in Python via NET, Python Save an Excel Chart to Image.
---
{{% alert color="primary" %}}

Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, kalıpları ve eğilimleri görmesini kolaylaştırır. Örneğin, çalışma sayfası numaralarının sütunlarını analiz etmek yerine, bir grafik bir bakışta satışların düşüp düşmediğini veya gerçek satışların öngörülen satışlarla karşılaştırıldığında nasıl olduğunu gösterir. İnsanlardan sıklıkla istatistiksel ve grafiksel bilgileri anlaşılması kolay ve bakımı kolay bir şekilde sunmaları istenir. Bir resim yardımcı olur.

Bazen bir uygulamada veya web sayfalarında grafiklere ihtiyaç duyulur. Veya bir Word belgesi, PDF dosyası, PowerPoint sunumu veya başka bir uygulama için gerekli olabilir. Her durumda, grafiği başka bir yerde kullanabilmeniz için resim olarak oluşturmak istersiniz.

{{% /alert %}}

##  **Grafikleri Görsellere Dönüştürme**

Buradaki örneklerde, bir pasta grafiği ve bir sütun karakteri görsellere dönüştürülmüştür.

###  **Pasta Grafiğini Görüntü Dosyasına Dönüştürme**

Öncelikle Microsoft Excel'de bir pasta grafiği oluşturun ve ardından bunu Aspose.Cells for Python via .NET ile bir resim dosyasına dönüştürün. Bu örnekteki kod, Microsoft Excel dosyası şablonundaki pasta grafiğini temel alarak bir EMF resmi oluşturur.

|**Çıktı: pasta grafik resmi**|
| :- |
|![yapılacak şey:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Microsoft Excel'de bir pasta grafiği oluşturun:
 1. Microsoft Excel'de yeni bir çalışma kitabı açıldı.
 1. Bazı verileri bir çalışma sayfasına girin.
 1. Verilere dayalı olarak pasta grafiği oluşturuldu.
 1. Dosyayı kaydedin.

|**Giriş dosyası.**|
| :- |
|![yapılacak şey:image_alt_text](convert-an-excel-chart-to-image_2.png)|

Python paketlerimizi PyPi depolarında barındırıyoruz.

Aspose.Cells for Python'i pypi'den yükleyin, komutu şu şekilde kullanın: $ pip install aspose-cells-python.

Ayrıca geliştirici ortamınıza “Aspose.Cells for Python via .NET” kurulumunun nasıl yapılacağına dair adım adım talimatları takip edebilirsiniz.
1. Aspose.Cells for Python via .NET'i indirin ve yükleyin:
 1. Aspose.Cells for Python via .NET'i şuradan yükleyin:[pypi](https://pypi.org/project/aspose-cells-python/)komutu şu şekilde kullanın: $ pip install aspose-cells-python.
 1. Ayrıca aşağıdakileri de takip edebilirsiniz:[adım adım talimatlar](https://docs.aspose.com/cells/python-net/getting-started/)geliştirici ortamınıza "Aspose.Cells for Python via .NET" nasıl kurulacağı hakkında.

 Tüm[Aspose](http://www.aspose.com/) bileşenler ilk kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca çıktı belgelerine filigranlar enjekte eder.

1. Bir proje oluşturun:
 1. Visual Studio'yu başlatın.
 1. Python projenize bir kütüphane referansı ekleyin (kütüphaneyi içe aktarın).
 1. Grafiği bulan ve dönüştüren kodu yazın. Aşağıda, bileşenin görevi gerçekleştirmek için kullandığı kod bulunmaktadır. Çok az kod satırı kullanılıyor.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

###  **Sütun Grafiğini Görüntü Dosyasına Dönüştürme**

Öncelikle Microsoft Excel'de bir sütun grafiği oluşturun ve bunu yukarıdaki gibi bir görüntü dosyasına dönüştürün. Örnek kod çalıştırıldıktan sonra şablon Excel dosyasındaki sütun grafiğine göre JPEG dosyası oluşturulur.

|**Çıktı dosyası: bir sütun grafiği görüntüsü.**|
| :- |
|![yapılacak şey:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Microsoft Excel'de bir sütun grafiği oluşturun:
 1. Microsoft Excel'de yeni bir çalışma kitabı açın.
 1. Bazı verileri bir çalışma sayfasına girin.
 1. Verilere dayalı bir sütun grafiği oluşturun.
 1. Dosyayı kaydedin.

|**Giriş dosyası.**|
| :- |
|![yapılacak şey:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Yukarıda açıklandığı gibi referanslarla birlikte bir proje oluşturun.
1. Grafiği dinamik olarak bir resme dönüştürün. Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıdadır. Kod öncekine benzer:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
