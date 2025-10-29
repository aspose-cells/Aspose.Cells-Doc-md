---
title: تصدير تنسيق CSS الخاص بورقة العمل بشكل منفصل في HTML الإخراجي باستخدام C++
linktitle: تصدير ورقة العمل CSS بشكل منفصل في ملف HTML الناتج
type: docs
weight: 80
url: /ar/cpp/export-worksheet-css-separately-in-output/
description: تعلم كيفية تصدير CSS ورقة العمل بشكل منفصل عند تحويل ملفات إكسل إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يقدم Aspose.Cells ميزة تصدير CSS ورقة العمل بشكل منفصل عند تحويل ملف إكسل إلى HTML. يرجى استخدام الخاصية [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/) لهذا الغرض وتعيينها إلى **صحيح** أثناء حفظ ملف إكسل إلى تنسيق HTML.

## **تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج**

يقوم الكود العيني التالي بإنشاء ملف Excel، وإضافة نص في الخلية **B5** بلون **أحمر** ثم يحفظه بتنسيق HTML باستخدام خاصية [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/). يُرجى رؤية [HTML الناتج](60489766.zip) الذي تم إنشاؤه من الكود للإطلاع. ستجد ملفًا بعنوان **stylesheet.css** داخله كنتيجة للكود العيني.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تصدير مصنف يحتوي على ورقة واحدة إلى HTML**

عندما يتم تحويل مصنف يحتوي على عدة أوراق إلى HTML باستخدام Aspose.Cells، يتم إنشاء ملف HTML بالإضافة إلى مجلد يحتوي على ملفات CSS وملفات HTML متعددة. عند فتح هذا الملف في المتصفح، تكون علامات التبويب مرئية. نفس السلوك مطلوب لمصنف يحتوي على ورقة عمل واحدة عند تحويله إلى HTML. سابقًا، لم يتم إنشاء مجلد منفصل لمصنفات الورق الواحد، وتم إنشاء ملف HTML فقط. هذا الملف لا يُظهر علامة تبويب عند فتحه في المتصفح. ينشئ MS Excel مجلد وHTML مناسبين للورقة الواحدة أيضًا، ولذلك تم تنفيذ نفس السلوك باستخدام واجهات برمجة تطبيقات Aspose.Cells. يمكن تنزيل ملف النموذج من الرابط التالي للاستخدام في الكود النموذجي أدناه:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **الكود المثالي**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
