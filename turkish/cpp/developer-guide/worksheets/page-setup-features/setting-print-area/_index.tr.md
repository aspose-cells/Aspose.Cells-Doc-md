---
title: C++ ile Yazdırma Alanını Nasıl Ayarlarsınız
linktitle: Yazdırma Alanı Nasıl Ayarlanır
type: docs
weight: 200
url: /tr/cpp/how-to-set-print-area/
description: Bu makale, C++ kullanarak Aspose.Cells kitaplığı ile yazdırma alanını nasıl ayarlayacağınızı açıklayan kodu gösterir.
keywords: Yazdırma aralığını sınırlandırma, Yazdırma Aralığını Ayarla, Yazdırma Aralığını Temizle, C++ kullanarak Yazdırma Alanını Ayarla ve Temizle, C++ ile Yazdırma Alanı Nasıl Ayarlanır, C++ kullanarak Yazdırma Alanını Temizle, C++ ile Yazdırma Alanını Sıfırla, Yazdırma alanını ekleme, Yazdırma alanını kaldırma, Excel de Yazdırma Alanını Ayarla, Excel de Yazdırma Alanını Temizle.
---

## **Olası Kullanım Senaryoları**

Bir belge, örneğin bir Excel sayfası, içinde yer alan içeriği kontrol etmek için yazdırma alanı ayarlamak faydalıdır. İşte yazdırma alanı ayarlamanın bazı nedenleri:

1. Belirli Verilere Odaklanma: Sadece en önemli bölümleri yazdırabilir, gereksiz içeriği engelleyebilirsiniz.
1. Gelişmiş Düzen: İçeriğin düzenlenmesine ve düzgün şekilde sığdırılmasına yardımcı olur, bölünmeleri veya istenmeyen sayfa sonlarını önler.
1. Kaynak Tasarrufu: Yazdırma alanını sınırlandırarak kağıt ve mürekkep kullanımını azaltabilirsiniz.
1. Profesyonel Sunum: Yalnızca verilerin düzgün ve son halini yazdırdığınızdan emin olur, bu özellikle raporlar veya sunumlar için önemlidir.
1. Tutarlılık: Aynı belgeyi birden fazla kez yazdırırken, belirli bir yazdırma alanı kullanmak, çıktıdaki tutarlılığı sağlar.

<br>
Yazdırma alanı ayarlamak, özellikle büyük belgelerde, yalnızca bir kısmının paylaşılması veya yazdırılmak üzere gözden geçirilmesi gerektiğinde çok kullanışlıdır.

## **Excel'de Yazdırma Alanı Nasıl Ayarlanır**

Excel'de yazdırma alanı belirlemek için şu adımları izleyin:

1. Hücreleri Seçin: Yazdırma alanı olarak ayarlamak istediğiniz hücre aralığını tıklayıp sürükleyerek seçin.
1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki şeritteki "Sayfa Düzeni" sekmesine gidin.
1. Yazdırma Alanını Ayarla: "Sayfa Kurulum" grubunda, "Yazdırma Alanı"na tıklayın. Açılan menüden "Yazdırma Alanını Ayarla"yı seçin.
<br>
<img src="3.png" width=60% />

1. Yazdırma Alanına Ekleyin: Mevcut yazdırma alanına başka hücreler ekmek istiyorsanız, ek hücreleri seçin, "Sayfa Düzeni" sekmesinde "Yazdırma Alanı"na gidin ve "Yazdırma Alanına Ekle"yi seçin.

<br>
Bu işlem, seçilen hücreleri yazdırma alanı olarak tanımlar. Çalışma sayfasını yazdırdığınızda, yalnızca bu tanımlı alan yazdırılır.

## **Excel'de Yazdırma Alanını Temizle Nasıl Yapılır**

Excel'de yazdırma alanını temizlemek için şu adımları izleyin:

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.
1. Yazdırma Alanını Temizle: "Sayfa Kurulum" grubunda, "Yazdırma Alanı"na tıklayın. Açılan menüden "Yazdırma Alanını Temizle"yi seçin.
<br>
<img src="4.png" width=60% />

<br>
Bu işlem, önceden ayarlanmış yazdırma alanını kaldırır ve tüm çalışma sayfasının yazdırılmasına izin verir.

## **Yazdırma Alanını Temizledikten Sonra Neler Olur**

Excel gibi elektronik tablo uygulamasında Aspose.Cells kullanarak yazdırma alanını temizlemek, belgenin tamamını yazdırmak anlamına gelir. Yazdırma alanı ayarlandıysa, yalnızca belirli hücre aralığı yazdırılır. Yazdırma alanı temizlendiğinde, herhangi bir belirli aralık tanımlanmaz ve varsayılan yazdırma davranışı devreye girer, bu da tüm sayfayı içerir.

1. Varsayılan Yazdırma Davranışı: Tüm çalışma sayfası yazdırılmak üzere değerlendirilir. Bu, tüm hücrelerin verileri veya biçimlendirmeleri kabul eder.
1. Yazdırma Alanı Sınırları Kalmadı: Önceden belirlenmiş yazdırma alanı sınırları kaldırılır. Önceden belirlenen satır ve sütunlar artık bu sınırlar içinde kalmaz.
1. Tüm İçeriğin Yazdırılması: Başlıklar, altbilgiler ve çalışma sayfasındaki diğer tüm veriler yazdırma işlemine dahil edilir.

## **Aspose.Cells kullanarak Yazdırma Alanını Nasıl Belirlerim**

Belirtilmiş bir çalışma sayfasında yazdırma alanını ayarlamak için: Önce [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) nesnesinin [**Worksheet.GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) özelliğini değiştirmeniz gerekir. Bu özelliği bir aralık dizisi olarak ayarlamak yazdırma alanını belirler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath(u"input.xlsx");
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Set the print area - specify the range you want to print
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea(u"A1:D10");

    // Save the workbook
    U16String outputFilePath(u"set_print_area.pdf");
    workbook.Save(outputFilePath);

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Aspose.Cells kullanarak Yazdırma Alanını Nasıl Temizlerim**

Belirtilmiş bir çalışma sayfasında yazdırma alanını temizlemek için: Önce [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) nesnesinin [**Worksheet.GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) özelliğini değiştirmeniz gerekir. Bu özelliği boş bir dize olarak ayarlamak yazdırma alanını temizler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath(u"input.xlsx");
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea(u"");

    // Save the workbook
    U16String outputFilePath(u"clear_print_area.pdf");
    workbook.Save(outputFilePath);

    std::cout << "Print area cleared and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Çıktı sonucu:
<br>
<img src="2.png" width=60% />
