---
title: Rapor Filtre Sayfalarını göster seçeneği with C++
linktitle: Rapor Filtresi Sayfalarını Göster Seçeneği
type: docs
weight: 110
url: /tr/cpp/show-report-filter-pages-option/
description: Pivot tablolarında "Rapor Filtresi Sayfalarını Göster" seçeneğini nasıl etkinleştireceğinizi Aspose.Cells for C++ kullanarak öğrenin.
---

## **Rapor Filtresi Sayfalarını Göster Seçeneği**
Excel, pivot tablolar oluşturmayı, rapor filtreleri eklemeyi ve "Rapor Filtresi Sayfalarını Göster" seçeneğini etkinleştirmeyi destekler. Aspose.Cells ayrıca bu özelliği destekler ve oluşturulan pivot tabloda "Rapor Filtresi Sayfalarını Göster" seçeneğini etkinleştirebilir. Aşağıda, Excel'deki "Rapor Filtresi Sayfalarını Göster" seçeneğini gösteren bir ekran görüntüsü vardır.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

Örnek kaynak dosyası ve çıktı dosyaları test etmek için buradan indirilebilir:

` ` [Kaynak Excel Dosyası](81920786.xlsx) 

[Çıktı Excel Dosyası](81920787.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
