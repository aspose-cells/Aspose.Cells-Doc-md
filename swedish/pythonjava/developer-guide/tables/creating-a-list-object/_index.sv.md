---
title: Skapar en listobject
type: docs
weight: 20
url: /sv/python-java/creating-a-list-object/
---

Användningen av kalkylbladet gör det enkelt att arbeta med olika typer av listor, till exempel telefonlistor, uppgiftslistor etc. Aspose.Cells stödjer skapande och hantering av listor.

## **Fördelar med en List-objekt**

Det finns ganska många fördelar när du konverterar en lista över data till en faktisk Listobjekt:

- Nya rader och kolumner inkluderas automatiskt.
- En totalrad längst ner i din lista kan enkelt läggas till för att visa SUMMA, MEDELVÄRDE, ANTAL, osv.
- Kolumner som läggs till till höger inkorporeras automatiskt i listobjektet.
- Diagram baserade på rader och kolumner kommer att utökas automatiskt.
- Namngivna intervall tilldelade rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig rad- och kolumnradering.

## **Skapa ett List-objekt med hjälp av Microsoft Excel**

**Välja dataområde för att skapa ett listobjekt** 

![todo:image_alt_text](picture1.png)

Detta visar skapa listdialogrutan.

**Skapa listdialogrutan** 

![todo:image_alt_text](picture2.png)

Genomförande av Listobjektet och specificera total rad (Välj **Data**, sedan **Lista**, följt av **Total rad**).

**Skapa ett listobjekt** 

![todo:image_alt_text](picture3.png)

## **Skapa en Listobjekt med hjälp av Aspose.Cells API**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)-samling som tillåter åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att skapa en [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) i ett kalkylblad, använd [**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)-samlingsegenskapen för klassen [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). Varje [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) är faktiskt ett objekt av klassen [**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection), som ytterligare tillhandahåller metoden [**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) för att lägga till ett Listobjekt och specificera en cellintervall för listan.

Enligt det angivna cellintervallen skapas Listobjektet på kalkylbladet av Aspose.Cells. Använd attributen (till exempel ShowTotals, ListColumns etc.) av klassen [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) för att styra listan.

I det givna exemplet har vi skapat samma [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) med hjälp av Aspose.Cells for Python via Java API som vi skapade med hjälp av Microsoft Excel i avsnittet ovan.

## Källkod

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
