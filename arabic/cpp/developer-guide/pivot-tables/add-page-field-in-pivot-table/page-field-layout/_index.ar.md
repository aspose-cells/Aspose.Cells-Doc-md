---
title: تعديل تخطيط حقل الصفحة في الجدول المحوري
linktitle: تعديل تخطيط حقل الصفحة في الجدول المحوري
description: تعرّف على كيفية التحكم في تخطيط منطقة حقل الصفحة في جدول محوري باستخدام Aspose.Cells for C++، بما في ذلك تعيين ترتيب العرض، وعدد الالتفاف، وترتيب الحقول لحقول الصفحة في أعلى الجدول المحوري.
keywords: Aspose.Cells, C++ library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /ar/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
هذه المقالة هي امتداد لموضوع **إضافة حقل صفحة في الجدول المحوري**. توضح كيفية التحكم في تخطيط منطقة حقل الصفحة — وهي شريط عناصر تحكم التصفية أعلى الجدول المحوري — بما في ذلك ترتيب العرض، وعدد الالتفاف، وإعادة ترتيب الحقول.
{{% /alert %}}
## **مقدمة**
يكشف الجدول المحوري في Microsoft Excel عن **منطقة حقل صفحة** مخصصة تقع أعلى جسم الصفوف/الأعمدة/البيانات في الجدول. تُعرض هذه المنطقة كشريط من عناصر تحكم التصفية المنسدلة (عنصر واحد لكل حقل صفحة)، وهي التي ينقر عليها المستخدمون النهائيون لتقطيع الجدول المحوري وفق معايير مثل السنة أو المنطقة. يُنمذج Aspose.Cells for C++ هذه المنطقة من خلال مجموعة `PivotTable.PageFields` ويعرض ثلاث خصائص تتحكم في كيفية عرض الشريط بصريًا:
- `PivotTable.PageFieldOrder` (قيمة من نوع `Aspose.Cells.PrintOrderType`) تقرر ما إذا كانت حقول الصفحة الإضافية تُوضع *بجانب* الحقول الحالية أم *أسفلها*.
- `PivotTable.PageFieldWrapCount` يحدد عدد حقول الصفحة التي تُوضع في كل صف أو عمود قبل الالتفاف.
- `PivotTable.PageFields.Move(currIndex, destIndex)` يعيد ترتيب حقول الصفحة دون تغيير وضع الترتيب.
تستعرض هذه المقالة ثلاثة أمثلة برمجية توضح كل عملية من هذه العمليات على مجموعة بيانات مشتركة، حتى تتمكن من مقارنة التخطيطات الناتجة جنبًا إلى جنب.
## **بيانات المصدر**
تقوم جميع الأمثلة الثلاثة أدناه بتحميل هذه الصفوف الثمانية من بيانات المبيعات في ورقة عمل باسم `PivotData`. تحتوي البيانات على مرشحين لحقول الصفحة (`Year`، `Region`)، ومرشح واحد لحقل الصف (`Fruit`)، ومقياس واحد (`Amount`)، مما يجعل شريط حقل الصفحة ذا جدوى في الفحص.
يتم تعبئة جميع الصفوف الثمانية في كل مثال برمجي، بنفس الترتيب، لذا لا تختلف بيانات المصدر أبدًا بين السيناريوهات — فقط خصائص تخطيط حقل الصفحة هي التي تختلف.
## **المثال 1: أفقي ثم رأسي**
في السيناريو الأول نهيئ حقلَي الصفحة (`Year`، `Region`) ليظهروا **جنبًا إلى جنب في صف واحد** في أعلى الجدول المحوري. نخصص `Fruit` لمحور الصف، ونضع `Year` أولًا و`Region` ثانيًا على محور الصفحة (يحدد ترتيب استدعاءات `AddFieldToArea` فهرس البدء)، ونضيف `Amount` (Sum) كحقل بيانات، ثم نضبط `PageFieldOrder` على `PrintOrderType.OverThenDown` مع `PageFieldWrapCount = 2`. مع `OverThenDown` وعدد الالتفاف 2، يتم ترتيب حقلَي الصفحة أفقيًا جنبًا إلى جنب في صف واحد في أعلى الجدول المحوري، بحيث يشغل الشريط صفًا واحدًا بعرض اثنين.
```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // العناوين (الصف 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // الصف 1: تفاح، 2022، الشمال، 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // الصف 2: تفاح، 2023، الشمال، 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // الصف 3: موز، 2022، الجنوب، 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // الصف 4: موز، 2023، الجنوب، 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // الصف 5: كرز، 2022، الشرق، 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // الصف 6: كرز، 2023، الشرق، 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // الصف 7: عنب، 2022، الغرب، 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // الصف 8: عنب، 2023، الغرب، 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // إضافة ورقة تقرير الجدول المحوري
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // إنشاء جدول محوري مصدره PivotData!A1:D9 موضوع في A1 على PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // إضافة الحقول
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // الفاكهة
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // السنة
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // المنطقة
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // المبلغ
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // تكوين تخطيط منطقة حقل الصفحة: ضع حقول الصفحة عبر الأفقي أولاً، والالتفاف بعد كل حقلين
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // التحديث والحساب
    pivotTable.CalculateData();

    // الحفظ
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **المثال 2: رأسي ثم أفقي**
في هذا المثال نضع `Fruit` على محور الصف، و`Year` و`Region` على محور الصفحة (مع `Year` أولًا)، و`Amount` (Sum) كحقل بيانات — تمامًا كما في المثال 1. ثم نضبط `PageFieldOrder` على `PrintOrderType.DownThenOver` و`PageFieldWrapCount` على `2`. مع `DownThenOver` وعدد الالتفاف 2، يتم تكديس حقلَي الصفحة رأسيًا — `Year` في الأعلى و`Region` تحته مباشرة — مكونين عمودًا واحدًا في أعلى الجدول المحوري. وبالتالي يشغل الشريط صفين بعرض واحد، على عكس المثال 1.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **المثال 3: نقل حقل صفحة**
في السيناريو الثالث نحتفظ بمجموعة البيانات وتخصيص الحقول هذا، ونضبط تخطيطًا محايدًا (`OverThenDown` مع عدد الالتفاف `2`)، ثم نوضح عملية `PageFields.Move`. ينقل استدعاء `Move(0, 1)` حقل الصفحة في الفهرس 0 (`Year`) إلى الموضع 1، ويتحول حقل الصفحة الذي كان في الموضع 1 (`Region`) إلى الموضع 0. بعد هذا الاستدعاء، يكون `Region` هو حقل الصفحة الأول و`Year` هو الثاني. لا يتغير وضع الالتفاف والترتيب، لذلك يظل الشريط معروضًا أفقيًا جنبًا إلى جنب — فقط ترتيب القائمتين المنسدلتين هو الذي تم تبديله.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **مقالات ذات صلة**
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/cpp/add-page-field-in-pivot-table/) — الصفحة الأم التي توضح كيفية إضافة حقول الصفحة إلى الجدول المحوري.
- [حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/cpp/row-and-column-fields/) — يغطي تخصيص الحقول لمحوري الصفوف والأعمدة، مما يُكمل العمل على محور الصفحة الموضح هنا.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/cpp/manage-value-fields/) — يصف كيفية تكوين منطقة البيانات (القيم)، بما في ذلك تجميع `Sum` المستخدم في هذه المقالة.
- [تحديث الجدول المحوري](/cells/ar/cpp/refresh-pivot-table/) — يوضح `RefreshData` و`CalculateData`، واللذين يُعدان مطلوبين بعد إعادة ترتيب حقول الصفحة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/cpp/apply-style-to-pivot-table/) — يوضح كيفية تنسيق الجدول المحوري المعروض بعد وضع شريط حقل الصفحة.
{{< app/cells/assistant language="" >}}