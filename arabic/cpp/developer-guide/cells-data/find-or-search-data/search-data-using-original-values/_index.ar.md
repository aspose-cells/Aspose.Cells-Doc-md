---
title: البحث عن البيانات باستخدام القيم الأصلية باستخدام C++
linktitle: البحث عن البيانات باستخدام القيم الأصلية
type: docs
weight: 380
url: /ar/cpp/search-data-using-original-values/
description: تعلم كيفية البحث عن البيانات باستخدام القيم الأصلية عبر واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: البحث عن البيانات باستخدام القيم الأصلية, العثور على البيانات باستخدام القيم الأصلية, البحث عن البيانات حسب القيم الأصلية, العثور على البيانات حسب القيم الأصلية
---

{{% alert color="primary" %}}

أحيانًا يكون قيمة البيانات مخفية لأنها مهيأة بطريقة ما. على سبيل المثال، لنفترض أن الخلية D4 لديها صيغة =Sum(A1:A2) وقيمتها 20 ولكنها مهيأة كما ---، عندها تكون القيمة 20 مخفية ولا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel. ومع ذلك، يمكنك العثور عليها باستخدام Aspose.Cells باستخدام [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/).

{{% /alert %}}

الشيفرة العينية التالية توضح النقطة السابقة. إنها تجد الخلية D4 التي لا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel ولكن يمكن لـ Aspose.Cells العثور عليها باستخدام [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/). يرجى قراءة التعليقات داخل الشيفرة لمزيد من المعلومات.

## كود C++ للبحث عن البيانات باستخدام القيم الأصلية

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

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add 10 in cell A1 and A2
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(10);

    // Add Sum formula in cell D4 but customize it as ---
    Cell cell = worksheet.GetCells().Get(u"D4");

    Style style = cell.GetStyle();
    style.SetCustom(u"---", true);
    cell.SetStyle(style);

    // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
    cell.SetFormula(u"=Sum(A1:A2)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
    FindOptions options;
    options.SetLookInType(LookInType::OriginalValues);
    options.SetLookAtType(LookAtType::EntireContent);

    Cell foundCell;
    int32_t obj = 20;

    // Find 20 which is Sum(A1:A2) and formatted as ---
    foundCell = worksheet.GetCells().Find(obj, foundCell, options);

    // Print the found cell
    std::cout << foundCell.ToString().ToUtf8() << std::endl;

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## الناتج على واجهة الأوامر الناتجة عن الكود المثال

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
