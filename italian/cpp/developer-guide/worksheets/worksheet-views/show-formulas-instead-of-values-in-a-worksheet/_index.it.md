---
title: Mostra formule invece di valori in un foglio di lavoro con C++
linktitle: Mostra Formule invece di Valori
type: docs
weight: 20
url: /it/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Questo articolo fornisce esempio di codice per usare l API C++ per visualizzare programmaticamente formule anziché valori in un foglio di lavoro di Excel.
---

{{% alert color="primary" %}}

È possibile mostrare le formule invece dei valori calcolati in Microsoft Excel utilizzando l'opzione **Mostra Formule** dalla scheda **Formule**. Quando le formule sono visualizzate, Microsoft Excel mostra le formule nel foglio di lavoro. Puoi ottenere lo stesso risultato utilizzando Aspose.Cells.

{{% /alert %}}

Aspose.Cells fornisce una proprietà [**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/). Imposta questo su **true** per impostare Microsoft Excel per mostrare le formule.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"source.xlsx";

    // Load the source workbook
    Workbook workbook(filePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Show formulas of the worksheet
    worksheet.SetShowFormulas(true);

    // Save the workbook
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Formulas shown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
