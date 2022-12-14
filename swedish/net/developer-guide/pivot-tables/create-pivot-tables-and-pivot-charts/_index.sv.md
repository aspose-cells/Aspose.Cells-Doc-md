---
title: Skapa pivottabeller och pivotdiagram
type: docs
weight: 20
url: /sv/net/create-pivot-tables-and-pivot-charts/
---
{{% alert color="primary" %}}

En pivottabell är en interaktiv sammanfattning av poster. Till exempel kan du ha hundratals fakturaposter i en lista i ett kalkylblad. En pivottabell kan summera fakturorna per kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt ordna om informationen i pivottabellen genom att dra knappar till en ny position.

Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu lättare att förstå data eftersom pivottabellen skapar delsummor och summor automatiskt.

 Aspose.Cells stöder[pivottabeller](/cells/sv/net/create-pivot-tables-and-pivot-charts/) och[pivotdiagram](/cells/sv/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Lägga till pivottabeller och diagram**

Aspose.Cells tillhandahåller en speciell uppsättning klasser som används för att skapa pivottabeller. Dessa klasser används för att skapa och ställa in PivotTable-objekt, som fungerar som ett PivotTable-objekts grundläggande byggstenar:

- PivotField, ett fält i en pivottabellsrapport.
- PivotFields, en samling av alla PivotField-objekt i en pivottabell.
- Pivottabell, en pivottabellrapport på ett kalkylblad.
- Pivottabeller, en samling av alla pivottabellobjekt på kalkylbladet.

### **Förbereder att använda Aspose.Cells**

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells](https://downloads.aspose.com/cells/net).
 1. Installera det på din utvecklingsdator.
 Allt[Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument. För att arbeta med komponenten i dess fulla kapacitet behöver du ha en giltig licens.
1. Skapa ett projekt:
 1. Starta Visual Studio.Net.
 1. Skapa en ny konsolapplikation.
1. Lägg till referenser:
 Lägg till referens till komponenten Aspose.Cells i ditt projekt, till exempel ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Lägga till en pivottabell**

Så här skapar du en pivottabell med Aspose.Cells:

1. Lägg till några data i ett kalkylbladsceller med hjälp av ett Cell-objekts PutValue/setValue-metod. Du använder också en mallfil som redan är fylld med data. Data kommer att användas som pivottabellens datakälla.
1. Lägg till en pivottabell till kalkylbladet genom att anropa PivotTables-samlingens add-metod (inkapslad i Worksheet-objektet).
1. Få tillgång till det nya PivotTable-objektet från PivotTables-samlingen genom att skicka dess index. # Använd något av pivottabellobjekten som är inkapslade i PivotTable-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Lägga till ett pivotdiagram**

Så här skapar du ett pivotdiagram med Aspose.Cells:

1. Lägg till ett diagram.
1. Ställ in pivotkällan för diagrammet så att den refererar till en befintlig pivottabell i kalkylarket.
1. Ställ in andra attribut.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

