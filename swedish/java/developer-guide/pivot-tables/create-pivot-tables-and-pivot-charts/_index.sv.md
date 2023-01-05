---
title: Skapa pivottabeller och pivotdiagram
type: docs
weight: 10
url: /sv/java/create-pivot-tables-and-pivot-charts/
description: Skapa pivottabeller och pivotdiagram med Aspose.Cells for Java API.
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

En pivottabell är en interaktiv sammanfattning av poster. Till exempel kan du ha hundratals fakturaposter i en lista i ett kalkylblad. En pivottabell kan summera fakturorna per kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt ordna om informationen i pivottabellen genom att dra knappar till en ny position.

Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu lättare att förstå data eftersom pivottabellen skapar delsummor och summor automatiskt.

 Aspose.Cells stöder[pivottabeller](/cells/sv/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) och[pivotdiagram](/cells/sv/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Lägga till pivottabeller och diagram**

Aspose.Cells tillhandahåller en speciell uppsättning klasser som används för att skapa pivottabeller. Dessa klasser används för att skapa och ställa in PivotTable-objekt, som fungerar som ett PivotTable-objekts grundläggande byggstenar:

- PivotField, ett fält i en pivottabellsrapport.
- PivotFields, en samling av alla PivotField-objekt i en pivottabell.
- Pivottabell, en pivottabellrapport på ett kalkylblad.
- Pivottabeller, en samling av alla pivottabellobjekt på kalkylbladet.

### **Förbereder att använda Aspose.Cells**

1. Ladda ner och installera Aspose.Cells.Zip:
   1. [Ladda ner Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Packa upp det på din utvecklingsdator.
 Allt[Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument.
1. Skapa ett projekt
 1. Du kan antingen skapa ett projekt med hjälp av någon Java Editor, t.ex. Eclipse, eller skapa ett enkelt program med en anteckningsblock.
1. Lägg till klasssökväg:
 Så här ställer du in en klasssökväg med Eclipse:
1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
 1. Ställ in klassvägen för projektet i Eclipse:
1. Välj ditt projekt i Eclipse och klicka sedan på menyerna Projekt-egenskaper.
 1. Välj "Java Build Path" till vänster i popup-fönstret, välj sedan fliken "Libraries", klicka på "Add JARs" eller "Add External JARs" för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägga till dem in på byggvägar.
 1. Skriv applikation för att anropa API:er för Aspose:s komponenter.
 Eller så kan du ställa in den vid körning vid dos-prompt i Windows.

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Skapa en pivottabell**

Så här skapar du en pivottabell med Aspose.Cells:

1. Lägg till några data i ett kalkylbladsceller med hjälp av ett Cell-objekts PutValue/setValue-metod. Du använder också en mallfil som redan är fylld med data. Data kommer att användas som pivottabellens datakälla.
1. Lägg till en pivottabell till kalkylbladet genom att anropa PivotTables-samlingens add-metod (inkapslad i Worksheet-objektet).
1. Få tillgång till det nya PivotTable-objektet från PivotTables-samlingen genom att skicka dess index.
1. Använd något av pivottabellobjekten som är inkapslade i PivotTable-objektet för att hantera tabellen.

Ett kodexempel ges nedan. När koden körs genereras en ny fil: pivotTable_test.xls.

**Indata** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Utgångspivottabellen**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Skapa ett pivotdiagram baserat på pivottabellen**

Så här skapar du ett pivotdiagram med Aspose.Cells:

1. Lägg till ett diagram.
1. Ställ in pivotkällan för diagrammet så att den refererar till en befintlig pivottabell i kalkylarket.
1. Ställ in andra attribut.

Nedan visas koden som används av komponenten för att utföra uppgiften. När koden körs genereras en ny fil: pivotChart_test.xls.

**Pivotdiagrambladet**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Den här artikeln visar hur du skapar pivottabeller och pivotdiagram med Aspose.Cells. Förhoppningsvis kommer det att hjälpa dig att använda dessa funktioner i dina egna scenarier.

Aspose.Cells har dragit nytta av år av forskning, design och noggrann justering.

 Vi välkomnar dina frågor, kommentarer och förslag på[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi garanterar ett snabbt svar.

{{% /alert %}}

## relaterade artiklar

- [Anpassad sortering i pivottabell](/cells/sv/java/custom-sorting-in-pivot-table/)
- [Formatera pivottabell](/cells/sv/java/formatting-pivot-table/)
- [Uppdatera och beräkna pivottabellen med beräknade objekt](/cells/sv/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Inaktivera pivottabellsband](/cells/sv/java/disable-pivot-table-ribbons/)

