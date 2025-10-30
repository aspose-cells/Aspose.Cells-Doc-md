---
title: Skapa pivottabeller och pivottabell diagram med Golang via C++
linktitle: Skapa pivottabeller och pivotdiagram
type: docs
weight: 20
url: /sv/go-cpp/create-pivot-tables-and-pivot-charts/
description: Lär dig hur du skapar pivottabeller och pivottabell diagram i Excel filer med Aspose.Cells med Golang via C++.
---

{{% alert color="primary" %}}

En pivottabell är en interaktiv sammanställning av poster. Till exempel kan du ha hundratals fakturaposter i en lista i ett kalkylblad. En pivottabell kan sammanställa fakturor efter kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt omorganisera informationen i pivottabellen genom att dra knappar till en ny position.

Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu enklare att förstå data eftersom pivottabellen skapar delsummer och totaler automatiskt.

Aspose.Cells stöder [pivottabeller](/cells/sv/cpp/create-pivot-tables-and-pivot-charts/) och [pivottabell-diagram](/cells/sv/cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Lägg till Pivottabeller och Diagram**

Aspose.Cells tillhandahåller en speciell uppsättning klasser som används för att skapa pivottabeller. Dessa klasser används för att skapa och ställa in PivotTable-objekt, som fungerar som en pivottabells grundläggande byggstenar:

- **PivotField**, ett fält i en pivottabellsrapport.
- **PivotFields**, en samling av alla PivotField-objekt i en pivottabell.
- **PivotTable**, en Pivottabell-rapport i ett kalkylblad.
- **PivotTables**, en samling av alla PivotTable-objekt på kalkylbladet.

### **Förberedelser för att använda Aspose.Cells**

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells](https://downloads.aspose.com/cells/go-cpp/).
   1. Installera det på din utvecklingsdator.
      Alla [Aspose](http://www.aspose.com/)-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och infogar endast vattenstämplar i genererade dokument. För att arbeta med komponenten i dess fulla kapacitet, måste du ha en giltig licens.
1. Skapa ett projekt:
   1. Starta din C++-IDE (t.ex. Visual Studio).
   1. Skapa en ny konsolapplikation.
1. Lägg till referenser:
   Lägg till referens till Aspose.Cells-komponenten i ditt projekt, till exempel, `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Lägga till en pivottabell**

För att skapa en pivot tabell med Aspose.Cells:

1. Lägg till data i ett kalkylblad genom att använda `PutValue`-metoden för ett `Cell`-objekt. Du kan även använda en mallfil som redan är fylld med data. Data kommer att användas som pivot-tabellens datakälla.
1. Lägg till en pivot-tabell i kalkylbladet genom att anropa `PivotTables`-samlingen `Add`-metod (inkapslad i `Worksheet`-objektet).
1. Få tillgång till det nya `PivotTable`-objektet från `PivotTables`-samlingen genom att ange dess index. Använd något av pivot-tabellobjekten som kapslas in i `PivotTable`-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}
### **Lägga till en PivotChart**

För att skapa en PivotChart med Aspose.Cells:

1. Lägg till en graf.
1. Ställ in `PivotSource` för diagrammet att hänvisa till en befintlig pivot-tabell i kalkylbladet.
1. Ange andra attribut.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}
