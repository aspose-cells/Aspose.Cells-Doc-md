---
title: Exportera kalkylblads CSS separat i utdata HTML med C++
linktitle: Exportera arbetsbladets CSS separat i utdata HTML filen
type: docs
weight: 80
url: /sv/cpp/export-worksheet-css-separately-in-output/
description: Lär dig hur du exporterar kalkylblads CSS separat när du konverterar Excel filer till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Aspose.Cells ger funktionen att exportera worksheet CSS separat när du konverterar din Excel-fil till HTML. Använd [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/)-egenskapen för detta ändamål och ställ in den på **true** vid sparning av Excel-filen i HTML-format.

## **Exportera arbetsbladets CSS separat i utdata-HTML-filen**

Följande exempelkod skapar en Excel-fil, lägger till lite text i cellan **B5** i **röd** färg och sparar sedan den i HTML-format med [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/)-egenskapen. Se [utdata-HTML-filen](60489766.zip) genererad av koden för referens. Du hittar **stylesheet.css** i utdata som ett resultat av exempelkoden.

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Exportera enkelbladig arbetsbok till HTML**

När en arbetsbok med flera blad konverteras till HTML med Aspose.Cells skapas en HTML-fil tillsammans med en mapp som innehåller CSS och flera HTML-filer. När denna HTML-fil öppnas i webbläsaren är flikarna synliga. Samma beteende krävs för en arbetsbok med ett enda arbetsblad när den konverteras till HTML. Tidigare skapades ingen separat mapp för enbladiga arbetsböcker, och endast en HTML-fil skapades. En sådan HTML-fil visar inte någon flik när den öppnas i webbläsaren. MS Excel skapar också en riktig mapp och HTML för ett enblad, och därför implementeras samma beteende med Aspose.Cells API:er. Mallen kan laddas ner från länken nedan för användning i exempel-koden nedan:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Exempelkod**

```c++
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
