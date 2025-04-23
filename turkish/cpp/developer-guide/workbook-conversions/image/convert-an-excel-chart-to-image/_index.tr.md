---
title: C++ ile Excel Grafiklerini Görüntüye Dönüştür
linktitle: Bir Excel Grafikini Görüntüye Dönüştür
type: docs
weight: 20
url: /tr/cpp/convert-an-excel-chart-to-image/
description: Aspose.Cells kullanarak C++ ile Excel grafiklerini görüntülere dönüştürmeyi öğrenin.
---

{{% alert color="primary" %}}

 Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, desenleri ve eğilimleri görmesine kolaylık sağlar. Örneğin, çalışma sayfası numaralarının sütunlarını analiz etmek yerine, bir grafik satışların düşüp yükseldiğini veya gerçek satışların projeksiyon satışlarıyla nasıl karşılaştırıldığını anında gösterir. İnsanlar düzenli ve kolay anlaşılır istatistiksel ve grafiksel bilgileri sunmak ister. Bir resim yardımcı olur.

 Bazen uygulamalarda veya web sayfalarında grafiklere ihtiyaç duyulur. Veya bunlar bir Word belgesi, PDF dosyası, PowerPoint sunumu veya başka bir uygulama için gerekebilir. Her durumda, grafiği başka yerlerde kullanabilmek için resmi olarak görüntülemeniz gerekir.

{{% /alert %}}

## **Grafikleri Görüntüye Dönüştürme**

Buradaki örneklerde, bir pasta grafiği ve bir sütun grafiği resimlere dönüştürülmüştür.

### **Bir Dilim Grafiğini Bir Görüntü Dosyasına Dönüştürme**

Öncelikle, Microsoft Excel'de bir dilim grafiği oluşturun ve ardından bu örneklerdeki kod, şablon Microsoft Excel dosyasındaki dilim grafiğine dayalı EMF bir görüntü oluşturur.

|**Çıktı: pasta dilimi grafiği resmi**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Microsoft Excel'de bir pasta grafiği oluşturun:
   1. Microsoft Excel'de yeni bir çalışma kitabı açın.
   1. Bir çalışsayfaya bazı veriler girin.
   1. Veriye dayanarak bir pasta grafiği oluşturun.
   1. Dosyayı kaydedin.

|**Giriş dosyası.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells for C++'i indirin](https://downloads.aspose.com/cells/cpp).
   1. Geliştirme bilgisayarınıza kurun.

Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun bir süresi yoktur ve yalnızca çıktı belgelerine filigran yerleştirir.

1. Bir proje oluşturun:
   1. C++ geliştirme ortamınızı başlatın (örn. Visual Studio).
   1. Yeni bir konsol uygulaması oluşturun.
   1. Aspose.Cells'e referans ekleyin. Bu proje Aspose.Cells kullanır, bu yüzden Aspose.Cells kütüphanesine referans ekleyin.
   1. Grafikleri bulan ve dönüştüren kodu yazın. Aşağıdaki kod, görevi gerçekleştirmek için bileşen tarafından kullanılan kod örneğidir. Çok az kod satırı kullanılmıştır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Bir Sütun Grafiğini Bir Görüntü Dosyasına Dönüştürme**

İlk olarak, Microsoft Excel'de bir sütun grafiği oluşturun ve yukarıdaki gibi bir görüntü dosyasına dönüştürün. Örnek kodu çalıştırdıktan sonra, şablon Excel dosyasındaki sütun grafiğine göre bir JPEG dosyası oluşturulur.

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

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
