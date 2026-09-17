---
title: كاميرا Excel في Aspose.Cells for C++
linktitle: كاميرا Excel في Aspose.Cells for C++
description: تعلم كيفية استخدام كاميرا Excel في Aspose.Cells for C++ لإنشاء صورة ديناميكية مرتبطة بنطاق خلايا تتزامن مع البيانات المصدر وتحافظ على جميع التنسيقات المصدر.
keywords: Aspose.Cells, C++, كاميرا Excel, صورة ديناميكية, صورة مرتبطة, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /ar/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

كاميرا Excel هي كائن في ورقة العمل يُقدِّم صورة حية لنطاق من الخلايا ويطفو على طبقة الرسم مثل أي صورة عادية. يدعم Aspose.Cells وضعين للإنشاء: صورة ديناميكية تتحدّث تلقائيًا عند تغيير البيانات المصدر، وصورة ثابتة تلتقط لقطة لمرة واحدة من النطاق. تتناول هذه المقالة كلا الأسلوبين حتى تتمكن من اختيار الأنسب لتخطيطك.

## ما هي كاميرا Excel؟
كاميرا Excel هي في الأساس كائن صورة مُثبَّت في صف وعمود محددين على طبقة الرسم في ورقة العمل. على عكس الصورة المُدرجة العادية، ترتبط الكاميرا بنطاق مصدر من خلال صيغة بأسلوب A1 مثل `"A1:F10"`. عند تغيير أي خلية داخل هذا النطاق، يتم تحديث صورة الكاميرا تلقائيًا لتعكس المحتوى الجديد. تحافظ الكاميرا على التنسيق الكامل للمنطقة المصدر — الحدود، ألوان الخلفية، الخطوط، وتنسيقات الأرقام — لذا فإن كل ما يظهر داخل الخلايا يظهر أيضًا داخل صورة الكاميرا. وهذا يجعل الكاميرا مفيدة بشكل خاص في لوحات المعلومات، والملخصات، والألواح الجانبية، وتخطيطات التقارير حيث تريد معاينة مرئية لمنطقة بعيدة دون التمرير أو تكرار البيانات. هناك تحذيران: يجب عليك استدعاء `UpdateSelectedValue()` قبل حفظ المصنف، وسيتم تصدير الملف إلى HTML أو PDF، لأن هذه التنسيقات تعتمد على بيانات الصورة المُضمَّنة بدلاً من إعادة الحساب الحي.

## الطريقة الأولى — إضافة صورة كاميرا ديناميكية
الكاميرا الديناميكية هي الأسلوب الأكثر شيوعًا وهي الأقرب تطابقًا لأداة الكاميرا المُدمجة في Excel. تعمل عن طريق إضافة صورة بدون محتوى صورة أولي، ثم تعيين `Formula` لها تُشير إلى النطاق المصدر. بعد تعيين الصيغة، يؤدي استدعاء `UpdateSelectedValue()` إلى تحديث بيانات الصورة المُضمَّنة بحيث تتزامن مع الخلايا التي تعكسها. لا يتم تنفيذ الكاميرا من خلال فئة مُخصصة — بل تُبنى بالكامل على نوع `Picture` القياسي.
واجهات برمجة التطبيقات الرئيسية هي:
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — تضيف صورة مُثبَّتة في الصف والعمود المُحددين. يؤدي تمرير `Vector<uint8_t>()` فارغة إلى إنشاء صورة فارغة تعمل كعنصر نائب للكاميرا الديناميكية. تُرجع هذه الطريقة فهرس الصورة الجديدة.
- `worksheet.GetPictures().Get(int index)` — تسترد `Picture` محددة من المجموعة حسب الفهرس.
- `Picture.SetFormula(U16String value)` — تُعيِّن المرجع بأسلوب A1 إلى النطاق المصدر الذي تعكسه الكاميرا، مثل `U16String("A1:F10")`.
- `Picture.UpdateSelectedValue()` — تُحدِّث بيانات الصورة المُضمَّنة من الخلايا المُشار إليها بواسطة `Formula`.

{{% alert color="primary" %}}
يجب استدعاء `UpdateSelectedValue()` قبل الحفظ عندما يكون الإخراج HTML أو PDF؛ وإلا فلن يحتوي الملف المُصدَّر على بيانات الصورة وستظهر الكاميرا فارغة في الإخراج المُقدَّم.
{{% /alert %}}

يُنشئ الكود التالي مصنفًا، ويُضيف صورة فارغة مُثبَّتة في الصف 10 والعمود 6، ويربطها بنطاق المصدر `A1:F10` من خلال خاصية `Formula`، ويُحدِّث بيانات الصورة المُضمَّنة، ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // الكاميرا الديناميكية: أضف صورة فارغة، اربطها عبر الصيغة بـ A1:F10، ثم حدّث
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## الطريقة الثانية — إضافة صورة كاميرا ثابتة
الكاميرا الثابتة هي في الأساس معاينة مُقدَّمة لمرة واحدة لنطاق من الخلايا. بدلاً من الحفاظ على رابط حي، تُقدِّم النطاق إلى مخزن مؤقت للبايتات من نوع `Vector<uint8_t>` مرة واحدة، وتمرِّر هذا المخزن مباشرة إلى `Pictures.Add(row, col, data)`. يتم تثبيت محتوى الصورة عند لحظة الإنشاء ولا يتحدّث تلقائيًا عند تغيير خلايا المصدر.
واجهات برمجة التطبيقات الرئيسية هي:
- `Cells.CreateRange(U16String address)` — تُنشئ كائن `Range` من عنوان بأسلوب A1 مثل `U16String("A1:F10")`.
- `Range.ToImage(ImageOrPrintOptions options)` — تُقدِّم النطاق إلى مخزن مؤقت للبايتات من نوع `Vector<uint8_t>`. يؤدي تمرير `nullptr` إلى استخدام خيارات التقديم الافتراضية؛ توجد أحمال زائدة للتحكم الدقيق في الإخراج.
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — تضيف الصورة مُثبَّتة في الصف والعمود المُحددين، وهذه المرة يُمرَّر مخزن البايتات الذي أنتجه `Range.ToImage`.
يُنشئ الكود التالي مصنفًا، ويُنشئ `Range` لـ `A1:F10`، ويُقدِّمه إلى بايتات صورة من خلال `Range.ToImage(nullptr)`، ويُضيف الصورة مُثبَّتة في الصف 10 والعمود 6، ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // الكاميرا الثابتة: بناء النطاق، تحويله إلى بايتات، إضافته كصورة
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## الاختيار بين الديناميكي والثابت
- **الكاميرا الديناميكية:** تُحدَّث عند كل إعادة حساب، وتدعم تصدير HTML وPDF بعد `UpdateSelectedValue()`، وتحافظ على سلوك الرابط الحي طوال عمر الملف.
- **الكاميرا الثابتة:** عرض لمرة واحدة لا يتحدّث أبدًا، مفيدة عندما تريد لقطة مرئية ثابتة مُضمَّنة في وقت البناء بدلاً من مرآة حية للبيانات.
يدعم Aspose.Cells كلاً من الكاميرا الديناميكية التي تتحدّث تلقائيًا والمبنية على `Picture.Formula` بالإضافة إلى `UpdateSelectedValue()`، والكاميرا الثابتة التي تُعرض لمرة واحدة والمبنية على `Range.ToImage` بالإضافة إلى `Vector<uint8_t>`. اختر الأسلوب الديناميكي عندما يحتاج إخراجك إلى البقاء متزامنًا مع خلايا المصدر، واختر الأسلوب الثابت عندما تحتاج فقط إلى لقطة مرئية ثابتة في وقت البناء.

{{< app/cells/assistant language="cpp" >}}