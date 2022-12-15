---
title: Skapa ett listobjekt
type: docs
weight: 20
url: /sv/python-java/creating-a-list-object/
---
Användningen av kalkylblad gör det enkelt att arbeta med olika typer av listor, till exempel. telefonlistor, uppgiftslistor. etc. Aspose.Cells stöder att skapa och hantera listor.

## **Fördelar med ett listobjekt**

Det finns en hel del fördelar när du konverterar en lista med data till ett faktiskt listobjekt:

- Nya rader och kolumner inkluderas automatiskt.
- En total rad längst ner på din lista kan enkelt läggas till för att visa SUMMA, AVERAGE, COUNT, etc.
- Kolumner som läggs till till höger infogas automatiskt i List-objektet.
- Diagram baserade på rader och kolumner utökas automatiskt.
- Namngivna intervall som tilldelats rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig radering och radering.

## **Skapa ett listobjekt med Microsoft Excel**

**Välja dataintervall för att skapa ett listobjekt** 

![todo:image_alt_text](picture1.png)

Detta visar dialogrutan Skapa lista.

**Dialogrutan Skapa lista** 

![todo:image_alt_text](picture2.png)

Implementera List-objektet och specificera Total Row (Välj**Data**, då**Lista**, följd av**Total rad**).

**Skapa ett listobjekt** 

![todo:image_alt_text](picture3.png)

## **Skapa ett listobjekt med Aspose.Cells API**

Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)klass. De[**Arbetsblad**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Att skapa en[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)i ett kalkylblad, använd[**Listobjekt**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)samling egendom av[**Arbetsblad**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)klass. Varje[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)är i själva verket ett föremål för[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)klass, som ytterligare ger[**Lägg till**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) metod för att lägga till ett List-objekt och ange ett cellintervall för listan.

Enligt det specificerade cellintervallet skapas List-objektet i kalkylbladet av Aspose.Cells. Använd attribut (till exempel ShowTotals, ListColumns, etc.) för[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)klass för att kontrollera listan.

I exemplet nedan har vi skapat detsamma[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)med Aspose.Cells for Python via Java API som vi skapade med Microsoft Excel i avsnittet ovan.

## Källkod

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
