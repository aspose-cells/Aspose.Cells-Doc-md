---
title: Lägg till beräknat fält i pivottabellen
type: docs
weight: 130
url: /sv/python-net/add-calculated-field-in-pivot-table/
description: Hur man lägger till ett beräknat fält i pivottabellen med Aspose.Cells for Python via .NET.
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
5. I fältet "Formel" anger du formeln för den beräkning du vill utföra med hjälp av lämpliga pivottabellfältnamn och matematiska operatorer.
<br>
<img src="1.png" width=80% />
6. Klicka på "ok" för att skapa det beräknade fältet.
7. Det nya beräknade fältet kommer att visas i Pivottabellfältlistan under avsnittet Värden.
8. Dra det beräknade fältet till avsnittet Värden i pivottabellen för att visa de beräknade värdena.
<br>
<img src="2.png" width=80% />

##  **Lägg till beräknat fält i pivottabellen med C#**
Lägg till beräknat fält i Excel-fil med Aspose.Cells for Python via .NET. Se följande exempelkod. Efter exekvering av exempelkoden läggs en pivottabell med beräknat fält till i kalkylbladet.
1.  Ställ in originaldata och skapa en pivottabell.
2. Skapa det beräknade fältet enligt det befintliga pivotfältet i pivottabellen.
 3. Lägg till det beräknade fältet i dataområdet.
 4. Slutligen sparar den arbetsboken i[utgång XLSX](out.xlsx) formatera.

##  **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Add-calculated-field-in-PivotTable.py" >}}
