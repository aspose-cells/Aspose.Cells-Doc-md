---
title: Convert JSON to CSV with C++
linktitle: Convert JSON to CSV
type: docs
weight: 210
url: /cpp/convert-json-to-csv/
description: Learn how to convert JSON to CSV using Aspose.Cells for C++ with simple and nested JSON examples.
---

## **Convert JSON to CSV**

Aspose.Cells supports converting simple as well as nested JSON to CSV. For this, the API provides [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) classes. The [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) class provides the options for JSON layout like [**SetIgnoreTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/setignoretitle/)(ignores the title if the array is a property of an object) or [**GetArrayAsTable()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/getarrayastable/)(processes the array as a table). The [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) class processes the JSON using the layout options set with the [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) class.

The following code sample demonstrates the use of [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) classes to load the [source JSON file](104398869.json) and generates the [output CSV file](104398870.csv).

### **Sample Code**

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String jsonFilePath = srcDir + u"SampleJson.json";
    U16String jsonData;
    std::ifstream jsonFile(jsonFilePath.ToUtf8().c_str());
    if (jsonFile.is_open())
    {
        std::stringstream buffer;
        buffer << jsonFile.rdbuf();
        jsonData = U16String(buffer.str().c_str());
        jsonFile.close();
    }
    else
    {
        std::cerr << "Failed to open JSON file: " << jsonFilePath.ToUtf8().c_str() << std::endl;
        return -1;
    }

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    JsonLayoutOptions importOptions;
    importOptions.SetConvertNumericOrDate(true);
    importOptions.SetArrayAsTable(true);
    importOptions.SetIgnoreTitle(true);

    JsonUtility::ImportData(jsonData, cells, 0, 0, importOptions);

    U16String outputFilePath = outDir + u"SampleJson_out.csv";
    workbook.Save(outputFilePath);

    std::cout << "JSON data imported and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```