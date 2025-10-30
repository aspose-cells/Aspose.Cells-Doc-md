---
title: Exportera Excel till HTML med rutnätlinjer med C++
linktitle: Exportera Excel till HTML med rutnätslinjer
type: docs
weight: 40
url: /sv/cpp/export-excel-to-html-with-gridlines/
description: Lär dig hur du exporterar Excel filer till HTML med rutnätlinjer med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Om du vill exportera din Excel-fil till HTML med rutnätlinjer, använd då egenskapen [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) och ställ in den på **true**.

{{% /alert %}} 

## **Exportera Excel till HTML med rutnätslinjer**
Följande exempel kod skapar en arbetsbok och fyller dess kalkylblad med vissa värden och sparar den sedan i HTML-format efter att ha ställt in [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) till **true**.

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
