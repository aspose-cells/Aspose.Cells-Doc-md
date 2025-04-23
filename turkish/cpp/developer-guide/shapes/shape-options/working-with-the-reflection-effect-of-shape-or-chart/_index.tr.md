---
title: C++ ile Şekil veya Grafiklerin Yansıma Etkisiyle Çalışma
linktitle: Şekil veya Grafik Yansıma Efekti Çalışmak
type: docs
weight: 210
url: /tr/cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Aspose.Cells kullanarak şekil veya grafiklerin yansıma etkisiyle çalışma yöntemini öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, şekil veya grafiklerin yansıma etkisiyle çalışmak için [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) özelliği ile [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) sınıfını sağlar. [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) sınıfı, uygulama ihtiyaçlarına göre farklı sonuçlar elde etmek için ayarlanabilecek aşağıdaki özellikleri içerir.

- [Bulanık](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getblur/)
- [Yön](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdirection/)
- [Mesafe](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdistance/)
- [Solma Yönü](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getfadedirection/)
- [Şekil ile Döndür](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getrotwithshape/)
- [Boyut](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getsize/)
- [Şeffaflık](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettransparency/)
- [Tür](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettype/)

## **Şekil veya Grafik Yansıma Efekti Çalışmak**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115424.xlsx) yükler ve varsayılan sayfadaki ilk şekli erişir ve [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) sınıfının farklı özelliklerini ayarlar ve ardından çalışma kitabını [çıkış excel dosyasına](5115423.xlsx) kaydeder.

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

    // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
    ReflectionEffect re = sh.GetReflection();
    re.SetBlur(30);
    re.SetSize(90);
    re.SetTransparency(0);
    re.SetDistance(80);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Reflection effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
