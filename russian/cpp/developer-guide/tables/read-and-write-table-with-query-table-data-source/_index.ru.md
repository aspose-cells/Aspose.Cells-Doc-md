---
title: Чтение и запись таблицы с источником данных QueryTable с помощью C++
linktitle: Чтение и запись таблицы с источником данных таблицы запросов
type: docs
weight: 30
url: /ru/cpp/read-and-write-table-with-query-table-data-source/
description: Узнайте, как читать и записывать таблицы с QueryTable в качестве источника данных, используя Aspose.Cells for C++.
---

## **Чтение и запись таблицы с источником данных из запроса к таблице**
С Aspose.Cells вы можете читать и писать таблицу, которая имеет QueryTable в качестве источника данных. Поддержка этой функции также существует для XLS файлов. Следующий пример кода демонстрирует чтение и запись такой таблицы, сначала читая таблицу, а затем модифицируя её для добавления строки итогов.

```cpp
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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

Исходный и конечный файлы Excel прикреплены для справки.

[Исходный файл](96928091.xls)

[Выходной файл](96928092.xls)
{{< app/cells/assistant language="cpp" >}}
