---
title: C++ ile Dilimleyici Çizimi
type: docs
weight: 40
url: /tr/cpp/rendering-slicer/
description: Aspose.Cells ile C++ kullanarak Excel dosyalarında dilimleyicileri çizin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells süzgeç şeklini görüntülemeyi destekler. Çalışma sayfanızı bir resme dönüştürür veya çalışma kitabını PDF veya HTML biçimlerinde kaydeder, süzgeçlerin düzgün bir şekilde görüntülendiğini göreceksiniz.
## **Dilimleyiciyi Oluşturma**
Aşağıdaki örnek kod, mevcut bir dilimleyici içeren [örnek Excel dosyasını](67338479.xlsx) yükler. Çalışma sayfasını, sadece dilimleyiciyi kapsayan yazdırma alanını ayarlayarak bir görüntüye dönüştürür. Aşağıdaki görüntü, render edilen dilimleyiciyi gösteren [çıktı görüntüsü](67338480.png). Görüldüğü gibi, dilimleyici düzgün görüntülenmiş ve örnek Excel dosyasındaki gibi görünmektedir.

![todo:image_alt_text](rendering-slicer_1)
## **Örnek Kod**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
