---
title: Rensa filter i pivottabellen
type: docs
weight: 130
url: /sv/net/clear-filter-in-pivot-table/
description: Hur man rensar pivotfiltret från det specifika pivotfältet i pivottabellen med Aspose.Cells.
keywords: Clear PivotFilter in pivot table.
---
##  **Möjliga användningsscenarier**
 När du skapar en pivottabell med känd data och vill filtrera pivottabellen måste du lära dig och använda filter. Det kan hjälpa dig att filtrera bort den information du vill ha effektivt. Genom att använda Aspose.Cells API kan du använda filter på fältvärden i pivottabeller.

##  **Rensa filter i pivottabell i Excel**
Rensa filter i pivottabell i Excel, följ dessa steg:

1.  Välj den pivottabell som du vill rensa filtret till.
2. Klicka på rullgardinsmenyn för filtret du vill rensa i pivottabellen.
3. Välj "Rensa filter" från rullgardinsmenyn.
<img src="1.png" width=80% />
4. Om du vill rensa alla filter från pivottabellen kan du också klicka på knappen "Rensa filter" på fliken Pivottabellanalys på menyfliksområdet i Excel.
<img src="2.png" width=80% />

##  **Rensa filtret i pivottabellen med C#**
 Rensa filtret i pivottabellen med Aspose.Cells. Se följande exempelkod.
1.  Ställ in data och skapa en pivottabell baserat på den.
2. Lägg till ett filter i pivottabellens radfält.
 3. Spara arbetsboken i[utgång XLSX](out_add.xlsx) formatera. Efter exekvering av exempelkoden läggs en pivottabell med top10-filter till i kalkylbladet.
 4. Rensa filtret på ett specifikt pivotfält. Efter exekvering av koden för att rensa filtret kommer filtret på det specifika pivotfältet att rensas. Vänligen kontrollera[utgång XLSX](out_delete.xlsx).

##  **Exempelkod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}