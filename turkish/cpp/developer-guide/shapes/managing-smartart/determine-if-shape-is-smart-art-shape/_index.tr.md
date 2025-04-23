---
title: C++ ile Şeklin Smart Art Şekli olup olmadığını belirleyin
linktitle: Şekil Akıllı Sanat Şekli mi Belirle
type: docs
weight: 400
url: /tr/cpp/determine-if-shape-is-smart-art-shape/
description: Aspose.Cells for C++ kullanarak bir şeklin Smart Art Şekli olup olmadığını nasıl belirleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Akıllı Sanat Şekilleri, otomatik olarak karmaşık diyagramlar oluşturmanıza olanak tanıyan Microsoft Excel'de özel şekillerdir. Şeklin akıllı sanat şekli veya normal şekil olup olmadığını [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) özelliğini kullanarak kontrol edebilirsiniz.

## **Şekil Akıllı Sanat Şekli mi Belirle**

Aşağıdaki örnek kod, bu ekran görüntüsünde gösterilen akıllı sanat şeklini içeren [örnek Excel dosyasını](55541792.xlsx) yükler. Ardından ilk şeklin [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) özelliğinin değerini yazdırır. Lütfen aşağıdaki örnek kodun konsol çıktısına bakınız.

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);

    // Access first shape
    ShapeCollection shapes = ws.GetShapes();
    Shape sh = shapes.Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
