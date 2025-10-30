---
title: Imposta il font predefinito durante la conversione di un foglio di calcolo in HTML con C++
linktitle: Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML
type: docs
weight: 370
url: /it/cpp/set-default-font-while-rendering-spreadsheet-to/
description: Impara come impostare il font predefinito durante la conversione di un foglio di calcolo in HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells permette di impostare il font predefinito durante la conversione di un foglio di calcolo in HTML. Usa [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) a tale scopo. Questa proprietà è utile quando alcune celle di un foglio di calcolo hanno font non validi o inesistenti. Quindi, quelle celle verranno renderizzate con il font specificato dalla proprietà [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML

Il seguente codice di esempio crea un workbook e aggiunge del testo nella cella B4 del primo foglio di lavoro e imposta il suo carattere su un font sconosciuto/inesistente. Quindi salva il workbook in HTML impostando diversi nomi di carattere predefinito come Courier New, Arial, Times New Roman, ecc.

Lo screenshot mostra l'effetto di impostare nomi di font predefiniti diversi tramite la proprietà [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Il codice genera [file HTML di output con Courier New](5115516), il [file HTML con Arial](5115518) e il [file HTML di output con Times New Roman](5115517).

## Codice di esempio

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

    // Create workbook object and access first worksheet
    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"B4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell B4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    cell.SetStyle(st);

    // Now save the workbook in html format and set the default font to Courier New
    HtmlSaveOptions opts;
    opts.SetDefaultFontName(u"Courier New");
    wb.Save(outDir + u"out_courier_new_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Arial
    opts.SetDefaultFontName(u"Arial");
    wb.Save(outDir + u"out_arial_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Times New Roman
    opts.SetDefaultFontName(u"Times New Roman");
    wb.Save(outDir + u"times_new_roman_out.htm", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
