---
title: Farklı Sayfalar İçin Farklı Başlık ve Altbilgi Ayarlama (C++) ile
linktitle: Farklı Başlık ve Altbilgi Ayarlama
type: docs
weight: 35
url: /tr/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Bu makale, C++ Kütüphanesi ve API kullanarak Excel çalışma sayfası Sayfa Düzeni ayarlarının çeşitli başlık ve altbilgilerini programlı olarak nasıl ayarlayacağınızı gösteren örnek kodlar sağlar. İlk sayfa, tekler ve çiftler için başlık ve altbilgileri ayarlayabilirsiniz.
keywords: İlk sayfa için Excel başlık ve altbilgi ayarlama c++, tekler ve çiftler sayfalar için ayarlama c++
---

{{% alert color="primary" %}}

MS Excel, ilk sayfa, tekler ve çiftler sayfalar için farklı başlık ve altbilgi ayarlamayı 2007'den beri desteklemektedir.
Aspose.Cells aynı özelliği destekler.

{{% /alert %}}

## **MS Excel'de Farklı Üstbilgi ve Altbilgiler Ayarlama**

**![Farklı Üstbilgi ve Altbilgiler Ayarlama](difpage.png)**

1. **Sayfa Düzeni > Yazdırma Başlıkları > Üstbilgi/Açıklama** tıklayın.
1. **Farklı Tek ve Çift Sayfalar** veya **Farklı İlk Sayfa** kutularını işaretleyin.
1. Farklı başlık ve altbilgileri girin.

## **Aspose.Cells ile Farklı Üstbilgi ve Altbilgi Ayarlama**

Aspose.Cells, Excel ile aynı davranışı sergiler.
1. [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) ve [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) bayraklarını ayarlar 
1. Farklı başlık ve altbilgileri girin.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
