---
title: Shape ın Glow Effect renk bilgisini C++ ile oku
linktitle: Şeklin Parlama Etkisinin Rengini Oku
type: docs
weight: 330
url: /tr/cpp/read-color-of-shape-s-glow-effect/
description: Herhangi bir şeklin glow efektinin rengini Aspose.Cells for C++ kullanarak nasıl okunacağını öğrenin.
---

## Olası Kullanım Senaryoları

Herhangi bir şeklin parlama efektinin rengini okumak istiyorsanız, lütfen [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) özelliğini kullanın. Bu, şeklin parlama efektinin rengi ile ilgili çeşitli özellikleri bulmanıza yardımcı olacaktır.

## Şeklin Parlama Efektinin Rengini Oku

Lütfen aşağıdaki örnek kodu ve [kaynak excel dosyasını](22774108.xlsx) ve başvurunuz için konsol çıktısını görün. Aşağıdaki ekran görüntüsü, Microsoft Excel'de görüldüğünde kaynak excel dosyasının parlama efektini gösterir.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## C++ ile şekillerin glow efekti rengini okuma kodu

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sourceGlowEffectColor.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);
    Shape shape = sheet.GetShapes().Get(0);
    GlowEffect effect = shape.GetGlow();
    CellsColor color = effect.GetColor();

    Color clr = color.GetColor();
    uint32_t argb = (static_cast<uint32_t>(clr.a) << 24) | 
                    (static_cast<uint32_t>(clr.r) << 16) | 
                    (static_cast<uint32_t>(clr.g) << 8) | 
                    static_cast<uint32_t>(clr.b);

    std::cout << "Color: " << argb << std::endl;
    std::cout << "ColorIndex: " << color.GetColorIndex() << std::endl;
    std::cout << "IsShapeColor: " << color.IsShapeColor() << std::endl;
    std::cout << "Transparency: " << color.GetTransparency() << std::endl;
    std::cout << "Type: " << static_cast<int>(color.GetType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Konsol Çıkışı

Yukarıdaki örnek kodun, sağlanan [kaynak excel dosyası](22774108.xlsx) ile birlikte çalıştırıldığında konsol çıktısı. İşte yukarıdaki örnek kodun konsol çıktısı.

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
