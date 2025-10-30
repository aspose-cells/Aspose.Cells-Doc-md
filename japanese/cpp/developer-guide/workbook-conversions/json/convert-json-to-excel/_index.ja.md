--- 
title: JSONをExcelに変換(C++) 
linktitle: JSONをExcelに変換します。 
type: docs 
weight: 300 
url: /ja/cpp/convert-json-to-excel/ 
description: Aspose.Cellsを使用してJSONからExcelファイルへの変換方法を学びます（C++）。 
keywords: Office 2013、Office 2016、Office 2019、Office 365なしでJSONをインポートします。 
--- 

{{% alert color="primary" %}} 

Aspose.Cellsは、Json（JavaScript Object Notation）ファイルをExcelワークブックに変換することをサポートしています。 

{{% /alert %}} 

## **JSONをExcelワークブックに変換する** 
JSONをExcelファイルに変換する方法を迷う必要はありません。Aspose.Cells for C++ライブラリは最適な解決策を提供します。APIはJSON形式をスプレッドシートに変換するサポートを提供します。[JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/)クラスを利用して追加設定を指定可能です。 

以下のコード例は、JSONをExcelワークブックにインポートする方法を示しています。コードで生成されたxlsxファイルへの変換のために、[source file](sample.json)を参照してください。 

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

以下のコード例は、JsonLoadOptionsクラスを使用して追加の設定を指定することで、JSONをExcelワークブックにインポートする方法を示しています。コードで生成されたxlsxファイルへの変換のために、[source file](sample.json)を参照してください。 

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

次のコード例は、JSON文字列をExcelワークブックにインポートする例です。インポート時にレイアウトの位置も指定できます。コード例も参考にしてください。 

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
{{< app/cells/assistant language="cpp" >}}
