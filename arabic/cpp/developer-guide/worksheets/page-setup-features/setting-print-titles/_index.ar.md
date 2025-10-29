---
title: كيفية تعيين عناوين الطباعة باستخدام C++
linktitle: كيفية ضبط عناوين الطباعة
type: docs
weight: 200
url: /ar/cpp/how-to-set-print-titles/
description: توضح لك هذه المقالة رمز برمجي يشرح كيفية تعيين عناوين الطباعة باستخدام مكتبة Aspose.Cells مع C++.
keywords: طباعة الصفوف والأعمدة بشكل متكرر، كيفية تعيين عناوين الطباعة في C++، تعيين ومسح عناوين الطباعة، مسح عناوين الطباعة في C++، إضافة عناوين الطباعة، إزالة عناوين الطباعة، كيفية تعيين عناوين الطباعة في Excel، مسح عناوين الطباعة في Excel.
---

## **سيناريوهات الاستخدام المحتملة**

ضبط عناوين الطباعة في إكسل يضمن تكرار صفوف أو أعمدة معينة في كل صفحة مطبوعة، وهو مفيد بشكل خاص للجداول الكبيرة التي تمتد عبر صفحات متعددة. إليك بعض الأسباب التي قد تدفعك لضبط عناوين الطباعة:

1. تحسين قابلية القراءة: تساعد عناوين الطباعة القراء على فهم البيانات من خلال إبقاء العناوين مرئية على جميع الصفحات، مما يجعل من الأسهل تفسير المعلومات على كل صفحة دون الحاجة للرجوع إلى الصفحة الأولى.

1. تقديم مظهر احترافي: عرض العناوين أو التسميات بشكل متكرر على كل صفحة يخلق مظهرًا أكثر أناقة واحترافية للمستندات المطبوعة.

1. تحسين التنقل: بالنسبة للمستندات التي تحتوي على بيانات موسعة، يساعد تكرار العناوين في كل صفحة على التنقل بسرعة والوصول إلى المعلومات، ويقلل من الحاجة للرجوع بين الصفحات.

1. تقليل الأخطاء: عندما تكون العناوين موجودة على كل صفحة، يقل احتمال سوء التفسير أو أخطاء الإدخال، حيث يمكن للمستخدمين رؤية سياق البيانات بسهولة.

1. التناسق: ضمان أن المعلومات المهمة، مثل عناوين الأعمدة أو تسميات الصفوف، دائمًا مرئية يحافظ على التناسق والوضوح Throughout المستند.

## **كيفية ضبط عناوين الطباعة في إكسل**

 لضبط عناوين الطباعة في إكسل، اتبع الخطوات التالية:

1. افتح علامة تبويب تخطيط الصفحة: انقر على علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة إكسل.
1. الوصول إلى عناوين الطباعة: في مجموعة "إعداد الصفحة"، انقر على "عناوين الطباعة".
1. تعيين الصفوف للتكرار: في مربع حوار "إعداد الصفحة"، انتقل إلى علامة التبويب "ورقة». في قسم "عناوين الطباعة"، حدد الصفوف التي تريد تكرارها في الأعلى بالنقر على المربع بجانب "تكرار الصفوف في أعلى" واختيار الصفوف التي تريد تكرارها.
1. تعيين الأعمدة للتكرار (إن لزم الأمر): بالمثل، يمكنك تحديد الأعمدة للتكرار على اليسار عن طريق النقر على المربع بجانب "تكرار الأعمدة على اليسار" واختيار الأعمدة التي تريد تكرارها.
<br>
<img src="3.png" width=60% />

1. أكد والطباعة: انقر على "موافق" لتطبيق الإعدادات. عند طباعة ورقة العمل، ستظهر الصفوف أو الأعمدة المحددة على كل صفحة مطبوعة.

## **كيفية مسح عناوين الطباعة في إكسل**

لمسح عناوين الطباعة في إكسل، تحتاج إلى إزالة الصفوف أو الأعمدة التي تم تعيينها للتكرار على كل صفحة مطبوعة. إليك الطريقة:

1. افتح علامة تبويب تخطيط الصفحة: انقر على علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة إكسل.
1. الوصول إلى عناوين الطباعة: في مجموعة "إعداد الصفحة"، انقر على "عناوين الطباعة".
1. مسح عناوين الطباعة: في مربع حوار "إعداد الصفحة"، انتقل إلى علامة التبويب "ورقة". امسح مربعات النص لـ "الصفوف لإعادة التكرار في الأعلى" و"الأعمدة لإعادة التكرار على اليسار" عن طريق حذف أي محتوى داخلها.
<br>
<img src="4.png" width=60% />

1. أكد وأغلق: انقر على "موافق" لتطبيق التغييرات.

## **كيفية تعيين عناوين الطباعة باستخدام Aspose.Cells**

لتعيين عناوين الطباعة في ورقة عمل محددة: أولاً، قم بتحميل [ملف العينة](input.xlsx)، ثم تحتاج إلى تعديل خصائص [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) و [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) من كائن [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) للورقة المرغوبة. تعيين هذه الخصائص إلى سلسلة نطاق سيحدد عناوين الطباعة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook workbook(u"input.xlsx");

    // Access the desired worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set rows to repeat at the top (e.g., rows 1 and 2)
    worksheet.GetPageSetup().SetPrintTitleRows(u"$1:$2");

    // Set columns to repeat at the left (e.g., columns A and B)
    worksheet.GetPageSetup().SetPrintTitleColumns(u"$A:$B");

    // Save the workbook
    workbook.Save(u"set_print_titles.pdf");

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

نتيجة الإخراج:
<br>
<img src="1.png" width=60% />

## **لمسح عناوين الطباعة باستخدام Aspose.Cells**

لمسح عناوين الطباعة في ورقة عمل محددة: أولاً، قم بتحميل [ملف العينة](input.xlsx)، ثم تحتاج إلى تعديل خصائص [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) و [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) من كائن [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) للورقة المرغوبة. تعيين هذه الخصائص إلى سلسلة فارغة سيمسح عناوين الطباعة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath = u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the rows and columns set to repeat
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows(u"");
    pageSetup.SetPrintTitleColumns(u"");

    // Save the workbook
    U16String outputFilePath = u"clear_print_titles.pdf";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();
}
```

نتيجة الإخراج:
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
