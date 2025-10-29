---
title: Извлечение темы данных из файла Excel с C++
linktitle: Извлечение данных темы из файла Excel
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц. Она поддерживает извлечение данных темы из Excel файлов, позволяя пользователям получать информацию о стиле и форматировании документов. В этой статье объясняется, как извлечь данные темы из Excel файлов с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, Файл Excel, Данные темы, Стиль, Формат
type: docs
weight: 120
url: /ru/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет пользователям извлекать данные, связанные с темой, из файла Excel. Например, можно извлечь название темы, применённой к рабочей книге, цвет темы, применённый к ячейке или границам ячейки и так далее.

Вы можете применить тему к своей рабочей книге через Microsoft Excel, используя команду Разметка страницы > Темы.

{{% /alert %}}

## C++ код для извлечения данных темы из файла Excel

Следующий пример кода извлекает название темы, применённой к исходной рабочей книге, а также извлекает цвет темы, применённый к ячейке A1, и цвет темы, применённый к нижней границе этой ячейки.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
