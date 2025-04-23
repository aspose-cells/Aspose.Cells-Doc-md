---
title: C++ ile Dilimleyici Kaldırma
linktitle: Dilimleyici Kaldırma
type: docs
weight: 30
url: /tr/cpp/removing-slicer/
description: Programlı olarak Excel dosyalarındaki dilimleyicileri nasıl kaldıracağınızı öğrenin (Aspose.Cells for C++).
---

## **Olası Kullanım Senaryoları**

Microsoft Excel'de bir dilimleyiciyi kaldırmak istiyorsanız, sadece seçin ve *Sil* düğmesine basın. Benzer şekilde, Aspose.Cells API'sini kullanarak programlama ile kaldırmak istiyorsanız, lütfen [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/) yöntemini kullanın. Bu, dilimleyiciyi çalışma sayfasından kaldıracaktır.

## **Süzgeci Kaldırma**

Aşağıdaki örnek kod, mevcut bir süzgeç içeren [örnek Excel dosyasını](67338478.xlsx) yükler. Süzgeçlere erişir ve ardından kaldırır. Son olarak, çalışma kitabını [çıktı Excel dosyası](67338477.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun yürütülmesinden sonra kaldırılacak süzgeci gösterir.

![todo:image_alt_text](removing-slicer_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
