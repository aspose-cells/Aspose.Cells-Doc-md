---
title: عرض النقاط بواسطة تعيين قيمة الخلية باستخدام HTML مع C++
linktitle: عرض الرموز باستخدام قيمة الخلية باستخدام HTML
type: docs
weight: 130
url: /ar/cpp/display-bullets-by-setting-cell-value-using/
description: إضافة النقاط إلى خلايا Excel باستخدام HTML و API سهل الاستخدام Aspose.Cells for C++.
keywords: إضافة نقاط في إكسل، إضافة نقاط في إكسل C++، عرض النقاط في إكسل، عرض النقاط في إكسل C++، إضافة نقاط باستخدام HTML، إضافة نقاط باستخدام HTML C++، عرض النقاط باستخدام HTML، عرض النقاط باستخدام HTML C++، عرض النقاط باستخدام HTML، إضافة نقاط في إكسل باستخدام HTML
---

{{% alert color="primary" %}}

تدعم Aspose.Cells عرض رموز النقاط بكود HTML. سيشرح هذا المقال كيفية عرض الرموز النقاط عن طريق تعيين قيمة الخلية باستخدام HTML. سنستخدم خاصية [**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) لتعيين قيمة الخلية بكود HTML.

{{% /alert %}}

## كود C++ لعرض النقاط بواسطة تعيين قيمة الخلية باستخدام HTML

يستخدم الكود التالي كود HTML لتعيين قيمة الخلية. بمجرد تشغيل هذا الكود، ستحصل على الإخراج كما هو موضح في الصورة أدناه.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## الإخراج الذي تم توليده بواسطة رمز العينة

تُظهر اللقطة الشاشية التالية الإخراج الناتج من الكود المثالي السابق.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
