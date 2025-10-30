---
title: Esporta Excel in HTML con linee di griglia usando C++
linktitle: Esportare Excel in HTML con linee della griglia
type: docs
weight: 40
url: /it/cpp/export-excel-to-html-with-gridlines/
description: Impara come esportare file Excel in HTML con linee di griglia usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Se vuoi esportare il tuo file Excel in HTML con le linee di griglia, utilizza la proprietà [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) e impostala su **true**.

{{% /alert %}} 

## **Esportare Excel in HTML con linee della griglia**
Il seguente esempio di codice crea un workbook e riempie il suo foglio di lavoro con alcuni valori e poi lo salva in formato HTML impostando [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) su **true**.

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
{{< app/cells/assistant language="cpp" >}}
