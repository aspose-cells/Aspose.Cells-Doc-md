---
title: إضافة تدرجات لون ذاتية وتدرجات لون ثلاثية باستخدام C++
linktitle: إضافة التدرج اللوني ثنائي اللون والثلاثي اللون وتنسيقهما الشرطي
description: كيفية استخدام مكتبة Aspose.Cells في C++ لإضافة التنسيق الشرطي لنسب الألوان الثنائية والثلاثية. من خلال ضبط هذه المعايير، لديك مزيد من السيطرة على مظهر وتنسيق الخلايا.
keywords: Aspose.Cells، التنسيق الشرطي، C++، نسبة الألوان، مقياس لونه ثنائي، مقياس لونه ثلاثي
type: docs
weight: 20
url: /ar/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

**إضافة الدالة المشروطة بمقياسي لون** و**مقياس اللون الثلاثي** تمت إضافتهم بنفس الطريقة باستثناء اختلافهم في خاصية [**FormatCondition.GetIs3ColorScale()**](https://reference.aspose.com/cells/cpp/aspose.cells/colorscale/getis3colorscale/). يكون هذه الخاصية **false** لـ مقياس اللون المزدوج و **true** لـ مقياس اللون الثلاثي للدوال المشروطة.

{{% /alert %}}

يقوم الكود العيني التالي بإضافة الدوال المشروطة بمقياسي اللون والدالة المشروطة بمقياس اللون الثلاثي. يولد [ملف الإكسيل الناتج](5115058.xlsx).

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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add some data in cells
    worksheet.GetCells().Get(u"A1").PutValue(u"2-Color Scale");
    worksheet.GetCells().Get(u"D1").PutValue(u"3-Color Scale");

    for (int i = 2; i <= 15; i++)
    {
        int row = i - 1;
        worksheet.GetCells().Get(row, 0).PutValue(i); // Column A (0)
        worksheet.GetCells().Get(row, 3).PutValue(i); // Column D (3)
    }

    // Adding 2-Color Scale Conditional Formatting
    CellArea ca = CellArea::CreateCellArea(u"A2", u"A15");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::ColorScale);
    fcc.AddArea(ca);

    FormatCondition fc = worksheet.GetConditionalFormattings().Get(idx).Get(0);
    fc.GetColorScale().SetIs3ColorScale(false);
    fc.GetColorScale().SetMaxColor(Color::LightBlue());
    fc.GetColorScale().SetMinColor(Color::LightGreen());

    // Adding 3-Color Scale Conditional Formatting
    ca = CellArea::CreateCellArea(u"D2", u"D15");

    idx = worksheet.GetConditionalFormattings().Add();
    fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::ColorScale);
    fcc.AddArea(ca);

    fc = worksheet.GetConditionalFormattings().Get(idx).Get(0);
    fc.GetColorScale().SetIs3ColorScale(true);
    fc.GetColorScale().SetMaxColor(Color::LightBlue());
    fc.GetColorScale().SetMidColor(Color::Yellow());
    fc.GetColorScale().SetMinColor(Color::LightGreen());

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
