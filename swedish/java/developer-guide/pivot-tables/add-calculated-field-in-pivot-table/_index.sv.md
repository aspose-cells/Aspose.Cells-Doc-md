---
title: Lägg till beräknat fält i pivottabellen
type: docs
weight: 130
url: /sv/java/add-calculated-field-in-pivot-table/
description: Hur man lägger till ett beräknat fält i pivottabellen med Aspose.Cells.
keywords: Adding a calculated field in pivot table.
---
##  **Möjliga användningsscenarier**
 När du skapar en pivottabell baserad på känd data, upptäcker du att data i den inte är vad du vill ha. Datan du vill ha är kombinationen av dessa originaldata. Till exempel måste du addera, subtrahera, multiplicera och dividera originaldata innan du vill ha data. Vid denna tidpunkt måste du bygga ett beräknat fält och ställa in motsvarande formel för beräkning. Utför sedan lite statistik och andra operationer på det beräknade fältet.

##  **Lägg till beräknat fält i pivottabell i Excel**
Infoga ett beräknat fält i en pivottabell i Excel, följ dessa steg:

1.  Välj den pivottabell som du vill lägga till ett beräknat fält till.
2. Gå till fliken Pivottabellanalys på menyfliksområdet.
3. Klicka på "Fält, objekt och uppsättningar" och välj sedan "Beräknat fält" från rullgardinsmenyn.
4. I fältet "Namn" anger du ett namn för det beräknade fältet.
 5. I fältet "Formel" anger du formeln du vill utföra med hjälp av lämpliga pivottabellfältnamn och matematiska operatorer.
<br>
<img src="1.png" width=80% />
6. Klicka på "ok" för att skapa det beräknade fältet.
7. Det nya beräknade fältet kommer att visas i Pivottabellfältlistan under avsnittet Värden.
8. Dra det beräknade fältet till avsnittet Värden i pivottabellen för att visa de beräknade värdena.
<br>
<img src="2.png" width=80% />

##  **Lägg till beräknat fält i pivottabellen**
Se följande exempelkod. Koden ställer först in originaldata och skapar en pivottabell. Skapa sedan det beräknade fältet enligt det befintliga pivotfältet i pivottabellen och lägg till det beräknade fältet i dataområdet. Slutligen sparar den arbetsboken[utgång XLSX](out.xlsx) formatera. Efter exekvering av exempelkoden läggs en pivottabell med beräknat fält till i kalkylbladet.

##  **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
