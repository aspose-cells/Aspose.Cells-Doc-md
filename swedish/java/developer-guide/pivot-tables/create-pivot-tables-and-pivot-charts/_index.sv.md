---
title: Skapa pivottabeller och pivotdiagram
type: docs
weight: 10
url: /sv/java/create-pivot-tables-and-pivot-charts/
description: Skapa pivot tabeller och pivot diagram med Aspose.Cells for Java API.
keywords: excel skapa pivot tabell java, excel skapa pivot diagram java, excel skapa pivot tabell och pivot diagram java, skapa excel pivot tabell java, skapa excel pivot diagram java, skapa excel pivot tabell och pivot diagram java, java skapa excel pivot tabell och pivot diagram, hur man skapar excel pivot tabell och pivot diagram java
---

{{% alert color="primary" %}}

En pivottabell är en interaktiv sammanfattning av poster. Till exempel kan du ha hundratals faktura-poster i en lista i ett kalkylblad. En pivottabell kan summera fakturorna efter kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt omorganisera informationen i pivottabellen genom att dra knappar till en ny position.

Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu enklare att förstå data eftersom pivottabellen skapar delsummer och totaler automatiskt.

Aspose.Cells stöder [pivot-tabeller](/cells/sv/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) och [pivot-diagram](/cells/sv/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Lägg till Pivottabeller och Diagram**

Aspose.Cells tillhandahåller en speciell uppsättning klasser som används för att skapa pivottabeller. Dessa klasser används för att skapa och ställa in PivotTable-objekt, som fungerar som en pivottabells grundläggande byggstenar:

- PivotField, ett fält i en pivottabellrapport.
- PivotFields, en samling av alla PivotField-objekt i en pivottabell.
- PivotTable, en pivottabellrapport på ett kalkylblad.
- PivotTables, en samling av alla PivotTable-objekt på kalkylbladet.

### **Förberedelser för att använda Aspose.Cells**

1. Hämta och installera Aspose.Cells.Zip:
   1. [Ladda ner Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Packa upp det på din utvecklingsdator.
      Alla [Aspose](http://www.aspose.com/) -komponenter fungerar i utvärderingsläge när de är installerade. Utvärderingsläget har ingen tidsbegränsning och det lägger bara till vattenstämplar i producerade dokument.
1. Skapa ett projekt
   1. Du kan antingen skapa ett projekt med någon Java-editor t.ex. Eclipse eller skapa ett enkelt program med Anteckningar.
1. Lägg till klasssökvägen:
   För att ställa in en klasssökväg med Eclipse:
   1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
   1. Ange klassens sökväg i Eclipse:
   1. Välj ditt projekt i Eclipse och klicka sedan på menyerna Projekt-Egenskaper.
   1. Välj "Java Build Path" på den vänstra sidan av popup-fönstret, välj sedan fliken "Libraries", klicka på "Add JARs" eller "Add External JARs" för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägg till dem i bygg sökvägar.
   1. Skriv applikation för att anropa API:er för Asposes komponenter.
      Eller så kan du ställa in det vid körning i kommandotolken i Windows.

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

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

## Relaterade artiklar

- [Anpassad sortering i Pivot-tabell](/cells/sv/java/custom-sorting-in-pivot-table/)
- [Formatering av Pivottabell](/cells/sv/java/formatting-pivot-table/)
- [Uppdatera och beräkna pivottabell med beräknade poster](/cells/sv/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Inaktivera ribbor för pivot-tabell](/cells/sv/java/disable-pivot-table-ribbons/)

{{< app/cells/assistant language="java" >}}
