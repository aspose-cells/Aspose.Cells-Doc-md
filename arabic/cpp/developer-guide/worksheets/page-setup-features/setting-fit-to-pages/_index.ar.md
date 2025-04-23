---
title: كيفية طباعة Excel كصفحات ملائمة للعرض والارتفاع باستخدام C++
linktitle: كيفية طباعة إكسل كصفحات مناسبة للعرض بشكل واسع ومرتفعة
type: docs
weight: 200
url: /ar/cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: تظهر لك هذه المقالة رمزًا يشرح كيفية تعيين FitToPagesWide و FitToPagesTall باستخدام مكتبة Aspose.Cells مع C++.
keywords: كيفيه تعيين FitToPagesWide و FitToPagesTall في C++، كيفية إضافة FitToPagesWide و FitToPagesTall في C++، كيفية تعيين FitToPagesWide و FitToPagesTall في Excel، كيفية مسح FitToPagesWide و FitToPagesTall في Excel، كيفيه طباعة Excel كصفحات مناسبة عريضا وطويلا، كيفيه طباعه ورقة عمل كصفحة واحدة، كيفيه طباعة جميع الأعمدة في ورقة العمل في صفحة واحدة.
---

## **مقدمة**

يتم استخدام إعدادات FitToPagesWide و FitToPagesTall في تطبيقات جداول البيانات (مثل مايكروسوفت إكسل) للتحكم في كيفية تكبير الجدول عند الطباعة. تساعد هذه الإعدادات على ضمان أن المخرجات المطبوعة تتوافق مع عدد معين من الصفحات، أفقياً وعمودياً. إليك شرح لكل إعداد:

1. FitToPagesWide: يحدد هذا الإعداد عدد الصفحات عرضه يجب أن تتناسب مع المخرجات المطبوعة. على سبيل المثال، ضبطه إلى 1 يعني أن المحتوى سيتم تكبيره ليتلاءم مع عرض صفحة واحدة بغض النظر عن عرض الجدول.
1. FitToPagesTall: يحدد هذا الإعداد عدد الصفحات ارتفاعاً يجب أن تتناسب معه المخرجات المطبوعة. على سبيل المثال، ضبطه إلى 1 يعني أن المحتوى سيتم تكبيره ليتناسب مع ارتفاع صفحة واحدة بغض النظر عن عدد الصفوف.

## **لماذا نستخدم FitToPagesWide و FitToPagesTall**
وفيما يلي بعض الأسباب لضبط هذا الإعداد:
1. التحكم في التنسيق المطبوع: من خلال تحديد عدد الصفحات عرضاً وارتفاعاً، يمكنك ضمان أن يكون المستند المطبوع سهل القراءة ومنظم بشكل جيد، دون تقسيم الأعمدة أو الصفوف بشكل غير مناسب عبر الصفحات.
1. الاتساق: إذا كنت تطبع عدة أوراق أو تقارير، فإن استخدام هذه الإعدادات يساعد على الحفاظ على تنسيق موحد، مما يسهل مقارنة وتحليل المستندات المطبوعة.
1. عرض احترافي: يمكن لضبط وتكيف المحتوى بشكل مناسب لعدد صفحات معين أن يؤدي إلى تقديم أكثر احترافية واناقة لبياناتك.

## **كيفية طباعة الملف كصفحات مناسبة عريضة وطويلة في Excel**

لتعيين إعدادات FitToPagesWide و FitToPagesTall في Microsoft Excel، اتبع الخطوات التالية:

1. افتح مصنف Excel الخاص بك وانتقل إلى الورقة التي تريد طباعةها.
1. انتقل إلى علامة التبويب تخطيط الصفحة على الشريط.
1. في مجموعة إعداد الصفحة، انقر على السهم الصغير في الزاوية اليمنى السفلى لفتح مربع حوار إعداد الصفحة.
1. في مربع حوار إعداد الصفحة، انتقل إلى علامة التبويب الصفحة.
1. تحت مقياس الحجم، اختر خيار "توافق" ثم حدد عدد الصفحات عريضة وطويلة التي تريدها: أدخل عدد الصفحات عريضة التي تريدها في المربع الأول (توافق مع x صفحات عريضة). أدخل عدد الصفحات طويلة التي تريدها في المربع الثاني (توافق مع y صفحات طويلة).
<br>
<img src="2.png" width=60% />

1. انقر على موافق لتطبيق الإعدادات.

## **كيفية طباعة Excel كصفحات مناسبة عريضة وطويلة باستخدام Aspose.Cells**

لتعيين FitToPagesWide و FitToPagesTall في ورقة عمل محددة: أولاً، حمّل [ملف العينة](input.xlsx)، ثم تحتاج إلى تعديل خصائص [**Worksheet.GetFitToPagesTall()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopagestall/) و [**Worksheet.GetFitToPagesWide()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopageswide/) لكائن [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) للورقة المطلوبة. إليك مثال في C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(U16String(u"input.xlsx"));

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Set the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Save the workbook
    workbook.Save(U16String(u"out_net.pdf"));

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

نتيجة الإخراج:
<br>
<img src="1.png" width=60% />

## **كيفية طباعة ورقة عمل كصفحة واحدة باستخدام Aspose.Cells**

لطباعة ورقة عمل كصفحة واحدة: أولاً، حمل [ملف العينة](sample.xlsx)، ثم تحتاج إلى تعيين الخاصية [**PdfSaveOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getonepagepersheet/) لكائن [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/). إليك مثال في C++:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions object
    PdfSaveOptions options;

    // Set options for exporting PDF
    options.SetOnePagePerSheet(true);

    // Save the workbook to a PDF file
    workbook.Save(u"OnePagePerSheet.pdf", options);

    std::cout << "Workbook saved as OnePagePerSheet.pdf!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

نتيجة الإخراج:
<br>
<img src="3.png" width=60% />

## **كيفية طباعة جميع الأعمدة في ورقة العمل في صفحة واحدة باستخدام Aspose.Cells**

لطباعة جميع أعمدة ورقة العمل في صفحة واحدة: أولاً، حمل [ملف العينة](sample.xlsx)، ثم تحتاج إلى تعيين الخاصية [**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getallcolumnsinonepagepersheet/) لكائن [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/). إليك مثال في C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object with the specified file.
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions instance.
    PdfSaveOptions options;

    // Set options for saving the workbook as a PDF.
    options.SetAllColumnsInOnePagePerSheet(true);

    // Save the workbook as a PDF file with the specified options.
    workbook.Save(u"AllColumnsInOnePagePerSheet.pdf", options);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

نتيجة الإخراج:
<br>
<img src="4.png" width=60% />
