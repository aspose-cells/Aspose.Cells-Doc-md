---
title: Получить уникальный идентификатор листа с помощью C++
linktitle: Получить уникальный ID листа
type: docs
weight: 190
url: /ru/cpp/get-worksheet-unique-id/
description: В этой статье показано, как получить уникальный ID листа Excel с помощью библиотеки C++ и API программным путём.
keywords: уникальный ID Excel лист C++, уникальный ID листа C++
---

## **Получить уникальный ID листа**

Aspose.Cells предоставляет возможность получения уникального ID листа с помощью метода [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/). Следующий пример показывает использование метода [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) для вывода уникального ID листа. В приведённом примере используется [пробный Excel файл](105480213.xlsx).

### Исходный код

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
