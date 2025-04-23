---
title: Чтение и запись таблицы запросов листа с помощью C++
linktitle: Чтение и запись запросов таблицы рабочего листа
type: docs
weight: 40
url: /ru/cpp/reading-and-writing-query-table-of-worksheet/
description: Узнайте, как читать и писать таблицы запросов в листах Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells обеспечивает коллекцию `Worksheet.QueryTables`, которая возвращает объект типа `QueryTable` по индексу. У нее есть следующие два свойства:

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

Это оба логических значения. Вы можете просмотреть их в Microsoft Excel через **Данные > Соединения > Свойства**.

{{% /alert %}}

## Чтение и запись запросов таблицы рабочего листа

Следующий пример кода читает первое `QueryTable` первого листа и выводит оба свойства `QueryTable`. Затем он устанавливает `QueryTable.PreserveFormatting` в `true`.

Вы можете загрузить исходный файл Excel, используемый в этом коде, и выходной файл Excel, созданный кодом, по следующим ссылкам.

- [Исходный файл Excel](5115533.xlsx)
- [Выходной файл Excel](5115537.xlsx)

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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Вывод в консоли

Вот вывод консоли для приведенного выше примера кода:

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Получить диапазон результата таблицы запроса

Aspose.Cells предоставляет возможность считать адрес (диапазон результата ячеек) таблицы запроса. Следующий код демонстрирует эту функцию, считывая адрес диапазона результата таблицы запроса. Образец файла можно скачать [здесь](72417290.xlsx).

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
