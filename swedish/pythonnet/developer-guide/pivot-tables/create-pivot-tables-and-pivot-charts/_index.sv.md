---
title: Skapa pivottabeller och pivotdiagram
type: docs
weight: 20
url: /sv/python-net/create-pivot-tables-and-pivot-charts/
description: Hur man lägger till pivottabeller och pivottabellsdiagram med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Lägg till pivottabeller och pivottabellsdiagram med Aspose.Cells för Python Excel Library.
---

{{% alert color="primary" %}}

En pivottabell är en interaktiv sammanfattning av poster. Till exempel kan du ha hundratals faktura-poster i en lista i ett kalkylblad. En pivottabell kan summera fakturorna efter kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt omorganisera informationen i pivottabellen genom att dra knappar till en ny position.

Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu enklare att förstå data eftersom pivottabellen skapar delsummer och totaler automatiskt.

Aspose.Cells för Python via .NET stöder [pivottabeller](/cells/sv/python-net/skapa-pivottabeller-och-pivottabell-diagram/) och [pivottabell-diagram](/cells/sv/python-net/skapa-pivottabeller-och-pivottabell-diagram/).

{{% /alert %}}

## **Lägg till pivottabeller och diagram med Aspose.Cells för Python Excel-bibliotek**

Aspose.Cells för Python via .NET tillhandahåller en speciell uppsättning klasser som används för att skapa pivottabeller. Dessa klasser används för att skapa och ställa in PivotTable-objekt, vilket fungerar som grundläggande byggstenar för ett PivotTable-objekt:

- PivotField, ett fält i en pivottabellrapport.
- PivotFields, en samling av alla PivotField-objekt i en pivottabell.
- PivotTable, en pivottabellrapport på ett kalkylblad.
- PivotTables, en samling av alla PivotTable-objekt på kalkylbladet.

### **Förbered att använda Aspose.Cells för Python via .NET**
1. Installera Aspose.Cells for Python via .NET från [pypi](https://pypi.org/project/aspose-cells-python/), använd kommandot: $ pip install aspose-cells-python.
1. Du kan också följa steg-för-steg-instruktionerna om hur du installerar “Aspose.Cells för Python via .NET” till din utvecklingsmiljö.


### **Hur du lägger till en pivottabell med hjälp av Aspose.Cells för Python Excel-bibliotek**

För att skapa en pivottabell med Aspose.Cells för Python via .NET:

1. Lägg till lite data i ett kalkylbladsceller med hjälp av en Cell-objekts put_value-metod. Du använder också en mallfil som redan är ifylld med data. Datan kommer att användas som pivottabellens datakälla.
1. Lägg till en pivot tabell till arbetsbladet genom att anropa PivotTables -samlingens add-metod (inkapslad i Worksheet-objektet).
1. Hämta det nya PivotTable-objektet från PivotTables-samlingen genom att ange dess index. # Använd något av de pivottabellobjekt som är inkapslade i PivotTable-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **Hur man lägger till ett pivottabell-diagram med hjälp av Aspsoe.Cells för Python Excel-bibliotek**

För att skapa ett pivotdiagram med Aspose.Cells för Python via .NET:

1. Lägg till en graf.
1. Ange grafens PivotSource så att den hänvisar till en befintlig pivot tabell i kalkylarket.
1. Ange andra attribut.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
