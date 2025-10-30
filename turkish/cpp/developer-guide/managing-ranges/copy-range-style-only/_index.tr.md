---
title: Yalnızca Aralık Stili Kopyala (C++)
linktitle: Sadece Aralık Stilini Kopyala
type: docs
weight: 620
url: /tr/cpp/copy-range-style-only/
description: Aspose.Cells kullanarak Excel’de sadece bir aralık stilini nasıl kopyalayacağınızı öğrenin.
---

{{% alert color="primary" %}}

[Yalnızca Aralık Verisini Kopyala](/cells/tr/cpp/copy-range-data-only/) ve [Stil ile Aralık Verisini Kopyala](/cells/tr/cpp/copy-range-data-with-style/) başlıklı makaleler, bir aralıktan veri kopyalama işlemini, kendi başına veya biçimlendirme ile birlikte gösterir. Ayrıca sadece biçimlendirmeyi de kopyalamak mümkündür. İşte detaylar.

{{% /alert %}} 

Bu örnek bir çalışma kitabı oluşturur, veri ile doldurur ve yalnızca bir aralığın stilini kopyalar.

1. Bir aralık oluştur.
1. Belirtilen biçimlendirme özniteliklerine sahip bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi oluşturur.
1. Stil biçimlendirmesini aralığa uygular.
1. Hücrelerin ikinci bir aralığını oluşturur.
1. İlk aralığın biçimlendirmesini ikinci aralığa kopyalar.

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    for (int i = 0; i < 50; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            std::wstring value = std::to_wstring(i) + L"," + std::to_wstring(j);
            cells.Get(i, j).PutValue(U16String(reinterpret_cast<const char16_t*>(value.c_str())));
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

    Range range2 = cells.CreateRange(u"C10", u"E13");
    range2.CopyStyle(range);

    U16String outputPath = outDir + u"copyrangestyle.out.xls";
    workbook.Save(outputPath);

    std::cout << "Range style copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
