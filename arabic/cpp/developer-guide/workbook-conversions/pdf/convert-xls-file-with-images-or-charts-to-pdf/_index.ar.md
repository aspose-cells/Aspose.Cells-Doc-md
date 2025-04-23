---
title: تحويل ملف XLS مع الصور أو المخططات إلى PDF باستخدام C++
linktitle: تحويل ملف XLS الذي يحتوي على صور أو رسومات إلى PDF
type: docs
weight: 50
url: /ar/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: تحويل ملفات XLS التي تحتوي على صور أو مخططات إلى مستندات PDF باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}} 

 يدعم Aspose.Cells تحويل ملفات XLS التي تحتوي على صور ومخططات إلى مستندات PDF. يمكن لـ Aspose.Cells for C++ العمل بشكل مستقل لتحويل جدول البيانات إلى PDF: لا يتطلب Aspose.PDF لـ C++ للتحويل. يمكن إتمام العملية في الذاكرة حيث لا تعتمد على ملفات XML مؤقتة أو وسيطة. هذا يعني أنه يمكن تحويل ملفات Excel الكبيرة، مثل تلك التي تحتوي على صور ومخططات وغيرها من الكائنات الرسومية، بسرعة وكفاءة.

{{% /alert %}} 
## **الكود المثالي**

```c++
#include <iostream>
#include <memory>
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

    // Path of input excel file
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

إذا احتوى جدول البيانات على صيغ، فمن الأفضل استدعاء طريقة [Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) قبل التصيير إلى PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغ بشكل صحيح، وعرض القيم الصحيحة في PDF.

{{% /alert %}}
