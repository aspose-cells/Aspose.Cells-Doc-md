---
title: تحديد فواصل الأرقام العشرية والمجمعة المخصصة لمفكرة العمل باستخدام C++
linktitle: تحديد فواصل الأرقام العشرية والمجمعة المخصصة
type: docs
weight: 110
url: /ar/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: تغيير فاصل الأرقام العشرية وفاصل التجميع في MS Excel وباستخدام كود C++ بواسطة واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: تحديد فاصل عشري مخصص في إكسل، تحديد فاصل عشري مخصص في إكسل باستخدام C++، تحديد فاصل تجمع مخصص في إكسل، تحديد فاصل تجمع مخصص في إكسل باستخدام C++، تحديد فاصل عشري وتجمع مخصص في إكسل، تغيير الفاصل العشري وفاصل التجميع في إكسل، تغيير فاصل عشري في إكسل، تغيير فاصل تجمع في إكسل، تغيير فاصل التجميع في إكسل باستخدام C++
---

{{% alert color="primary" %}}

يمكنك في Microsoft Excel تحديد الفاصل العشري المخصص وفاصل الآلاف بدلاً من استخدام الفواصل النظامية من **خيارات Excel المتقدمة** كما هو موضح في اللقطة أدناه.

توفر Aspose.Cells خصائص [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/) و[**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) لتعيين الفواصل المخصصة لتنسيق/تحليل الأرقام.

{{% /alert %}}

## **تحديد الفواصل المخصصة باستخدام Microsoft Excel**

تُظهر اللقطة الشاشية التالية **خيارات Excel المتقدمة** وتبرز القسم الخاص بتحديد **الفواصل المخصصة**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **تحديد الفواصل المخصصة باستخدام Aspose.Cells**

يوضح الكود العينة التالي كيفية تحديد الفواصل المخصصة باستخدام واجهة برمجة التطبيقات Aspose.Cells. يحدد فاصل العدد المخصص وفاصل المجموعة المخصصين على أنهما نقطة ومسافة على التوالي.

### كود C++ لتحديد فواصل الأرقام العشرية والمجمعة المخصصة

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

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
