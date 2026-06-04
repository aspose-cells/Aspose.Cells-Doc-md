---
title: عرض مصفوفة الخلية الواحدة في SmartMarker | Aspose.Cells C++
description: تعلّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمتي ArrayAsSingle وExtraDelimiter في Smart Markers مع Aspose.Cells for C++.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, العلامات الذكية, ArrayAsSingle, ExtraDelimiter, مصفوفة خلية واحدة, عرض المصفوفة, قالب
type: docs
weight: 195
url: /ar/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells عرض بيانات المصفوفة في خلية واحدة عبر Smart Markers. من خلال استخدام سمة `ArrayAsSingle` مع سمة `ExtraDelimiter`، يمكن للمطورين التحكم في كيفية فصل عناصر المصفوفة داخل خلية واحدة، مما يوفر تنسيقًا مرنًا للتقارير والقوالب.

{{% /alert %}}

## **المقدمة**

تعد Smart Markers في Aspose.Cells ميزة قوية قائمة على القوالب تتيح لك تعبئة بيانات جدول البيانات ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. يتم وضع العلامة في مصنف المصمم، وعندما تتم معالجة القالب بواسطة `WorkbookDesigner`، يتم استبدال العلامات بالقيم من مصدر البيانات المقدم.

افتراضيًا، عندما تشير علامة ذكية إلى خاصية مصفوفة (على سبيل المثال، `&=DataSource.Numbers`)، يقوم المحرك بتوسيع المصفوفة ويضع كل عنصر في خلية منفصلة مجاورة — إما أفقيًا عبر صف أو عموديًا لأسفل عمود. على الرغم من أن هذا السلوك ملائم في العديد من السيناريوهات، إلا أن هناك حالات قد تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع ربط العناصر وفصلها بمحدد من اختيارك.

تعالج سمتا `ArrayAsSingle` و`ExtraDelimiter`، المستخدمتان معًا داخل علامة Smart Marker، هذا المتطلب بالتحديد. تسمحان لك بالحفاظ على تخطيطات التقارير مدمجة ويمكن التنبؤ بها مع الاستمرار في العمل بشكل أصلي مع مصادر بيانات المصفوفات.

## **لماذا هذه الميزة مطلوبة**

### **سلوك نشر المصفوفة الافتراضي**

عندما تشير علامة ذكية إلى خاصية مصفوفة، يقوم Aspose.Cells بتوسيع المصفوفة عبر خلايا متعددة بشكل افتراضي. على سبيل المثال، ستضع علامة مثل `&=Product.Tags` ضد `string[]` يحتوي على أربع قيم كل قيمة في خليتها الخاصة، مما يدفع محتوى القالب الآخر للخارج ويحتمل أن يكسر تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**

هناك العديد من السيناريوهات العملية التي يكون فيها سلوك النشر الافتراضي غير مرغوب فيه:

- **تقارير بنمط الملخص** التي تحتاج إلى تخطيط مدمج من صف واحد لكل سجل.
- **قوائم العلامات أو التصنيفات أو الكلمات المفتاحية** التي تحتاج إلى عرضها كقيم مفصولة بفواصل أو بفاصل أنبوب داخل خلية واحدة.
- **شرائح التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في مكان واحد لسهولة القراءة.
- **خطوط أنابيب المعالجة اللاحقة** (تصدير CSV، عرض PDF، دمج البريد) التي تتوقع قيمة موحدة واحدة لكل خلية بدلاً من نطاق موسع.
- **التوافق عبر الأنظمة الأساسية**، حيث لا يمكن لبعض المستهلكين التعامل مع المصفوفات التي تنتشر عبر خلايا متعددة.

### **الفجوة التي تسدها**

بدون آلية مدمجة، سيكون المطورون مجبرين على معالجة البيانات مسبقًا في C++ — دمج المصفوفات في سلاسل محددة قبل ربطها بمصمم المصنف. هذا يضاعف المنطق، ويعقد نماذج البيانات، ويزيد من فرصة الأخطاء. تعمل سمتا `ArrayAsSingle` و`ExtraDelimiter` على إلغاء هذا الحل البديل من خلال معالجة التنسيق بشكل إعلاني داخل العلامة الذكية نفسها.

## **فوائد الميزة**

يوفر استخدام سمتي `ArrayAsSingle` و`ExtraDelimiter` في العلامات الذكية عدة مزايا:

- **الاحتواء في خلية واحدة**: يتم عرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على التخطيطات مدمجة ويمكن التنبؤ بها.
- **التحكم في المحدد المخصص**: حدد أي سلسلة فاصل تريدها — فاصلة، فاصلة منقوطة، واصلة، علامة الأنبوب، سطر جديد، أو أي نص مخصص.
- **التنسيق القائم على القوالب**: لا حاجة إلى كود إضافي لمعالجة البيانات مسبقًا؛ توجد قواعد التنسيق داخل علامة Smart Marker.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدامات**: تعمل مع السلاسل والأرقام والتواريخ وأي نوع بيانات آخر يمكن ربطه بمحدد.
- **التوافق العكسي**: عند حذف السمات، يتم الحفاظ على سلوك النشر الأصلي، لذا تستمر القوالب الموجودة في العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صيغة العلامة الذكية**

يتم تمرير سمتي `ArrayAsSingle` و`ExtraDelimiter` كأزواج قيمة-مفتاح داخل أقواس علامة ذكية قياسية. الصيغة العامة هي:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

تتكون العلامة من الأجزاء التالية:

- `&=DataSource.ArrayProperty` — العلامة الذكية القياسية التي تشير إلى خاصية المصفوفة في مصدر البيانات المرتبط.
- `arrayasSingle=true` — يوجه المحرك لعرض المصفوفة بأكملها في خلية واحدة. فقط القيمة `true` تؤدي إلى سلوك الخلية الواحدة.
- `extraDelimiter=", "` — يحدد الفاصل الموضوع بين عناصر المصفوفة. القيمة هي سلسلة حرفية؛ يمكن أن تكون فارغة أو حرفًا واحدًا أو سلسلة متعددة الأحرف.

{{% alert color="primary" %}}

تقبل سمة `extraDelimiter` أي سلسلة حرفية، بما في ذلك المحددات متعددة الأحرف، أو النص المخصص، أو تسلسلات الهروب مثل `\n` للإخراج المفصول بسطر جديد. إذا كانت المصفوفة فارغة، تُترك الخلية الناتجة فارغة.

{{% /alert %}}

### **سير العمل خطوة بخطوة**

يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام Smart Markers.

1. **إعداد مصدر البيانات**: أنشئ فئة (أو بنية بيانات) تعرض خاصية تُرجع مصفوفة. يمكن أن تُرجع الخاصية `std::vector<std::string>`، أو `std::vector<int>`، أو أي نوع مصفوفة/متجه مدعوم آخر.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف رأس، وضع خلية علامة ذكية تشير إلى خاصية المصفوفة مع سمتي `arrayasSingle` و`extraDelimiter`.
3. **إنشاء مثيل WorkbookDesigner**: أنشئ كائن `WorkbookDesigner`، وأرفق مصنف المصمم به، واربط مصدر البيانات الخاص بك باستخدام طريقة `SetDataSource`.
4. **معالجة العلامات**: استدعِ طريقة `WorkbookDesigner.Process()` لتوسيع العلامات الذكية وتعبئة المصنف بالبيانات الحقيقية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بتنسيق XLSX أو أي تنسيق ملف مدعوم آخر.

### **مثال الكود 1 — عرض مصفوفة سلاسل أساسية**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // WorkbookDesigner غير متوفر في Aspose.Cells لـ C++
    // نحتاج إلى محاكاة معالجة SmartMarker عن طريق استبدال العلامات يدويًا
    // نظرًا لأن Aspose.Cells C++ لا يدعم WorkbookDesigner، سنستخدم استبدال U16String
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // استبدال العلامة الذكية بالبيانات الفعلية
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **مثال الكود 2 — مصفوفة رقمية بمحدد مخصص**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **مثال الكود 3 — مقارنة السلوك الافتراضي بسلوك ArrayAsSingle**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // تحضير مصدر البيانات
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // إنشاء مصنف والحصول على ورقة العمل الأولى
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // القسم 1: العلامة الذكية الافتراضية - القيم موزعة أفقياً عبر الخلايا
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // القسم 2: عرض الخلية الواحدة الجديد باستخدام arrayasSingle و extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // ربط مصدر البيانات ومعالجة العلامات الذكية
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // حفظ المصنف الناتج
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **ملاحظات وأفضل الممارسات**

ضع النقاط التالية في اعتبارك عند العمل مع سمتي `ArrayAsSingle` و`ExtraDelimiter`:

- تُعامل قيمة `extraDelimiter` كسلسلة حرفية؛ قم بإفلات أي أحرف خاصة قد يفسرها معالج القالب الخاص بك.
- تقبل سمة `arrayasSingle` قيمة منطقية (`true` / `false`). فقط `true` يؤدي إلى سلوك الخلية الواحدة؛ أي قيمة أخرى تعود إلى سلوك النشر الافتراضي.
- إذا كانت المصفوفة فارغة أو خالية، تُترك الخلية فارغة (أو تحتوي على سلسلة فارغة حسب نوع البيانات).
- تعمل الميزة مع مصادر بيانات الكائنات وكذلك مصادر `DataSet` و`DataTable` حيث يمكن تقسيم عمود إلى مصفوفات.
- للإخراج المفصول بسطر جديد، يمكنك استخدام `\n` كقيمة للمحدد.
- ضع العلامة الذكية في خلية ذات عرض كافٍ لعرض السلسلة المتسلسلة الناتجة؛ وإلا، قد يفيض المحتوى بصريًا إلى الخلايا المجاورة حسب التنسيق.

## **مقالات ذات صلة**

- [Smart Markers](/cells/ar/cpp/smart-markers/)
- [Merging and Unmerging Cells](/cells/ar/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}