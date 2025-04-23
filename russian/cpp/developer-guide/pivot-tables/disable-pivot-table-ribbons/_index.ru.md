---
title: Отключение лент сводных таблиц с помощью C++
linktitle: Отключить ленту сводных таблиц
type: docs
weight: 90
url: /ru/cpp/disable-pivot-table-ribbons/
description: Научитесь отключать ленты сводных таблиц в файлах Excel с использованием Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Отчеты на основе сводных таблиц полезны, но могут содержать ошибки, если пользователи не имеют подробных знаний о Excel для настройки этих отчетов. В таких случаях организации захотят ограничить возможность пользователей изменять отчеты на основе сводных таблиц. Общие функции сводных таблиц, такие как добавление дополнительных фильтров, слайсеров, полей или изменение порядка элементов в отчете, в основном не рекомендуется для каждого пользователя. С другой стороны, эти пользователи должны иметь возможность обновлять отчет и использовать существующие фильтры или слайсеры. Aspose.Cells предоставила разработчикам эту возможность ограничивать изменение таких отчетов во время их создания. Для этого Excel предоставляет функцию отключения ленты сводных таблиц, которая также реализована в Aspose.Cells. Разработчики могут отключить ленту, содержащую элементы управления для изменения этих отчетов.

{{% /alert %}}

## **Отключение ленты сводной таблицы с помощью PivotTable.EnableWizard**

Следующий код демонстрирует эту функцию, получая доступ к сводной таблице из листа, а затем устанавливая [**GetEnableWizard()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getenablewizard/) в значение **false**. Образец файла с сводной таблицей можно скачать по этой [ссылке](pivot_table_test.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
