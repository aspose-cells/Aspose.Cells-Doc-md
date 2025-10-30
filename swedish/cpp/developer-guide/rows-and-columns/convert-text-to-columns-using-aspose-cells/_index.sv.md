---
title: Omvandla text till kolumner med Aspose.Cells med C++
linktitle: Konvertera Text till Kolumner
type: docs
weight: 30
url: /sv/cpp/convert-text-to-columns-using-aspose-cells/
description: Lär dig hur du konverterar text till kolumner i Excel filer med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan konvertera din text till kolumner med Microsoft Excel. Denna funktion är tillgänglig under *Data Tools* under *Data* fliken. För att dela innehållet i en kolumn till flera kolumner, bör datan innehålla en specifik avgränsare såsom ett kommatecken (eller något annat tecken) baserat på vilket Microsoft Excel delar innehållet i en cell till flera celler. Aspose.Cells tillhandahåller också denna funktion via [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) metoden.

## **Konvertera Text till Kolumner med Aspose.Cells**

Följande exempel förklarar användningen av [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) metod. Koden lägger först till några personnamn i kolumn A i det första kalkbladet. Förnamn och efternamn är separerade med ett mellanslag. Sedan tillämpar den [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) metod på kolumn A och sparar det som en utgångs-Excel-fil. Om du öppnar den [utgångs-Excel-filen](25395213.xlsx) ser du att förnamnen är i kolumn A medan efternamnen är i kolumn B, som visas i denna skärmbild.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Exempelkod**

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
