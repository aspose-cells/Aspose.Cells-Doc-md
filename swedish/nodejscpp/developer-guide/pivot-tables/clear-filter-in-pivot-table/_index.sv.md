---
title: Rensa filter i pivot tabell
type: docs
weight: 130
url: /sv/nodejs-cpp/clear-filter-in-pivot-table/
description: Hur man rensar PivotFilter från den specifika PivotField i pivottabellen med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js bibliotek, Rensa PivotFilter i pivottabell med Aspose.Cells for Node.js via C++ Excel bibliotek.
---

## **Möjliga användningsscenario**
När du skapar en pivottabell med känd data och vill filtrera pivottabellen måste du lära dig och använda filter. Det kan hjälpa dig att effektivt filtrera bort de data du vill ha. Med Aspose.Cells for Node.js via C++ API kan du operera filter på fältvärden i pivottabeller. 

## **Hur man rensar filter i pivot-tabell i Excel**
Rensa filter i pivot-tabell i Excel, följ dessa steg:

1. Välj den pivot-tabell du vill rensa filtret på. 
2. Klicka på nedåtpilen för filtret som du vill rensa i pivot-tabellen.
3. Välj "Rensa filter" från rullgardinsmenyn.
<img src="1.png" width=80% />
4. Om du vill rensa alla filter från pivottabellen kan du också klicka på knappen "Rensa filter" på fliken PivotTable Analyze i Excel-ribbon.
<img src="2.png" width=80% />

## **Hur man rensar filter i Pivot-tabell med Aspose.Cells for Node.js via C++**
Rensa filter i Pivot-tabell med hjälp av Aspose.Cells for Node.js via C++. Se följande exempelkod. 
1. Ställ in datan och skapa en pivottabell baserad på det. 
2. Lägg till ett filter på radfältet i pivottabellen. 
3. Spara arbetsboken i [utdata XLSX](ut_add.xlsx) -format. Efter att exemplet har körts läggs en pivottabell med top10-filter till i arket. 
4. Rensa filtret på ett specifikt pivotfält. Efter att koden har körts för att rensa filtret kommer filtret på det specifika pivotfältet att rensas. Vänligen kontrollera [utdata XLSX](ut_delete.xlsx).

## **Exempelkod**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-Clear-filter-in-PivotTable.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
