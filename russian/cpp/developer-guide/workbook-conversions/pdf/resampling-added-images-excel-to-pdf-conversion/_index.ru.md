---
title: Пересэмплирование добавленных изображений — преобразование Excel в PDF с помощью C++
linktitle: Добавление перерасчета изображений  конвертация Excel в PDF
type: docs
weight: 150
url: /ru/cpp/resampling-added-images-excel-to-pdf-conversion/
description: Узнайте, как пересэмплировать добавленные изображения для уменьшения размера PDF с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

При работе с большими файлами Microsoft Excel с большим количеством изображений вам может потребоваться сжимать добавленные изображения, чтобы уменьшить размер выходного PDF файла и улучшить общую производительность конвертации. Aspose.Cells поддерживает перерасчет добавленных изображений для уменьшения размера выходного PDF файла и улучшения производительности в некоторой степени.

{{% /alert %}}

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, описывающим, как выполнить задачу с использованием API Aspose.Cells. В примере происходит преобразование файла Microsoft Excel в файл PDF с одновременным сжатием изображений в файле.

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

Использование опции [**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/) позволяет минимизировать размер выходного PDF, но это может немного повлиять на качество изображения.

{{% /alert %}} 

{{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}

