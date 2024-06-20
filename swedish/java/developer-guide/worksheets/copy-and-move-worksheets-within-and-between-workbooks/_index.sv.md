---
title: Kopiera och flytta arbetsblad inom och mellan arbetsböcker
type: docs
weight: 20
url: /sv/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Ibland behöver du ett antal arbetsblad med gemensam formatering och datainmatning. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det tre gånger.

Aspose.Cells stöder att kopiera eller flytta arbetsblad inom eller mellan arbetsböcker. Arbetsblad inklusive data, formatering, tabeller, matriser, diagram, bilder och andra objekt kopieras med högsta noggrannhet.

{{% /alert %}}

## **Kopiera och flytta arbetsblad**

Den här artikeln förklarar hur man använder Aspose.Cells för att:

- [Kopiera ett arbetsblad inom en arbetsbok](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Flytta ett arbetsblad inom en arbetsbok](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Kopiera ett arbetsblad mellan arbetsböcker](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Flytta ett arbetsblad mellan arbetsböcker](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Kopiera ett arbetsblad inom en arbetsbok**

De inledande stegen är desamma för alla exemplen.

1. Skapa två arbetsböcker med lite data i Microsoft Excel. För detta exempel skapade vi två nya arbetsböcker i Microsoft Excel och matade in data i kalkylbladen.

- FirstWorkbook.xls (3 kalkylblad)
- SecondWorkbook.xls (1 kalkylblad).

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Packa upp det på din utvecklingsdator.
      Alla [Aspose](http://www.aspose.com/) -komponenter fungerar i utvärderingsläge när de är installerade. Utvärderingsläget har ingen tidsbegränsning och det lägger bara till vattenstämplar i producerade dokument.
1. Skapa ett projekt:
   1. Skapa ett projekt med hjälp av en Java-redigerare som Eclipse eller skapa ett enkelt program med hjälp av en textredigerare.
1. Lägg till en klass sökväg:
   1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
   1. Ange klassens sökväg i Eclipse:
      1. Välj ditt projekt i Eclipse och klicka på menyer ** Project ** och sedan ** Egenskaper **.
      1. Välj ** Java Build Path ** på vänster sida om dialogrutan, välj sedan fliken Bibliotek,
      1. Klicka på ** Lägg till JAR-filer ** eller ** Lägg till externa JAR-filer ** för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägg till dem i byggbanor.

{{% alert color="primary" %}}

Eller så kan du ange klasssökvägen vid körningstid i en DOS-prompt på Windows.
Exempelvis:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Kopiera kalkylblad inom en arbetsbok:
   Nedan är koden som används för att utföra uppgiften. Den kopierar kalkylbladet Copy inom FirstWorkbook.xls.

Genom att köra koden flyttas kalkylbladet med namnet Copy inom FirstWorkbook.xls med det nya namnet Last Sheet.

**Utgångsfil**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Flytta ett kalkylblad inom en arbetsbok**

Nedan är koden som används för att utföra uppgiften.

Genom att köra koden flyttas kalkylbladet Move från index 1 till index 2 i FirstWorkbook.xls.

**Utgångsfil**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Kopiera ett kalkylblad mellan arbetsböcker**

Genom att köra koden kopieras kalkylbladet Copy till SecondWorkbook.xls med det nya namnet Sheet2.

**Utgångsfil**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Flytta ett kalkylblad mellan arbetsböcker**

Körning av koden flyttar kalkylbladet från FirstWorkbook.xls till SecondWorkbook.xls med det nya namnet Sheet3.

**Resultat FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Resultat SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Slutsats**

{{% alert color="primary" %}}

Den här artikeln förklarar hur man kopierar och flyttar kalkylblad inom och mellan arbetsböcker med hjälp av Aspose.Cells.

Aspose.Cells har gynnats av år av forskning, design och noggrann justering. Vi välkomnar dina frågor, kommentarer och förslag på [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi garanterar ett snabbt svar.

{{% /alert %}}
