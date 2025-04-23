---
title: Настройка внешних ссылок в формулах с помощью C++
linktitle: Установка внешних ссылок в формулах
type: docs
weight: 20
url: /ru/cpp/set-external-links-in-formulas/
description: Узнайте, как включать ссылки на внешние файлы в формулах с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}} 

Иногда необходимо включить ссылки на внешние файлы в формулах, например, для оценки значения ячейки или диапазона по ним. Aspose.Cells предоставляет эту функцию, и в этом документе объясняется, как ею пользоваться.

{{% /alert %}} 

Ниже приведен пример кода, показывающий, как включить внешние файлы в формулы.

```cpp
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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get first Worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get Cells collection
    Cells cells = sheet.GetCells();

    // Set formula with external links
    cells.Get(u"A1").SetFormula(U16String(u"=SUM('[") + srcDir + u"book1.xlsx]Sheet1'!A2, '[" + srcDir + u"book1.xlsx]Sheet1'!A4)");

    // Set formula with external links
    cells.Get(u"A2").SetFormula(U16String(u"='[") + srcDir + u"book1.xlsx]Sheet1'!A8");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully with external links!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
