---
title: Rensa filter i pivot tabell
type: docs
weight: 130
url: /sv/net/clear-filter-in-pivot-table/
description: Hur man rensar PivotFilter från en specifik PivotField i pivot tabellen med Aspose.Cells.
keywords: Rensa PivotFilter i pivot tabell.
---

## **Möjliga användningsscenario**
När du skapar en pivot-tabell med känd data och vill filtrera pivot-tabellen, måste du lära dig och använda filter. Det kan hjälpa dig att effektivt filtrera ut de data du vill ha. Genom att använda Aspose.Cells API kan du operaera filter på fältvärden i Pivot-tabeller. 

## **Rensa filter i pivot-tabell i Excel**
Rensa filter i pivot-tabell i Excel, följ dessa steg:

1. Välj den pivot-tabell du vill rensa filtret på. 
2. Klicka på nedåtpilen för filtret som du vill rensa i pivot-tabellen.
3. Välj "Rensa filter" från rullgardinsmenyn.
<img src="1.png" width=80% />
4. Om du vill rensa alla filter från pivottabellen kan du också klicka på knappen "Rensa filter" på fliken PivotTable Analyze i Excel-ribbon.
<img src="2.png" width=80% />

## **Rensa filter i pivottabell med C#**
Rensa filter i pivottabell med hjälp av Aspose.Cells. Se följande exempelkod. 
1. Ställ in datan och skapa en pivottabell baserad på det. 
2. Lägg till ett filter på radfältet i pivottabellen. 
3. Spara arbetsboken i [utdata XLSX](ut_add.xlsx) -format. Efter att exemplet har körts läggs en pivottabell med top10-filter till i arket. 
4. Rensa filtret på ett specifikt pivotfält. Efter att koden har körts för att rensa filtret kommer filtret på det specifika pivotfältet att rensas. Vänligen kontrollera [utdata XLSX](ut_delete.xlsx).

## **Exempelkod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
