---
title: تحديد عدد الصفحات التي تم إنشاؤها  تحويل Excel إلى PDF باستخدام C++
linktitle: تحديد عدد الصفحات التي تم إنشاؤها
type: docs
weight: 180
url: /ar/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: تعلم كيفية تحديد عدد الصفحات التي يتم إنشاؤها عند تحويل Excel إلى PDF باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، ترغب في طباعة مجموعة من الصفحات إلى ملف PDF الناتج. تحتوي Aspose.Cells على القدرة على تحديد الحد الأقصى لعدد الصفحات التي يتم توليدها عند تحويل جدول بيانات Excel إلى صيغة ملف PDF.

{{% /alert %}}

## **تحديد الحد الأقصى لعدد الصفحات المولدة**

المثال التالي يظهر كيفية عرض مجموعة من الصفحات (3 و 4) في ملف Microsoft Excel إلى صيغة PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"TestBook.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Instantiate the PdfSaveOption
    PdfSaveOptions options;

    // Print only Page 3 and Page 4 in the output PDF
    // Starting page index (0-based index)
    options.SetPageIndex(3);
    // Number of pages to be printed
    options.SetPageCount(2);

    // Path of output PDF file
    U16String outputFilePath = srcDir + u"outPDF1.out.pdf";

    // Save the PDF file
    wb.Save(outputFilePath, options);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

إذا كان جدول البيانات يحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) قبل عرضه إلى صيغة PDF. القيام بذلك يضمن إعادة حساب القيم التي تعتمد على الصيغ، وتقديم القيم الصحيحة في ملف الإخراج.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
