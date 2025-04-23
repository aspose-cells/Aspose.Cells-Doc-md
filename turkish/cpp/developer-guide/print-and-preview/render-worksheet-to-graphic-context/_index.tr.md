---
title: Çalışma Sayfasını Grafik Bağlamına Dönüştürme (C++)
linktitle: Grafiksel Ortama Çalışsayısı Renderleme
type: docs
weight: 300
url: /tr/cpp/render-worksheet-to-graphic-context/
description: Aspose.Cells for C++ kullanarak çalışma sayfasını grafik bağlamına nasıl dönüştüreceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells artık bir çalışma sayfasını grafik bağlamına dönüştürebilir. Grafik bağlamı herhangi bir şey olabilir; bir görüntü dosyası, ekran veya yazıcı vb. Lütfen çalışma sayfasını bir grafik bağlamına dönüştürmek için aşağıdaki iki yöntemden birini kullanın.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

Aşağıdaki kod, Aspose.Cells kullanarak bir çalışma sayfasını grafik bağlamına nasıl dönüştüreceğinizi gösterir. Kodu çalıştırdığınızda, tüm çalışma sayfasını yazdıracak ve kalan boş alanı mavi renkle dolduracak, ayrıca resmi **OutputImage_out_.png** dosyası olarak kaydedecektir. Bu kodu denemek için herhangi bir kaynak Excel dosyasını kullanabilirsiniz. Ayrıca kod içindeki yorumları da daha iyi anlamak için okuyunuz.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
