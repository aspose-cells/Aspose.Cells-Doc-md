---
title: Renderizar hoja de trabajo a contexto gráfico con C++
linktitle: Renderizar hoja de cálculo en contexto gráfico
type: docs
weight: 300
url: /es/cpp/render-worksheet-to-graphic-context/
description: Aprende cómo renderizar una hoja de trabajo a un contexto gráfico usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells ahora puede renderizar una hoja de trabajo a un contexto gráfico. El contexto gráfico puede ser cualquier cosa como un archivo de imagen, pantalla o impresora, etc. Por favor, usa uno de los siguientes dos métodos para renderizar una hoja de trabajo a un contexto gráfico.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

El siguiente código ilustra cómo usar Aspose.Cells para renderizar una hoja de trabajo a un contexto gráfico. Una vez que ejecutes el código, imprimirá toda la hoja de trabajo y llenará el espacio vacío restante con color azul en el contexto gráfico y guardará la imagen como el archivo **OutputImage_out_.png**. Puedes usar cualquier archivo Excel de origen para probar este código. Por favor, también lee los comentarios dentro del código para mejor comprensión.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
