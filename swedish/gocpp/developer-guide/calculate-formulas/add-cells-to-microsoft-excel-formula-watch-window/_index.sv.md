---
title: Lägg till celler i Microsoft Excel Formel Watch Window med Golang via C++
linktitle: Lägg till celler till formelvaktfönster
description: Lär dig hur du använder Aspose.Cells for C++ för att lägga till celler i formelbevakningsfönstret i Excel. Ladda eller skapa en Excel fil, manipulera celler, ställ in formler och spara den modifierade filen.
keywords: Aspose.Cells, Excel, Formel bevakningsfönster, Cell, Lägg till, C++
type: docs
weight: 60
url: /sv/go-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Möjliga användningsscenario**

Microsoft Excel bevakningsfönster är ett användbart verktyg för bekvämt att övervaka cellvärden och deras formler i ett fönster. Du kan öppna *Bevakningsfönster* i Microsoft Excel genom att klicka på *Formler > Bevakningsfönster*. Det har knappen *Lägg till bevakning* som kan användas för att lägga till celler för inspektion. På liknande sätt kan du använda [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/go-cpp/cellwatchcollection/add_int_int/)-metoden för att lägga till celler i *Bevakningsfönstret* med Aspose.Cells API.

## **Lägg till celler i Microsoft Excel Formelövervakningsfönstret**

Följande exempelkod sätter formeln för cellerna C1 och E1 och lägger till båda i Bevaka fönstret. Den sparar sedan arbetsboken som en [utgångs Excel-fil](67338481.xlsx). Om du öppnar utgångs Excel-filen och tittar i *Bevakningsfönstret*, kommer du att se båda cellerna som visas i denna skärmdump.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCellsToMicrosoftExcelFormulaWatchWindow.go" >}}
