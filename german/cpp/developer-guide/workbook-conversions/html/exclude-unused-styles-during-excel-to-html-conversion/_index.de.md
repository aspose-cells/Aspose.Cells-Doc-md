---
title: Unbenutzte Stile während der Excel zu HTML Konvertierung mit C++ ausschließen
linktitle: Unbenutzte Stile ausschließen
type: docs
weight: 30
url: /de/cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Lernen, wie unbenutzte Stile während der Excel zu HTML Konvertierung mit Aspose.Cells for C++ ausgeschlossen werden.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel-Dateien können viele unbenutzte Stile enthalten. Beim Exportieren der Excel-Datei in HTML werden diese unbenutzten Stile ebenfalls exportiert, was die HTML-Größe erhöhen kann. Sie können unbenutzte Stile während der Konvertierung einer Excel-Datei in HTML mit der [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) Eigenschaft ausschließen. Wenn Sie sie auf **true** setzen, werden alle unbenutzten Stile vom Ausgab-HTML ausgeschlossen. Das folgende Bild zeigt einen Beispiel-Unbenutzten Stil im HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen**

Der folgende Beispielcode erstellt eine Arbeitsmappe und einen unbenutzten benannten Stil. Da [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) auf **true** gesetzt ist, wird dieser unbenutzte Stil nicht in das [Ausgabe-HTML](61767778.zip) exportiert. Wenn Sie es auf **false** setzen, wird dieser unbenutzte Stil im Ausgabe-HTML sichtbar sein, was Sie im HTML-Markup sehen können, wie im oben genannten Screenshot.

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create an unused named style
    Style unusedStyle = wb.CreateStyle();
    unusedStyle.SetName(u"UnusedStyle_XXXXXXXXXXXXXX");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some value in cell C7
    ws.GetCells().Get(u"C7").PutValue(u"This is sample text.");

    // Specify html save options, we want to exclude unused styles
    HtmlSaveOptions opts;

    // Comment this line to include unused styles
    opts.SetExcludeUnusedStyles(true);

    // Save the workbook in html format
    wb.Save(u"outputExcludeUnusedStylesInExcelToHTML.html", opts);

    std::cout << "Workbook saved successfully with unused styles excluded!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
