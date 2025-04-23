---
title: Converti cartella di lavoro in JSON con C++
linktitle: Converti cartella di lavoro in JSON
type: docs
weight: 300
url: /it/cpp/convert-workbook-to-json/
description: Impara come convertire le cartelle di lavoro Excel in formato JSON usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di un workbook in JSON (JavaScript Object Notation).

{{% /alert %}}

## **Converti Workbook Excel in JSON**

L’API di Aspose.Cells supporta la conversione dei fogli di calcolo in formato JSON. Per esportare la cartella di lavoro in JSON, passa [**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) come secondo parametro del metodo [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Puoi anche usare la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) per specificare impostazioni aggiuntive per l’esportazione del foglio di lavoro in JSON.

L'esempio di codice seguente dimostra l'esportazione del foglio attivo in JSON utilizzando il membro di enumerazione [**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Si prega di consultare il codice per convertire [file sorgente](book1.xlsx) nel [file JSON di output](book1.json) generato dal codice come riferimento.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    U16String outputFilePath = srcDir + u"book1.json";
    workbook.Save(outputFilePath);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Convertire CSV in JSON](/cells/it/cpp/convert-csv-to-json/)
- [Converti Excel in JSON](/cells/it/cpp/convert-excel-to-json/)
- [Convertire JSON in CSV](/cells/it/cpp/convert-json-to-csv/)
- [Converti JSON in Excel](/cells/it/cpp/convert-json-to-excel/)
