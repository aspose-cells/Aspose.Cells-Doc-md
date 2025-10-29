---
title: Загрузка и управление файлами Excel, OpenOffice, Json, Csv и Html с помощью C++
linktitle: Открытие файлов
type: docs
weight: 20
url: /ru/cpp/loading-saving-and-managing/
description: С Aspose.Cells for C++ легко создавать, открывать и управлять файлами Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Image, Mht и XPS.
---

{{% alert color="primary" %}}

С Aspose.Cells for C++ легко создавать, открывать и управлять файлами Excel, например, получать данные или использовать шаблон дизайнера для ускорения процесса разработки.

{{% /alert %}}

## **Создание новой книги**
Следующий пример создает новую книгу с нуля.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    try
    {
        // Create a License object
        License license;

        // Set the license of Aspose.Cells to avoid the evaluation limitations
        license.SetLicense(srcDir + u"Aspose.Cells.lic");
    }
    catch (const std::exception& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    // Instantiate a Workbook object that represents Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Input the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Открытие и сохранение файла**
С Aspose.Cells for C++ легко открывать, сохранять и управлять файлами Excel.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"dest.xlsx";

    // Create a Workbook object and open an Excel file using its file path
    Workbook workbook1(inputFilePath);

    // Adding new sheet
    WorksheetCollection sheets = workbook1.GetWorksheets();
    Worksheet sheet = sheets.Add(u"MySheet");

    // Setting active sheet
    sheets.SetActiveSheetIndex(1);

    // Setting values
    Cells cells = sheet.GetCells();

    // Setting text
    cells.Get(u"A1").PutValue(u"Hello!");

    // Setting number
    cells.Get(u"A2").PutValue(1000);

    // Setting Date Time
    Cell cell = cells.Get(u"A3");
    Date currentDate;
    currentDate.year = 2023; // Replace with actual current year
    currentDate.month = 10;  // Replace with actual current month
    currentDate.day = 5;     // Replace with actual current day
    currentDate.hour = 12;   // Replace with actual current hour
    currentDate.minute = 30; // Replace with actual current minute
    currentDate.second = 0;  // Replace with actual current second
    cell.PutValue(currentDate);

    // Setting style for date
    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    // Setting formula
    cells.Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Saving the workbook to disk
    workbook1.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Дополнительные темы**
- [Различные способы открытия файлов](/cells/ru/cpp/different-ways-to-open-files/)
- [Фильтрация определенных имен при загрузке рабочей книги](/cells/ru/cpp/filter-defined-names-while-loading-workbook/)
- [Фильтрация объектов при загрузке рабочей книги или листа](/cells/ru/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Фильтрация типа данных при загрузке рабочей книги из файла шаблона](/cells/ru/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Предупреждения при загрузке файла Excel](/cells/ru/cpp/get-warnings-while-loading-excel-file/)
- [Загрузка исходного файла Excel без диаграмм](/cells/ru/cpp/load-source-excel-file-without-charts/)
- [Загрузка конкретных листов в книге](/cells/ru/cpp/load-specific-worksheets-in-a-workbook/)
- [Загрузка рабочей книги с указанным размером бумаги принтера](/cells/ru/cpp/load-workbook-with-specified-printer-paper-size/)
- [Открытие файлов с различными форматами](/cells/ru/cpp/opening-different-microsoft-excel-versions-files/)
- [Открытие файлов с различными форматами](/cells/ru/cpp/opening-files-with-different-formats/)
- [Оптимизация использования памяти при работе с большими файлами с крупными наборами данных](/cells/ru/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Чтение таблицы чисел, разработанной компанией Apple Inc., с использованием Aspose.Cells](/cells/ru/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Прекратить преобразование или загрузку с помощью InterruptMonitor, если это занимает слишком много времени](/cells/ru/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Использование API LightCells](/cells/ru/cpp/using-lightcells-api/)
- [Преобразовать CSV в JSON](/cells/ru/cpp/convert-csv-to-json/)
- [Преобразование Excel в JSON](/cells/ru/cpp/convert-excel-to-json/)
- [Преобразовать JSON в CSV](/cells/ru/cpp/convert-json-to-csv/)
- [Преобразовать JSON в Excel](/cells/ru/cpp/convert-json-to-excel/)
- [Преобразование Excel в Html](/cells/ru/cpp/convert-excel-to-html/)
{{< app/cells/assistant language="cpp" >}}
