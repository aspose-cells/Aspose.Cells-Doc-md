---
title: C++ ile Şekil veya Grafik Parıltı Etkisiyle Çalışma
linktitle: Şekil veya Grafik Gölgelendirme Efekti Çalışmak
type: docs
weight: 240
url: /tr/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Aspose.Cells for C++ kullanarak şekil veya grafiklerin parıltı etkisiyle çalışma yöntemini öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, şekil veya grafiklerin parıltı etkisiyle çalışmak için [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) özelliği ile [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) sınıfını sağlar. [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) sınıfı, uygulama ihtiyaçlarına göre farklı sonuçlar elde etmek için ayarlanabilecek aşağıdaki özellikleri içerir.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **Şekil veya Grafik Gölgelendirme Efekti Çalışmak**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115407.xlsx) yükler ve ilk sayfadaki ilk şekli erişir ve [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) özelliğinin alt özelliklerini ayarlar ve ardından çalışma kitabını [çıkış excel dosyasına](5115414.xlsx) kaydeder.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the glow effect of the shape, Set its Size and Transparency properties
    GlowEffect ge = sh.GetGlow();
    ge.SetSize(30);
    ge.SetTransparency(0.4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Glow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
