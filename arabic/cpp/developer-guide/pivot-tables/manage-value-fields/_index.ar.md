---
title: حقول القيم في Aspose.Cells for C++
description: تعلّم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيم على محور الصفوف أو الأعمدة في Aspose.Cells for C++.
linktitle: حقول القيم في Aspose.Cells for C++
keywords: Aspose.Cells, C++, جدول محوري, حقل القيم, PivotField, PivotField.Function, حقل البيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تُعدّ إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يعرض Aspose.Cells `PivotTable.AddFieldToArea(PivotFieldType, string)`، وهي صيغة محمّلة تقبل الثابت `PivotFieldType.Data` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، تعرضه واجهة البرمجة من خلال مجموعة `PivotTable.DataFields` بالترتيب الذي أُضيفت به الحقول. افتراضيًا، يتم تلخيص عمود المصدر الرقمي باستخدام `ConsolidationFunction.Sum`، بينما يكون العمود غير الرقمي افتراضيًا `Count`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
 Aspose::Cells::Startup();
 Workbook workbook;
 Worksheet worksheet = workbook.GetWorksheets().Get(0);
 worksheet.SetName(u"Data");
 Cells cells = worksheet.GetCells();
 // العناوين في A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));
 // صفوف البيانات A2:D9 باستخدام حلقات متداخلة متفرعة على j
 for (int i = 1; i <= 8; i++)
 {
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 cells.Get(i, j).PutValue(U16String(i <= 4 ? "Fruit" : "Vegetable"));
 break;
 case 1:
 if (i == 1 || i == 2) cells.Get(i, j).PutValue(U16String("Apple"));
 else if (i == 3 || i == 4) cells.Get(i, j).PutValue(U16String("Banana"));
 else if (i == 5 || i == 6) cells.Get(i, j).PutValue(U16String("Carrot"));
 else cells.Get(i, j).PutValue(U16String("Daikon"));
 break;
 case 2:
 cells.Get(i, j).PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) cells.Get(i, j).PutValue(100);
 else if (i == 2) cells.Get(i, j).PutValue(150);
 else if (i == 3) cells.Get(i, j).PutValue(80);
 else if (i == 4) cells.Get(i, j).PutValue(90);
 else if (i == 5) cells.Get(i, j).PutValue(50);
 else if (i == 6) cells.Get(i, j).PutValue(60);
 else if (i == 7) cells.Get(i, j).PutValue(40);
 else cells.Get(i, j).PutValue(45);
 break;
 }
 }
 }
 // إضافة جدول محوري في F3 باسم PivotTable1
 PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);
 // تخطيط الجدول المحوري: Category و Item في الصف، Year في العمود، Amount كحقل بيانات
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");
 Aspose::Cells::Cleanup();
 return 0;
}
```

## تغيير دالة التلخيص
يتم تغليف كل حقل موضوع في منطقة البيانات داخليًا كنسخة من `PivotField`، وتُعيد خاصية `Function` الخاصة به قيمة من تعداد `ConsolidationFunction`. يتيح لك مُعيِّن `Function` ذاته التنقل بين التجمّعات المتاحة، بما في ذلك `Sum` و `Count` و `Average` و `Max` و `Min` و `Product` و `StdDev` و `StdDevp` و `Var` و `Varp`.

{{% alert color="primary" %}}
تغيير `Function` يؤثر فقط على التجمّع، ولا يتغير عمود المصدر.
لذا يمكنك ترك حقل بيانات واحد كـ `Sum` بينما تُضيف حقل بيانات ثانٍ يستهدف عمود المصدر نفسه لكنه يستخدم `Count` أو `Average`، وكل ذلك في جدول محوري واحد.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana", u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) {
                worksheet.GetCells().Get(i, j).PutValue(i <= 4 ? u"Fruit" : u"Vegetable");
            } else if (j == 1) {
                worksheet.GetCells().Get(i, j).PutValue(items[i - 1]);
            } else if (j == 2) {
                worksheet.GetCells().Get(i, j).PutValue(years[i - 1]);
            } else {
                worksheet.GetCells().Get(i, j).PutValue(amounts[i - 1]);
            }
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField countField = pivotTable.GetDataFields().Get(1);
    countField.SetFunction(ConsolidationFunction::Count);

    pivotTable.CalculateData();

    wb.Save(u"output_function.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## رسم حقول القيم على محور الصفوف أو الأعمدة
عندما يحتوي الجدول المحوري على حقلين من البيانات أو أكثر، يعرض Aspose.Cells حقلًا افتراضيًا إضافيًا يُسمى `PivotTable.ValuesField`. يمثّل هذا الحقل الافتراضي تجمّع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة كحقل محوري أساسي، وهو أمر مفيد لعرض مقاييس متعددة جنبًا إلى جنب.

{{% alert color="primary" %}}
لا يعمل `PivotTable.ValuesField` إذا لم يكن هناك حقل قيم أو كان هناك حقل قيم واحد فقط.
تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة توضح كل قدرة موصوفة أعلاه على نفس بنية الجدول المحوري.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Category"));
    cells.Get(0, 1).PutValue(U16String("Item"));
    cells.Get(0, 2).PutValue(U16String("Year"));
    cells.Get(0, 3).PutValue(U16String("Amount"));

    std::vector<U16String> categories = {
        U16String("Fruit"), U16String("Fruit"), U16String("Fruit"), U16String("Fruit"),
        U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable")
    };
    std::vector<U16String> items = {
        U16String("Apple"), U16String("Apple"), U16String("Banana"), U16String("Banana"),
        U16String("Carrot"), U16String("Carrot"), U16String("Daikon"), U16String("Daikon")
    };
    int years[8] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[8] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) cells.Get(i, j).PutValue(categories[i - 1]);
            else if (j == 1) cells.Get(i, j).PutValue(items[i - 1]);
            else if (j == 2) cells.Get(i, j).PutValue(years[i - 1]);
            else cells.Get(i, j).PutValue(amounts[i - 1]);
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::Count);

    pivotTable.AddFieldToArea(PivotFieldType::Column, pivotTable.GetValuesField().GetName());

    pivotTable.CalculateData();
    workbook.Save(u"output_plot.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}