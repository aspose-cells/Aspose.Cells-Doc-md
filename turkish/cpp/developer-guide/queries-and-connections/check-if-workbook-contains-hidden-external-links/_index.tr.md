---
title: Bir çalışma kitabında gizli dış bağlantılar olup olmadığını C++ ile kontrol edin
linktitle: Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin
type: docs
weight: 230
url: /tr/cpp/check-if-workbook-contains-hidden-external-links/
description: Aspose.Cells for C++ kullanarak Excel çalışma kitaplarındaki gizli dış bağlantıları nasıl tespit edeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**
Bazen, çalışma kitabında gizli ve Microsoft Excel'de görüntülenemeyen dış bağlantılar bulunur. Aspose.Cells, görünür veya gizli olsun, tüm dış bağlantıları getirir. Ancak, [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) özelliğini kullanarak dış bağlantının görünür olup olmadığını kontrol edebilirsiniz.

## **Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin**
Aşağıdaki örnek kod, gizli dış bağlantılar içeren bir [kaynak excel dosyasını](5115413.xlsx) yükler. Bu bağlantılar Microsoft Excel'de görüntülenemez, ancak çalışma kitabında bulunur. [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) ve [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/) özelliklerini yazdırdıktan sonra [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) özelliği yazdırılır. Aşağıdaki konsol çıktısında, tüm dış bağlantıların görünmediğini görebilirsiniz.

### **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Konsol Çıktısı**
Aşağıdaki örnek kodun, verilen [örnek excel dosyası](5115413.xlsx) ile çalıştırılması sonucu konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
