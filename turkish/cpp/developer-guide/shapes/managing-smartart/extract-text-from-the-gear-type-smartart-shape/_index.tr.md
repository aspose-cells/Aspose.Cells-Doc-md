---
title: C++ kullanarak Gear Türü SmartArt Şekli’nden Metin çıkarın
linktitle: Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama
type: docs
weight: 500
url: /tr/cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aspose.Cells for C++ kullanarak Excel de Gear Türü SmartArt şekillerinden metin çıkarmayı adım adım ve kod örnekleriyle öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for C++, Gear Türü SmartArt Şekli'nden metin çıkarabilir. Bunu başarmak için şu adımları izleyin:
1. SmartArt Şekli’ni [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4) yöntemiyle Grup Şekli’ne dönüştürün.
2. [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a) yöntemi kullanarak Grup Şekli oluşturan tüm bireysel şekilleri alın.
3. Her bireysel şekil üzerinde döngü yapıp metin çıkarın [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a) yöntemiyle.

## **Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama**

Aşağıdaki örnek kod, Gear Türü SmartArt Şekli içeren bir [örnek Excel dosyasını](67338483.xlsx) yükler ve bireysel şekillerinden metin çıkarır. Sonuçlar için aşağıdaki konsol çıktısına bakın.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing gear type smart art shape
    U16String inputFile(u"sampleExtractTextFromGearTypeSmartArtShape.xlsx");
    Workbook wb(inputFile);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
    for (int i = 0; i < shps.GetLength(); i++)
    {
        Shape s = shps[i];
        AutoShapeType shapeType = s.GetType();

        if (shapeType == AutoShapeType::Gear9 || shapeType == AutoShapeType::Gear6)
        {
            std::cout << "Gear Type Shape Text: " << s.GetText().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
