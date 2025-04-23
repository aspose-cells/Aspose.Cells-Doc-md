---
title: SmartArt ı Gruplandırılmış Şekil Yapısına C++ ile dönüştürün
linktitle: Akıllı Sanatı Grup Şekline Dönüştür
type: docs
weight: 200
url: /tr/cpp/convert-the-smart-art-to-group-shape/
description: Aspose.Cells for C++ kullanarak Smart Art Şekli nin Grup Şekli’ne nasıl dönüştürüleceğini ve grup şeklinin bireysel parçalarına erişimi öğrenin.
---

## **Olası Kullanım Senaryoları**

Grup Şeklini Kullanarak Akıllı Sanat Şeklini Grup Şekline Dönüştürebilirsiniz. Bu yöntemle akıllı sanat şeklini bir grup şekli gibi işleyebilirsiniz. Sonuç olarak, grup şeklinin bireysel parçalarına veya şekillerine erişebileceksiniz.

## **Akıllı Sanatı Grup Şekline Dönüştür**

Aşağıdaki örnek kod, bu ekran görüntüsünde gösterilen SmartArt şekli içeren [örnek Excel dosyasını](55541793.xlsx) yükler. Daha sonra SmartArt şekli grup şekline dönüştürülür ve Shape::IsGroup özellikleri yazdırılır. Aşağıda verilen örnek kodun çıktılarına bakın.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
