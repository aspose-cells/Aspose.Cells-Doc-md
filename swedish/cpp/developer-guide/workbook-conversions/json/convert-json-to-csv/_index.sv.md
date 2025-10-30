---
title: Convert JSON till CSV med C++
linktitle: Konvertera JSON till CSV
type: docs
weight: 210
url: /sv/cpp/convert-json-to-csv/
description: Lär dig hur man konverterar JSON till CSV med Aspose.Cells for C++ med enkla och inbäddade JSON exempel.
---

## **Konvertera JSON till CSV**

Aspose.Cells stöder konvertering av enkel och inbäddad JSON till CSV. För detta tillhandahåller API:n [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) klasser. Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) erbjuder val för JSON-layout, som [**SetIgnoreTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/setignoretitle/) (ignorerar titeln om arrayen är en egenskap i ett objekt) eller [**GetArrayAsTable()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/getarrayastable/) (behandlar arrayen som ett bord). Klassen [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) bearbetar JSON med layoutalternativ som ställts in med klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/).

Följande kodexempel visar användningen av klasserna [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) för att ladda [käljsonfil](104398869.json) och generera [utdata CSV-fil](104398870.csv).

### **Exempelkod**

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
{{< app/cells/assistant language="cpp" >}}
