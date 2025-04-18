--- 
title: Convert JSON to Excel with C++ 
linktitle: Convert JSON to Excel 
type: docs 
weight: 300 
url: /cpp/convert-json-to-excel/ 
description: Learn how to convert json to excel file with Aspose.Cells with C++. 
keywords: Importing json without office 2013, office 2016, office 2019 and office 365. 
--- 

{{% alert color="primary" %}} 

Aspose.Cells supports converting a Json (JavaScript Object Notation) file to Excel Workbook. 

{{% /alert %}} 

## **Convert JSON to Excel Workbook** 
No need to wonder how to convert JSON to an Excel file, because Aspose.Cells for C++ library has the best solution. The Aspose.Cells API provides support for converting JSON format to spreadsheets. You can use [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) class to specify additional settings for importing JSON to Workbook. 

The following code example demonstrates importing JSON to Excel Workbook. Please see the code to convert [source file](sample.json) to the xlsx file generated by the code for reference. 

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

The following code example which uses JsonLoadOptions class to specify additional settings demonstrates importing JSON to Excel Workbook. Please see the code to convert [source file](sample.json) to the xlsx file generated by the code for reference. 

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

The following code example demonstrates importing a JSON string to an Excel Workbook. You can also specify the location of the layout when importing JSON. Please see the code to convert JSON string to the xlsx file generated by the code for reference. 

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
