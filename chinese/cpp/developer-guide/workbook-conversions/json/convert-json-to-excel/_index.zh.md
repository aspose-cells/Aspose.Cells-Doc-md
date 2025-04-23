--- 
title: 用 C++ 将 JSON 转换为 Excel 
linktitle: 转换 JSON 为 Excel 
type: docs 
weight: 300 
url: /zh/cpp/convert-json-to-excel/ 
description: 学习如何用 C++ 和 Aspose.Cells 将 JSON 转换为 Excel 文件。 
keywords: 导入不依赖office 2013、office 2016、office 2019和office 365的json。 
--- 

{{% alert color="primary" %}} 

 Aspose.Cells 支持将 JSON 文件转换为 Excel 工作簿。 

{{% /alert %}} 

## **将JSON转换为Excel工作簿** 
 不必担心如何将 JSON 转换为 Excel 文件，因为 Aspose.Cells for C++ 库提供了最佳解决方案。Aspose.Cells API 支持将 JSON 格式转换为电子表格。你可以使用 [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) 类为导入 JSON 到工作簿指定额外设置。 

以下示例演示了将JSON导入Excel工作簿的代码。请查看代码以将[source file](sample.json)转换为代码生成的xlsx文件。 

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

以下使用JsonLoadOptions类指定附加设置的示例代码演示了将JSON导入到Excel工作簿。请参阅用于参考的代码将源文件转换为由代码生成的xlsx文件。 

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

 以下代码示例演示了导入 JSON 字符串到 Excel 工作簿的方式。你还可以在导入 JSON 时指定排版位置。请查看代码以将 JSON 字符串转换为由代码生成的 xlsx 文件作为参考。 

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
