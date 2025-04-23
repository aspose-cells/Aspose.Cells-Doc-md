---
title: Exportar Excel a HTML con líneas de cuadrícula con C++
linktitle: Exportar Excel a HTML con Líneas de Cuadrícula
type: docs
weight: 40
url: /es/cpp/export-excel-to-html-with-gridlines/
description: Aprenda cómo exportar archivos de Excel a HTML con líneas de cuadrícula usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Si deseas exportar tu archivo de Excel en HTML con líneas de cuadrícula, utiliza la propiedad [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) y configúrala en **true**.

{{% /alert %}} 

## **Exportar Excel a HTML con Líneas de Cuadrícula**
El siguiente código de ejemplo crea un libro y llena su hoja con algunos valores, luego lo guarda en formato HTML configurando [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) en **true**.

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

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Fill worksheet with some integer values
    for (int r = 0; r < 10; r++)
    {
        for (int c = 0; c < 10; c++)
        {
            ws.GetCells().Get(r, c).PutValue(r * 1);
        }
    }

    // Save workbook in HTML format and export gridlines
    HtmlSaveOptions opts;
    opts.SetExportGridLines(true);
    wb.Save(outDir + u"ExportToHTMLWithGridLines_out.html", opts);

    std::cout << "Workbook exported to HTML with gridlines successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
