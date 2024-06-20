---
title: Formatera ett Listobjekt  Tabell
type: docs
weight: 50
url: /sv/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

För att hantera och analysera en grupp relaterade data är det möjligt att göra om ett cellområde till ett listobjekt (även känt som en Exceltabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende från data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverat i rubrikraden så att du snabbt kan filtrera eller sortera dina listobjektdata. Du kan lägga till en totalrad (en specialrad i en lista som ger ett urval av aggregeringsfunktioner som är användbara för att arbeta med numeriska data) till listobjektet som ger en rullista med aggregeringsfunktioner för varje cell i totalraden. Aspose.Cells tillhandahåller alternativ för att skapa och hantera listor (eller tabeller).

{{% /alert %}}

## **Formatera ett Listobjekt**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)samling som ger åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klassen. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att skapa ett [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)i ett arbetsblad, använd [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)samlingsegenskapen i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klassen. Varje [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)är faktiskt ett objekt av [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)klassen, som vidare tillhandahåller add-metoden för att lägga till ett listobjekt och ange det område av celler det bör omfatta.

I det följande exemplet läggs provdata till ett arbetsblad, ett [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)läggs till och standardformat tillämpas på det. [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)format stöds av Microsoft Excel 2007/2010.

Följande resultat genereras när koden körs.

**En formaterad tabell skapas i arbetsbladet** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
