---
title: Slicer ı biçimlendirme (C++)
linktitle: Dilimleyici Biçimlendirme
type: docs
weight: 20
url: /tr/cpp/formatting-slicer/
description: Microsoft Excel de dilimleyicileri Aspose.Cells ile C++ kullanarak biçimlendirin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel'de dilimleyiciyi biçimlendirebilirsiniz; sütun sayısını ayarlayarak veya stilini belirleyerek vb. Aspose.Cells ayrıca bunu [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/) ve [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/) özellikleri kullanarak yapmanıza olanak tanır.

## **Dilimleyici Biçimlendirme**

Lütfen aşağıdaki kodu inceleyin; bu, dilimleyici içeren [örnek Excel dosyasını](67338473.xlsx) yükler. Dilimleyiciye erişir ve sütun sayısını ile stil türünü ayarlar ve [çıktı Excel dosyası](67338474.xlsx) olarak kaydeder. Ekran görüntüsü, örnek kodun çalıştırılmasından sonra dilimleyicinin nasıl göründüğünü gösterir.

![todo:image_alt_text](formatting-slicer_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
