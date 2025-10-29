---
title: Обнаружение типа гиперссылки с помощью C++
linktitle: Обнаружение типа гиперссылки
type: docs
weight: 160
url: /ru/cpp/detect-hyperlink-type/
description: Узнайте, как обнаруживать тип гиперссылки через API Aspose.Cells for C++.
keywords: Определить тип гиперссылки, Определить тип гиперссылки, Получить тип гиперссылки
---

## **Определение типа гиперссылки**

В электронной таблице Excel могут быть разные типы гиперссылок, такие как внешние, ссылки на ячейки, пути к файлам и т. д. Aspose.Cells поддерживает возможность определить тип гиперссылки. Типы гиперссылок представлены перечислением [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). Перечисление [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) имеет следующие элементы.

- Внешние: внешняя ссылка
- Путь к файлу: Локальный и полный путь к файлам\папкам.
- Электронная почта: Электронная почта
- СсылкаНаКлетку: Ссылка на клетку или именованный диапазон.

Для проверки типа гиперссылки, класс [**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) предоставляет свойство [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) с возвращаемым типом [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). В следующем фрагменте кода демонстрируется использование свойства [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/), используя этот [исходный файл Excel](94896195.xlsx).

### Исходный код

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

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Ниже приведен вывод, сгенерированный указанным выше фрагментом кода.

### Вывод в консоли
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
{{< app/cells/assistant language="cpp" >}}
