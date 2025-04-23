---
title: Skapa och hantera tabeller i Microsoft Excel filer.
linktitle: Tabeller
type: docs
weight: 150
url: /sv/net/create-and-format-table/
description: Infoga, ändra storlek, redigera, ta bort, formatera tabell i Excel filer med hjälp av Aspose.Cells biblioteket.
---

## **Skapa tabell**

En av fördelarna med kalkylblad är att de tillåter dig att skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan samarbeta för att använda, skapa och underhålla olika listor.

Aspose.Cells stödjer skapande och hantering av listor.

### **Fördelar med en List-objekt**

Det finns ganska många fördelar när du konverterar en lista med data till ett faktiskt List-objekt

- Nya rader och kolumner inkluderas automatiskt.
- En totalrad längst ner i din lista kan enkelt läggas till för att visa SUMMA, MEDELVÄRDE, ANTAL, osv.
- Kolumner som läggs till till höger inkorporeras automatiskt i listobjektet.
- Diagram baserade på rader och kolumner kommer att utökas automatiskt.
- Namngivna intervall tilldelade rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig rad- och kolumnradering.

### **Skapa ett List-objekt med hjälp av Microsoft Excel**

- Välja dataintervall för att skapa ett List-objekt
- Detta visar skapa List-dialogrutan.
- Implementera List-objektet för datan och specificera total rad (Välj **Data**, sedan **Lista**, följt av **Total rad**).

### **Använda Aspose.Cells API**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje arbetsblad i en Excel-fil.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att skapa en [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) i ett kalkylblad, använd [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)-egenskapen i klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Varje [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) är i själva verket en objekt av klassen [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection), som dessutom tillhandahåller [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)-metoden för att lägga till ett List-objekt och specificera en intervall av celler för listan.

Enligt det angivna cellintervallet skapas List-objektet av Aspose.Cells. Använd attribut (till exempel [**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns), etc.) för klassen [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) för att kontrollera listan.

I det exempel som ges nedan har vi skapat samma [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) med hjälp av Aspose.Cells API som vi skapade med hjälp av Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Formatera en tabell**

För att hantera och analysera en grupp relaterade data är det möjligt att göra om ett cellområde till ett listobjekt (även känt som en Exceltabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende från data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverat i rubrikraden så att du snabbt kan filtrera eller sortera dina listobjektdata. Du kan lägga till en totalrad (en specialrad i en lista som ger ett urval av aggregeringsfunktioner som är användbara för att arbeta med numeriska data) till listobjektet som ger en rullista med aggregeringsfunktioner för varje cell i totalraden. Aspose.Cells tillhandahåller alternativ för att skapa och hantera listor (eller tabeller).

### **Formatera ett Listobjekt**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje arbetsblad i en Excel-fil.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att skapa en [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) i ett kalkylblad, använd [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)-egenskapen i klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Varje [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) är i själva verket en objekt av klassen [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection), som dessutom tillhandahåller [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)-metoden för att lägga till ett List-objekt och specificera det intervall av celler den ska omfatta. Enligt det angivna cellintervallet skapas en [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) i kalkylbladet av Aspose.Cells. Använd attribut (till exempel [**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)) för klassen [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) för att formatera tabellen enligt dina behov.

I exemplet nedan läggs provdata till ett kalkylblad, ett [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) läggs till och standardstilar tillämpas på det. [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)-stilar stöds av Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Fortsatta ämnen**
- [Konvertera tabell till ODS](/cells/sv/net/convert-table-to-ods/)
- [Hitta frågetabeller och lista objekt relaterade till externa dataanslutningar](/cells/sv/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Läs och skriv tabell med datakälla för frågetabell](/cells/sv/net/read-and-write-table-with-query-table-data-source/)
- [Ange kommentaren för tabell eller listobjekt inne i kalkylbladet](/cells/sv/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabeller och områden](/cells/sv/net/tables-and-ranges/)

{{< app/cells/assistant language="csharp" >}}
