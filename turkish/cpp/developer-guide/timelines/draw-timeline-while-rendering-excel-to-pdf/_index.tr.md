---
title: C++ ile Excel i PDF ye aktarırken Zaman Çizelgesi Çizin
linktitle: Excel i PDF ye dönüştürürken Zaman Çizelgesi çizin
type: docs
weight: 60
url: /tr/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Aspose.Cells ile C++ kullanarak Excel dosyalarının zaman çizelgelerini yönetin.
keywords: Ofis 2013, Ofis 2016, Ofis 2019 ve Ofis 365 olmadan zaman çizelgesini PDF ye dönüştürme
---

## **Excel'i PDF'ye dönüştürürken Zaman Çizelgesi çizin**
Excel dosyasına zaman çizelgesi uygulanmış ve bu ayarlarla PDF olarak dışa aktarmak istediğiniz bir dosyanız varsa, Aspose.Cells bunun desteklenmesini varsayılan hale getirir. Sadece zaman çizelgesi içeren Excel dosyasını PDF olarak dışa aktarın ve oluşturulan PDF'de zaman çizelgesinin gösterildiğini göreceksiniz.

Aşağıdaki örnek kod, var olan bir zaman çizelgesi içeren [örnek Excel dosyasını](input.xlsx) yükler. Ardından, çalışma kitabını [çıktı PDF dosyası](out.pdf) olarak kaydeder. Aşağıdaki ekran görüntüsü, kaynak Excel dosyasını ve oluşturulan PDF dosyasını karşılaştırır.

<img src="out.png" width="60%">

## **Örnek Kod**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

