---
title: Conversione Excel in JSON con C++
linktitle: Converti Excel in JSON
type: docs
weight: 300
url: /it/cpp/convert-excel-to-json/
description: Impara come convertire un file Excel in JSON con Aspose.Cells usando C++.
keywords: Esportazione del Workbook in json senza office 2013, office 2016, office 2019 e office 365
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di un Workbook in un file Json(JavaScript Object Notation).

{{% /alert %}}

## **Converti Workbook Excel in JSON**

Non c'è bisogno di chiedersi come convertire un Workbook di Excel in JSON, perché la libreria Aspose.Cells for C++ offre la soluzione migliore. L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato JSON. Per esportare il workbook in JSON, passa [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Puoi anche usare la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) per specificare impostazioni aggiuntive per esportare il foglio di lavoro in JSON.

Il seguente esempio di codice dimostra come esportare un Workbook di Excel in JSON. Consulta il codice per convertire il file di origine (sample.xlsx) nel file JSON generato dal codice come riferimento.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Il seguente esempio di codice, che utilizza la classe JsonSaveOptions per specificare impostazioni aggiuntive, dimostra come esportare un Workbook di Excel in JSON. Consulta il codice per convertire il file di origine (sample.xlsx) nel file JSON generato dal codice come riferimento.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
