---
title: Editar Hiperenlaces de la Hoja de Trabajo con C++
linktitle: Editando hipervínculos de la hoja de cálculo
type: docs
weight: 330
url: /es/cpp/editing-hyperlinks-of-worksheet/
description: Aprende cómo editar hiper en la hoja de trabajo usando la API Aspose.Cells for C++.
keywords: Editar Hipervínculos, Editar Hipervínculos de la Hoja de Cálculo, Editar hipervínculo de celda, Acceder a todos los hipervínculos de la hoja de cálculo
---

{{% alert color="primary" %}}

Aspose.Cells le permite acceder a todos los hipervínculos de la hoja de cálculo mediante la colección [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Puede acceder a cada hipervínculo de esta colección uno por uno y editar sus propiedades.

{{% /alert %}}

El siguiente código de ejemplo accede a todos los hiper en la hoja de trabajo y cambia su propiedad [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/) al sitio web de Aspose.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
