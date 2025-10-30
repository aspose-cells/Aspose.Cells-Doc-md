---
title: Skapa pivottabeller och pivotdiagram
type: docs
weight: 20
url: /sv/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: Hur man lägger till Pivot tabeller och Pivot diagram med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js bibliotek, Lägg till pivot tabeller och pivot diagram med Aspose.Cells for Node.js via C++ Excel bibliotek.
---

{{% alert color="primary" %}}

En pivottabell är en interaktiv sammanfattning av poster. Till exempel kan du ha hundratals faktura-poster i en lista i ett kalkylblad. En pivottabell kan summera fakturorna efter kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt omorganisera informationen i pivottabellen genom att dra knappar till en ny position.

Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu enklare att förstå data eftersom pivottabellen skapar delsummer och totaler automatiskt.

Aspose.Cells for Node.js via C++ stöder [pivot-tabeller](/cells/sv/nodejs-cpp/create-pivot-tables-and-pivot-charts/) och [pivot-diagram](/cells/sv/nodejs-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Lägg till pivot-tabeller och diagram med Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ tillhandahåller en särskild uppsättning klasser för att skapa pivot-tabeller. Dessa klasser används för att skapa och ställa in PivotTable-objekt, som fungerar som grundläggande byggstenar för en PivotTable:

- PivotField, ett fält i en pivottabellrapport.
- PivotFields, en samling av alla PivotField-objekt i en pivottabell.
- PivotTable, en pivottabellrapport på ett kalkylblad.
- PivotTables, en samling av alla PivotTable-objekt på kalkylbladet.

### **Förbered att använda Aspose.Cells for Node.js via C++**
1. Installera Aspose.Cells for Node.js via C++ från NPM, använd kommandot: $ npm install aspose.cells.node.
1. Du kan också följa steg-för-steg-instruktionerna för att installera "Aspose.Cells for Node.js via C++" i din utvecklarmiljö.


### **Hur man lägger till en Pivot-tabell med Aspose.Cells for Node.js via C++**

För att skapa en pivot-tabell med Aspose.Cells for Node.js via C++:

1. Lägg till lite data i ett kalkylbladsceller med hjälp av en Cell-objekts put_value-metod. Du använder också en mallfil som redan är ifylld med data. Datan kommer att användas som pivottabellens datakälla.
1. Lägg till en pivot tabell till arbetsbladet genom att anropa PivotTables -samlingens add-metod (inkapslad i Worksheet-objektet).
1. Hämta det nya PivotTable-objektet från PivotTables-samlingen genom att ange dess index. # Använd något av de pivottabellobjekt som är inkapslade i PivotTable-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **Hur man lägger till ett Pivot-diagram med Aspose.Cells for Node.js via C++-biblioteket**

För att skapa ett PivotDiagram med Aspose.Cells for Node.js via C++:

1. Lägg till en graf.
1. Ange grafens PivotSource så att den hänvisar till en befintlig pivot tabell i kalkylarket.
1. Ange andra attribut.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
