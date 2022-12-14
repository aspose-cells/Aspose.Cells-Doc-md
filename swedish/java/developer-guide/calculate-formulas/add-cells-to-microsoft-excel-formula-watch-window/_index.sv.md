---
title: Lägg till Cells i Microsoft Excel Formula Watch Window
type: docs
weight: 20
url: /sv/java/add-cells-to-microsoft-excel-formula-watch-window/
---
## **Möjliga användningsscenarier**

Microsoft Excel Watch Window är ett användbart verktyg för att titta på cellvärdena och dess formler bekvämt i ett fönster. Du kan öppna*Watch Window*använda Microsoft Excel genom att klicka på*Formler > Titta* *Fönster*. Den har*Lägg till Watch*knapp som kan användas för att lägga till cellerna för inspektion. På samma sätt kan du använda[**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int)) metod för att lägga till celler i*Watch Window*använder Aspose.Cells API.

## **Lägg till Cells i Microsoft Excel Formula Watch Window**

 Följande exempelkod anger formeln för cellerna C1 och E1 och lägger till dem båda till*Watch Window*. Den sparar sedan arbetsboken som[utdata Excel-fil](67338509.xlsx). Om du öppnar utdata Excel-filen och tittar på*Watch Window*, kommer du att se båda cellerna som visas i den här skärmdumpen.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
