---
title: تحميل وإدارة ملفات إكسل، OpenOffice، Json، Csv، و Html باستخدام C++
linktitle: فتح الملفات
type: docs
weight: 20
url: /ar/cpp/loading-saving-and-managing/
description: مع Aspose.Cells for C++، من السهل إنشاء، فتح، وإدارة ملفات إكسل، CSV، TSV، ODS، HTML، Numbers، Json، XML، Pdf، Jpg، Tiff، صورة، Mht، و XPS.
---

{{% alert color="primary" %}}

مع Aspose.Cells for C++، من السهل إنشاء، فتح، وإدارة ملفات إكسل، على سبيل المثال، استرجاع البيانات أو استخدام قالب مصمم لتسريع عملية التطوير.

{{% /alert %}}

## **إنشاء مصنف جديد**
يُظهر المثال التالي إنشاء دفتر عمل جديد من الصفر.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    try
    {
        // Create a License object
        License license;

        // Set the license of Aspose.Cells to avoid the evaluation limitations
        license.SetLicense(srcDir + u"Aspose.Cells.lic");
    }
    catch (const std::exception& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    // Instantiate a Workbook object that represents Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Input the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **فتح وحفظ الملف**
مع Aspose.Cells for C++، من السهل فتح، حفظ، وإدارة ملفات إكسل.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"dest.xlsx";

    // Create a Workbook object and open an Excel file using its file path
    Workbook workbook1(inputFilePath);

    // Adding new sheet
    WorksheetCollection sheets = workbook1.GetWorksheets();
    Worksheet sheet = sheets.Add(u"MySheet");

    // Setting active sheet
    sheets.SetActiveSheetIndex(1);

    // Setting values
    Cells cells = sheet.GetCells();

    // Setting text
    cells.Get(u"A1").PutValue(u"Hello!");

    // Setting number
    cells.Get(u"A2").PutValue(1000);

    // Setting Date Time
    Cell cell = cells.Get(u"A3");
    Date currentDate;
    currentDate.year = 2023; // Replace with actual current year
    currentDate.month = 10;  // Replace with actual current month
    currentDate.day = 5;     // Replace with actual current day
    currentDate.hour = 12;   // Replace with actual current hour
    currentDate.minute = 30; // Replace with actual current minute
    currentDate.second = 0;  // Replace with actual current second
    cell.PutValue(currentDate);

    // Setting style for date
    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    // Setting formula
    cells.Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Saving the workbook to disk
    workbook1.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **الموضوعات المتقدمة**
- [طرق مختلفة لفتح الملفات](/cells/ar/cpp/different-ways-to-open-files/)
- [تصفية الأسماء المعرفة أثناء تحميل دفتر العمل](/cells/ar/cpp/filter-defined-names-while-loading-workbook/)
- [تصفية الكائنات أثناء تحميل دفتر العمل أو ورقة العمل](/cells/ar/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [تصفية نوع البيانات أثناء تحميل دفتر العمل من ملف قالب](/cells/ar/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [الحصول على تحذيرات أثناء تحميل ملف إكسل](/cells/ar/cpp/get-warnings-while-loading-excel-file/)
- [تحميل ملف Excel المصدر دون الرسوم البيانية](/cells/ar/cpp/load-source-excel-file-without-charts/)
- [تحميل الأوراق العمل المحددة في كتيب عمل](/cells/ar/cpp/load-specific-worksheets-in-a-workbook/)
- [تحميل دفتر العمل بحجم ورق طابعة محدد](/cells/ar/cpp/load-workbook-with-specified-printer-paper-size/)
- [فتح ملفات Microsoft Excel مختلفة الإصدارات](/cells/ar/cpp/opening-different-microsoft-excel-versions-files/)
- [فتح الملفات بتنسيقات مختلفة](/cells/ar/cpp/opening-files-with-different-formats/)
- [تحسين استهلاك الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات ضخمة](/cells/ar/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [قراءة جدول الأرقام الذي طورته شركة آبل باستخدام Aspose.Cells](/cells/ar/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [إيقاف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً](/cells/ar/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [استخدام واجهة برمجة التطبيقات LightCells](/cells/ar/cpp/using-lightcells-api/)
- [تحويل CSV إلى JSON](/cells/ar/cpp/convert-csv-to-json/)
- [تحويل إكسل إلى JSON](/cells/ar/cpp/convert-excel-to-json/)
- [تحويل JSON إلى CSV](/cells/ar/cpp/convert-json-to-csv/)
- [تحويل JSON إلى إكسل](/cells/ar/cpp/convert-json-to-excel/)
- [تحويل إكسل إلى Html](/cells/ar/cpp/convert-excel-to-html/)
