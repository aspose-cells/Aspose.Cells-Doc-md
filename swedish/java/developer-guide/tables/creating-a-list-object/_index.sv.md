---
title: Skapa en tabell
type: docs
weight: 40
url: /sv/java/creating-a-list-object/
---

{{% alert color="primary" %}}

En av fördelarna med kalkylblad är att de tillåter dig att skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan samarbeta för att använda, skapa och underhålla olika listor.

Aspose.Cells stödjer skapande och hantering av listor.

{{% /alert %}}

## **Fördelar med en tabell**

Det finns ganska många fördelar när du konverterar en lista över data till en faktisk Listobjekt:

- Nya rader och kolumner inkluderas automatiskt.
- En totalrad längst ner i din lista kan enkelt läggas till för att visa SUMMA, MEDELVÄRDE, ANTAL, osv.
- Kolumner som läggs till till höger inkorporeras automatiskt i listobjektet.
- Diagram baserade på rader och kolumner kommer att utökas automatiskt.
- Namngivna intervall tilldelade rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig rad- och kolumnradering.

## **Skapa en tabell med hjälp av Microsoft Excel**

**Välja dataområde för att skapa ett listobjekt** 

![todo:image_alt_text](creating-a-list-object_1.png)

Detta visar skapa listdialogrutan.

**Skapa listdialogrutan** 

![todo:image_alt_text](creating-a-list-object_2.png)

Implementering av List-objektet och specificering av Total rad (Välj **Data**, sedan **List**, följt av **Total rad**).

**Skapa ett listobjekt** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Skapa en tabell med hjälp av Aspose.Cells API**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)samling som ger åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klassen. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att skapa en [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)i ett arbetsblad, använd [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)samlingsegenskapen i Worksheet-klassen. Varje [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)är faktiskt ett objekt av [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)klassen, som vidare tillhandahåller add-metoden för att lägga till ett listobjekt och ange ett område av celler för listan.

Enligt det angivna cellintervallet skapas List-objektet i arbetsbladet av Aspose.Cells. Använd attribut (till exempel ShowTotals, ListColumns etc.) av [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)klassen för att styra listan.

I det exempel som ges nedan har vi skapat samma [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) med hjälp av Aspose.Cells API som vi skapade med hjälp av Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
{{< app/cells/assistant language="java" >}}
