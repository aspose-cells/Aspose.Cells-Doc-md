---
title: Formeln anstelle von Werten in einem Arbeitsblatt mit C++ anzeigen
linktitle: Formeln anstelle von Werten anzeigen
type: docs
weight: 20
url: /de/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Dieses Beispiel bietet Code, um die C++ API zu verwenden, um Formeln programmatisch anstelle von Werten in einem Excel Arbeitsblatt oder Spreadsheet anzuzeigen.
---

{{% alert color="primary" %}}

In Microsoft Excel ist es möglich, Formeln anstelle von berechneten Werten anzuzeigen, indem Sie die Option **Formeln anzeigen** im **Formeln**-Menüband verwenden. Wenn Formeln angezeigt werden, zeigt Microsoft Excel die Formeln im Arbeitsblatt an. Sie können das Gleiche mit Aspose.Cells erreichen.

{{% /alert %}}

Aspose.Cells bietet eine [**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/)-Eigenschaft. Setzen Sie diese auf **true**, um Microsoft Excel anzuweisen, Formeln anzuzeigen.

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
