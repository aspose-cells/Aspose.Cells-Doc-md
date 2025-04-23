---
title: Вычисление функций MINIFS и MAXIFS Excel 2016 с помощью C++
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для вычисления функций MINIFS и MAXIFS в Microsoft Excel 2016 с помощью C++.
keywords: Aspose.Cells, Excel, 2016, функция MINIFS, функция MAXIFS, вычисление
type: docs
weight: 300
url: /ru/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Возможные сценарии использования**
Microsoft Excel 2016 поддерживает функции MINIFS и MAXIFS. Эти функции не поддерживаются в Excel 2013 или более ранних версиях. Aspose.Cells также поддерживает вычисление этих функций. Следующий скриншот иллюстрирует использование этих функций. Пожалуйста, прочитайте комментарии внутри скриншота, чтобы понять, как работают эти функции.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Расчет функций MINIFS и MAXIFS Excel 2016**
Следующий пример загружает [образец файла Excel](5115149.xlsx) и вызывает метод [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/), чтобы выполнить вычисление формул через Aspose.Cells, а затем сохраняет результаты в [выводной PDF](5115154.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
