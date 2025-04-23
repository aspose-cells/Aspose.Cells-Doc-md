---
title: نسخ بيانات النطاق مع الأنماط في C++
linktitle: نسخ بيانات النطاق مع النمط
type: docs
weight: 610
url: /ar/cpp/copy-range-data-with-style/
description: نسخ بيانات النطاق بما في ذلك أنماط الخلايا في ملفات إكسل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[نسخ بيانات النطاق فقط](/cells/ar/cpp/copy-range-data-only/) شرح كيفية نسخ بيانات الخلايا بين النطاقات. يوضح هذا المقال كيفية نسخ نطاقات الخلايا مع الحفاظ على أنماط التنسيق الخاصة بها باستخدام Aspose.Cells for C++.

{{% /alert %}}

يوفر Aspose.Cells فصول وأساليب للعمل مع النطاقات بما في ذلك [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)، [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)، و [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

يوضح هذا المثال كيفية:

1. إنشاء مصنف
1. تعبئة الخلايا بالبيانات
1. إنشاء [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)
1. إنشاء وتكوين كائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)
1. تطبيق الأنماط على النطاق
1. إنشاء نطاق ثانٍ
1. نسخ البيانات المنسقة بين النطاقات

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
