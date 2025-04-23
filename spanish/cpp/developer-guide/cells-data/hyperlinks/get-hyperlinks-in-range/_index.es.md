---
title: Obtener Hiperenlaces en un Rango con C++
linktitle: Obtener Hipervínculos en Rango
type: docs
weight: 100
url: /es/cpp/get-hyperlinks-in-range/
description: Aprende cómo obtener hiper en rangos usando la API Aspose.Cells for C++.
keywords: Obtener hipervínculos en rango, Obtener todos los hipervínculos en el rango seleccionado, Eliminar hipervínculo en rango, Eliminar los hipervínculos en el rango seleccionado
---

## **Obtener Hipervínculos en Rango**

La clase [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) proporciona una propiedad [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/) que devuelve todos los hipervínculos en el rango seleccionado. También puede eliminar el hipervínculo llamando al método [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
