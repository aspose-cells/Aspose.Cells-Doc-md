---
title: JSON in CSV mit C++ konvertieren
linktitle: Konvertieren Sie JSON in CSV
type: docs
weight: 210
url: /de/cpp/convert-json-to-csv/
description: Erfahren Sie, wie Sie JSON mit einfachen und verschachtelten JSON Beispielen mit Aspose.Cells for C++ in CSV konvertieren.
---

## **JSON in CSV konvertieren**

Aspose.Cells unterstützt die Konvertierung von einfachem sowie verschachteltem JSON in CSV. Hierfür stellt die API die Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) und [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) bereit. Die Klasse [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) bietet Optionen für das JSON-Layout wie [**SetIgnoreTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/setignoretitle/) (ignoriert den Titel, wenn das Array eine Eigenschaft eines Objekts ist) oder [**GetArrayAsTable()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/getarrayastable/) (verarbeitet das Array als Tabelle). Die Klasse [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) verarbeitet JSON unter Verwendung der mit [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) festgelegten Layout-Optionen.

Das folgende Codebeispiel demonstriert die Verwendung der Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) und [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/), um die [Quelldatei JSON](104398869.json) zu laden und die [Ausgabedatei CSV](104398870.csv) zu generieren.

### **Beispielcode**

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
