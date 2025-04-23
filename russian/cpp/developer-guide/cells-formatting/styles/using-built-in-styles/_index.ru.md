---
title: Использование встроенных стилей с C++
linktitle: Использование встроенных стилей
type: docs
weight: 80
url: /ru/cpp/using-built-in-styles/
description: Код C++ для использования встроенных стилей Excel с API Aspose.Cells for C++
keywords: использование стилей Excel в c++, программное применение стилей в рабочей книге, программное применение стилей в рабочей книге, применение встроенных стилей в Excel c++, применение встроенных стилей в рабочей книге, код c++ для применения встроенных стилей в рабочей книге, код c++ для применения встроенных стилей в Excel рабочей книге
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет обширную коллекцию многократно используемых стилей для форматирования ячейки в документе электронной таблицы. Мы можем использовать встроенные стили в нашей книге и также создавать пользовательские стили.

{{% /alert %}}

## **Как использовать встроенные стили**

Метод [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) и перечисление [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) делают использование встроенных стилей удобным. Вот список всех возможных встроенных стилей:

- ДВАДЦАТЬ ПРОЦЕНТОВ АКЦЕНТ 1
- ДВАДЦАТЬ ПРОЦЕНТОВ АКЦЕНТ 2
- ДВАДЦАТЬ ПРОЦЕНТОВ АКЦЕНТ 3
- ДВАДЦАТЬ ПРОЦЕНТОВ АКЦЕНТ 4
- ДВАДЦАТЬ ПРОЦЕНТОВ АКЦЕНТ 5
- ДВАДЦАТЬ ПРОЦЕНТОВ АКЦЕНТ 6
- СОРОК ПРОЦЕНТОВ АКЦЕНТ 1
- СОРОК ПРОЦЕНТОВ АКЦЕНТ 2
- СОРОК ПРОЦЕНТОВ АКЦЕНТ 3
- СОРОК ПРОЦЕНТОВ АКЦЕНТ 4
- СОРОК ПРОЦЕНТОВ АКЦЕНТ 5
- СОРОК ПРОЦЕНТОВ АКЦЕНТ 6
- ШЕСТЬДЕСЯТ ПРОЦЕНТОВ АКЦЕНТ 1
- ШЕСТЬДЕСЯТ ПРОЦЕНТОВ АКЦЕНТ 2
- ШЕСТЬДЕСЯТ ПРОЦЕНТОВ АКЦЕНТ 3
- ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_4
- ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_5
- ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_6
- АКЦЕНТ_1
- АКЦЕНТ_2
- АКЦЕНТ_3
- АКЦЕНТ_4
- АКЦЕНТ_5
- АКЦЕНТ_6
- ПЛОХОЙ
- ВЫЧИСЛЕНИЕ
- ПРОВЕРКА_ЯЧЕЙКИ
- ЗАПЯТАЯ
- ЗАПЯТАЯ_1
- ВАЛЮТА
- ВАЛЮТА_1
- ПОЯСНИТЕЛЬНЫЙ_ТЕКСТ
- ХОРОШО
- ЗАГОЛОВОК_1
- ЗАГОЛОВОК_2
- ЗАГОЛОВОК_3
- ЗАГОЛОВОК_4
- HYPERLINK
- СЛЕДУЮЩАЯ_ГИПЕРССЫЛКА
- ВВОД
- СВЯЗАННАЯ_ЯЧЕЙКА
- НЕЙТРАЛЬНЫЙ
- НОРМАЛЬНЫЙ
- ЗАМЕЧАНИЕ
- ВЫВОД
- ПРОЦЕНТ
- ЗАГОЛОВОК
- ВСЕГО
- ТЕКСТ_ПРЕДУПРЕЖДЕНИЯ
- УРОВЕНЬ_СТРОКИ
- УРОВЕНЬ_СТОЛБЦА

## Код C++ для использования встроенных стилей

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
