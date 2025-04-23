---
title: إعادة الت sampling للصور المضافة  تحويل Excel إلى PDF باستخدام C++
linktitle: إعادة عينات الصور المضافة  تحويل Excel إلى PDF
type: docs
weight: 150
url: /ar/cpp/resampling-added-images-excel-to-pdf-conversion/
description: تعلم كيفية إعادة sampling للصور المضافة لتقليل حجم PDF باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

أثناء العمل مع ملفات Microsoft Excel الكبيرة مع الكثير من الصور، قد تحتاج إلى ضغط الصور التي تمت إضافتها لتقليل حجم ملف PDF الناتج وتحسين أداء التحويل الكلي. Aspose.Cells تدعم إعادة عينات الصور المضافة لتقليل حجم ملف PDF الناتج وتحسين الأداء بشكل ملحوظ.

{{% /alert %}}

يرجى الاطلاع على الكود النموذجي التالي الذي يصف كيفية إجراء المهمة باستخدام واجهة برمجة التطبيقات Aspose.Cells. النموذج يحول ملف Microsoft Excel إلى ملف PDF مع ضغط الصور في الملف.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputPath = srcDir + u"input.xlsx";
    Workbook workbook(inputPath);

    // Instantiate the PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set Image Resample properties
    pdfSaveOptions.SetImageResample(300, 70);

    // Save the PDF file
    U16String outputPath = outDir + u"OutputFile_out_pdf.pdf";
    workbook.Save(outputPath, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

باستخدام الخيار [**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/) يُقلل من حجم ملف PDF الناتج ولكن قد يؤثر ذلك قليلاً على جودة الصورة.

{{% /alert %}} 

{{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}

