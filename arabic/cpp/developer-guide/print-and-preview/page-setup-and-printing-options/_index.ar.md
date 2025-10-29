---
title: إعداد الصفحة وخيارات الطباعة باستخدام C++
linktitle: إعدادات الصفحة وخيارات الطباعة
type: docs
weight: 60
url: /ar/cpp/page-setup-and-printing-options/
description: قم بتكوين إعداد الصفحة وإعدادات الطباعة للتحكم في عملية الطباعة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المطورون إلى تكوين إعدادات الصفحة وخيارات الطباعة للتحكم في عملية الطباعة. تقدم إعدادات الصفحة وخيارات الطباعة خيارات متنوعة ومعتمدة بشكل كامل في Aspose.Cells.

يستعرض هذا المقال كيفية إنشاء تطبيق سطر أوامر في Visual Studio، وتطبيق إعدادات الصفحة وخيارات الطباعة على ورقة عمل ببضع سطور برمجية بسيطة باستخدام API الخاص بـ Aspose.Cells.

{{% /alert %}}

## **العمل مع إعدادات الصفحة والطباعة**

لهذا المثال، أنشأنا سجل عمل في Microsoft Excel واستخدمنا Aspose.Cells لضبط إعدادات الصفحة وخيارات الطباعة.

### **استخدام Aspose.Cells لضبط خيارات إعداد الصفحة**

ابدأ أولا بإنشاء ورقة عمل بسيطة في Microsoft Excel. ثم قم بتطبيق خيارات إعداد الصفحة عليها. سيقوم تنفيذ الكود بتغيير خيارات إعداد الصفحة كما هو موضح في صورة الشاشة أدناه.

|**ملف الإخراج.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. إنشاء ورقة عمل ببعض البيانات في Microsoft Excel:
   1. افتح برنامج Excel الجديد في Microsoft Excel.
   1. أضف بعض البيانات.
1. ضبط خيارات إعداد الصفحة:
   قم بتطبيق خيارات إعداد الصفحة على الملف. وفيما يلي صورة للخيارات الافتراضية، قبل تطبيق الخيارات الجديدة.

|**خيارات إعداد الصفحة الافتراضية.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تحميل](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.
      جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.
1. أنشئ مشروعًا:
   1. بدء Visual Studio.
   1. أنشئ تطبيقًا جديدًا على الكونسول.
      سيعرض هذا المثال تطبيق سطر أوامر بـ C++.
1. أضف مراجع:
   1. يستخدم هذا المثال Aspose.Cells لذا أضف مرجعًا إلى تلك المكونة للمشروع. على سبيل المثال:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. اكتب التطبيق الذي يستدعي واجهة برمجة التطبيق:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ضبط خيارات الطباعة**

إعدادات إعداد الصفحة توفر أيضًا العديد من خيارات الطباعة (المسمى أيضًا خيارات الورقة) التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورق العمل. تسمح للمستخدمين ب:

- تحديد منطقة طباعة معينة من ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف/الأعمدة.
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.

المثال التالي يطبق خيارات الطباعة على الملف الذي تم إنشاؤه في المثال أعلاه (PageSetup.xls). يظهر اللقطة الشاشية أدناه الخيارات الافتراضية للطباعة قبل تطبيق الخيارات الجديدة.

|**مستند الإدخال**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
تغيير خيارات الطباعة ينفذ الشيفرة.

|**ملف الإخراج**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
