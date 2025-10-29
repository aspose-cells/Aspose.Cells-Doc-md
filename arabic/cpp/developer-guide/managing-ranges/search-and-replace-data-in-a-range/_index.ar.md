---
title: البحث والاستبدال البيانات في نطاق باستخدام C++
linktitle: البحث واستبدال البيانات في نطاق
type: docs
weight: 170
url: /ar/cpp/search-and-replace-data-in-a-range/
description: هذه المقالة تظهر كيفية البحث واستبدال البيانات في نطاق في إكسل باستخدام كود C++.
keywords: البحث والاستبدال البيانات في Excel باستخدام C++، البحث عن البيانات في Excel باستخدام C++، البحث واستبدال البيانات في نطاق باستخدام C++، البحث عن البيانات في نطاق، البحث عن البيانات في نطاق باستخدام C++، البحث عن البيانات داخل نطاق، البحث عن البيانات في Excel، البحث عن البيانات في نطاق، البحث واستبدال البيانات في Excel باستخدام C++، البحث واستبدال البيانات في نطاق باستخدام C++، البحث واستبدال البيانات في النطاق باستخدام C++
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى البحث عن واستبدال بيانات معينة في نطاق، مع تجاهل أي قيم خلايا خارج النطاق المطلوب. يسمح لك Aspose.Cells بتقييد البحث على نطاق معين. يوضح هذا المقال كيف.

{{% /alert %}}

يوفر Aspose.Cells طريقة [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/) لتحديد نطاق عند البحث عن البيانات. يوضح العينة البرمجية أدناه كيفية البحث واستبدال البيانات في نطاق.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"input.xlsx";

    // Create workbook
    Workbook workbook(filePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Specify the range where you want to search
    // Here the range is E9:H15
    CellArea area = CellArea::CreateCellArea(u"E9", u"H15");

    // Specify Find options
    FindOptions opts;
    opts.SetLookInType(LookInType::Values);
    opts.SetLookAtType(LookAtType::EntireContent);
    opts.SetRange(area);

    Cell cell;
    do
    {
        // Search the cell with value search within range
        cell = worksheet.GetCells().Find(u"search", cell, opts);

        // If no such cell found, then break the loop
        if (!cell)
            break;

        // Replace the cell with value replace
        cell.PutValue(u"replace");

    } while (true);

    // Save the workbook
    U16String outputPath = srcDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
