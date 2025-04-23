--- 
title: Преобразование JSON в Excel с помощью C++ 
linktitle: Конвертировать JSON в Excel 
type: docs 
weight: 300 
url: /ru/cpp/convert-json-to-excel/ 
description: Узнайте, как преобразовать JSON в файл Excel с помощью Aspose.Cells и C++. 
keywords: Импорт JSON без Office 2013, Office 2016, Office 2019 и Office 365. 
--- 

{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование файла Json (JavaScript Object Notation) в рабочую книгу Excel. 

{{% /alert %}} 

## **Преобразование JSON в книгу Excel** 
Не нужно гадать, как конвертировать JSON в файл Excel, потому что библиотека Aspose.Cells for C++ предоставляет лучшее решение. API Aspose.Cells поддерживает преобразование JSON-формата в таблицы. Вы можете использовать класс [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/), чтобы указать дополнительные параметры при импорте JSON в рабочую книгу. 

В следующем примере кода демонстрируется импорт JSON в книгу Excel. Пожалуйста, ознакомьтесь с кодом для преобразования [исходного файла](sample.json) в файл xlsx, сгенерированный кодом для справки. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a Workbook object from a JSON file
    Workbook workbook(u"sample.json");

    // Save the file to xlsx format
    workbook.Save(u"sample_out.xlsx");

    std::cout << "File saved successfully in xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 

В следующем примере кода, который использует класс JsonLoadOptions для указания дополнительных параметров, демонстрируется импорт JSON в книгу Excel. Пожалуйста, ознакомьтесь с кодом для преобразования [исходного файла](sample.json) в файл xlsx, сгенерированный кодом для справки. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options for loading the file.
    JsonLoadOptions options;

    // Indicates whether importing each attribute of JsonObject object as one worksheet when all child nodes are array nodes.
    options.SetMultipleWorksheets(true);

    // Create a workbook from the JSON file with the specified options.
    U16String inputFilePath(u"sample.json");
    Workbook book(inputFilePath, options);

    // Save file to xlsx format.
    U16String outputFilePath(u"sample_out.xlsx");
    book.Save(outputFilePath);

    std::cout << "File converted successfully to xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 

Следующий пример демонстрирует импорт строки JSON в рабочую книгу Excel. Также можно указать расположение макета при импорте JSON. Посмотрите код для преобразования строки JSON в файл xlsx, созданный этим кодом. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // JSON input string
    U16String inputJson = uR"([
                        { BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
                    ])";

    U16String sheetName = u"Sheet1";
    int32_t row = 3;
    int32_t column = 2;

    // Create a Workbook object
    Workbook book;
    Worksheet worksheet = book.GetWorksheets().Get(sheetName);

    // Set JsonLayoutOptions to treat Arrays as Table
    JsonLayoutOptions jsonLayoutOptions;
    jsonLayoutOptions.SetArrayAsTable(true);

    // Import JSON data into the worksheet
    JsonUtility::ImportData(inputJson, worksheet.GetCells(), row, column, jsonLayoutOptions);

    // Save the file to xlsx format
    book.Save(u"out.xlsx");

    std::cout << "Data imported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
