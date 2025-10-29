---
title: Convertir JSON en CSV avec C++
linktitle: Convertir JSON en CSV
type: docs
weight: 210
url: /fr/cpp/convert-json-to-csv/
description: Apprenez comment convertir JSON en CSV en utilisant Aspose.Cells for C++ avec des exemples JSON simples et imbriqués.
---

## **Convertir JSON en CSV**

Aspose.Cells prend en charge la conversion de JSON simple ainsi que de JSON imbriqué en CSV. Pour cela, l'API fournit les classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) et [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) offre les options pour la disposition JSON comme [**SetIgnoreTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/setignoretitle/) (ignore le titre si le tableau est une propriété d'un objet) ou [**GetArrayAsTable()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/getarrayastable/) (traite le tableau comme une table). La classe [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) traite le JSON en utilisant les options de disposition définies avec la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/).

L'exemple de code suivant montre l'utilisation des classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) et [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) pour charger le fichier JSON source et générer le fichier CSV de sortie.

### **Code d'exemple**

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
