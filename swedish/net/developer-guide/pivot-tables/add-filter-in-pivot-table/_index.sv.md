---
title: Pivottfilter
type: docs
weight: 130
url: /sv/net/add-or-clear-pivot-filter/
description: Lär dig hur du lägger till ett filter i pivot tabell med Aspose.Cells.
keywords: Lägga till ett filter i pivot tabell utan office 2013, office 2016, office 2019 och office 365.
---

## **Möjliga användningsscenario**
När du skapar en pivottabell med kända data och vill filtrera pivottabellen måste du lära dig och använda filter. Det kan hjälpa dig att effektivt filtrera ut de data du vill ha. Genom att använda Aspose.Cells API kan du lägga till och rensa filter på fältvärden i pivottabeller. 

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
Se följande exempelkod. Den anger datan och skapar en pivot-tabell baserad på den. Sedan läggs ett filter på radfältet i pivot-tabellen. Slutligen sparas arbetsboken i [utmatnings XLSX](filterout.xlsx) format. Efter att ha kört exempelkoden läggs en pivottabell med topp10-filter till arbetsbladet.

### **Exempelkod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Add-filter-in-PivotTable.cs" >}}

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
Rensa filter i pivottabell med hjälp av Aspose.Cells. Se följande exempelkod. 
1. Ställ in datan och skapa en pivottabell baserad på det. 
2. Lägg till ett filter på radfältet i pivottabellen. 
3. Spara arbetsboken i [utdata XLSX](ut_add.xlsx) -format. Efter att exemplet har körts läggs en pivottabell med top10-filter till i arket. 
4. Rensa filtret på ett specifikt pivotfält. Efter att koden har körts för att rensa filtret kommer filtret på det specifika pivotfältet att rensas. Vänligen kontrollera [utdata XLSX](ut_delete.xlsx).

### **Exempelkod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
