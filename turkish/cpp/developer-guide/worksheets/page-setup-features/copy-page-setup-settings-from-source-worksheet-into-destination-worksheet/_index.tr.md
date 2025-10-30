---
title: Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Sayfa Ayarlarını Kopyala (C++)
linktitle: Sayfa Ayarlarını Kopyala
type: docs
weight: 80
url: /tr/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Bu makale, C++ API veya Kütüphane örnek kodunu kullanarak kaynak çalışma sayfasından hedef çalışma sayfasına sayfa ayarlarını programatik olarak nasıl kopyalayacağınızı açıklar.
keywords: Sayfa ayarlarını kopyala c++, hedef çalışma sayfasına sayfa ayarlarını kopyala c++
---

## **Olası Kullanım Senaryoları**

Yeni bir çalışma sayfası eklediğinizde, varsayılan *Sayfa Ayarı ayarları* içerir. Bir çalışma sayfasındaki ayarları başka bir çalışma sayfasına aktarmanız gereken zamanlar olabilir. Bu belge, Aspose.Cells API'leri kullanarak bir çalışma sayfasından diğerine Sayfa Ayarı ayarlarını kopyalamanın nasıl yapılacağını açıklar.

## **Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Sayfa Ayarı Ayarlarını Kopyala**

Aşağıdaki örnek kod, [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/) yöntemini kullanarak bir çalışma sayfasındaki *Sayfa Ayarı ayarlarını* diğerine kopyalamanın örneklerini göstermektedir. Lütfen örnek kodu ve konsol çıktısını referans için inceleyin.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
