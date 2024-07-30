---
title: Hur man lägger till ett PivotChart med hjälp av Aspose.Cells
linktitle: Pivotdiagram
type: docs
weight: 100
url: /sv/java/how-to-add-pivot-chart/
description: Hur man lägger till ett PivotChart med hjälp av Aspose.Cells.
keywords: PivotChart
---
## Vad är PivotChart
En pivottabell är en visuell representation av data i en pivot-tabell. Pivotdiagram tillhandahåller en metod för att sammanfatta, analysera, utforska och presentera sammanfattad data. Här är några nyckelfunktioner och aspekter av pivotdiagram:

1. Dynamisk datavisning: Pivotdiagram uppdateras automatiskt för att återspegla ändringar i pivottabellen. Om du lägger till eller tar bort fält i pivottabellen uppdateras pivotdiagrammet därefter.

1. Interaktivt: Pivotdiagram är interaktiva och tillåter användare att filtrera, sortera och gå djupt in i data. Det gör det enkelt att utforska olika aspekter av datamängden.

1. Flexibel layout: Användare kan ändra layouten för pivotdiagrammet genom att dra och släppa fält, vilket erbjuder flexibilitet i hur data visualiseras.

1. Olika diagramtyper: Pivotdiagram kan skapas med olika diagramtyper som stapeldiagram, linjediagram, cirkeldiagram med mera, beroende på datakaraktären och insikterna du vill få.

1. Sammanfattning: Pivotdiagram sammanfattar stora mängder data och kan visa totaler, genomsnitt, räkningar eller annan sammanfattande statistik.

1. Filtrering: De erbjuder filtreringsfunktioner som gör det möjligt att visa endast den data som uppfyller vissa kriterier.

<br>
Pivotdiagram används vanligtvis inom affärsinformatik och dataanalys för att ge en tydlig och konkret visuell sammanfattning av komplexa datamängder. De är ett kraftfullt verktyg för att fatta data-drivna beslut.

## Hur man lägger till en PivotChart med hjälp av Aspose.Cells
### **Skapa en Pivot Table**

För att skapa en pivot tabell med Aspose.Cells:

1. Lägg till lite data till arbetsbladsceller med hjälp av en Cell-objekts PutValue/setValue-metod. Du kan också använda en mallfil som redan är ifylld med data. Data kommer att användas som pivot tabellens datakälla.
1. Lägg till en pivot tabell till arbetsbladet genom att anropa PivotTables -samlingens add-metod (inkapslad i Worksheet-objektet).
1. Få åtkomst till det nya PivotTable-objektet från PivotTables-samlingen genom att skicka dess index.
1. Använd något av pivot tabellens objekt som är inkapslade i PivotTable-objektet för att hantera tabellen.

Ett kodexempel ges nedan. Genom att köra koden skapas en ny fil: pivotTable_test.xls.

**Indatadata** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Utgångspivot tabell**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Skapa en Pivot Chart baserad på Pivot Tabellen**

För att skapa en pivot chart med Aspose.Cells:

1. Lägg till en graf.
1. Ange grafens PivotSource så att den hänvisar till en befintlig pivot tabell i kalkylarket.
1. Ange andra attribut.

Nedan är koden som används av komponenten för att utföra uppgiften. Genom att köra koden skapas en ny fil: pivotChart_test.xls.

**Pivot chart-bladet**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Den här artikeln visar hur man skapar pivot tabeller och pivot charts med Aspose.Cells. Förhoppningsvis kommer det att hjälpa dig att använda dessa funktioner i dina egna scenarier.

Aspose.Cells har gynnats av års forskning, design och noggrann finjustering.

Vi välkomnar dina frågor, kommentarer och förslag på [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi garanterar ett snabbt svar.

{{% /alert %}}
