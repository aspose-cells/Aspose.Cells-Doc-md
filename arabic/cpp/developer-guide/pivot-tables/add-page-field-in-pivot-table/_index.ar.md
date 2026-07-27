---
title: إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: إضافة حقول التصفية
description: تعرّف على كيفية إضافة وتكوين حقول التصفية في الجداول المحورية باستخدام Aspose.Cells for C++، بما في ذلك إضافة حقول التصفية، والتصفية بخيار واحد، والتصفية متعددة الخيارات.
keywords: Aspose.Cells, C++, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /ar/cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells دورة الحياة الكاملة لحقول التصفية في الجداول المحورية. يمكنك إضافة حقل صفحة من خلال واجهة برمجة تطبيقات عالية المستوى أو من خلال مجموعة `PageFields` منخفضة المستوى، ويمكنك تشغيل مرشح الصفحة في وضع الخيار الواحد، أو مسحه لإظهار جميع عناصر الصفحة، أو تبديل الحقل إلى التحديد المتعدد حتى يتمكن المستخدمون من اختيار عدة عناصر صفحة دفعة واحدة من خلال واجهة مربعات الاختيار في Excel.
{{% /alert %}}

## **المقدمة**

حقل التصفية هو حقل محوري يتحكم في *أي مجموعة فرعية* من البيانات المصدرية يعرضها جسم الجدول المحوري. يراه المستخدمون النهائيون كقائمة منسدلة في أعلى الجدول المحوري المعروض في Excel، وتحديد أحد عناصر الصفحة المتاحة يعيد بناء جسم الجدول المحوري بحيث يتم تلخيص السجلات التي تنتمي إلى عنصر التصفية هذا فقط. يصبح حقل المحور حقل صفحة عند تسجيله كـ `PivotFieldType.Page` بدلاً من `PivotFieldType.Row` أو `PivotFieldType.Column` أو `PivotFieldType.Data`.

يمكن أن يعمل حقل التصفية بسلوكين. في السلوك الافتراضي **تحديد واحد**، يكون عنصر صفحة واحد فقط مرئيًا في كل مرة، لذلك يلخص جسم الجدول المحوري مجموعة فرعية واحدة بالضبط. في سلوك **التحديد المتعدد**، يعرض الحقل قائمة مربعات اختيار، ويلخص جسم الجدول المحوري اتحاد كل عناصر الصفحة المحددة. يمكن نقل نفس حقل المصدر ذهابًا وإيابًا بين هذه السلوكيات عن طريق تبديل خاصية واحدة.

يوفر Aspose.Cells for C++ طريقتين متكافئتين لتسجيل حقل صفحة. واجهة برمجة التطبيقات عالية المستوى هي `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`، التي تأخذ اسم عمود المصدر وتضيف الحقل في استدعاء واحد. واجهة برمجة التطبيقات منخفضة المستوى هي `PivotTable.PageFields.Add(PivotField)`، التي تُستخدم عندما يكون لديك بالفعل مرجع `PivotField` وترغب في إضافة نفس مثيل الحقل إلى منطقة التصفية. تنتهي كلتا واجهتي البرمجة إلى ملء نفس مجموعة `PageFields`، وتوضح بقية هذه المقالة كيفية الاختيار بينهما وكيفية تشغيل كل وضع تصفية.

## **إضافة حقل صفحة**

توجد طريقتان لتسجيل حقل محور في منطقة التصفية. يأخذ الاستدعاء عالي المستوى اسم عمود المصدر كسلسلة وهو المسار الأكثر شيوعًا. يقبل الاستدعاء منخفض المستوى مثيل `PivotField` موجودًا وهو مناسب عندما يجب إعادة استخدام نفس كائن الحقل عبر مناطق محورية متعددة. يضع كلا الاستدعاءين الحقل في `PivotTable.PageFields`، وبعد ذلك يظهر كقائمة منسدلة للصفحة في أعلى الجدول المحوري المعروض.

### إضافة حقل صفحة باستخدام AddFieldToArea

يبني المثال التالي مجموعة بيانات صغيرة من الفاكهة / السنة / المبلغ، ويضع جدولاً محوريًا في الخلية E3 مع `Fruit` في منطقة الصفوف، و`Amount` في منطقة البيانات، و`Year` في منطقة التصفية، ويُحدّث الجدول المحوري، ويحفظ المصنف.

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

    // إعداد صف الرأس
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // ملء 9 صفوف من البيانات النموذجية: الفاكهة، السنة، المبلغ
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };

    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }

    // إضافة جدول محوري مثبت في الخلية E3
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // إضافة الحقول إلى مناطقها: الفاكهة كصف، المبلغ كبيانات، السنة كحقل صفحة
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // تحديث وحساب بيانات الجدول المحوري
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // حفظ المصنف
    workbook.Save(u"pageFieldSample.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### إضافة حقل صفحة باستخدام PageFields.Add

عندما تعمل بالفعل مع مثيل `PivotField`، يمكنك تمريره مباشرة إلى `PivotTable.PageFields.Add`. يتم إنشاء الجدول المحوري وحقل التصفية تمامًا كما في السيناريو السابق؛ يتم استبدال تسجيل منطقة التصفية النهائي فقط باستدعاء واجهة البرمجة منخفضة المستوى.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // العناوين
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // بيانات عينة (9 صفوف)
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
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // الفاكهة -> الصف، المبلغ -> البيانات
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // نهج منخفض المستوى: حدد موقع حقل المحور "السنة" الموجود في BaseFields
    // وقم بتسجيله في منطقة الصفحة عبر PageFields.Add(PivotField).
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // قم بالتحديث حتى ينعكس حقل الصفحة الجديد في المصنف المحفوظ
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **التصفية بخيار واحد (عرض عنصر صفحة واحد)**

في سلوك التحديد الواحد الافتراضي، يُعرض حقل التصفية كقائمة منسدلة واحدة ويحدد عدد `PivotField.CurrentPageItem` الصحيح عنصر التصفية الذي يدفع جسم الجدول المحوري. تعيين فهرس محدد يختار هذا العنصر فقط؛ تعيين الحارس الخاص `0x7FFD` (عشري 32765) يمسح المرشح بحيث يتم تلخيص جميع عناصر الصفحة مرة واحدة. التحديد الواحد هو الافتراضي؛ لا تحتاج إلى تفعيله صراحةً.

### عرض جميع العناصر

تعيين `CurrentPageItem` إلى القيمة السحرية `0x7FFD` يكافئ مسح مرشح الصفحة: يلخص جسم الجدول المحوري جميع عناصر الصفحة كما لو لم يتم تطبيق أي مرشح.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### عرض عنصر محدد واحد

تعيين `CurrentPageItem` إلى فهرس حقيقي يختار عنصر التصفية الواحد فقط. الفهرس هو موقع العنصر في قائمة العناصر المرتبة لحقل التصفية، فعلى سبيل المثال يحدد `1` العنصر الثاني بعد الفرز.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **التصفية متعددة الخيارات**

تحول التصفية متعددة الخيارات القائمة المنسدلة للصفحة إلى قائمة مربعات اختيار وتتيح للمستخدم النهائي اختيار عدة عناصر صفحة في وقت واحد. يعرض Aspose.Cells خاصيتين تعملان معًا. يجب تعيين `PivotField.IsMultipleItemSelectionAllowed` إلى `true` قبل أن تصبح واجهة التحديد المتعددة فعالة على الإطلاق. بعد تفعيلها، تتحكم `PivotItem.IsHidden` في العناصر التي تظهر في قائمة مربعات الاختيار، حتى تتمكن من إما إظهار جميع العناصر أو إدراج عناصر محددة فقط في القائمة البيضاء.

يعمل الكود أدناه على تفعيل التحديد المتعدد في نفس حقل صفحة Year الذي تم إنشاؤه في السيناريو 1a، ثم يعرض نمطين: الجزء A يكشف عن جميع عناصر الصفحة بترك `IsHidden` مضبوطًا على `false` لكل إدخال، بينما الجزء B يدرج في القائمة البيضاء فقط قيم المصدر التي تختارها ويخفي كل شيء آخر من خلال كتلة `switch (pivotItems[i].GetStringValue())`.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // بيانات نموذجية: الفاكهة | السنة | المبلغ
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
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // — تمكين التحديد المتعدد في حقل الصفحة
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);

    // الجزء أ — تحديد جميع العناصر (جعل كل عنصر مرئيًا)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }

    // الجزء ب — تحديد عناصر محددة فقط حسب القيمة المصدرية
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

> **ملاحظة:** عند استخدام التصفية متعددة الخيارات من خلال `PivotItem.IsHidden`، **يجب أن يظل عنصر `PivotItem` واحد على الأقل مرئيًا** (`IsHidden == false`). إذا تم إخفاء جميع العناصر، فإن Excel إما يتعطل عند فتح الملف أو يعرض جدولاً محوريًا فارغًا. تحقق دائمًا من أن القائمة البيضاء للتحديد المتعدد تتضمن عنصرًا واحدًا على الأقل من بيانات المصدر الخاصة بك.

## **أي واجهة برمجة تطبيقات وأي وضع يجب أن أستخدم؟**

يلخص الجدول أدناه متى تستخدم كل واجهة برمجة تطبيقات ووضع حتى تتمكن من اختيار المجموعة الصحيحة دون قراءة كل سيناريو بالتفصيل.

| السيناريو / حالة الاستخدام | واجهة البرمجة الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل صفحة باسم عمود المصدر (الأكثر شيوعًا) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | لا ينطبق | عالية المستوى، سطر واحد. استخدم هذا ما لم تكن بحاجة إلى مرجع `PivotField`. |
| إضافة حقل صفحة عندما يكون لديك بالفعل كائن `PivotField` | `PivotTable.PageFields.Add(PivotField)` | لا ينطبق | استخدم عندما تم الحصول على كائن الحقل من مكان آخر أو يحتاج إلى إعادة استخدامه. |
| التصفية إلى عنصر صفحة واحد (الوضع الافتراضي) | `PivotField.CurrentPageItem` | تعيين إلى فهرس محدد | على سبيل المثال، يعرض `1` العنصر الثاني في القائمة المرتبة. |
| عرض جميع العناصر / مسح مرشح الصفحة | `PivotField.CurrentPageItem` | تعيين إلى `0x7FFD` | القيمة السحرية `0x7FFD` (عشري 32765) هي الحارس لـ "جميع العناصر". |
| تفعيل واجهة التحديد المتعدد في Excel | `PivotField.IsMultipleItemSelectionAllowed` | تعيين إلى `true` | مطلوب قبل أن تصبح أي استدعاءات `IsHidden` فعالة. |
| إخفاء / إظهار عناصر فردية في قائمة التحديد المتعدد | `PivotItem.IsHidden` | تعيين لكل عنصر | يجب أن يظل عنصر واحد على الأقل مرئيًا (`IsHidden == false`). |

{{% alert color="primary" %}}
تذكر دائمًا قيد الرؤية عند تكوين التصفية متعددة الخيارات. إذا تم إخفاء كل `PivotItem` في حقل صفحة التحديد المتعدد، فإن Excel يتعطل عند الفتح أو يعرض جدولاً محوريًا فارغًا. أنشئ قائمتك البيضاء مقابل بيانات المصدر بحيث يظل عنصر واحد على الأقل مرئيًا، وستفتح المصنفات المحفوظة لديك بشكل موثوق على كل جهاز.
{{% /alert %}}



{{< app/cells/assistant language="cpp" >}}