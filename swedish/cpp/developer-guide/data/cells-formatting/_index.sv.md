---
title: Cells Formatering
type: docs
weight: 50
url: /sv/cpp/cells-formatting/
---
## **Format Cell eller intervall på Cells**
 Om du vill formatera cell eller cellområde, tillhandahåller Aspose.Cells[IS-stil](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)klass. Du kan utföra all formatering av cellen eller cellintervallet med den här klassen. Några av de saker som rör formatering som kan åstadkommas med IStyle-klassen följer

- Ställ in fyllningsfärg för cellen
- Ställ in cellens textomslutning
- Ställ in gränserna för cellerna som topp-, vänster-, botten- och högerkanter, etc.
- Ställ in teckensnittsfärg, teckenstorlek, teckensnittsnamn, strejk, fetstil, kursiv, understruken, etc.
- Ställ in texten horisontell eller vertikal justering till höger, vänster, topp, botten, mitten osv.

 Om du vill ställa in stilen för en enskild cell, använd[ICell->SetIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5) metod och om du vill ställa in stilen för ett cellintervall, använd då[IRange->ApplyIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)metod.
## **Exempelkod**
 Följande exempelkod formaterar cell C4 i kalkylbladet på olika sätt och skärmdumpen visar[output excel-fil](21266438.xlsx) genereras av den för din referens.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
