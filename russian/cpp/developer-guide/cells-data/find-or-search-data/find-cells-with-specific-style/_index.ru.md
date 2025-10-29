---
title: Найти ячейки с определенным стилем с помощью C++
linktitle: Поиск ячеек с определенным стилем
type: docs
weight: 190
url: /ru/cpp/find-cells-with-specific-style/
description: Узнайте, как найти или искать ячейки с примененным определенным стилем через API Aspose.Cells for C++.
keywords: Найти ячейки с примененным определенным стилем, Поиск ячеек с примененным определенным стилем
---

{{% alert color="primary" %}}

Иногда вам нужно найти ячейки с примененным определенным стилем. Вы можете использовать Aspose.Cells для поиска всех ячеек с общим стилем. Aspose.Cells предоставляет свойство [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/), которое вы можете использовать для указания стиля поиска ячеек.

{{% /alert %}}

Код в этом примере находит все ячейки, у которых такой же стиль, как у ячейки A1. После выполнения кода все ячейки, у которых такой же стиль, как у A1, содержат текст "Найдено".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
