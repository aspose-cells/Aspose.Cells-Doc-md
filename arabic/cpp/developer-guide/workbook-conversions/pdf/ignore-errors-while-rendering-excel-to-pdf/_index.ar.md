---
title: تجاهل الأخطاء أثناء عرض Excel كـ PDF باستخدام C++
linktitle: تجاهل الأخطاء أثناء تحويل Excel إلى PDF
type: docs
weight: 80
url: /ar/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: تعلم كيفية تجاهل الأخطاء أثناء تحويل Excel إلى PDF باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان عند تحويل ملف Excel إلى PDF، تحدث أخطاء أو استثناءات ويتم إنهاء عملية التحويل. يمكنك تجاهل جميع تلك الأخطاء أثناء عملية التحويل باستخدام خاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). بهذه الطريقة، ستتم عملية التحويل بسلاسة دون إلقاء أي خطأ أو استثناء ولكن قد يحدث فقدان للبيانات. لذلك، يرجى استخدام هذه الخاصية فقط إذا لم يكن فقدان البيانات حرجًا بالنسبة لك.

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**

الكود التالي يحمّل ملف إكسل العينة [ملف Excel النموذجي](55541778.xlsx)، لكنه يحتوي على أخطاء ويُظهر خطأ أثناء [التحويل إلى PDF](55541779.pdf) في إصدار 17.11 ولكن نظرًا لأننا نستخدم خاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)، فلن يتسبب ذلك في حدوث خطأ. ومع ذلك، يتم فقدان شكل سهم أحمر مستدير كما هو موضح في صورة الشاشة هذه.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
