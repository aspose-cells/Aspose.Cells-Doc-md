---
title: إعداد خيارات الطباعة باستخدام C++
linktitle: ضبط خيارات الطباعة
type: docs
weight: 40
url: /ar/cpp/setting-print-options/
description: توضح هذه المقالة كيفية ضبط خيارات طباعة ورقة العمل في Excel برمجيًا باستخدام واجهة برمجة التطبيقات والمكتبة الخاصة بـ C++. يمكنك تحديد منطقة الطباعة، عناوين الطباعة، وترتيب الصفحة.
keywords: تعيين منطقة الطباعة في Excel، تعيين عناوين الطباعة في Excel، تعيين ترتيب الصفحة في Excel باستخدام C++
---

{{% alert color="primary" %}}

توفر إعدادات تهيئة الصفحة في ميكروسوفت إكسيل العديد من خيارات الطباعة التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورق العمل.

{{% /alert %}}

## **ضبط خيارات الطباعة**

تسمح هذه الخيارات بالطباعة:

- تحديد منطقة طباعة معينة على ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف/الأعمدة.
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.

يدعم Aspose.Cells جميع خيارات الطباعة التي تقدمها Microsoft Excel، ويمكن للمطورين تكوين هذه الخيارات بسهولة لورقات العمل باستخدام الخصائص التي تقدمها فئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). تتم مناقشة كيفية استخدام هذه الخصائص بالتفصيل أدناه.

### **تعيين منطقة الطباعة**

اف فعل، منطقة الطباعة تشمل جميع مناطق ورقة العمل التي تحتوي على بيانات. يمكن للمطورين تحديد منطقة الطباعة المحددة لورقة العمل.

لتحديد منطقة الطباعة المحددة، استخدم خاصية [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) لفئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). قم بتعيين نطاق الخلايا الذي يعرف منطقة الطباعة لهذه الخاصية.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **تحديد عناوين الطباعة**

تسمح Aspose.Cells لك بتحديد عناوين الصف والعمود لتكرارها على جميع الصفحات لورقة العمل المطبوعة. للقيام بذلك، استخدم خاصية [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) و [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) لفئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/).

يتم تعريف الصفوف أو الأعمدة التي ستتكرر عن طريق تمرير أرقامها. على سبيل المثال، يتم تعريف الصفوف كـ $1:$2 والأعمدة كـ $A:$B.

```c++
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **تحديد خيارات الطباعة الأخرى**

فئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) توفر أيضا عدة خصائص أخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/): خاصية من نوع Boolean تحدد ما إذا كان سيتم طباعة الشبكة أم لا.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/): خاصية بوليانية تعرف ما إذا كان سيتم طباعة عناوين الصف والعمود أم لا.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/): خاصية بوليانية تعرف ما إذا كان سيتم طباعة ورقة العمل في وضع أسود وأبيض أم لا.
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/): يحدد ما إذا كان سيتم عرض التعليقات المطبوعة على ورقة العمل أم في نهايتها.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/): خاصية من نوع Boolean تحدد ما إذا كان سيتم طباعة الورقة بدون رسومات.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/): يحدد ما إذا كان سيتم طباعة أخطاء الخلايا كما هو موضح، فارغة، إشارة، أو N/A.

لضبط الخاصيتين [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) و[**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/)، يوفر Aspose.Cells أيضًا اثنين من التعدادات، [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) و[**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) التي تحتوي على قيم محددة مسبقًا ليتم تعيينها على الخصائص [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) و[**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) على التوالي.

تتم إدراج القيم المحددة مسبقًا في تعداد [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) أدناه مع وصفها.

|**أنواع التعليقات المطبوعة**|**الوصف**|
| :- | :- |
|PrintInPlace|تحدد طباعة التعليقات كما هي معروضة على ورقة العمل.|
|PrintNoComments|تحدد عدم طباعة التعليقات.|
|PrintSheetEnd|تحدد طباعة التعليقات في نهاية ورقة العمل.|

تم إدراج القيم المحددة مسبقًا لتعداد [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) أدناه مع وصفها.

| **أنواع أخطاء الطباعة** | **الوصف** |
| :- | :- |
|PrintErrorsBlank|يحدد عدم طباعة الأخطاء.
|PrintErrorsDash|يحدد طباعة الأخطاء على شكل "--".
|PrintErrorsDisplayed|يحدد طباعة الأخطاء على النحو الذي يتم عرضه.
|PrintErrorsNA|يحدد طباعة الأخطاء على شكل "#N/A".

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **تحديد ترتيب الصفحة**

توفر صفيف [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) خاصية [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) التي تستخدم لترتيب صفحات ورق العمل المتعددة المطبوعة. هناك احتمالان لترتيب الصفحات على النحو التالي.

- **اسفل ثم يمين:** يطبع جميع الصفحات أسفل الصفحة قبل طباعة أي صفحات على اليمين.
- **يمين ثم أسفل:** يطبع الصفحات من اليسار إلى اليمين قبل طباعة الصفحات أسفلها.

يوفّر Aspose.Cells تعدادًا، [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/)، يحتوي على جميع أنواع ترتيب محدد مسبقًا.

يتم سرد القيم المحددة مسبقًا لتعداد [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) أدناه.

| **أنواع ترتيب الطباعة** | **الوصف** |
| :- | :- |
|DownThenOver|يمثل ترتيب الطباعة كاسفل ثم يمين.
|OverThenDown|يمثل ترتيب الطباعة كيمين ثم أسفل.

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
