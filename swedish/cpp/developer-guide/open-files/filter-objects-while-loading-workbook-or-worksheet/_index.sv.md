---
title: Filtrera objekt medan du laddar arbetsbok eller kalkylblad med C++
linktitle: Filtrera objekt när du laddar arbetsbok eller kalkylblad
type: docs
weight: 330
url: /sv/cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Lär dig hur du filtrerar objekt som diagram, former och villkorlig formatering medan du laddar arbetsboken eller kalkylblad med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
Använd gärna egenskapen [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) när du filtrerar data från arbetsboken. Men om du vill filtrera data från enskilda kalkylblad måste du åsidosätta metoden [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). Ange ett lämpligt värde från enumerationen [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) vid skapandet eller arbetet med [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

Enumerationen [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) har följande möjliga värden.

- Alla
- Bokinställningar
- CellTom
- CellBool
- CellData
- CellFel
- CellNumeriskt
- CellSträng
- CellVärde
- Chart
- VillkorligFormatering
- DataValidering
- DefinieradeNamn
- Dokumentegenskaper
- Formel
- Hyperlänkar
- SammanslagnaOmråde
- PivotTabell
- Inställningar
- Form
- ArkData
- Arkinställningar
- Struktur
- Stil
- Tabell
- VBA
- XmlKarta

## **Filtrera objekt när du laddar arbetsbok**
Följande exempelkod illustrerar hur du filtrerar diagram från arbetsboken. Kontrollera den [exempel-Excel-filen](5115258.xlsx) som används i denna kod och den [utdata PDF](5115257.pdf) som genererats av den. Som du kan se i utdata PDF:en har alla diagram filtrerats bort från arbetsboken.

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

    // Filter charts from the workbook
    LoadOptions lOptions;
    lOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Load the workbook with the above filter
    U16String inputFilePath = srcDir + u"sampleFilterCharts.xlsx";
    Workbook workbook(inputFilePath, lOptions);

    // Save worksheet to a single PDF page
    PdfSaveOptions pOptions;
    pOptions.SetOnePagePerSheet(true);

    // Save the workbook in PDF format
    U16String outputFilePath = outDir + u"sampleFilterCharts.pdf";
    workbook.Save(outputFilePath, pOptions);

    std::cout << "Workbook saved successfully with filtered charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Filtrera objekt när du laddar kalkylblad**
Följande exempelkod laddar den [ursprungliga excel-filen](5115255.xlsx) och filtrerar följande data från dess kalkylblad med en anpassad filter.

- Det filtrerar diagram från kalkylbladet som heter NoCharts.
- Det filtrerar former från kalkylbladet som heter NoShapes.
- Det filtrerar villkorlig formatering från kalkylbladet som heter NoConditionalFormatting.

När den laddar [ursprungliga excel-filen](5115255.xlsx) med en anpassad filter tar den bilderna av alla kalkylblad en efter en. Här är utdata bilderna för din referens. Som du kan se har den första bilden inga diagram, den andra bilden har inga former och den tredje bilden har ingen villkorlig formatering.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    void StartSheet(Worksheet& sheet) override
    {
        U16String sheetName = sheet.GetName();

        if (sheetName == u"NoCharts")
        {
            // Load everything and filter charts
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Chart)));
        }

        if (sheetName == u"NoShapes")
        {
            // Load everything and filter shapes
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Drawing)));
        }

        if (sheetName == u"NoConditionalFormatting")
        {
            // Load everything and filter conditional formatting
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::ConditionalFormatting)));
        }
    }
};

// Add main function to serve as entry point
int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Cleanup();
    return 0;

}
```

Så här använder du klassen CustomLoadFilter enligt kalkylbladsnamn.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    CustomLoadFilter() : LoadFilter(LoadDataFilterOptions::All) {}
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter worksheets using CustomLoadFilter class
    LoadOptions loadOpts;
    CustomLoadFilter customLoadFilter;
    loadOpts.SetLoadFilter(&customLoadFilter);

    // Load the workbook with filter defined in CustomLoadFilter class
    Workbook workbook(srcDir + u"sampleCustomFilteringPerWorksheet.xlsx", loadOpts);

    // Take the image of all worksheets one by one
    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        // Access worksheet at index i
        Worksheet worksheet = sheets.Get(i);

        // Create an instance of ImageOrPrintOptions
        // Render entire worksheet to image
        ImageOrPrintOptions imageOpts;
        imageOpts.SetOnePagePerSheet(true);
        imageOpts.SetImageType(Aspose::Cells::Drawing::ImageType::Png);

        // Convert worksheet to image
        SheetRender render(worksheet, imageOpts);
        render.ToImage(0, outDir + u"outputCustomFilteringPerWorksheet_" + worksheet.GetName() + u".png");
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
