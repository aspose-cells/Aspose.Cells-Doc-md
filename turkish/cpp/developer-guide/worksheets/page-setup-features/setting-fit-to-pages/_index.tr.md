---
title: Excel i Sığdırılmış Sayfalar Geniş ve Yüksek olarak Yazdırma (C++) ile
linktitle: Excel i Geniş ve Yüksek olarak Yazdırma
type: docs
weight: 200
url: /tr/cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Bu makale, Aspose.Cells kütüphanesi kullanarak C++ ile FitToPagesWide ve FitToPagesTall nasıl ayarlanır gösteren kodu anlatır.
keywords: C++ FitToPagesWide ve FitToPagesTall Nasıl Ayarlanır, FitToPagesWide ve FitToPagesTall Nasıl Eklenir, Excel de FitToPagesWide ve FitToPagesTall Nasıl Ayarlanır, Excel de FitToPagesWide ve FitToPagesTall Nasıl Temizlenir, Excel i Uyumlu Sayfalar Geniş ve Yüksek olarak Yazdırma, Çalışma Sayfasını Tek Sayfada Yazdırma, Çalışma Sayfasının Tüm Sütunlarını Tek Sayfada Yazdırma.
---

## **Giriş**

FitToPagesWide ve FitToPagesTall ayarları, e-print uygulamalarında (Microsoft Excel gibi) baskı sırasında bir e-tablonun nasıl ölçekleneceğini kontrol etmek için kullanılır. Bu ayarlar, baskı alınan çıktının yatay ve dikey olarak belirli bir sayfa sayısı içinde kalmasını sağlar. İşte her ayarın detayları:

1. FitToPagesWide: Bu ayar, baskı sonucunun kaç sayfa genişliğinde olacağını belirtir. Örneğin, FitToPagesWide 1 olarak ayarlandığında, içeriğin tek bir sayfa genişliğine sığacak şekilde ölçeklendiği anlamına gelir, sayfanın genişliği ne olursa olsun.
1. FitToPagesTall: Bu ayar, baskı sonucunun kaç sayfa yüksekliğinde olacağını belirtir. Örneğin, FitToPagesTall 1 olarak ayarlandığında, içeriğin tek bir sayfa yüksekliğine sığacak şekilde ölçeklendiği anlamına gelir, satır sayısı ne olursa olsun.

## **Neden FitToPagesWide ve FitToPagesTall Kullanılır**
İşte FitToPagesWide ve FitToPagesTall ayarlarını kullanmanın bazı nedenleri:
1. Yazdırılan Düzen Üzerinde Kontrol: Genişlik ve yükseklik olarak sayfa sayısını belirleyerek, yazdırılan belgenin okunabilir ve iyi organize edilmiş olmasını sağlayabilirsiniz, hiçbir sütun veya satır sayfalar arasında garip şekilde bölünmez.
1. Tutarlılık: Birden fazla sayfa veya rapor yazdırıyorsanız, bu ayarları kullanmak tutarlı bir format sağlar, böylece yazdırılan belgeleri karşılaştırmak ve analiz etmek daha kolay olur.
1. Profesyonel Sunum: İçeriği uygun şekilde ölçeklendirmek ve belirli sayfa sayısına sığdırmak, verilerinizin daha profesyonel ve göze hoş gelen bir sunumunu sağlar.

## **Excel'de Dosyayı Geniş ve Yüksek olarak Yazdırmak için nasıl yapılır**

Microsoft Excel'de FitToPagesWide ve FitToPagesTall ayarlarını yapmak için aşağıdaki adımları izleyin:

1. Excel çalışma kitabınızı açın ve yazdırmak istediğiniz sayfaya gidin.
1. Şerit üzerindeki Sayfa Düzeni sekmesine gidin.
1. Sayfa Yapılandırması grubunda, sağ alt köşedeki küçük oka tıklayarak Sayfa Yapılandırma iletişim kutusunu açın.
1. Sayfa Yapılandırma iletişim kutusunda, Sayfa sekmesine gidin.
1. Ölçeklendirme altında, "Sığdır" seçeneğini seçin ve ardından istediğiniz genişlik ve yükseklik sayfa sayısını belirtin: İlk kutuya kaç sayfa genişliğinde olmasını istediğinizi girin (Sığdır x sayfa genişliği). İkinci kutuya ise kaç sayfa yüksekliğinde olmasını istediğinizi girin (Sığdır y sayfa yüksekliği).
<br>
<img src="2.png" width=60% />

1. Ayarları uygulamak için Tamam'a tıklayın.

## **Aspose.Cells kullanarak Excel'i Uyumlu Sayfalar Geniş ve Yüksek olarak Yazdırma Yöntemi**

Belirli bir çalışma sayfasında FitToPagesWide ve FitToPagesTall ayarlarını yapmak için: Önce [örnek dosyayı](input.xlsx) yükleyin, ardından istediğiniz sayfa için [**Worksheet.GetFitToPagesTall()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopagestall/) ve [**Worksheet.GetFitToPagesWide()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopageswide/) özelliklerini [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) nesnesinde değiştirmeniz gerekir. İşte C++ örneği:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(U16String(u"input.xlsx"));

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Set the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Save the workbook
    workbook.Save(U16String(u"out_net.pdf"));

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Çalışma Sayfasını Tek Sayfada Yazdırma Aspose.Cells ile nasıl yapılır**

Çalışma sayfasını tek sayfa olarak yazdırmak için: Önce [örnek dosyayı](sample.xlsx) yükleyin, ardından [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getonepagepersheet/) özelliğini ayarlayın. İşte C++ örneği:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions object
    PdfSaveOptions options;

    // Set options for exporting PDF
    options.SetOnePagePerSheet(true);

    // Save the workbook to a PDF file
    workbook.Save(u"OnePagePerSheet.pdf", options);

    std::cout << "Workbook saved as OnePagePerSheet.pdf!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Çıktı sonucu:
<br>
<img src="3.png" width=60% />

## **Aspose.Cells kullanarak Çalışma Sayfasının Tüm Sütunlarını Tek Sayfada Yazdırma**

Çalışma Sayfasındaki tüm sütunları tek sayfa olarak yazdırmak için: Önce [örnek dosyayı](sample.xlsx) yükleyin, ardından [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getallcolumnsinonepagepersheet/) özelliğini ayarlayın. İşte C++ örneği:

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object with the specified file.
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions instance.
    PdfSaveOptions options;

    // Set options for saving the workbook as a PDF.
    options.SetAllColumnsInOnePagePerSheet(true);

    // Save the workbook as a PDF file with the specified options.
    workbook.Save(u"AllColumnsInOnePagePerSheet.pdf", options);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Çıktı sonucu:
<br>
<img src="4.png" width=60% />
