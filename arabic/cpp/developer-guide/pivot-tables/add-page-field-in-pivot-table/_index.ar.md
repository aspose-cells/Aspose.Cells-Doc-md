---
title: إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for C++
linktitle: إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for C++
description: تعلّم كيفية إضافة حقول التصفية وتكوينها في الجداول المحورية باستخدام Aspose.Cells for C++، بما في ذلك إضافة حقول التصفية، والتصفية بتحديد عنصر واحد، والتصفية بتحديد متعدد.
keywords: Aspose.Cells, C++, جدول محوري, حقل تصفية, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, تصفية
type: docs
weight: 250
url: /ar/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells دورة الحياة الكاملة لحقول التصفية في الجداول المحورية. يمكنك إضافة حقل تصفية من خلال واجهة API عالية المستوى أو من خلال مجموعة `PageFields` ذات المستوى الأدنى. كما يمكنك التحكم في التصفية في وضع التحديد الفردي، أو مسحها لعرض جميع عناصر التصفية، أو تحويل الحقل إلى وضع التحديد المتعدد ليتمكن المستخدمون من اختيار عدة عناصر تصفية في الوقت نفسه عبر واجهة مربعات الاختيار في Excel.
{{% /alert %}}

## **مقدمة**
حقل التصفية هو حقل محوري يتحكم في *المجموعة الفرعية* من بيانات المصدر التي يعرضها الجدول المحوري. يراه المستخدم النهائي في صورة قائمة منسدلة أعلى الجدول المحوري المعروض في Excel، ويؤدي اختيار أحد عناصر التصفية المتاحة إلى إعادة بناء محتوى الجدول المحوري بحيث تُلخّص فقط السجلات المنتمية إلى عنصر التصفية. يصبح الحقل المحوري حقل تصفية عند تسجيله في الجدول المحوري بوصفه `PivotFieldType.Page` بدلاً من `PivotFieldType.Row` أو `PivotFieldType.Column` أو `PivotFieldType.Data`.

## **إضافة حقل تصفية**

### إضافة حقل تصفية باستخدام AddFieldToArea
ينشئ المثال التالي مجموعة بيانات صغيرة من Fruit / Year / Amount، ويضع جدولاً محوريًا عند الخلية E3 مع `Fruit` في منطقة الصفوف، و`Amount` في منطقة البيانات، و`Year` في منطقة التصفية، ثم يحدّث الجدول المحوري ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // إنشاء مصنف جديد
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    Cells cells = worksheet.GetCells();
    // إعداد صف العناوين
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    // تعبئة 9 صفوف من بيانات العينة: الفاكهة، السنة، المبلغ
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };
    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // إضافة جدول محوري مرتبط بالخلية E3
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // إضافة الحقول إلى مناطقها: الفاكهة كصف، المبلغ كبيانات، السنة كحقل صفحة
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    // تحديث بيانات الجدول المحوري وحسابها
    pivotTable.CalculateData();
    // حفظ المصنف
    workbook.Save(u"pageFieldSample.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### إضافة حقل تصفية باستخدام PageFields.Add
عند العمل مع مثيل `PivotField` بالفعل، يمكنك تمريره مباشرةً إلى `PivotTable.PageFields.Add`. يُنشأ الجدول المحوري وحقل التصفية تمامًا كما في السيناريو السابق؛ ويكمن الاختلاف الوحيد في أن تسجيل الحقل في منطقة التصفية يُستبدل باستدعاء API ذي المستوى الأدنى.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // الرؤوس
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    // بيانات نموذجية (9 صفوف)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);
    // إضافة جدول محوري عند E3 يغطي A1:C10
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"A1:C10"), U16String(u"E3"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    // الفاكهة -> الصفوف، المبلغ -> البيانات
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    // نهج منخفض المستوى: العثور على حقل PivotField الموجود باسم Year في BaseFields
    // وتسجيله في منطقة Page عبر PageFields.Add(PivotField).
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }
    // تحديث البيانات بحيث ينعكس حقل الصفحة الجديد في مصنف العمل المحفوظ
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **التصفية بتحديد عنصر واحد (عرض عنصر تصفية واحد)**
في وضع التحديد الفردي الافتراضي، يُعرض حقل التصفية كقائمة منسدلة واحدة، ويحدد العدد الصحيح `PivotField.CurrentPageItem` عنصر التصفية الذي يحدد النتائج المعروضة في الجدول المحوري. ويؤدي إسناد فهرس محدد إلى اختيار ذلك العنصر وحده، بينما يؤدي إسناد القيمة الخاصة `0x7FFD` (32765 بالأساس العشري) إلى مسح التصفية بحيث تُلخّص جميع عناصر التصفية معًا. وضع التحديد الفردي هو الوضع الافتراضي، ولا يلزم تفعيله صراحةً.

### عرض جميع العناصر
ضبط `CurrentPageItem` على القيمة السحرية `0x7FFD` يماثل مسح التصفية: يلخّص الجدول المحوري جميع عناصر التصفية، كأن لم تُطبَّق أي تصفية.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};
    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    pivotTable.CalculateData();
    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### عرض عنصر محدد واحد
يؤدي ضبط `CurrentPageItem` على فهرس صالح إلى اختيار عنصر تصفية واحد فقط. يمثل الفهرس موضع العنصر في قائمة عناصر حقل التصفية مرتبة، لذا يختار `1`، على سبيل المثال، العنصر الثاني بعد الترتيب.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));
    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));
    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));
    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));
    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **التصفية بتحديد متعدد**
تحوّل التصفية بتحديد متعدد قائمة التصفية المنسدلة إلى قائمة تحتوي على مربعات اختيار، وتتيح للمستخدم النهائي اختيار عدة عناصر تصفية في الوقت نفسه. يعرض Aspose.Cells خاصيتين تعملان معًا. يجب ضبط `PivotField.IsMultipleItemSelectionAllowed` على `true` قبل أن تصبح واجهة التحديد المتعدد فعالة. وبعد تمكينها، تتحكم `PivotItem.IsHidden` في العناصر التي تظهر في قائمة مربعات الاختيار، بحيث يمكنك إظهار جميع العناصر أو تقييد العناصر المعروضة إلى عناصر محددة.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // بيانات العينة: الفاكهة | السنة | الكمية
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");
    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };
    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }
    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    // — تمكين التحديد المتعدد في حقل الصفحة
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);
    // الجزء A — تحديد جميع العناصر (جعل كل عنصر مرئيًا)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }
    // الجزء B — تحديد عناصر محددة فقط حسب قيمة المصدر
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

> **ملاحظة:** عند استخدام التصفية بتحديد متعدد عبر `PivotItem.IsHidden`، **يجب أن يظل عنصر `PivotItem` واحد على الأقل ظاهرًا** (`IsHidden == false`). وإذا كانت جميع العناصر مخفية، فإن Excel إما يتعطل عند فتح الملف أو يعرض جدولاً محوريًا فارغًا. تحقق دائمًا من أن قائمة العناصر المسموح بها في وضع التحديد المتعدد تتضمن عنصرًا واحدًا على الأقل من بيانات المصدر.

## **أي API وأي وضع ينبغي استخدامهما؟**
يوضح الجدول التالي متى يُستخدم كل API ولكل وضع، لمساعدتك على اختيار التركيبة المناسبة دون الحاجة إلى قراءة تفاصيل كل سيناريو.
| السيناريو / حالة الاستخدام | API الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل تصفية باسم عمود المصدر (الأكثر شيوعًا) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | غير منطبق | API عالية المستوى في سطر واحد. استخدمها ما لم تكن بحاجة إلى مرجع `PivotField`. |
| إضافة حقل تصفية عندما يكون لديك كائن `PivotField` بالفعل | `PivotTable.PageFields.Add(PivotField)` | غير منطبق | استخدم هذه الطريقة عندما يكون كائن الحقل قدobtained من موضع آخر أو يحتاج إلى إعادة استخدامه. |
| التصفية إلى عنصر تصفية واحد (الوضع الافتراضي) | `PivotField.CurrentPageItem` | تُضبط على فهرس محدد | يعرض `1` العنصر الثاني في القائمة المرتبة. |
| عرض جميع العناصر / مسح التصفية | `PivotField.CurrentPageItem` | تُضبط على `0x7FFD` | القيمة السحرية `0x7FFD` (32765 بالأساس العشري) هي القيمة الخاصة التي تشير إلى «جميع العناصر». |
| تمكين واجهة المستخدم متعددة التحديد في Excel | `PivotField.IsMultipleItemSelectionAllowed` | تُضبط على `true` | مطلوب قبل أن تصبح استدعاءات `IsHidden` فعالة. |
| إخفاء / إظهار عناصر فردية في قائمة متعددة التحديد | `PivotItem.IsHidden` | تُضبط لكل عنصر | يجب أن يظل عنصر واحد على الأقل ظاهرًا (`IsHidden == false`). |

{{% alert color="primary" %}}
تذكّر دائمًا قاعدة إبقاء عنصر واحد على الأقل ظاهرًا عند تكوين التصفية بتحديد متعدد. إذا كانت جميع عناصر `PivotItem` في حقل تصفية متعدد التحديد مخفية، فإن Excel إما يتعطل عند فتح الملف أو يعرض جدولاً محوريًا فارغًا. أنشئ قائمة العناصر المسموح بها استنادًا إلى بيانات المصدر بحيث يظل عنصر واحد على الأقل ظاهرًا، مع ضمان فتح المصنفات المحفوظة دون مشكلات على جميع الأجهزة.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}