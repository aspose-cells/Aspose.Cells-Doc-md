---
title: Formatera ett listobjekt - tabell
type: docs
weight: 50
url: /sv/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

För att hantera och analysera en grupp relaterade data är det möjligt att förvandla ett cellintervall till ett listobjekt (även känt som en Excel-tabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende av data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverad i rubrikraden så att du snabbt kan filtrera eller sortera dina listobjektdata. Du kan lägga till en totalrad (en speciell rad i en lista som ger ett urval av aggregerade funktioner som är användbara för att arbeta med numerisk data) till listobjektet som tillhandahåller en rullgardinslista med aggregerade funktioner för varje total radcell. Aspose.Cells ger alternativ för att skapa och hantera listor (eller tabeller).

{{% /alert %}}

## **Formatera ett listobjekt**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. Att skapa en[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) i ett kalkylblad, använd[**Listobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) samling egendom av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. Varje[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) är i själva verket ett föremål för[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)klass, som vidare tillhandahåller add-metoden för att lägga till ett List-objekt och specificera cellintervallet det ska omfatta. Enligt det specificerade cellområdet, a[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) skapas i kalkylbladet av Aspose.Cells. Använd attribut (t.ex.[**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) ) av[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)klass för att formatera tabellen för ditt krav.

 Exemplet nedan lägger till exempeldata till ett kalkylblad, lägger till en[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) och tillämpar standardstilar på den.[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)stilar stöds av Microsoft Excel 2007/2010.

Följande utdata genereras när koden exekveras.

**En formaterad tabell skapas i kalkylbladet** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
