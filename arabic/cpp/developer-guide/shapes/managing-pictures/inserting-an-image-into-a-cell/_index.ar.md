---
title: إدراج صورة في خلية
linktitle: إدراج صورة في خلية
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات. توضح هذه المقالة كيفية ملاءمة صورة بدقة في خلية واحدة، سواء عن طريق وضع صورة عائمة فوق الخلية أو عن طريق تضمين الصورة مباشرة في الخلية.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, إدراج صورة, تضمين صورة, صورة في خلية, ملاءمة صورة لخلية, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ar/cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells طريقتين متميزتين لربط صورة بخلية واحدة. الصورة العائمة هي شكل موجود على طبقة الرسم في ورقة العمل ويغطي بصريًا نطاقًا من الخلايا، بينما تُخزَّن الصورة المضمنة داخل الخلية نفسها وتتدرج تلقائيًا لتتناسب مع مساحة عرض الخلية. اختر الأسلوب الذي يناسب متطلبات التخطيط لديك بشكل أفضل.

## **المقدمة**
تعد ملاءمة الصورة بدقة في خلية واحدة متطلبًا شائعًا عند تصميم جداول البيانات التي تعمل كتقارير مرئية، أو كتالوجات منتجات، أو أدلة موظفين، أو لوحات معلومات، أو قوائم جرد. بدلًا من تمديد الصورة عبر عدة خلايا أو وضعها بشكل فضفاض على ورقة العمل، قد ترغب في صورة نظيفة ومرتبطة بالخلية تظل محاذية مع الخلية التي تملكها.
يدعم Aspose.Cells هذا السيناريو بطريقتين متكاملتين:
- **الأسلوب 1 — وضع صورة عائمة فوق خلية.** أضف `Picture` إلى ورقة العمل، وعيّن `Placement` إلى `MoveAndSize`، واضبط خلايا الربط (`UpperLeftRow`، `UpperLeftColumn`، `LowerRightRow`، `LowerRightColumn`) بحيث تغطي الصورة خلية واحدة بالضبط.
- **الأسلوب 2 — تضمين صورة مباشرة في خلية.** عيّن وحدات بايت الصورة إلى خاصية `EmbeddedImage` الخاصة بالخلية. تتدرج الصورة تلقائيًا لتلائم مساحة عرض الخلية وتنتقل معها.
يتناول باقي هذه المقالة كلا الأسلوبين، ويشرح واجهات برمجة التطبيقات ذات الصلة، ويوضح كيفية استخدامهما في التعليمات البرمجية.

## **الأسلوب 1: وضع صورة فوق خلية**
الصورة العائمة هي كائن `Picture` يعيش على طبقة الرسم في ورقة العمل. على الرغم من أنها ليست جزءًا من أي خلية واحدة، إلا أنها مرتبطة بنطاق من الخلايا. تحدد خلايا ربط الصورة — الزاوية العلوية اليسرى والسفلية اليمنى — امتدادها المرئي على ورقة العمل. افتراضيًا، تمتد الصورة المضافة حديثًا عبر عدة خلايا.
لجعل الصورة العائمة تغطي **خلية واحدة بالضبط**، تحتاج إلى:
1. إضافة الصورة باستخدام `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`، والذي يربط الصورة الجديدة بالخلية المحددة.
2. تعيين خصائص الربط الأربعة بحيث يتطابق المستطيل المحيط بالصورة مع الخلية المستهدفة.
3. تعيين `Picture.Placement` إلى `PlacementType.MoveAndSize` بحيث تنتقل الصورة وتعيد تحجيمها مع الخلية الأساسية عندما يغير المستخدم عرض العمود أو ارتفاع الصف.

### **ربط الصورة بخلية واحدة**
يتم تعريف ربط الصورة بأربع خصائص فهرسة تبدأ من الصفر:
- `Picture.UpperLeftRow` — فهرس الصف للحافة العلوية للصورة.
- `Picture.UpperLeftColumn` — فهرس العمود للحافة اليسرى للصورة.
- `Picture.LowerRightRow` — فهرس الصف للحافة السفلية للصورة. لجعل الحافة السفلية للصورة في أسفل الصف `r`، عيّن هذه القيمة إلى `r + 1`.
- `Picture.LowerRightColumn` — فهرس العمود للحافة اليمنى للصورة. لجعل الحافة اليمنى للصورة في يمين العمود `c`، عيّن هذه القيمة إلى `c + 1`.

{{% alert color="primary" %}}
تعد فهارس الصفوف والأعمدة في Aspose.Cells **مبنية على الصفر**. الخلية C6 لها فهرس صف 5 وفهرس عمود 2. أخطاء الفرق بواحد في ربط الزاوية السفلية اليمنى هي المصدر الأكثر شيوعًا لظهور الصور متداخلة في خلية مجاورة.

### **التحكم في سلوك الموضع**
`Picture.Placement` هو تعداد من نوع `PlacementType` يتحكم في كيفية تصرف الصورة عندما يعيد المستخدم تحجيم الصف أو العمود الذي تحتها. القيمة الموصى بها لصورة خلية واحدة هي `PlacementType.MoveAndSize`، والتي تتسبب في انتقال الصورة وإعادة تحجيمها معًا مع الخلية الأساسية، محافظةً على الملاءمة الدقيقة.

### **إرشادات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا (أو افتح مصنفًا موجودًا).
2. الوصول إلى `Worksheet` المستهدفة من `workbook.GetWorksheets().Get(0]`.
3. اقرأ ملف الصورة من القرص إلى مخزن مؤقت للبايتات من نوع `Vector<uint8_t>` حتى تتوفر وحدات بايت الصورة لواجهة برمجة التطبيقات.
4. استدعِ `worksheet.Pictures.Add(5, 2, imageData)` لإضافة صورة مرتبطة بالخلية C6. احفظ مرجع `Picture` المُعاد.
5. عيّن إحداثيات الربط الأربعة بحيث تغطي الصورة الخلية C6 فقط: `UpperLeftRow = 5`، `UpperLeftColumn = 2`، `LowerRightRow = 6`، `LowerRightColumn = 3`.
6. عيّن `picture.Placement = PlacementType.MoveAndSize` للحفاظ على محاذاة الصورة مع C6 عند تغيير حجم العمود أو الصف.
7. اختياريًا، أضف نصًا نموذجيًا إلى الخلايا المحيطة لإثبات أن الخلية C6 فقط تحتوي على الصورة.
8. احفظ المصنف على القرص كملف `.xlsx`.
يوضح الكود التالي الأسلوب الكامل.

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();
    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));
    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);
    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الأسلوب 2: تضمين صورة مباشرة في خلية**
يعرض Aspose.Cells أيضًا آلية أبسط للصور المرتبطة بالخلايا: خاصية `Cell.EmbeddedImage`. يؤدي تعيين وحدات بايت الصورة إلى هذه الخاصية إلى إرفاق الصورة بالخلية نفسها، كما لو كانت محتوى داخليًا.

### **كيف تعمل الصور المضمنة**
- تُخزَّن الصورة كجزء من محتوى الخلية بدلاً من كونها شكلًا على طبقة الرسم.
- تتدرج الصورة تلقائيًا لتلائم داخل الحدود المعروضة للخلية. لا حاجة إلى إحداثيات ربط أو إعدادات موضع.
- تظل الخلية خلية حقيقية بعنوان حقيقي يمكن الإشارة إليه بواسطة الصيغ، أو فرزها كجزء من صف، أو استخدامها في عمليات أخرى على مستوى الخلية.
يجعل هذا من `Cell.EmbeddedImage` الخيار الأكثر إيجازًا عندما يكون هدفك ببساطة "صورة تعيش داخل هذه الخلية."

### **إرشادات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا (أو افتح مصنفًا موجودًا).
2. الوصول إلى `Worksheet` المستهدفة من `workbook.GetWorksheets().Get(0]`.
3. اقرأ ملف الصورة من القرص في مصفوفة بايتات من نوع `Vector<uint8_t>`.
4. احصل على مرجع للخلية المستهدفة — إما من خلال `worksheet.GetCells().Get("C6"]` أو `worksheet.GetCells().Get(5, 2]`.
5. عيّن مصفوفة البايتات إلى خاصية `EmbeddedImage` الخاصة بالخلية.
6. اختياريًا، اضبط ارتفاع الصف وعرض العمود للصف والعمود المستهدفين لإعطاء الصورة المضمنة مظهرًا أكثر بروزًا.
7. احفظ المصنف على القرص كملف `.xlsx`.
يوضح الكود التالي الأسلوب الكامل.

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C6");
    // قراءة ملف الصورة في مصفوفة بايتات
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    // تحويل std::vector إلى Aspose::Cells::Vector باستخدام مُنشئ المؤشر+الحجم
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());
    // تضمين الصورة مباشرة في الخلية
    cell.SetEmbeddedImage(imageData);
    // اختياريًا ضبط ارتفاع الصف وعرض العمود بحيث تكون الصورة المضمنة أكثر وضوحًا
    worksheet.GetCells().SetColumnWidth(2, 30);   // العمود C (الفهرس 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // الصف 6 (الفهرس 5)
    // حفظ المصنف الناتج كملف .xlsx
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **اختيار الأسلوب الصحيح**
ينتج كلا الأسلوبين صورة تتناسب داخل خلية واحدة، لكنهما يختلفان في كيفية تخزين الصورة وكيفية تصرفها:
- **استخدم صورة عائمة (الأسلوب 1) عندما:**
  - تحتاج إلى تحكم أدق في الموضع أو الطبقات أو المحاذاة مع كائنات الرسم الأخرى.
  - تريد أن تتصرف الصورة كشكل يمكن تحديده أو إعادة ترتيبه أو تجميعه مع أشكال أخرى.
  - تتطلب توافقًا مع الإصدارات السابقة من التعليمات البرمجية التي تعمل بالفعل مع `PictureCollection`.
  - تحتاج إلى حساب إحداثيات الربط ديناميكيًا استنادًا إلى تخطيط ورقة العمل.
- **استخدم صورة مضمنة (الأسلوب 2) عندما:**
  - تريد أبسط إدراج ممكن لصورة في خلية.
  - يجب أن تنتقل الصورة مع الخلية مثل أي محتوى آخر للخلية.
  - لا تحتاج إلى معالجة الصورة كشكل.
{{% /alert %}}

{{% /alert %}}

## المقالات ذات الصلة
- [كاميرا Excel في Aspose.Cells for C++](/cells/ar/cpp/excel-camera/)
- [إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for C++](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for C++](/cells/ar/cpp/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/cpp/change-page-field-layout/)
- [تحويل سباركلاين إلى صورة وHTML في Aspose.Cells for C++](/cells/ar/cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="cpp" >}}