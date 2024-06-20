---
title: Skapa pivottabeller och pivotdiagram
type: docs
weight: 20
url: /sv/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

En pivottabell är en interaktiv sammanfattning av poster. Till exempel kan du ha hundratals faktura-poster i en lista i ett kalkylblad. En pivottabell kan summera fakturorna efter kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt omorganisera informationen i pivottabellen genom att dra knappar till en ny position.

Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu enklare att förstå data eftersom pivottabellen skapar delsummer och totaler automatiskt.

Aspose.Cells stödjer [pivottabeller](/cells/sv/net/skapa-pivottabeller-och-pivotdiagram/) och [pivotdiagram](/cells/sv/net/skapa-pivottabeller-och-pivotdiagram/).

{{% /alert %}}

## **Lägg till Pivottabeller och Diagram**

Aspose.Cells tillhandahåller en speciell uppsättning klasser som används för att skapa pivottabeller. Dessa klasser används för att skapa och ställa in PivotTable-objekt, som fungerar som en pivottabells grundläggande byggstenar:

- PivotField, ett fält i en pivottabellrapport.
- PivotFields, en samling av alla PivotField-objekt i en pivottabell.
- PivotTable, en pivottabellrapport på ett kalkylblad.
- PivotTables, en samling av alla PivotTable-objekt på kalkylbladet.

### **Förberedelser för att använda Aspose.Cells**

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells](https://downloads.aspose.com/cells/net).
   1. Installera det på din utvecklingsdator.
      När alla [Aspose](http://www.aspose.com/) -komponenter är installerade fungerar de i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det infogar bara vattenstämplar i producerade dokument. För att använda komponenten i full kapacitet måste du ha en giltig licens.
1. Skapa ett projekt:
   1. Starta Visual Studio.Net.
   1. Skapa en ny konsolapplikation.
1. Lägg till referenser:
   Lägg till en referens till Aspose.Cells-komponenten i ditt projekt, till exempel ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Lägga till en pivottabell**

För att skapa en pivot tabell med Aspose.Cells:

1. Lägg till lite data till arbetsbladsceller med hjälp av en Cell-objekts PutValue/setValue-metod. Du kan också använda en mallfil som redan är ifylld med data. Data kommer att användas som pivot tabellens datakälla.
1. Lägg till en pivot tabell till arbetsbladet genom att anropa PivotTables -samlingens add-metod (inkapslad i Worksheet-objektet).
1. Hämta det nya PivotTable-objektet från PivotTables-samlingen genom att ange dess index. # Använd något av de pivottabellobjekt som är inkapslade i PivotTable-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Lägga till en PivotChart**

För att skapa en PivotChart med Aspose.Cells:

1. Lägg till en graf.
1. Ange grafens PivotSource så att den hänvisar till en befintlig pivot tabell i kalkylarket.
1. Ange andra attribut.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

