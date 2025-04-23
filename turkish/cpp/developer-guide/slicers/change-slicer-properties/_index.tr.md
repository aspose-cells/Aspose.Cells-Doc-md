---
title: Slicer Özelliklerini Değiştirme (C++)
linktitle: Slice Özelliklerini Değiştir
type: docs
weight: 70
url: /tr/cpp/change-slicer-properties/
description: Aspose.Cells ile Excel dosyalarında Slicer özelliklerini değiştirin.
---

## **Olası Kullanım Senaryoları**

Dilimleyicinin konumu veya satır yüksekliği gibi dilimleyici özelliklerini değiştirmek isteyebileceğiniz durumlar olabilir. Aspose.Cells size bu özellikleri güncelleme seçeneği sunar.

## **Slice Özelliklerini Değiştir**

Lütfen aşağıdaki örnek kodu görün. İçinde bir tablo içeren [örnek Excel dosyasını](sampleCreateSlicerToExcelTable.xlsx) yükler. Ardından, ilk sütuna dayalı olarak dilimleyici oluşturur ve satır yüksekliği, genişlik, yazdırılabilir, başlık vb. gibi özelliklerini değiştirir. Çalışma kitabını [çıkışDilimleyiciÖzellikleriniDeğiştir.xlsx](çıkışDilimleyiciÖzellikleriniDeğiştir.xlsx) olarak kaydeder.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
