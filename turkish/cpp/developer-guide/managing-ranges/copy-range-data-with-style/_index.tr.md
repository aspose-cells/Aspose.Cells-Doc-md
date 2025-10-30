---
title: Stil ile Aralık Verisini Kopyala (C++)
linktitle: Stil ile Aralık Verileri Kopyalama
type: docs
weight: 610
url: /tr/cpp/copy-range-data-with-style/
description: Excel dosyalarında hücre stilleri de dahil olmak üzere aralık verisini kopyalayın, Aspose.Cells for C++ ile.
---

{{% alert color="primary" %}}

[Sadece Kopyala Aralığı Verisi](/cells/tr/cpp/copy-range-data-only/) nasıl hücre verilerini aralıklar arasında kopyalayacağınızı açıkladı. Bu makale, Aspose.Cells for C++ kullanarak biçimlendirme stillerini koruyarak hücre aralıklarını nasıl kopyalayacağınızı gösterir.

{{% /alert %}}

Aspose.Cells, [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) ve [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) dahil olmak üzere aralıklarla çalışma için sınıf ve metodlar sağlar.

Bu örnek şu işlemleri gösterir:

1. Bir çalışma kitabı oluştur
1. Hücreleri veri ile doldurun
1. Bir [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) oluşturun
1. Bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi oluşturun ve yapılandırın
1. Aralığa stiller uygulayın
1. İkinci bir aralık oluşturun
1. Biçimlendirilmiş verileri aralıklar arasında kopyalayın

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    for (int i = 0; i < 50; ++i)
    {
        for (int j = 0; j < 10; ++j)
        {
            cells.Get(i, j).PutValue((std::to_wstring(i) + L"," + std::to_wstring(j)).c_str());
        }
    }

    Range range = cells.CreateRange(u"A1", u"D3");
    Style style = workbook.CreateStyle();

    style.GetFont().SetName(u"Calibri");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Blue());

    StyleFlag flag1;
    flag1.SetFontName(true);
    flag1.SetCellShading(true);
    flag1.SetBorders(true);

    range.ApplyStyle(style, flag1);

    Range range2 = cells.CreateRange(u"C10", u"F12");
    range2.Copy(range);

    U16String outputPath = outDir + u"CopyRange.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Range copied with formatting successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
