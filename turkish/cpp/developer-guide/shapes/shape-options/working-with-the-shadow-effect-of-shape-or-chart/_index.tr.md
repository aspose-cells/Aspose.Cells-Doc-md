---
title: C++ ile Şekil veya Grafiklerin Gölge Etkisiyle Çalışma
linktitle: Şekil veya Grafik Gölgelendirme Efekti Çalışmak
type: docs
weight: 220
url: /tr/cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Aspose.Cells for C++ kullanarak şekil veya grafiklerin gölge etkisini manipüle etmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) metodu ile [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) sınıfını sağlar ve şekil veya grafiklerin gölge etkisiyle çalışma sağlar. [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) sınıfı, uygulama ihtiyaçlarına göre farklı sonuçlar elde etmek için ayarlanabilecek aşağıdaki özellikleri içerir.

- [Açı Al()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getangle/)
- [Bulanıklaştır()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getblur/)
- [Renk Al()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getcolor/)
- [Uzaklık Al()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getdistance/)
- [Önayar Türü Al()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)
- [Boyut Al()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getsize/)
- [Saydamlık Al()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/gettransparency/)

## **Şekil veya Grafik Gölgelenme Efekti ile Çalışma**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115425.xlsx) yükler ve ilk sayfadaki ilk şekli erişir ve [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) özelliğinin alt özelliklerini ayarlar ve ardından çalışma kitabını [çıkış excel dosyasına](5115411.xlsx) kaydeder.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the shadow effect of the shape, Set its Angle, Blur, Distance and Transparency properties
    ShadowEffect se = sh.GetShadowEffect();
    se.SetAngle(150);
    se.SetBlur(4);
    se.SetDistance(45);
    se.SetTransparency(0.3);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Shadow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
