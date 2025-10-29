---
title: Преобразование JSON в CSV с помощью C++
linktitle: Конвертировать JSON в CSV
type: docs
weight: 210
url: /ru/cpp/convert-json-to-csv/
description: Узнайте, как преобразовать JSON в CSV с помощью Aspose.Cells for C++, используя простые и вложенные примеры JSON.
---

## **Преобразовать JSON в CSV**

Поддержка Aspose.Cells для преобразования простого и вложенного JSON в CSV. Для этого API предоставляет классы [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). Класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) задаёт параметры для форматирования JSON, такие как [**SetIgnoreTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/setignoretitle/) (игнорирует заголовок, если массив является свойством объекта) или [**GetArrayAsTable()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/getarrayastable/) (обрабатывает массив как таблицу). Класс [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) обрабатывает JSON, используя установленные параметры разметки с помощью класса [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/).

Следующий пример демонстрирует использование классов [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) для загрузки [исходного JSON файла](104398869.json) и генерации [выходного CSV файла](104398870.csv).

### **Образец кода**

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
