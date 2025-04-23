---
title: Zaman Çizelgesini Render Etme C++ ile
type: docs
weight: 40
url: /tr/cpp/rendering-timeline/
description: Aspose.Cells ile C++ kullanarak Excel dosyalarının zaman çizelgelerini yönetin.
keywords: Ofis 2013, Ofis 2016, Ofis 2019 ve Ofis 365 olmadan zaman çizelgesini dönüştürme
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, ofis 2013, ofis 2016, ofis 2019 ve ofis 365 kullanmadan zaman çizelgesi şeklinin dönüştürülmesini destekler. Çalışma sayfanızı bir görüntüye dönüştürürseniz veya çalışma kitabını PDF veya HTML biçimlerinde kaydederseniz, zaman çizelgelerinin doğru şekilde dönüştürüldüğünü göreceksiniz.

## **Zaman Çizelgesini Dönüştürme**
Aşağıdaki örnek kod, mevcut bir zaman çizelgesi içeren [örnek Excel dosyasını](input.xlsx) yükler. Ardından, zaman çizelgesinin adına göre şekil nesnesini alır ve sonra Shape.ToImage() yöntemi aracılığıyla bir resme dönüştürür. Aşağıdaki resim, dönüştürülen zaman çizelgesini gösteren [çıktı resmi](out.png)'dir. Görebileceğiniz gibi, zaman çizelgesi doğru bir şekilde dönüştürüldü ve örnek Excel dosyasında olduğu gibi görünüyor.

![todo:image_alt_text](out.png)
### **Örnek Kod**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
