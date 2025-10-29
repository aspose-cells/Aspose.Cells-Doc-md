---
title: ميزات إعداد الصفحة باستخدام C++
linktitle: ميزات إعداد الصفحة
type: docs
weight: 60
url: /ar/cpp/page-setup-features/
description: تعلم كيفية تكوين ميزات إعداد الصفحة في ملفات إكسل باستخدام Aspose.Cells مع C++.
---

## **ميزات إعداد الصفحة**

يوفر Aspose.Cells مجموعة شاملة من الميزات لتكوين خيارات إعداد الصفحة لملفات Excel. تتيح لك هذه الميزات التحكم في جوانب مختلفة من تخطيط الصفحة، مثل الهوامش، الاتجاه، حجم الورق، وأكثر.

### **تعيين هوامش الصفحة**

يمكنك تعيين هوامش الصفحة لورقة العمل باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين الهوامش العلوية والسفلية واليسرى واليمنى:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **تعيين اتجاه الصفحة**

يمكنك ضبط اتجاه الصفحة إما إلى الرأس أو العرض باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين اتجاه الصفحة إلى العرض:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **تعيين حجم الورق**

يمكنك تعيين حجم الورق للطباعة باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية ضبط حجم الورق إلى A4:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **تعيين منطقة الطباعة**

يمكنك تحديد نطاق معين من الخلايا ليتم طباعته باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين منطقة الطباعة:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **تعيين فواصل الصفحات**

يمكنك إدراج فواصل صفحات في ورقة العمل للتحكم في مكان نهاية الصفحات وبدء صفحات جديدة. يوضح المثال التالي كيفية إدراج فاصل صفحة أفقي:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **تعيين رأس وتذييل الصفحة**

يمكنك تخصيص رأس وتذييل صفحة ورقة العمل باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين رأس وتذييل مخصصين:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **تعيين عناوين الطباعة**

يمكنك تحديد صفوف أو أعمدة لتكرارها في أعلى أو يسار كل صفحة مطبوعة باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين عناوين الطباعة:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **تعيين جودة الطباعة**

يمكنك ضبط جودة الطباعة لورقة العمل باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية ضبط جودة الطباعة:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **تعيين ترتيب الطباعة**

يمكنك ضبط ترتيب الطباعة لورقة العمل باستخدام فئة `PageSetup`. يوضح المثال التالي كيف يتم ضبط ترتيب الطباعة على "الطابعة فوق، ثم للأسفل":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **تعيين خطوط الشبكة للطباعة**

يمكنك التحكم فيما إذا كانت خطوط الشبكة ستطبع باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تفعيل طباعة خطوط الشبكة:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **تعيين رؤوس الصفحات**

يمكنك التحكم فيما إذا كانت رؤوس الصفوف والأعمدة ستطبع باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تفعيل طباعة الرؤوس:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **تعيين الطباعة بالأبيض والأسود**

يمكنك التحكم فيما إذا كانت ورقة العمل ستطبع بالأبيض والأسود باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تفعيل الطباعة بالأبيض والأسود:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### **تعيين وضع الطباعة للمسودة**

يمكنك التحكم فيما إذا كانت ورقة العمل ستطبع بجودة مسودة باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تفعيل طباعة بجودة المسودة:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **تعيين تعليقات الطباعة**

يمكنك التحكم فيما إذا كانت التعليقات ستطبع باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تفعيل طباعة التعليقات:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **تعيين أخطاء الطباعة**

يمكنك التحكم في كيفية طباعة الأخطاء باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين خيار طباعة الأخطاء:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **تعيين ملائمة منطقة الطباعة للصفحات**

يمكنك التحكم فيما إذا تم تكبير منطقة الطباعة لتناسب عددًا معينًا من الصفحات باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين منطقة الطباعة لتناسب صفحة واحدة عرضًا وواحدة طولاً:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **تعيين مقياس الطباعة**

يمكنك تعيين مقياس الطباعة لورقة العمل باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين مقياس الطباعة إلى 50%:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **تعيين مركز الطباعة أفقيًا وعموديًا**

يمكنك التحكم فيما إذا كانت ورقة العمل متمركزه أفقيًا وعموديًا على الصفحة المطبوعة باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية موازنة ورقة العمل أفقيًا وعموديًا:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **تعيين رقم الصفحة الأولى للطباعة**

يمكنك تعيين رقم الصفحة الأولى للطباعة باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تعيين رقم الصفحة الأولى:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **تعيين رقم صفحة الطباعة**

يمكنك التحكم فيما إذا كان رقم الصفحة يُطبع باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية تفعيل طباعة رقم الصفحة:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **تعيين ترتيب صفحات الطباعة**

يمكنك تعيين ترتيب الصفحات التي يتم طباعتها باستخدام فئة `PageSetup`. يوضح المثال التالي كيفية ضبط ترتيب الصفحات ليكون "أسفل، ثم عبر":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
{{< app/cells/assistant language="cpp" >}}
