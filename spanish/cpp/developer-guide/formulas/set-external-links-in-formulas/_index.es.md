---
title: Establecer enlaces externos en fórmulas con C++
linktitle: Establecer vínculos externos en fórmulas
type: docs
weight: 20
url: /es/cpp/set-external-links-in-formulas/
description: Aprende cómo incluir enlaces a archivos externos en fórmulas usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

A veces, es necesario incluir enlaces a archivos externos en fórmulas, por ejemplo, para evaluar un valor de celda o rango en comparación con ellos. Aspose.Cells proporciona esta función y este documento explica cómo utilizarla.

{{% /alert %}} 

El código de ejemplo a continuación muestra cómo incluir archivos externos en fórmulas.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get first Worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get Cells collection
    Cells cells = sheet.GetCells();

    // Set formula with external links
    cells.Get(u"A1").SetFormula(U16String(u"=SUM('[") + srcDir + u"book1.xlsx]Sheet1'!A2, '[" + srcDir + u"book1.xlsx]Sheet1'!A4)");

    // Set formula with external links
    cells.Get(u"A2").SetFormula(U16String(u"='[") + srcDir + u"book1.xlsx]Sheet1'!A8");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully with external links!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
