---
title: Получить проверку, примененную к ячейке с помощью C++
linktitle: Получить примененную валидацию для ячейки
type: docs
weight: 200
url: /ru/cpp/get-validation-applied-on-a-cell/
description: Эта статья показывает, как применить проверку к ячейке с помощью C++.
keywords: применить проверку ячейки в Excel с помощью C++, применить проверку к ячейке в Excel с помощью C++, установить проверку в Excel с помощью C++, проверка ячейки в Excel с помощью C++, C++ применение проверки ячейки в Excel, C++ установка проверки для ячейки в Excel, C++ проверка ячейки в Excel, C++ проверка ячейки в Excel
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells, чтобы получить проверку, примененную к ячейке. Aspose.Cells предоставляет метод [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) для этой цели. Если на ячейке не применена проверка, он возвращает null.

Точно так же можно использовать метод [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/), чтобы получить примененную валидацию для ячейки, указав её индексы строки и столбца.

{{% /alert %}}

## C++ код для получения примененной проверки к ячейке

Следующий пример показывает, как получить проверку, примененную к ячейке.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access its first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Cell C1 has the Decimal Validation applied on it. It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Access the validation applied on this cell
    Validation validation = cell.GetValidation();

    // Read various properties of the validation
    std::cout << "Reading Properties of Validation" << std::endl;
    std::cout << "--------------------------------" << std::endl;
    std::cout << "Type: " << static_cast<int>(validation.GetType()) << std::endl;
    std::cout << "Operator: " << static_cast<int>(validation.GetOperator()) << std::endl;
    std::cout << "Formula1: " << validation.GetFormula1().ToUtf8() << std::endl;
    std::cout << "Formula2: " << validation.GetFormula2().ToUtf8() << std::endl;
    std::cout << "Ignore blank: " << validation.GetIgnoreBlank() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Связанные статьи

- [Валидация данных](/cells/ru/cpp/data-validation/)
