---
title: نسخ نمط النطاق فقط باستخدام C++
linktitle: نسخ نمط النطاق فقط
type: docs
weight: 620
url: /ar/cpp/copy-range-style-only/
description: تعلم كيفية نسخ نمط النطاق فقط في إكسل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

[نسخ بيانات النطاق فقط](/cells/ar/cpp/copy-range-data-only/) و [نسخ بيانات النطاق مع النمط](/cells/ar/cpp/copy-range-data-with-style/) شرح كيفية نسخ البيانات من نطاق إلى آخر بمفرده أو مع التنسيق الكامل. كما يمكن نسخ التنسيق فقط. يوضح هذا المقال الطريقة.

{{% /alert %}} 

هذا المثال ينشئ دفتر عمل، يملأه بالبيانات وينسخ نمط النطاق فقط.

1. إنشاء نطاق.
1. إنشاء [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object باستخدام سمات التنسيق المحددة.
1. تطبيق تنسيق النمط على النطاق.
1. إنشاء مجموعة ثانية من الخلايا.
1. نسخ تنسيق المجموعة الأولى إلى المجموعة الثانية.

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
