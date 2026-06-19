---
title: إدراج صورة في خلية
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات. توضح هذه المقالة كيفية ملاءمة صورة بدقة بحجم خلية واحدة باستخدام طريقتين مختلفتين: وضع صورة عائمة فوق الخلية، أو تضمين الصورة مباشرة في الخلية.
keywords: Aspose.Cells, C++ library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ar/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

يوفر Aspose.Cells طريقتين مختلفتين لربط صورة بخلية واحدة. الصورة العائمة هي شكل على طبقة الرسم في ورقة العمل يغطي بصريًا نطاقًا من الخلايا، بينما تُخزَّن الصورة المضمنة داخل الخلية نفسها وتُكبَّر تلقائيًا لتتناسب مع مساحة عرض الخلية. اختر الطريقة التي تتناسب بشكل أفضل مع متطلبات التخطيط لديك.

{{% /alert %}}

## **المقدمة**

تعد ملاءمة صورة بدقة بخلية واحدة متطلبًا شائعًا عند تصميم جداول البيانات التي تعمل كتقارير مرئية، أو كتالوجات منتجات، أو أدلة موظفين، أو لوحات معلومات، أو قوائم جرد. بدلاً من تمديد الصورة عبر العديد من الخلايا أو وضعها بشكل فضفاض على ورقة عمل، قد ترغب في صورة نظيفة مرتبطة بخلية تظل محاذية للخلية التي تملكها.

يدعم Aspose.Cells هذا السيناريو بطريقتين متكاملتين:

- **الطريقة 1 — وضع صورة عائمة فوق خلية.** أضف `Picture` إلى ورقة العمل، واضبط `Placement` على `MoveAndSize`، وعدّل خلايا الإرساء (`UpperLeftRow`، `UpperLeftColumn`، `LowerRightRow`، `LowerRightColumn`) بحيث تغطي الصورة خلية واحدة بالضبط.
- **الطريقة 2 — تضمين صورة مباشرة في خلية.** خصّص بايتات الصورة إلى خاصية `EmbeddedImage` للخلية. تتغير أبعاد الصورة تلقائيًا لتتناسب مع مساحة عرض الخلية وتنتقل مع الخلية.

يتناول باقي هذه المقالة كلتا الطريقتين، ويشرح واجهات برمجة التطبيقات ذات الصلة، ويوضح كيفية استخدامها في الكود.

## **الطريقة 1: وضع صورة فوق خلية**

الصورة العائمة هي كائن `Picture` يوجد على طبقة الرسم في ورقة العمل. على الرغم من أنها ليست جزءًا من أي خلية واحدة، إلا أنها مُرساءة في نطاق خلايا. تحدد خلايا الإرساء الخاصة بالصورة — زواياها العلوية اليسرى والسفلية اليمنى — مدى ظهورها المرئي على ورقة العمل. بشكل افتراضي، تمتد الصورة المُضافة حديثًا عبر عدة خلايا.

لجعل الصورة العائمة تغطي **خلية واحدة بالضبط**، تحتاج إلى:

1. أضف الصورة باستخدام `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`، والذي يُرسي الصورة الجديدة في الخلية المُعطاة.
2. اضبط خصائص الإرساء الأربعة بحيث يتطابق المستطيل المُحِيط بالصورة مع الخلية المستهدفة.
3. اضبط `Picture.Placement` على `PlacementType.MoveAndSize` بحيث تتحرك الصورة وتُعيد تحجيمها مع الخلية الأساسية عندما يغير المستخدم عرض العمود أو ارتفاع الصف.

### **إرساء الصورة في خلية واحدة**

يتم تعريف إرساء الصورة من خلال أربع خصائص فهرسة قائمة على الصفر:

- `Picture.UpperLeftRow` — فهرس صف الحافة العلوية للصورة.
- `Picture.UpperLeftColumn` — فهرس عمود الحافة اليسرى للصورة.
- `Picture.LowerRightRow` — فهرس صف الحافة السفلية للصورة. لجعل الحافة السفلية للصورة عند أسفل الصف `r`، اضبط هذا على `r + 1`.
- `Picture.LowerRightColumn` — فهرس عمود الحافة اليمنى للصورة. لجعل الحافة اليمنى للصورة عند يمين العمود `c`، اضبط هذا على `c + 1`.

على سبيل المثال، لملاءمة الصورة بدقة في الخلية **C6** (فهرس الصف `5`، فهرس العمود `2`)، اضبط `UpperLeftRow = 5`، و`UpperLeftColumn = 2`، و`LowerRightRow = 6`، و`LowerRightColumn = 3`.

{{% alert color="primary" %}}

فهارس الصفوف والأعمدة في Aspose.Cells **قائمة على الصفر**. الخلية C6 لها فهرس صف 5 وفهرس عمود 2. أخطاء بمقدار واحد في إرساء الزاوية السفلية اليمنى هي المصدر الأكثر شيوعًا للصور التي تظهر متداخلة في خلية مجاورة.

{{% /alert %}}

### **التحكم في سلوك الموضع**

`Picture.Placement` هو تعداد من نوع `PlacementType` يتحكم في كيفية تصرف الصورة عندما يُعيد المستخدم تحجيم الصف أو العمود تحتها. القيمة الموصى بها لصورة خلية واحدة هي `PlacementType.MoveAndSize`، والتي تتسبب في تحرك الصورة وإعادة تحجيمها مع خليتها الأساسية، محافظةً على الملاءمة الدقيقة.

### **إرشادات خطوة بخطوة**

1. أنشئ `Workbook` جديدًا (أو افتح واحدًا موجودًا).
2. الوصول إلى `Worksheet` المستهدف من `workbook.Worksheets[0]`.
3. اقرأ ملف الصورة من القرص إلى مخزن مؤقت بايتات `Vector<uint8_t>` بحيث تتوفر بايتات الصورة لواجهة برمجة التطبيقات.
4. استدعِ `worksheet.Pictures.Add(5, 2, imageData)` لإضافة صورة مُرساءة في الخلية C6. احتفظ بمرجع الكائن `Picture` المُرجَع.
5. اضبط إحداثيات الإرساء الأربعة بحيث تغطي الصورة الخلية C6 فقط: `UpperLeftRow = 5`، `UpperLeftColumn = 2`، `LowerRightRow = 6`، `LowerRightColumn = 3`.
6. اضبط `picture.Placement = PlacementType.MoveAndSize` لإبقاء الصورة محاذية لـ C6 عند إعادة تحجيم العمود أو الصف.
7. اختياريًا، أضف نصًا نموذجيًا إلى الخلايا المحيطة لإظهار أن الخلية C6 فقط هي التي تحتوي على الصورة.
8. احفظ المصنف على القرص كملف `.xlsx`.

يوضح الكود التالي الطريقة الكاملة.

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

## **الطريقة 2: تضمين صورة مباشرة في خلية**

يكشف Aspose.Cells أيضًا عن آلية أبسط للصور المرتبطة بالخلية: خاصية `Cell.EmbeddedImage`. يؤدي تخصيص بايتات الصورة لهذه الخاصية إلى إرفاق الصورة بالخلية نفسها، كما لو كانت محتوى مضمّنًا.

### **كيف تعمل الصور المضمنة**

- تُخزَّن الصورة كجزء من محتوى الخلية وليس كشكل على طبقة الرسم.
- تتغير أبعاد الصورة تلقائيًا لتتناسب مع الحدود المعروضة للخلية. لا يلزم وجود إحداثيات إرساء أو إعدادات موضع.
- تظل الخلية خلية حقيقية بعنوان حقيقي يمكن الإشارة إليه بواسطة الصيغ، أو فرزها كجزء من صف، أو استخدامها في عمليات أخرى على مستوى الخلية.

هذا يجعل `Cell.EmbeddedImage` الخيار الأكثر إيجازًا عندما يكون هدفك ببساطة "صورة تعيش داخل هذه الخلية".

### **إرشادات خطوة بخطوة**

1. أنشئ `Workbook` جديدًا (أو افتح واحدًا موجودًا).
2. الوصول إلى `Worksheet` المستهدف من `workbook.Worksheets[0]`.
3. اقرأ ملف الصورة من القرص إلى مصفوفة بايتات `Vector<uint8_t>`.
4. احصل على مرجع للخلية المستهدفة — إما من خلال `worksheet.Cells["C6"]` أو `worksheet.Cells[5, 2]`.
5. خصّص مصفوفة البايتات على خاصية `EmbeddedImage` للخلية.
6. اختياريًا، اضبط ارتفاع الصف وعرض العمود للصف والعمود المستهدفين لإعطاء الصورة المضمنة مظهرًا أكثر بروزًا.
7. احفظ المصنف على القرص كملف `.xlsx`.

يوضح الكود التالي الطريقة الكاملة.

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

    // قراءة ملف الصورة إلى مصفوفة بايتات
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // تحويل std::vector إلى Aspose::Cells::Vector باستخدام مُنشئ المؤشر+الحجم
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // تضمين الصورة مباشرة في الخلية
    cell.SetEmbeddedImage(imageData);

    // اختياريًا ضبط ارتفاع الصف وعرض العمود لجعل الصورة المضمنة أكثر وضوحًا
    worksheet.GetCells().SetColumnWidth(2, 30);   // العمود C (المؤشر 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // الصف 6 (المؤشر 5)

    // حفظ المصنف الناتج كملف .xlsx
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **اختيار الطريقة المناسبة**

تنتج كلتا الطريقتين صورة تتناسب داخل خلية واحدة، لكنهما تختلفان في كيفية تخزين الصورة وكيف تتصرف:

- **استخدم صورة عائمة (الطريقة 1) عندما:**
  - تحتاج إلى تحكم أدق في الموضع، أو الطبقات، أو المحاذاة مع كائنات الرسم الأخرى.
  - تريد أن تتصرف الصورة كشكل يمكن تحديده، أو إعادة ترتيبه، أو تجميعه مع أشكال أخرى.
  - تتطلب توافقًا قديمًا مع الكود الذي يعمل بالفعل مع `PictureCollection`.
  - تحتاج إلى حساب إحداثيات الإرساء ديناميكيًا بناءً على تخطيط ورقة العمل.

- **استخدم صورة مضمنة (الطريقة 2) عندما:**
  - تريد أبسط إدراج ممكن لصورة في خلية.
  - يجب أن تنتقل الصورة مع الخلية مثل أي محتوى خلية آخر.
  - لا تحتاج إلى معالجة الصورة كشكل.

{{% alert color="primary" %}}

يمكن أن تتعايش كلتا الطريقتين في نفس المصنف. يمكنك وضع صور عائمة فوق مجموعة واحدة من الخلايا وتضمين الصور مباشرة في خلايا أخرى، حيث تستخدم الآليتان طبقات تخزين مختلفة في الملف.

{{% /alert %}}

## **مقالات ذات صلة**

- [كيفية إدراج صورة في خلية](/cells/ar/cpp/how-to-place-image-to-cell/)
- [إضافة ارتباطات تشعبية للصور](/cells/ar/cpp/add-image-hyperlinks/)
- [تحميل صورة ويب من عنوان URL إلى ورقة عمل Excel](/cells/ar/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [معالجة موضع وحجم رسم المصمم](/cells/ar/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}