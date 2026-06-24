---
title: خطوط المؤشرات في Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط المؤشرات — وهي رسوم بيانية مصغرة تُوضع داخل خلايا ورقة العمل. توضح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشرات الخطية والعمودية وخطوط الربح/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة C++, جداول البيانات, خطوط المؤشرات, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشرات للربح/الخسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إنشاء خطوط المؤشرات داخل خلايا ورقة العمل. خطوط المؤشرات هي رسوم بيانية مصغرة تتناسب مع خلية واحدة، وتوفر تمثيلاً مرئياً سريعاً لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشرات الخطية والعمودية وخطوط الربح/الخسارة، ويمكن تخصيص كل منها من حيث اللون ووزن الخط ونقاط القمة/القاع والعلامات.

{{% /alert %}}

## **المقدمة**

خطوط المؤشرات هي رسوم بيانية صغيرة داخل الخلايا تكون مفيدة عندما تريد عرض اتجاه سريع بجوار صف أو عمود من البيانات دون أن تأخذ مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشرات: **خطي**، **عمودي**، و**ربح/خسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الأسماء `Aspose.Cells.Charts`.

في Aspose.Cells، يتم إنشاء كل خط مؤشرات تضيفه من خلال `worksheet.SparklineGroups.Add(...)`، والتي تُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشرات، ونطاق البيانات، والخلية الوجهة، والخصائص المرئية مثل لون الخط، ووزن الخط، والعلامات، ومؤشرات نقاط القمة/القاع.

{{% alert color="primary" %}}

يمكن أن يحتوي `SparklineGroup` واحد على خط مؤشرات واحد أو أكثر تشترك في نفس النمط. عندما تستدعي `Add` وتمرر صفاً من البيانات بالإضافة إلى خلية وجهة واحدة، تحصل على خط مؤشرات واحد داخل تلك الخلية. إذا كان نطاق الوجهة أوسع من خلية واحدة، فسيتم رسم خط مؤشرات منفصل في كل خلية وجهة، جميعها تستخدم نفس النمط ونطاق البيانات.

{{% /alert %}}

تستعرض هذه المقالة كل نوع من أنواع خطوط المؤشرات الثلاثة التي يدعمها Aspose.Cells — **خطي**، **عمودي**، و**ربح/خسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشرات الخطية**

يرسم خط المؤشرات الخطي خطاً متصلاً عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات بمرور الوقت. في Aspose.Cells، يتم إنشاء خط المؤشرات الخطي بتمرير `SparklineType.Line` إلى طريقة `SparklineGroups.Add`.

سير العمل هو نفسه كما هو الحال في أي نوع آخر من خطوط المؤشرات:

1. أنشئ `Workbook` جديداً وانتقل إلى ورقة العمل الأولى.
2. املأ صفاً من بيانات المصدر (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم خط المؤشرات.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يُخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس عمودياً (عمود).
5. اختيارياً، خصص `SparklineGroup` المُرجع. لخط المؤشرات الخطي يمكنك تعيين لون الخط باستخدام `group.Line.Color` (الذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط وزن الخط، وتبديل علامات نقاط القمة/القاع.
6. احفظ المصنف.

ينشئ المثال التالي مصنفاً، ويكتب القيم 5، -3، 8، -2، 6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يُخصص لون الخط إلى الأحمر ويُفعّل علامات لنقاط القمة والقاع.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // الخطوة 1: إنشاء مصنف والحصول على أول ورقة عمل
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // الخطوة 2: كتابة القيم النموذجية 5، -3، 8، -2، 6 في الخلايا A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // الخطوة 3: إنشاء CellArea يشير إلى الخلية الوجهة F1
    CellArea dest;
    dest.StartColumn = 5;   // العمود F (بفهرس يبدأ من 0)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // الصف 1 (بفهرس يبدأ من 0)
    dest.EndRow = 0;

    // الخطوة 4: إضافة سباركلاين خطي من A1:E1 إلى F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون خط السباركلاين
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // الخطوة 6: تمكين علامات النقطة العالية والنقطة المنخفضة
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // الخطوة 7: حفظ المصنف
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **خطوط المؤشرات العمودية**

يُقدم خط المؤشرات العمودي كل نقطة بيانات كعمود عمودي. وهذا يجعله مناسباً تماماً للبيانات التي يكون مقدارها ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدادات. في Aspose.Cells، تنشئ خط المؤشرات العمودي بتمرير `SparklineType.Column` إلى طريقة `SparklineGroups.Add`.

الإجراء يعكس مثال خط المؤشرات الخطي:

1. أنشئ `Workbook` جديداً وانتقل إلى ورقة العمل الأولى.
2. املأ نفس نطاق المصدر (A1:E1) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. اختيارياً، خصص `SparklineGroup` الناتج — على سبيل المثال، بتعيين `group.Type` لتأكيد النوع، أو بضبط لون الأعمدة.
6. احفظ المصنف في ملف إخراج منفصل بحيث لا يكتب فوق مثال خط المؤشرات الخطي.

يكتب المثال أدناه القيم 5، -3، 8، -2، 6 في A1:E1 ويُقدم خط مؤشر عمودي في F1. تُرسم القيم السالبة كأعمدة تتجه لأسفل والقيم الموجبة كأعمدة تتجه لأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة واحدة.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // الخطوة 2: كتابة قيم عينة في A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // الخطوة 3: بناء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // الخطوة 4: إضافة خط مؤشر عمودي إلى خلية الوجهة
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // الخطوة 5: تأكيد نوع خط المؤشر بقراءة group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // الخطوة 6: حفظ المصنف
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **خطوط المؤشرات للربح/الخسارة**

خط المؤشرات للربح/الخسارة هو تباين خاص لخط المؤشرات العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كعمود "لأعلى" (ربح) وتُرسم القيمة الصفرية أو السالبة كعمود "لأسفل" (خسارة). تُستخدم خطوط المؤشرات للربح/الخسارة بشكل شائع لتصور تسلسلات الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية بمرور الوقت.

في Aspose.Cells، يتم إنشاء خط المؤشرات للربح/الخسارة بتمرير `SparklineType.Stacked` إلى طريقة `SparklineGroups.Add`. (على الرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب تقديم الربح/الخسارة.)

الإجراء هو نفسه كما في النوعين الآخرين:

1. أنشئ `Workbook` جديداً وانتقل إلى ورقة العمل الأولى.
2. املأ نطاق المصدر. ولأن خطوط المؤشرات للربح/الخسارة تعامل كل قيمة إما على أنها ربح أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أعمدة لأعلى والقيم غير الموجبة تصبح أعمدة لأسفل.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. اختيارياً، خصص `SparklineGroup` المُرجع، على سبيل المثال بتعيين ألوان مميزة لأعمدة الربح والخسارة.
6. احفظ المصنف باسم ملف مميز بحيث يمكن أن تتعايش الأمثلة الثلاثة على القرص.

يستخدم المثال أدناه نفس بيانات الإدخال كما في القسمين السابقين. تُفسر القيم 5، -3، 8، -2، 6 على أنها ربح، خسارة، ربح، خسارة، ربح — ويعكس خط المؤشرات المرسوم في F1 هذا النمط بالضبط.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // الخطوة 2: ملء بيانات العينة في الصف 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // الخطوة 3: بناء CellArea يشير إلى F1 (العمود 5، الصف 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // الصف 1
    dest.EndRow = 0;

    // الخطوة 4: إضافة سباركلاين فوز/خسارة (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // الخطوة 5: تخصيص مجموعة سباركلاين
    // تمكين علامات النقطة العالية والنقطة المنخفضة
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // تعيين لون النقطة العالية إلى اللون الأخضر
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // تعيين لون النقطة المنخفضة إلى اللون الأحمر
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // تعيين لون النقاط السلبية إلى اللون البرتقالي
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // تعيين لون السلسلة الافتراضي (المستخدم للأشرطة الموجبة)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // الخطوة 6: حفظ المصنف
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الجمع بين أنواع خطوط المؤشرات الثلاثة**

ينتج كل مثال من الأمثلة الثلاثة السابقة مصنفاً خاصاً به بحيث يسهل فحص ملفات الإخراج بمعزل عن غيرها. في سيناريو العالم الحقيقي، ومع ذلك، غالباً ما ترغب في مقارنة عدة سلاسل بيانات جنباً إلى جنب. إن أنظف طريقة للقيام بذلك هي وضع أكثر من مجموعة خطوط مؤشر في نفس ورقة العمل، مع تقديم كل مجموعة لنمط مختلف.

يمكنك إضافة كائنات `SparklineGroup` متعددة إلى نفس `SparklineGroupCollection`، ويمكن لكل مجموعة استهداف خلية وجهة مختلفة أو نطاق مختلف. على سبيل المثال، يمكنك وضع خط مؤشر خطي في F1، وخط مؤشر عمودي في F2، وخط مؤشر ربح/خسارة في F3 — جميعها تقرأ من نفس بيانات المصدر في الصف 1 — حتى يتمكن القارئ من رؤية ثلاثة معالجات مرئية مختلفة لنفس الأرقام.

ينشئ المثال المجمع أدناه مصنفاً واحداً، ويملأ الصف 1 بالقيم 5، -3، 8، -2، 6، ثم يضيف ثلاث مجموعات خطوط مؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يوضح الملف الناتج أنماط خطوط المؤشرات الثلاثة دفعة واحدة.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // الخطوة 2: ملء بيانات نموذجية في الصف 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // الخطوة 3: إضافة مجموعة مخطط خطي مصغر عند F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // تخصيص لون المخطط الخطي المصغر عبر CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // الخطوة 4: إضافة مجموعة مخطط عمودي مصغر عند F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // تخصيص لون سلسلة المخطط العمودي المصغر
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // الخطوة 5: إضافة مجموعة مخطط فوز/خسارة (مكدس) مصغر عند F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // تخصيص لون سلسلة المخطط المصغر فوز/خسارة
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // الخطوة 6: حفظ المصنف
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

عندما تجمع بين مجموعات خطوط المؤشرات المتعددة في ورقة عمل واحدة، تكون كل مجموعة مستقلة. يمكنها مشاركة نفس نطاق المصدر أو استخدام نطاقات مصدر مختلفة، ويمكن تنسيقها بشكل مستقل. وهذا يجعل من السهل بناء "لوحة معلومات" صغيرة من التصورات داخل الخلايا مباشرة داخل ورقة عمل موجودة.

{{% /alert %}}

## **تخصيص مظهر خط المؤشرات**

بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.SparklineGroups`، يمكنك قراءة أو تعديل عدة من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر تخصيصاً بشكل شائع هي:

- **`group.Type`** — الـ `SparklineType` (خطي، عمودي، أو متراكم). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.Line.Color`** — لون الخط، معبراً عنه كـ `CellsColor` تم إنشاؤه عبر `workbook.CreateCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون ضربة خط المؤشرات الخطي.
- **`group.Line.Weight`** — وزن الخط بالنقاط. القيم الأعلى تنتج خطوطاً أسمك.
- **علامات نقاط القمة/القاع** — علامات تُشغّل علامات صغيرة على أعلى وأدنى نقاط البيانات، مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — علامات تُبدّل علامات على نقاط البيانات الأولى والأخيرة والسالبة.

لتغيير اللون، أنشئ دائماً مثيلاً من `CellsColor` وعيّنه إلى الخاصية ذات الصلة. لا تعين قيمة لون خام مباشرة إلى خصائص لون خط المؤشرات — فهي تتوقع النوع `CellsColor` من `Aspose.Cells.Drawing`. إن طريقة `SparklineGroups.Add` نفسها تُرجع كائن `SparklineGroup` مكتوب بالكامل، حتى تتمكن من ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.



{{< app/cells/assistant language="cpp" >}}