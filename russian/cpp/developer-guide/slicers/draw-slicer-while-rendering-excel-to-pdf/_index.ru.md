---
title: Отрисовка сегмента слайсера при преобразовании Excel в PDF с помощью C++
linktitle: Нарисуйте фильтр при рендеринге Excel в PDF
type: docs
weight: 60
url: /ru/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Экспортируйте Excel в PDF с настройками сегмента слайсера, используя Aspose.Cells и C++.
---

## **Нарисуйте фильтр при рендеринге Excel в PDF**
Если у вас есть файл Excel с применённым сегментом слайсера, и вы хотите экспортировать его в PDF с сохранением настроек сегмента, Aspose.Cells теперь поддерживает это по умолчанию. Просто экспортируйте файл Excel с сегментом слайсера в PDF, и полученный PDF отобразит применённый сегмент слайсера.

Следующий образец кода загружает [образец файла Excel](94044165.xlsx), содержащий существующую срезку. Затем он сохраняет книгу как [выходной файл PDF](94044166.pdf). На следующем скриншоте сравниваются исходный файл Excel и сгенерированный файл PDF.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Образец кода**
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleSlicerChart.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"SampleSlicerChart.pdf";

    // Create workbook from the excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PDF file
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
