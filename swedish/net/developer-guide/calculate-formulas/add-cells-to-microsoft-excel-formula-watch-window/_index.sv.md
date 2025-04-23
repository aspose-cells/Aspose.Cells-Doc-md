---
title: Lägg till celler i Microsoft Excel Formelövervakningsfönstret
description: Hur man använder Aspose.Cells biblioteket för att lägga till celler i formelövervakningsfönstret i Excel. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi manipulera cellerna i den och ange formler. Slutligen sparar vi den ändrade Excel filen på disk.
keywords: Aspose.Cells, Excel, Formelövervakningsfönster, Celler, Lägga till
type: docs
weight: 60
url: /sv/net/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Möjliga användningsscenario**

Microsoft Excel Watch Window är ett användbart verktyg för att bekvämt övervaka cellvärden och dess formler i ett fönster. Du kan öppna *Watch Window* i Microsoft Excel genom att klicka på *Formler > Watch* *Fönster*. Det har en *Lägg till övervakning* knapp som kan användas för att lägga till cellerna för inspektion. På liknande sätt kan du använda [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index)-metoden för att lägga till celler i *Watch Window* med Aspose.Cells API.

## **Lägg till celler i Microsoft Excel Formelövervakningsfönstret**

Följande kodexempel anger formeln för cellerna C1 och E1 och lägger till båda i Watch Window. Sedan sparar den arbetsboken som [utdata Excel-fil](67338481.xlsx). Om du öppnar utdata Excel-filen och visar *Watch Window*, kommer du att se båda cellerna som visas på denna skärmbild.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
{{< app/cells/assistant language="csharp" >}}
