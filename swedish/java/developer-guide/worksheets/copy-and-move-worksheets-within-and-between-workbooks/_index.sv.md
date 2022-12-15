---
title: Kopiera och flytta arbetsblad inom och mellan arbetsböcker
type: docs
weight: 20
url: /sv/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Ibland behöver du ett antal kalkylblad med vanlig formatering och datainmatning. Om du till exempel arbetar med kvartalsbudgetar kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett ark och sedan kopiera det tre gånger.

Aspose.Cells stöder kopiering eller flyttning av kalkylblad i eller mellan arbetsböcker. Arbetsblad inklusive data, formatering, tabeller, matriser, diagram, bilder och andra objekt kopieras med högsta precision.

{{% /alert %}}

## **Kopiera och flytta arbetsblad**

Den här artikeln förklarar hur du använder Aspose.Cells för att:

- [Kopiera ett kalkylblad i en arbetsbok](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Flytta ett kalkylblad i en arbetsbok](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Kopiera ett kalkylblad mellan arbetsböcker](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Flytta ett kalkylblad mellan arbetsböcker](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Kopiera ett arbetsblad i en arbetsbok**

De första stegen är desamma för alla exempel.

1. Skapa två arbetsböcker med lite data i Microsoft Excel. För detta exempel skapade vi två nya arbetsböcker i Microsoft Excel och matade in lite data i kalkylbladen.

- FirstWorkbook.xls (3 kalkylblad)
- SecondWorkbook.xls (1 kalkylblad).

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Packa upp det på din utvecklingsdator.
 Allt[Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument.
1. Skapa ett projekt:
 1. Skapa ett projekt med en Java-redigerare som Eclipse eller skapa ett enkelt program med en textredigerare.
1. Lägg till en klasssökväg:
1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
 1. Ställ in klassvägen för projektet i Eclipse:
 1. Välj ditt projekt i Eclipse och klicka på menyer**Projekt** , då**Egenskaper**.
 1. Välj**Java Byggväg** i den vänstra sidan av dialogrutan, välj sedan fliken Bibliotek,
 1. Klicka**Lägg till JAR** eller**Lägg till externa JAR** för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägga till dem i byggvägar.

{{% alert color="primary" %}}

Eller så kan du ställa in klasssökvägen vid körning i en DOS-prompt på Windows.
Till exempel:

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Kopiera kalkylblad i en arbetsbok:
 Nedan finns koden som används av för att utföra uppgiften. Den kopierar arbetsbladet Copy inom FirstWorkbook.xls.

Genom att köra koden flyttas kalkylbladet med namnet Copy inom FirstWorkbook.xls med det nya namnet Last Sheet.

**Utdatafil**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Flytta ett kalkylblad med i en arbetsbok**

Nedan finns koden som används för att utföra uppgiften.

Genom att köra koden flyttas kalkylbladet Flytta från index 1 till index 2 i FirstWorkbook.xls.

**Utdatafil**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Kopiera ett arbetsblad mellan arbetsböcker**

När koden körs kopieras arbetsbladet Copy till SecondWorkbook.xls med det nya namnet Sheet2.

**Utdatafil**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Flytta ett kalkylblad mellan arbetsböcker**

Genom att köra koden flyttas flyttningsarket från FirstWorkbook.xls till SecondWorkbook.xls med det nya namnet Sheet3.

**Utdata FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Utdata SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Slutsats**

{{% alert color="primary" %}}

Den här artikeln förklarar hur du kopierar och flyttar kalkylblad inom och mellan arbetsböcker med Aspose.Cells.

 Aspose.Cells har dragit nytta av år av forskning, design och noggrann justering. Vi välkomnar dina frågor, kommentarer och förslag på[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi garanterar ett snabbt svar.

{{% /alert %}}
