---
title: Convert CSV to JSON with C++
linktitle: Convert CSV to JSON
type: docs
weight: 220
url: /cpp/convert-csv-to-json/
description: Convert CSV file to JSON by using the simple to use Aspose.Cells for C++ API.
keywords: Convert, Convert CSV to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON C++, C++ code to convert CSV to JSON
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Convert CSV to JSON**

Aspose.Cells supports converting CSV to JSON. For this, the API provides [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) classes. The [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) class provides the options for exporting range to JSON. The [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) class has the following properties.

- [**GetExportAsString()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getexportasstring/): This exports the string value of the cells to JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/gethasheaderrow/): This indicates whether the range contains a header row.
- [**GetIndent()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getindent/): Indicates the indent.

The [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) class exports the JSON using the export options set with the [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) class.

The following code sample demonstrates the use of [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) classes to load the [source CSV file](104398879.csv) and prints the JSON output in the console.

### **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options for CSV format
    LoadOptions loadOptions(LoadFormat::Csv);

    // Load CSV file
    Workbook workbook(srcDir + u"SampleCsv.csv", loadOptions);

    // Get the last cell in the worksheet
    Cell lastCell = workbook.GetWorksheets().Get(0).GetCells().GetLastCell();

    // Set JsonSaveOptions
    JsonSaveOptions jsonSaveOptions;

    // Create a range from the first cell to the last cell
    Range range = workbook.GetWorksheets().Get(0).GetCells().CreateRange(0, 0, lastCell.GetRow() + 1, lastCell.GetColumn() + 1);

    // Export the range to JSON
    U16String data = JsonUtility::ExportRangeToJson(range, jsonSaveOptions);

    // Print JSON
    std::cout << data.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Console Output**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
