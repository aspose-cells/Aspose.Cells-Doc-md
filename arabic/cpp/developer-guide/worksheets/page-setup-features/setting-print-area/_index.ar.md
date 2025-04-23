---
title: كيفية تعيين منطقة الطباعة باستخدام C++
linktitle: كيفية تعيين منطقة الطباعة
type: docs
weight: 200
url: /ar/cpp/how-to-set-print-area/
description: تظهر لك هذه المقالة رمزًا يشرح كيفية تعيين منطقة الطباعة باستخدام مكتبة Aspose.Cells مع C++.
keywords: تحديد نطاق الطباعة، إعداد نطاق الطباعة، مسح نطاق الطباعة، تعيين ومسح نطاق الطباعة باستخدام C++، كيفية تعيين منطقة الطباعة في C++، إعداد ومسح منطقة الطباعة باستخدام C++، كيفية مسح منطقة الطباعة في C++، كيفية إضافة منطقة طباعة باستخدام C++، كيفية إزالة منطقة الطباعة باستخدام C++، كيفية تعيين منطقة الطباعة في Excel، كيفية مسح منطقة الطباعة في Excel.
---

## **سيناريوهات الاستخدام المحتملة**

تساعدك إعداد منطقة الطباعة في مستند، مثل جدول بيانات Excel، على التحكم في المحتوى الذي يتم تضمينه عند الطباعة. إليك بعض الأسباب لتعيين منطقة طباعة:

1. التركيز على البيانات المحددة: يمكنك طباعة الأقسام الأكثر أهمية فقط، وتجنب المحتوى غير الضروري.
1. تحسين التنسيق: يساعد في تنظيم وتناسب المحتوى بشكل مرتب على الصفحات المطبوعة، وتجنب الانقسامات أو فواصل الصفحات غير المرغوب فيها.
1. توفير الموارد: من خلال تحديد منطقة الطباعة، يمكنك تقليل كمية الورق والحبر المستخدمين.
1. العرض الاحترافي: يضمن أن البيانات المطبوعة تكون مصقولة ونهائية، وهو أمر مهم بشكل خاص للتقارير أو العروض التقديمية.
1. الاتساق: عند طباعة نفس المستند مرات متعددة، فإن وجود منطقة طباعة محددة يضمن الاتساق في المخرجات.

<br>
يعد تعيين منطقة الطباعة مفيدًا بشكل خاص في المستندات الكبيرة حيث يحتاج جزء فقط للمشاركة أو المراجعة بشكل مطبوع.

## **كيفية تعيين منطقة الطباعة في Excel**

لتعيين منطقة طباعة في Excel، اتبع الخطوات التالية:

1. تحديد الخلايا: انقر السحب لتحديد نطاق الخلايا الذي تريد تعيينه كمنطقة طباعة.
1. فتح علامة التبويب تخطيط الصفحة: انتقل إلى علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة Excel.
1. تعيين منطقة الطباعة: في مجموعة "إعداد الصفحة"، انقر على "منطقة الطباعة". من القائمة المنسدلة، اختر "تعيين منطقة الطباعة".
<br>
<img src="3.png" width=60% />

1. إضافة إلى منطقة الطباعة: إذا كنت تريد إضافة خلايا إضافية إلى منطقة الطباعة الحالية، حدد الخلايا الإضافية، وانتقل إلى "منطقة الطباعة" في علامة التبويب "تخطيط الصفحة"، واختر "إضافة إلى منطقة الطباعة".

<br>
سيعرف هذا الإجراء الخلايا المحددة كمجال للطباعة. عند طباعة ورقة العمل، سيتم طباعة هذا المجال المحدد فقط.

## **كيفية مسح مجال الطباعة في إكسل**

لمسح مجال الطباعة في إكسل، اتبع الخطوات التالية:

1. افتح علامة تبويب تخطيط الصفحة: انقر على علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة إكسل.
1. مسح مجال الطباعة: في مجموعة "إعداد الصفحة"، انقر على "مجال الطباعة". من القائمة المنسدلة، حدد "مسح مجال الطباعة".
<br>
<img src="4.png" width=60% />

<br>
سيؤدي هذا الإجراء إلى إزالة أي مجال طباعة تم تحديده مسبقًا، مما يسمح لطباعة كامل ورقة العمل.

## **ماذا يحدث بعد مسح مجال الطباعة**

مسح مجال الطباعة في تطبيق جدول بيانات مثل إكسل باستخدام Aspose.Cells سيؤدي إلى تضمين كامل ورقة العمل عند طباعة المستند. إذا تم تعيين مجال طباعة، فسيتم طباعة النطاق المحدد فقط من الخلايا. بمسح مجال الطباعة، تضمن عدم تحديد نطاق معين وسيتحقق سلوك الطباعة الافتراضي، الذي يتضمن كامل الورقة.

1. السلوك الافتراضي للطباعة: ستعتبر كامل ورقة العمل للطباعة. هذا يعني أن جميع الخلايا ذات البيانات أو التنسيق ستُطبع.
1. لا حدود لمجال الطباعة: ستتم إزالة الحدود المحددة سابقًا لمجال الطباعة. إذا كانت هناك صفوف وأعمدة معينة مخصصة للطباعة، فلن تكون مقيدة بتلك الحدود.
1. طباعة المحتوى الكامل: سيتم تضمين كافة المحتويات، بما في ذلك العناوين، والتذييلات، وأي بيانات أخرى داخل ورقة العمل، في عملية الطباعة.

## **كيفية ضبط مجال الطباعة باستخدام Aspose.Cells**

لضبط مجال الطباعة في ورقة عمل محددة: أولاً، قم بتحميل [الملف النموذجي](input.xlsx)، ثم عليك تعديل خاصية [**Worksheet.GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) من كائن [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) لورقة العمل المرغوبة. إعداد هذه الخاصية إلى سلسلة نطاق سيُحدد مجال الطباعة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath(u"input.xlsx");
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Set the print area - specify the range you want to print
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea(u"A1:D10");

    // Save the workbook
    U16String outputFilePath(u"set_print_area.pdf");
    workbook.Save(outputFilePath);

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

نتيجة الإخراج:
<br>
<img src="1.png" width=60% />

## **كيفية مسح مجال الطباعة باستخدام Aspose.Cells**

لمسح مجال الطباعة في ورقة عمل محددة: أولاً، قم بتحميل [الملف النموذجي](input.xlsx)، ثم عليك تعديل خاصية [**Worksheet.GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) من كائن [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) لورقة العمل المرغوبة. تعيين هذه الخاصية إلى سلسلة فارغة سيمسح مجال الطباعة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath(u"input.xlsx");
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea(u"");

    // Save the workbook
    U16String outputFilePath(u"clear_print_area.pdf");
    workbook.Save(outputFilePath);

    std::cout << "Print area cleared and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

نتيجة الإخراج:
<br>
<img src="2.png" width=60% />
