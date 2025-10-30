---
title: Trimma ledande tomma rader och kolumner vid export av kalkblad till CSV med C++
linktitle: Trimma ledande tomma rader och kolumner
type: docs
weight: 100
url: /sv/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Lär dig hur man trimmar ledande tomma rader och kolumner vid export av kalkblad till CSV med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland innehåller din Excel- eller CSV-fil ledande tomma kolumner eller rader. Till exempel, överväg denna rad:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Här är de första tre cellerna eller kolumnerna tomma. När du öppnar en sådan CSV-fil i Microsoft Excel, då tar Microsoft Excel bort dessa ledande tomma rader och kolumner.

Som standard tar inte Aspose.Cells bort ledande tomma kolumner och rader vid sparandet, men om du vill ta bort dem precis som Microsoft Excel gör, så tillhandahåller Aspose.Cells [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) egenskapen. Ställ in den till **true** och sedan kommer alla ledande tomma rader och kolumner att tas bort vid sparandet.

{{% alert color="primary" %}}

innan utgåvan av Aspose.Cells for C++ 20.4 var standardvärdet för [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) **false**. Sedan utgåvan 20.4 är standardvärdet för [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) **true.**

{{% /alert %}}

## **Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format**

Den följande exempelkoden laddar [käll-excelfilen](sampleTrimBlankColumns.xlsx) som har två ledande tomma kolumner. Den sparar först excelfilen i CSV-format utan ändringar och sedan ställer den in [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/)-egenskapen till **true** och sparar den igen. Skärmdumpen visar [käll-excelfilen](sampleTrimBlankColumns.xlsx), [utdata-CSV-filen utan beskärning](outputWithoutTrimBlankColumns.csv) och utdata-CSV-filen med beskärning(outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleTrimBlankColumns.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Save in csv format without trimming blank columns
    wb.Save(outDir + u"outputWithoutTrimBlankColumns.csv", SaveFormat::Csv);

    // Create TxtSaveOptions and set TrimLeadingBlankRowAndColumn to true
    TxtSaveOptions opts;
    opts.SetTrimLeadingBlankRowAndColumn(true);

    // Save in csv format with trimming blank columns
    wb.Save(outDir + u"outputTrimBlankColumns.csv", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
