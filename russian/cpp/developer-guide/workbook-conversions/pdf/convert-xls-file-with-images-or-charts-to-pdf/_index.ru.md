---
title: Конвертация XLS файла с изображениями или графиками в PDF на C++
linktitle: Преобразование XLS файла с изображениями или диаграммами в PDF
type: docs
weight: 50
url: /ru/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Конвертируйте файлы XLS с изображениями или графиками в PDF документы, используя Aspose.Cells с C++.
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование XLS файлов, содержащих изображения и графики, в PDF-документы. Aspose.Cells for C++ может работать независимо для преобразования таблицы в PDF: для этого не требуется Aspose.PDF для C++. Процесс может выполняться в памяти, так как он не зависит от временных или промежуточных XML-файлов. Это означает, что крупные файлы Excel, например, содержащие изображения, графики и другие объекты рисования, могут быть быстро и эффективно преобразованы.

{{% /alert %}} 
## **Образец кода**

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

Если в таблице есть формулы, лучше всего вызвать метод [Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) непосредственно перед преобразованием в PDF. Это гарантирует перерасчет зависимых от формул значений и правильное отображение их в PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
