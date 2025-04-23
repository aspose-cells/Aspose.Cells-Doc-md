--- 
title: Convert JSON till Excel med C++ 
linktitle: Konvertera JSON till Excel 
type: docs 
weight: 300 
url: /sv/cpp/convert-json-to-excel/ 
description: Lär dig hur man konverterar json till Excel fil med Aspose.Cells och C++. 
keywords: Importera JSON utan Office 2013, Office 2016, Office 2019 och Office 365. 
--- 

{{% alert color="primary" %}} 

Aspose.Cells stöder konvertering av en Json (JavaScript Object Notation) fil till Excel Arbetsbok. 

{{% /alert %}} 

## **Konvertera JSON till Excel-arbetsbok** 
Det är ingen anledning att undra hur man konverterar JSON till en Excel-fil, för bibliotek Aspose.Cells for C++ har den bästa lösningen. API:n Aspose.Cells stödjer konvertering av JSON-format till kalkylblad. Du kan använda [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) klassen för att specificera ytterligare inställningar för import av JSON till Arbetsbok. 

Följande kodexempel visar import av JSON till Excel-arbetsbok. Se koden för att konvertera [källfilen](sample.json) till den xlsx-fil som genereras av koden som referens. 

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

Följande kodexempel som använder klassen JsonLoadOptions för att ange ytterligare inställningar visar import av JSON till Excel-arbetsbok. Se koden för att konvertera [källfilen](sample.json) till den xlsx-fil som genereras av koden för referens. 

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

Nedan visar kodexemplet import av en JSON-sträng till Excel-Arbetsbok. Du kan också specificera platsen för layouten vid import av JSON. Se koden för att konvertera JSON-sträng till den xlsx-fil som genereras av koden för referens. 

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
