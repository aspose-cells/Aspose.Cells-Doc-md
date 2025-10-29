---
title: تصدير نطاق منطقة الطباعة إلى HTML باستخدام C++
linktitle: تصدير نطاق منطقة الطباعة إلى HTML
type: docs
weight: 60
url: /ar/cpp/export-print-area-range-to/
description: تعلم كيفية تصدير نطاق منطقة الطباعة إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

هذه حالة شائعة حيث نحتاج إلى تصدير فقط منطقة الطباعة، أي نطاق معين من الخلايا، بدلاً من الورقة بأكملها إلى HTML. تتوفر هذه الميزة حاليًا لتصنيع PDF، ومع ذلك، يمكنك الآن تنفيذ هذه المهمة لـ HTML أيضًا. أولاً، ضع منطقة الطباعة في كائن إعداد الصفحة لورقة العمل. لاحقًا، استخدم علم [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/) لتصدير النطاق المحدد فقط.

## **الكود المثالي**

يحمِّل رمز النموذج التالي مصنف عمل ثم يصدر منطقة الطباعة إلى HTML. يمكن تنزيل ملف الاختبار لهذه الميزة من الرابط التالي:

[sampleInlineCharts.xlsx](79527946.xlsx)

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
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
