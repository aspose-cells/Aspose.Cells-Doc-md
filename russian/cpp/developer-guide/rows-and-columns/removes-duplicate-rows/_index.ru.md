---
title: Удаление дублирующихся строк в листе с помощью C++
linktitle: Удаление дублирующихся строк в листе
type: docs
weight: 370
url: /ru/cpp/remove-duplicate-rows-in-a-worksheet/
description: Узнайте, как удалить дублирующиеся строки в листе с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Удаление дублирующихся строк — одна из многих полезных функций Microsoft Excel. Она позволяет пользователям удалять дублирующиеся строки в листе, и вы можете выбрать столбцы, которые следует проверять на дублирующуюся информацию.

Aspose.Cells предоставляет метод `Cells::RemoveDuplicates()` для этой цели. Также можно установить `startRow`, `startColumn`, `endRow` и `endColumn`, чтобы указать столбцы.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
