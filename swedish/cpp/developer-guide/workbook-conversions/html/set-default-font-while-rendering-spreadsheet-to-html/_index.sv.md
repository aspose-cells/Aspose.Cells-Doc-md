---
title: Ställ in standardteckensnitt vid rendering av kalkylblad till HTML med C++
linktitle: Ange standardfonten vid rendering av kalkylblad till HTML
type: docs
weight: 370
url: /sv/cpp/set-default-font-while-rendering-spreadsheet-to/
description: Lär dig hur du ställer in standardteckensnitt vid rendering av kalkylblad till HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att ställa in standardteckensnitt vid rendering av kalkylblad till HTML. Använd [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) för detta ändamål. Denna egenskap är användbar om vissa celler i kalkylbladet har ogiltiga eller icke-existerande teckensnitt. Då kommer dessa celler att renderas med det teckensnitt som anges med [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) egenskapen.

{{% /alert %}}

## Ställ in standardtypsnittet vid rendering av kalkylblad till HTML

Den följande exempelkoden skapar en arbetsbok och lägger till lite text i cellen B4 på den första arbetsbladet och anger dess font till någon okänd/icke-existerande font. Sedan sparar den arbetsboken i HTML genom att ange olika standardfontnamn som Courier New, Arial, Times New Roman, osv.

Skärmbilden visar effekten av att ställa in olika standardteckensnittsnamn via [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) egenskap.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Koden genererar [utmatnings-HTML-fil med Courier New](5115516), [utmatnings-HTML med Arial](5115518) och [utmatnings-HTML-fil med Times New Roman](5115517).

## Exempelkod

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
