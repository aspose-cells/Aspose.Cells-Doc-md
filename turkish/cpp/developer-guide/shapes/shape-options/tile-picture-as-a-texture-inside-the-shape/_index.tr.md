---
title: C++ ile Şekil İçinde Doku Olarak Seramik Resmi
linktitle: Resmin Bir Desen Olarak Şeklin İçine Yerleştirilmesi
type: docs
weight: 1700
url: /tr/cpp/tile-picture-as-a-texture-inside-the-shape/
description: Aspose.Cells for C++ kullanarak resmi bir şekil içinde doku olarak karolama yöntemini öğrenin.
---

## **Olası Kullanım Senaryoları**

Resim küçükse ve kalitesini kaybetmeden şeklin tüm yüzeyini kaplamıyorsa, koyulma seçeneğiniz vardır. Koyulma, küçük bir resmi tekrarlayarak şekil yüzeyini doldurur.

## **Resmin Bir Desen Olarak Şeklin İçine Yerleştirilmesi**

Şekil yüzeyini bir resimle doldurup, [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) özelliğini kullanarak karo haline getirebilir ve bu değeri **true** olarak ayarlayabilirsiniz. Lütfen aşağıdaki örnek kodu, [örnek Excel dosyasını](46465050.xlsx) ve referans için ekran görüntüsünü inceleyin.

## **Ekran Görüntüsü**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Örnek Kod**

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

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
