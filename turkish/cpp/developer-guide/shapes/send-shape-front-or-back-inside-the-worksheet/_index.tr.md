---
title: Çalışma sayfasında Shape Z sırasını değiştirmek ve işlevselliğini öğrenmek için C++ ile Shape Ön veya Arka sıraya gönderin
linktitle: Çalışma sayfası içindeki Şekil Önüne veya Arkasına Gönderme
type: docs
weight: 3400
url: /tr/cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aspose.Cells for C++ kullanarak, çalışma sayfasındaki şekillerin z sırasını nasıl değiştireceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Aynı konumda birden fazla şekil varsa, görünürlükleri z-sıra konumlarına göre belirlenir. Aspose.Cells, şeklin z-sıra konumunu değiştiren [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/) yöntemini sağlar. Bir şekli arka plana göndermek istiyorsanız, -1, -2, -3 gibi negatif bir sayı kullanırsınız. Bir şekli en öne almak istiyorsanız, 1, 2, 3 gibi pozitif sayılar kullanırsınız.

## **Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme**

Aşağıdaki örnek kod, [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/) yönteminin kullanımını göstermektedir. Lütfen kodda kullanılan [örnek Excel dosyasını](50528330.xlsx) ve onun tarafından oluşturulan [çıkış Excel dosyasını](50528331.xlsx) inceleyin. Ekran görüntüsü, kodun çalıştırılmasıyla örnek Excel dosyasındaki etkisini göstermektedir.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
