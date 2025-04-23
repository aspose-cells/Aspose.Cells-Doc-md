---
title: Реализация несмежных диапазонов с помощью C++
linktitle: Реализация неупорядоченных диапазонов
type: docs
weight: 700
url: /ru/cpp/implementing-non-sequential-ranges/
description: Узнайте, как создавать именованные диапазоны с несмежными ячейками с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}} 

Обычно именованные диапазоны являются прямоугольными с непрерывными и смежными ячейками. Но иногда может потребоваться использовать не связанный диапазон ячеек, в котором ячейки не являются смежными. Aspose.Cells поддерживает создание именованного диапазона с несмежными ячейками.

{{% /alert %}} 

Пример ниже показывает, как создавать именованный несмежный диапазон с помощью Aspose.Cells for C++.

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

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
