---
title: Проверка пользовательского числового формата при установке свойства Style.Custom с C++
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц, которая поддерживает проверку пользовательских числовых форматов при стилизации. В этой статье будет показано, как использовать библиотеку Aspose.Cells для проверки пользовательских числовых форматов, чтобы обеспечить правильность стиля.
keywords: Aspose.Cells, библиотеки C++, таблицы, стилизация, пользовательский числовой формат, проверка, валидация
type: docs
weight: 170
url: /ru/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Возможные сценарии использования**

Если присвоить недопустимый пользовательский числовой формат свойству [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/), то Aspose.Cells не выбросит исключение. Но если вы хотите, чтобы Aspose.Cells проверял правильность присвоенного пользовательского числового формата, установите свойство [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) в значение **true**.

## **Проверить настраиваемый формат чисел при установке свойства Style.Custom**

Следующий пример кода присваивает недопустимый пользовательский числовой формат свойству [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). Так как мы уже установили свойство [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) в **true**, происходит выброс исключения, например, неверный числовой формат. Ознакомьтесь с комментариями внутри кода для получения дополнительной информации.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
