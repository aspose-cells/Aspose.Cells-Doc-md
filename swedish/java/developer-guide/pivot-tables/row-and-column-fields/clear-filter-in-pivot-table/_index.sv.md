---
title: Rensa filter i pivot tabell
type: docs
weight: 130
url: /sv/java/clear-filter-in-pivot-table/
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

## **Rensa filter i Pivot-tabellen**
Vänligen se följande exempelkod. Det ställer in datat och skapar en PivotTabell baserad på det. Lägg sedan till ett filter på radfältet i Pivot-tabellen. Slutligen sparar den arbetsboken i formatet [output XLSX](out_add.xlsx). Efter att ha utfört exempelkoden har en pivot-tabell med top10-filter lagts till i kalkylarket. Efter att ha lagt till ett filter, när vi behöver oberikatat data kan vi rensa filtret på ett specifikt pivoton. Efter att ha utfört koden för att rensa filtret, kommer filtret på det specifika pivotelementet rensas. Var vänlig och kolla [output XLSX](out_delete.xlsx).

## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
