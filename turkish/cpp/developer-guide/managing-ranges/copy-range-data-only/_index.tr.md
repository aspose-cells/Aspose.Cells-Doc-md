---
title: Yalnızca Aralık Verisini Kopyala (C++)
linktitle: Yalnızca Aralık Verilerini Kopyala
type: docs
weight: 600
url: /tr/cpp/copy-range-data-only/
description: Aspose.Cells kullanarak biçimlendirme olmadan yalnızca aralık verisini nasıl kopyalayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazen, verileri bir hücre aralığından başka bir hücre aralığına kopyalamak isteyebilirsiniz, sadece verileri ve biçimlendirmeyi kopyalayarak. Aspose.Cells bu özelliği sunar.

Bu makale, Aspose.Cells'i veri aralığını kopyalamak için kullanan bir örnek kod sunmaktadır.

{{% /alert %}}

Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Bir [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) oluşturma.
1. Belirtilen biçimlendirme özniteliklerine sahip bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi oluşturur.
1. Stil biçimlendirmesini aralığa uygular.
1. Başka bir hücre aralığı oluşturun.
1. İlk aralığın verilerini bu ikinci aralığa kopyalayın.

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

    Range range2 = cells.CreateRange(u"C10", u"F12");
    range2.CopyData(range);

    U16String outputPath = outDir + u"CopyRangeData.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Range data copied and styled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
