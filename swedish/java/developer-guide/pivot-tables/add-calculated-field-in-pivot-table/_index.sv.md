---
title: Lägg till beräknat fält i pivottabell
type: docs
weight: 130
url: /sv/java/add-calculated-field-in-pivot-table/
description: Hur man lägger till ett beräknat fält i pivottabell med Aspose.Cells.
keywords: Lägger till ett beräknat fält i pivottabell.
---

## **Möjliga användningsscenario**
När du skapar en pivottabell baserad på kända data finner du att datan i den inte är det du vill ha. Den data du vill ha är kombinationen av denna ursprungliga data. Till exempel behöver du lägga till, subtrahera, multiplicera och dividera den ursprungliga datan innan du vill ha datan. Vid den här tiden behöver du bygga ett beräknat fält och ställa in motsvarande formel för beräkning. Utför sedan vissa statistik och andra operationer på det beräknade fältet. 

## **Lägg till beräknat fält i pivottabell i Excel**
Så här lägger du till ett beräknat fält i en pivot-tabell i Excel, följ dessa steg:

1. Välj pivottabellen som du vill lägga till ett beräknat fält i. 
2. Gå till fliken Pivottabell analysera på menyfliken.
3. Klicka på "Fält, artiklar och uppsättningar" och välj sedan "Beräknat fält" i rullgardinsmenyn.
4. I fältet "Namn" anger du ett namn för det beräknade fältet.
5. I fältet "Formel" ange formeln du vill använda med lämpliga PivotTable-fältnamn och matematiska operatorer. 
<br>
<img src="1.png" width=80% />
6. Klicka på "ok" för att skapa det beräknade fältet.
7. Det nya beräknade fältet kommer att visas i PivotTable Field List under avsnittet Värden.
8. Dra det beräknade fältet till värdesektionen i PivotTable för att visa de beräknade värdena.
<br>
<img src="2.png" width=80% />

## **Lägg till beräknat fält i Pivot-tabell**
Se följande exempelkod. Koden ställer först in den ursprungliga datan och skapar en pivot tabell. Sedan skapas det beräknade fältet enligt det befintliga PivotField i pivot tabellen och läggs det beräknade fältet till dataområdet. Till sist sparas arbetsboken i [output XLSX](out.xlsx)-formatet. Efter att exempelkoden har körts, har en pivot-tabell med ett beräknat fält lagts till i kalkylbladet.

## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
