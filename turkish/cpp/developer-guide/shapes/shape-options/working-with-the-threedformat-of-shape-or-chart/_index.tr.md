---
title: C++ ile Shape veya Grafik’nin Üç Boyut Formatı ile Çalışma
linktitle: Şekil veya Grafik ThreeDFormat ile Çalışma
type: docs
weight: 250
url: /tr/cpp/working-with-the-threedformat-of-shape-or-chart/
description: Aspose.Cells kullanarak şekil veya grafiklerin 3D Formatını manipüle etmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) özelliği ile [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) sınıfını sağlar. [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) sınıfı, uygulama ihtiyaçlarına göre farklı sonuçlar almak için farklı özellikler içerir.

## **Şekil veya Grafik ThreeDFormat ile Çalışma**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115419.xlsx) yükler ve ilk sayfadaki ilk şekli erişir. Ardından, [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) özelliğinin alt özelliklerini ayarlar ve çalışma kitabını [çıkış excel dosyasına](5115410.xlsx) kaydeder.

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

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
