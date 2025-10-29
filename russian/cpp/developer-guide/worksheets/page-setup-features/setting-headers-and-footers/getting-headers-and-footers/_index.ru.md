---
title: Получение заголовков или нижних колонтитулов с помощью C++
linktitle: Получение заголовков или нижних колонтитулов
type: docs
weight: 30
url: /ru/cpp/get-headers-or-footers/
description: В этой статье объясняется, как программно получать заголовки и нижние колонтитулы из файлов Excel или OpenOffice с помощью API или библиотеки C++.
---

{{% alert color="primary" %}}

Заголовки и нижние колонтитулы отображаются только в представлении макета страницы, предварительном просмотре и на распечатанных страницах. 

Также вы можете использовать диалоговое окно настройки страницы, если хотите просмотреть заголовки или нижние колонтитулы для более чем одного листа одновременно. 

Для других типов листов, таких как листы диаграмм или диаграммы, вы можете вставлять заголовки и нижние колонтитулы только с помощью диалогового окна настройки страницы.

{{% /alert %}}

## **Получение заголовков и нижних колонтитулов в MS Excel**
1. Нажмите на лист, где вы хотите просмотреть или изменить заголовки или нижние колонтитулы.
2. На вкладке Вид в группе Просмотры рабочей книги щёлкните «Разметка страницы».
  Excel отображает лист в режиме макета страницы.
3. Чтобы просмотреть или отредактировать заголовок или нижний колонтитул, щелкните на текстовом поле заголовка или колонтитула слева, по центру или справа вверху или внизу страницы листа (под заголовком или над колонтитулом).


## **Получение заголовков и нижних колонтитулов с помощью Aspose.Cells for C++**
С помощью методов [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) и [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/) разработчики на C++ могут просто получать заголовки или нижние колонтитулы из файла.

1. Создайте рабочую книгу для открытия файла.
2. Получить лист, где вы хотите получить заголовки или колонтитулы.
3. Получить заголовок или колонтитул с определенным идентификатором раздела.

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Разбор заголовков и колонтитулов в список команд**
Текст заголовка или колонтитула может содержать специальные команды, например заполнитель для номера страницы, текущей даты или атрибутов форматирования текста.

Специальные команды представлены одним символом с ведущим амперсандом ("&").

Строки заголовка и нижнего колонтитула создаются с использованием грамматики ABNF. Без просмотрщика их понять сложно.

Aspose.Cells for C++ предоставляет метод [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) для парсинга заголовков и нижних колонтитулов как списка команд.

Следующий код показывает, как парсить заголовок или нижний колонтитул как список команд и обрабатывать команды:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
