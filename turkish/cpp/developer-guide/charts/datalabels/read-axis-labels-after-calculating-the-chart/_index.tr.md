---
title: Grafiği Hesapladıktan Sonra Eksen Etiketlerini Okuma ile C++
linktitle: Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma
description: Aspose.Cells for C++ kullanarak grafiği hesapladıktan sonra eksen etiketlerini nasıl okuyacağınızı öğrenin. Kılavuzumuz, erişme ve alma, formatlama ve konumlandırma dahil olmak üzere eksen etiketlerini nasıl alacağınızı gösterecek.
keywords: Aspose.Cells for C++, grafik, eksen etiketleri, hesaplama, okuma, erişim, alma, biçimlendirme, konumlandırma.
type: docs
weight: 90
url: /tr/cpp/read-axis-labels-after-calculating-the-chart/
---

## **Olası Kullanım Senaryoları**

Grafiğinizin değerlerini hesapladıktan sonra eksen etiketlerini okuyabilirsiniz. Bu amaçla lütfen bu amaç için [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/) yöntemini kullanın, bu size eksen etiketlerinin listesini döndürecektir.

## **Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma**

Lütfen aşağıdaki örnek kodu inceleyin; bu örnek Excel dosyasını yükler ve çalışma sayfasındaki grafiğin kategori eksen etiketlerini okur. Ardından eksen etiketlerinin değerlerini konsolda yazdırır. Referans için aşağıdaki örnek kodun konsol çıktısına bakınız.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"ReadAxisLabels.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    Chart ch = ws.GetCharts().Get(0);

    ch.Calculate();

    Vector<U16String> lstLabels = ch.GetCategoryAxis().GetAxisTexts();

    std::wcout << L"Category Axis Labels: " << std::endl;
    std::wcout << L"---------------------" << std::endl;

    for (int32_t i = 0; i < lstLabels.GetLength(); ++i)
    {
        std::wcout << reinterpret_cast<const wchar_t*>(lstLabels[i].GetData()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
