---
title: Escludi Stili Non Utilizzati durante la conversione da Excel a HTML con C++
linktitle: Escludi Stili Non Utilizzati
type: docs
weight: 30
url: /it/cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Scopri come escludere stili non utilizzati durante la conversione da Excel a HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

I file Microsoft Excel possono contenere tanti stili inutilizzati. Quando esporti il file Excel in formato HTML, anche questi stili inutilizzati vengono esportati, il che può aumentare la dimensione dell'HTML. Puoi escludere gli stili inutilizzati durante la conversione di un file Excel in HTML usando la proprietà [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/). Quando la imposti su **true**, tutti gli stili inutilizzati vengono esclusi dall'HTML di output. Il seguente screenshot mostra un esempio di stile inutilizzato all'interno dell'HTML di output.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Escludere Stili Non Utilizzati durante la conversione da Excel a HTML**

Il seguente esempio di codice crea un workbook e crea anche uno stile nominato inutilizzato. Poiché [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) è impostato su **true**, questo stile inutilizzato non verrà esportato nell'[HTML di output](61767778.zip). Tuttavia, se lo imposti su **false**, allora questo stile inutilizzato sarà presente nell'HTML di output, visibile nel markup HTML come mostrato nello screenshot sopra.

## **Codice di Esempio**

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
{{< app/cells/assistant language="cpp" >}}
