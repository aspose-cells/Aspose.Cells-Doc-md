---
title: Парсинг кешированных записей сводной таблицы при загрузке файла Excel с помощью C++
linktitle: Парсинг кешированных записей сводной таблицы
type: docs
weight: 70
url: /ru/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Узнайте, как парсить кешированные записи сводной таблицы при загрузке файлов Excel с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

При создании сводной таблицы Microsoft Excel делает копию исходных данных и хранит их в кэше сводной таблицы. Кэш сводной таблицы хранится в памяти Microsoft Excel. Вы его не видите, но это данные, на которые ссылается сводная таблица при построении или изменении выбора среза или перемещении строк/столбцов. Это позволяет Microsoft Excel очень быстро реагировать на изменения сводной таблицы, но также может удвоить размер вашего файла. В конце концов, кэш сводной таблицы просто дублирует ваши исходные данные, поэтому логично, что размер вашего файла может увеличиться вдвое.

При загрузке файла Excel в объект Workbook можно решить, хотите ли вы также загружать записи из кэша сводной таблицы или нет, используя свойство [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). Значение по умолчанию этого свойства - **false**. Если кэш сводной таблицы довольно большой, это может улучшить производительность. Но если вы также хотите загрузить записи кэша сводной таблицы, вы должны установить это свойство как **true**.

## **Анализ кэшированных записей сводной таблицы при загрузке файла Excel**

Приведенный ниже образец кода объясняет использование свойства [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). Он загружает [образец файла Excel](61767773.xlsx), разбирая кэшированные записи сводной таблицы. Затем он обновляет сводную таблицу и сохраняет ее как [выходной файл Excel](61767774.xlsx).

## **Образец кода**

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

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
