---
title: Ändra cellplanering och behåll befintlig formatering med C++
description: Använd Aspose.Cells biblioteket för att ändra cells justering och behålla befintlig formatering
keywords: Aspose.Cells, C++, celljustering, bevara befintlig formatering
type: docs
weight: 340
url: /sv/cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Möjliga användningsscenario**

 Ibland vill du ändra inriktningen för flera celler men också behålla befintlig formatering. Aspose.Cells gör det möjligt med [**GetAlignments()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getalignments/)-egenskapen. Om du ställer in den till **true**, kommer justeringen att ändras, annars inte. Observera att [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag)-objektet skickas som parameter till [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)-metoden som faktiskt tillämpar formateringen på en cellområde.

## **Ändra cellers justering och behåll befintlig formatering**

Den följande exempelkoden läser in den [exempel Excel-filen](67338585.xlsx), skapar området och centrera justerar det horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmdump jämför exempel Excel-filen och [utdata Excel-filen](67338586.xlsx) och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centralt justerade horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing cells with formatting.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx");

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create cells range.
    Range rng = ws.GetCells().CreateRange(u"B2:D7");

    // Create style object.
    Style st = wb.CreateStyle();

    // Set the horizontal and vertical alignment to center.
    st.SetHorizontalAlignment(TextAlignmentType::Center);
    st.SetVerticalAlignment(TextAlignmentType::Center);

    // Create style flag object.
    StyleFlag flag;

    // Set style flag alignments true. It is the most crucial statement.
    // Because if it is false, no changes will take place.
    flag.SetAlignments(true);

    // Apply style to range of cells.
    rng.ApplyStyle(st, flag);

    // Save the workbook in XLSX format.
    wb.Save(outputDir + u"outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
