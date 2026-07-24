---
title: Pivottfilter
type: docs
weight: 130
url: /sv/java/add-or-clear-pivot-filter/
description: Lär dig hur du lägger till ett filter i pivot tabell med Aspose.Cells Java biblioteket.
keywords: Lägga till ett filter i pivot tabell utan office 2013, office 2016, office 2019 och office 365.
---

## **Möjliga användningsscenario**
När du skapar en pivot-tabell med känd data och vill filtrera pivot-tabellen behöver du lära dig och använda filter. Det kan hjälpa dig att effektivt filtrera ut önskad data. Genom att använda Aspose.Cells Java API kan du lägga till filter på fältvärden i pivot tabeller. 

## **Lägg till filter i pivottabell i Excel**
Lägg till filter i pivottabell i Excel, följ dessa steg:

1. Välj den pivot-tabell du vill rensa filtret på. 
2. Klicka på nedåtpilen för filtret du vill lägga till i pivottabellen.
3. Välj "Topp 10" från rullgardinsmenyn.
<br>
<img src="3.png" width=80% />
4. Ange visningsläge och antalet filter.
<br>
<img src="4.png" width=80% />

## **Lägg till filter i pivottabell**
Se följande exempelkod. Den ställer in datan och skapar en PivotTable baserat på den. Sedan läggs ett filter på radfältet i pivot tabellen. Slutligen sparas arbetsboken i [output XLSX](out.xlsx)-formatet. Efter att exempelkoden har körts har en pivot-tabell med top10-filter lagts till i kalkylbladet.

### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-filter-in-PivotTable.java" >}}


## **Rensa filter i pivottabell i Excel**
Rensa filter i pivot-tabell i Excel, följ dessa steg:

1. Välj den pivot-tabell du vill rensa filtret på. 
2. Klicka på nedåtpilen för filtret som du vill rensa i pivot-tabellen.
3. Välj "Rensa filter" från rullgardinsmenyn.
<br>
<img src="1.png" width=80% />
4. Om du vill rensa alla filter från pivottabellen kan du också klicka på knappen "Rensa filter" på fliken PivotTable Analyze i Excel-ribbon.
<br>
<img src="2.png" width=80% />

## **Rensa filter i pivottabell**
Vänligen se följande exempelkod. Det ställer in datat och skapar en PivotTabell baserad på det. Lägg sedan till ett filter på radfältet i Pivot-tabellen. Slutligen sparar den arbetsboken i formatet [output XLSX](out_add.xlsx). Efter att ha utfört exempelkoden har en pivot-tabell med top10-filter lagts till i kalkylarket. Efter att ha lagt till ett filter, när vi behöver oberikatat data kan vi rensa filtret på ett specifikt pivoton. Efter att ha utfört koden för att rensa filtret, kommer filtret på det specifika pivotelementet rensas. Var vänlig och kolla [output XLSX](out_delete.xlsx).

### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
