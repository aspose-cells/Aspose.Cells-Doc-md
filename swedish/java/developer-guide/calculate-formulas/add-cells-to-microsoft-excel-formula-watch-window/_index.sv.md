---
title: Lägg till celler i Microsoft Excel Formelövervakningsfönstret
type: docs
weight: 20
url: /sv/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Möjliga användningsscenario**

Microsoft Excel Watch Window är ett användbart verktyg för att bekvämt övervaka cellvärden och dess formler i ett fönster. Du kan öppna *Watch Window* med Microsoft Excel genom att klicka på *Formler > Watch* *Fönster*. Det har en *Lägg till Watch*-knapp som kan användas för att lägga till celler för inspektion. På liknande sätt kan du använda [**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add-int-int-)-metoden för att lägga till celler i *Watch Window* med Aspose.Cells API.

## **Lägg till celler i Microsoft Excel Formelövervakningsfönstret**

Följande provkod anger formeln för cellerna C1 och E1 och lägger till båda i *Watch Window*. Sedan sparar den kalkylbladet som [utdata Excel-fil](67338509.xlsx). Om du öppnar utdata Excel-filen och visar *Watch Window* kommer du att se båda cellerna som visas i denna skärmbild.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
{{< app/cells/assistant language="java" >}}
