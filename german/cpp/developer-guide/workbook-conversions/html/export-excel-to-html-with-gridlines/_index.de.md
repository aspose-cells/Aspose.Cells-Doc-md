---
title: Excel mit Gitternetzlinien in C++ in HTML exportieren
linktitle: Excel in HTML mit Gitterlinien exportieren
type: docs
weight: 40
url: /de/cpp/export-excel-to-html-with-gridlines/
description: Erfahren Sie, wie Sie Excel Dateien mit Gitternetzlinien im HTML Format mithilfe von Aspose.Cells for C++ exportieren.
---

{{% alert color="primary" %}} 

Wenn Sie Ihre Excel-Datei mit Gitternetzlinien in HTML exportieren möchten, verwenden Sie bitte die Eigenschaft [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) und setzen Sie sie auf **true**.

{{% /alert %}} 

## **Excel in HTML mit Rasterlinien exportieren**
Der folgende Beispielcode erstellt eine Arbeitsmappe und füllt das Arbeitsblatt mit einigen Werten, speichert es dann im HTML-Format, nachdem die [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) auf **true** gesetzt wurde.

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
