---
title: Поддержка немецкой локали в формулах именованных диапазонов с C++
linktitle: Поддержка немецкой локали в формулах для именованных диапазонов
type: docs
weight: 60
url: /ru/cpp/support-for-german-locale-in-named-range-formulae/
description: Узнайте, как обрабатывать формулы именованных диапазонов на немецком языке с помощью Aspose.Cells и C++.
---

Английские формулы записаны в именованные области. Этот файл Excel можно открыть в среде, где настроена немецкая локаль; однако английская формула будет переведена на немецкий язык. Ниже приведен пример этой функции, но он требует установки Excel на немецком языке и настройки системной локали на немецкий язык.

Образец файла для тестирования этой функции может быть загружен по следующей ссылке:

[sampleNamedRangeTest.xlsm](73990165.xlsm)

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

    // Define the name and formula for the named range
    const U16String name(u"HasFormula");
    const U16String value(u"=GET.CELL(48, INDIRECT(\"ZS\",FALSE))");

    // Load the source workbook
    Workbook wbSource(srcDir + u"sampleNamedRangeTest.xlsm");

    // Get the worksheet collection
    WorksheetCollection wsCol = wbSource.GetWorksheets();

    // Add a new named range and get its index
    int32_t nameIndex = wsCol.GetNames().Add(name);

    // Get the named range by index
    Name namedRange = wsCol.GetNames().Get(nameIndex);

    // Set the formula for the named range
    namedRange.SetRefersTo(value);

    // Save the workbook with the new named range
    wbSource.Save(outDir + u"sampleOutputNamedRangeTest.xlsm");

    std::cout << "Named range added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
