---
title: C++ kullanarak çalışma sayfasını nasıl ölçeklendirebilirim
linktitle: Sayfa Çalışma Sayfasını Nasıl Ölçeklendirilir
type: docs
weight: 130
url: /tr/cpp/how-to-scale-a-worksheet/
description: Bu makale, C++ ile Aspose.Cells kütüphanesini kullanarak çalışma sayfasını nasıl ölçeklendireceğinize dair kodlar göstermektedir.
keywords: C++ ile çalışma sayfasını ölçeklendir, C++ kullanarak çalışma sayfasını nasıl ölçeklenir, C++ da çalışma sayfası ölçeklendirme.
---

## **Olası Kullanım Senaryoları**
Çalışma sayfasını ölçeklendirmek, çalıştığınız bağlama bağlı olarak çeşitli yarar sağlayabilir. İşte birkaç yaygın neden:
1. Sayfaya Sığdır: Yazdırırken tüm içeriğin tek bir sayfaya veya belirli sayıda sayfaya sığmasını sağlamak, böylece okumayı ve yönetimi kolaylaştırmak, çok sayfalı sayfaları çevirmeye gerek kalmadan.

1. Sunum: Çalışma sayfasını daha düzenli ve profesyonel görünmesini sağlamak, özellikle toplantılarda veya raporlarda başkalarıyla paylaşıldığında.

1. Okunabilirlik: Metin ve diğer öğelerin boyutunu daha iyi okunabilirlik için ayarlamak, özellikle küçük fontları okumakta zorluk çeken kişiler için.

1. Alan Yönetimi: Çalışma sayfasında alan kullanımını optimize etmek, gereksiz boş alanın olmamasını ve tüm önemli bilgilerin görünür olmasını sağlamak, aşırı kaydırmadan.

1. Veri Görselleştirme: Çizelge ve grafiklerde, uygun alanı doldurmak için boyut ayarlaması yaparak onları daha anlaşılır hale getirmeye yardımcı olabilir.

1. Tutarlılık: Birden fazla çalışma sayfası veya belge arasında tutarlı görünüm ve his sağlamak, özellikle profesyonel ve eğitimsel ortamlar için önemlidir.

## **Excel'de Çalışma Sayfasını Nasıl Ölçeklendirilir**
Excel’de çalışma sayfasını ölçeklendirmek, içeriğinizi yazdırırken tek bir sayfaya veya belirli sayfa sayısına sığdırmaya yardımcı olabilir. İşte çalışma sayfasını ölçeklendirme adımları:

1. Çalışma Sayfanızı Açın: Ölçeklendirmek istediğiniz Excel çalışma sayfasını açın.

1. Sayfa Düzeni Sekmesine Gidin: Ribbon'da Sayfa Düzeni sekmesine tıklayın.

1. Ölçekleme Gruplarına Göz Atma: Sayfa Düzeni sekmesinde, Ölçekleyecek Gruplarını bulun. Burada ölçeklendirme ayarlarını yapabilirsiniz. Genişlik: Yazdırılan çalışma sayfasının kaç sayfa genişliğinde olacağını belirlemenizi sağlar. Yükseklik: Yazdırılan çalışma sayfasının kaç sayfa yüksekliğinde olacağını belirlemenizi sağlar. Ölçek: Burada özel bir ölçek yüzdesi de ayarlayabilirsiniz.
<br>
<img src="1.png" width=60% />

1. Genişlik ve Yükseklik Ayarları: Genişlik ve yüksekliği istediğiniz sayfa sayısına ayarlayın. Örneğin, çalışma sayfasını tek sayfaya sığdırmak istiyorsanız her ikisini de 1 sayfa yapın.

1. Ölçekleme Yüzdesini (gerekirse) Ayarlayın: Belirli bir ölçek yüzdesi ayarlamak istiyorsanız, Ölçek kutusunu ayarlayın. Örneğin, %50 olarak ayarlarsanız, her şey yarı boyutuna gelir.


## **C++ Kullanarak Çalışma Sayfası Ölçeklendirme**
Aspose.Cells, Excel dosyalarıyla programlama yapmayı sağlayan güçlü bir kütüphanedir. Bir çalışma sayfasını Aspose.Cells kullanarak ölçeklendirmek için şu adımları izlemelisiniz: [örnek dosyayı](sample.xlsx) yükleyin ve çıktı ayarlarını, içeriğin istenen sayfa sayısına veya belirli bir yüzdeye sığmasını sağlayacak şekilde düzenleyin.

### **Örnek: Sayfaya Sığdır**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the worksheet to fit to 1 page wide and 1 page tall
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the modified workbook
    workbook.Save(u"output_fit_to_page.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
<br>
<img src="3.png" width=60% />

### **Örnek: Yüzdeye Ölçekle**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the scaling to a specific percentage (e.g., 75%)
    pageSetup.SetZoom(75);

    // Save the modified workbook
    workbook.Save(u"output_scaled_percentage.xlsx");

    // Clean up Aspose.Cells resources
    Aspose::Cells::Cleanup();

    return 0;
}
```
<br>
<img src="2.png" width=60% />
