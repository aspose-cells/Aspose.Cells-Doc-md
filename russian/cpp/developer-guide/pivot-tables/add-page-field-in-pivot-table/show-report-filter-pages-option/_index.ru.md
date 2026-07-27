---
title: Показать страницу фильтра отчёта с помощью C++
linktitle: Показать опцию страниц фильтрации отчета
type: docs
weight: 110
url: /ru/cpp/show-report-filter-pages-option/
description: Узнайте, как включить опцию "Показать страницы фильтров отчета" в сводных таблицах, используя Aspose.Cells for C++.
---

## **Показать опцию страниц фильтрации отчета**
Excel поддерживает создание сводных таблиц, добавление фильтров отчетов и включение опции "Показать страницы фильтров отчета". Aspose.Cells также поддерживает эту функцию для включения опции "Показать страницы фильтров отчета" на созданной сводной таблице. Ниже приведен скриншот, показывающий опцию "Показать страницы фильтров отчета" в Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

Образец исходного файла и выходных файлов можно загрузить отсюда для тестирования образца кода:

` ` [Исходный файл Excel](81920786.xlsx) 

[Выходной файл Excel](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
