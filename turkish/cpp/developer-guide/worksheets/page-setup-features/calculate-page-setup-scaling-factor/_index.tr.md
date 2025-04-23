---
title: Baskı Ayarı Ölçeklenme Faktörünü C++ ile Hesapla
linktitle: Sayfa Ayarı Ölçek Faktörünü Hesaplayın
type: docs
weight: 300
url: /tr/cpp/calculate-page-setup-scaling-factor/
description: Bu makale, Excel çalışma sayfasında n genişliğinde ve m yüksekliğinde sayfaya sığdırma seçeneği kullanarak Baskı Ayarları ölçekleme faktörünü programatik olarak hesaplamak için C++ API veya kütüphane kullanma örnek kodunu sağlar.
keywords: Excel c++, n sayfa genişliği ve m yüksekliğinde sığdırmak için sayfa ayarlarını hesapla, ölçekleme faktörü c++
---

{{% alert color="primary" %}}

Sayfa Ayarı Ölçeklendirme'yi **n sayfa genişliğine m sayfa yüksekliğine oturt** seçeneğini kullanarak ayarladığınızda, Microsoft Excel Sayfa Ayarı Ölçek Faktörünü hesaplar. Aynı şeyi [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/) özelliğini kullanarak hesaplayabilirsiniz. Bu özellik, yüzde değerine dönüştürülebilen bir double değeri döndürür. Örneğin, 0,5 döndürüyorsa, bu ölçek faktörünün %50 olduğu anlamına gelir.

{{% /alert %}}

Aşağıdaki örnek kod, [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/) özelliğini kullanarak sayfa ayarı ölçek faktörünü hesaplamanın örneklerini göstermektedir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
