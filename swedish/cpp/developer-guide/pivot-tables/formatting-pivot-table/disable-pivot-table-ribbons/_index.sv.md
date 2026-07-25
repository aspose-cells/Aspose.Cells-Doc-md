---
title: Inaktivera PivotTabellflikar med C++
linktitle: Inaktivera pivottabellribbon
type: docs
weight: 90
url: /sv/cpp/disable-pivot-table-ribbons/
description: Lär dig hur man avaktiverar pivot tabellflikar i Excel filer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Pivot-tabellbaserade rapporter är användbara men sårbara för fel om målbrukare inte har tillräcklig kunskap om Excel för att konfigurera dessa rapporter. I dessa fall vill organisationer begränsa användare från att kunna ändra en pivot-tabellbaserad rapport. Vanliga funktioner som att lägga till ytterligare filter, slicers, fält eller ändra ordningen i rapporten rekommenderas ofta inte för alla användare. Å andra sidan ska dessa användare också kunna uppdatera rapporten och använda befintliga filter eller slicers. Aspose.Cells har gett utvecklare möjligheten att begränsa användare från att ändra dessa rapporter under skapandet. För detta ändamål erbjuder Excel en funktion att inaktivera pivot-tabellfliken, och detta stöds även av Aspose.Cells. Utvecklare kan inaktivera fliken som innehåller kontroller för att ändra dessa rapporter.

{{% /alert %}}

## **Inaktivera pivottabellribbon med hjälp av PivotTable.EnableWizard**

Följande kod demonstrerar denna funktion genom att komma åt en pivot-tabell från ett blad och sedan ställa in [**GetEnableWizard()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getenablewizard/) till **falskt**. En exempel-pivot-tabell kan laddas ner från denna [länk](pivot_table_test.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
