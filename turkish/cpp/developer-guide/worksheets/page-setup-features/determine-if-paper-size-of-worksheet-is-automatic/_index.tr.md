---
title: Çalışma sayfasının Kağıt Boyutu Otomatik mi olduğunu C++ ile belirleme
linktitle: Çalışma Sayfasının Kağıt Boyutunun Otomatik Olup Olmadığını Belirleyin
type: docs
weight: 90
url: /tr/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Bu makale, C++ API veya kütüphane örnek kodunu kullanarak çalışma sayfasının Kağıt Boyutunun otomatik olup olmadığını programatik olarak belirleme yöntemini açıklar.
keywords: Çalışma sayfası otomatik kağıt boyutu olup olmadığını belirleyin c++
---

## **Olası Kullanım Senaryoları**

Çoğu zaman, çalışma sayfasının kağıt boyutu otomatik olur. Otomatik olduğunda, genellikle *Letter* olarak ayarlanır. Bazen kullanıcı, çalışma sayfasının kağıt boyutunu ihtiyaçlarına göre ayarlar. Bu durumda, kağıt boyutu otomatik değildir. Çalışma sayfası kağıt boyutunun otomatik olup olmadığını [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/) özelliğini kullanarak bulabilirsiniz.**

## **Çalışma Sayfasının Kağıt Boyutunu Otomatik Olup Olmadığını Belirleme**

Aşağıda verilen örnek kod, aşağıdaki iki Excel dosyasını yükler

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ve ilk çalışma sayfasının kağıt boyutunun otomatik olup olmadığını kontrol eder. Microsoft Excel'de, sayfa Düzeni penceresi aracılığıyla kağıt boyutunun otomatik olup olmadığını kontrol edebilirsiniz, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

Verilen örnek Excel dosyaları ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı işte böyle olur.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
