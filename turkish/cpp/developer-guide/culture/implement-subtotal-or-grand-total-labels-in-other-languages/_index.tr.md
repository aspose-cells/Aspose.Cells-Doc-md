---
title: Diğer Dillerde Alt Toplam veya Genel Toplam Etiketi Uygula
linktitle: Diğer Dillerde Alt Toplam veya Genel Toplam Etiketi Uygula
type: docs
weight: 50
url: /tr/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Aspose.Cells for C++ kullanarak, diğer dillerde alt toplam ve genel toplam etiketlerinin nasıl uygulanacağı hakkında bilgi edinin.
---

## **Olası Kullanım Senaryoları**

 Bazen, Çin, Japon, Arap, Hint gibi başka dillerde alt toplam ve genel toplam etiketleri göstermek istersiniz. Aspose.Cells, bunu [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfı ve [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) özelliği kullanarak yapmanızı sağlar. İşte [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfını nasıl kullanacağınızı anlatan bu makaleye göz atın:

- [Özel Ara Toplamların Kullanımı ve Pasta Grafiği Etiketleri İçin GlobalizationSettings Sınıfını Kullanma](/cells/tr/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## ** Diğer Dillerde Alt Toplam veya Genel Toplam Etiketi Uygula**

 Aşağıdaki örnek kod, [örnek Excel dosyasını](5115151.xlsx) yükler ve Çin dilinde alt toplam ve genel toplam adlarını uygular. Lütfen bu kod tarafından oluşturulan [çıktı Excel dosyasını](5115152.xlsx) inceleyin. Öncelikle [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfını oluşturup, kodumuzda kullanıyoruz.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings
{
public:
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }

    U16String GetGrandTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Grand Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }
};
```

 Artık yukarıda oluşturulan sınıfı aşağıdaki gibi kodda kullanabilirsiniz:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings {
public:
    virtual U16String GetTotalName(ConsolidationFunction functionType) override {
        return u"Custom Total";
    }

    virtual U16String GetGrandTotalName(ConsolidationFunction functionType) override {
        return u"Custom Grand Total";
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sample.xlsx");

    GlobalizationSettingsImp gsi;
    wb.GetSettings().SetGlobalizationSettings(&gsi);

    Worksheet ws = wb.GetWorksheets().Get(0);

    CellArea ca = CellArea::CreateCellArea(u"A1", u"B10");
    ws.GetCells().Subtotal(ca, 0, ConsolidationFunction::Sum, {2, 3, 4});

    ws.GetCells().SetColumnWidth(0, 40);

    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
