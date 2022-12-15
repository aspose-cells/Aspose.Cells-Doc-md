---
title: Skapa en tabell
type: docs
weight: 40
url: /sv/java/creating-a-list-object/
---
{{% alert color="primary" %}}

En av fördelarna med kalkylblad är att de låter dig skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan arbeta tillsammans för att använda, skapa och underhålla olika listor.

Aspose.Cells stöder att skapa och hantera listor.

{{% /alert %}}

## **Fördelar med ett bord**

Det finns en hel del fördelar när du konverterar en lista med data till ett faktiskt listobjekt:

- Nya rader och kolumner inkluderas automatiskt.
- En total rad längst ner på din lista kan enkelt läggas till för att visa SUMMA, AVERAGE, COUNT, etc.
- Kolumner som läggs till till höger infogas automatiskt i List-objektet.
- Diagram baserade på rader och kolumner utökas automatiskt.
- Namngivna intervall som tilldelats rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig radering och radering.

## **Skapa en tabell med Microsoft Excel**

**Välja dataintervall för att skapa ett listobjekt** 

![todo:image_alt_text](creating-a-list-object_1.png)

Detta visar dialogrutan Skapa lista.

**Dialogrutan Skapa lista** 

![todo:image_alt_text](creating-a-list-object_2.png)

 Implementera List-objektet och specificera Total Row (Välj**Data** , då**Lista** , följd av**Total rad**).

**Skapa ett listobjekt** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Skapa en tabell med hjälp av Aspose.Cells API**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Att skapa en[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) i ett kalkylblad, använd[**Listobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) samlingsegenskapen för klassen Worksheet. Varje[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) är i själva verket ett föremål för[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)klass, som vidare tillhandahåller add-metoden för att lägga till ett List-objekt och ange ett cellintervall för listan.

Enligt det specificerade cellintervallet skapas List-objektet i kalkylbladet av Aspose.Cells. Använd attribut (till exempel ShowTotals, ListColumns etc.) för[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)klass för att kontrollera listan.

 I exemplet nedan har vi skapat detsamma[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)med Aspose.Cells API som vi skapade med Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
