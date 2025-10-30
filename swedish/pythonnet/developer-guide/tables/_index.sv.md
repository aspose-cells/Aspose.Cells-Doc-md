---
title: Skapa och hantera tabeller i Microsoft Excel filer.
linktitle: Tabeller
type: docs
weight: 150
url: /sv/python-net/create-and-format-table/
description: Infoga, ändra storlek, redigera, ta bort, formatera tabell i Excel filer med hjälp av Aspose.Cells biblioteket.
---

## **Skapa tabell**

En av fördelarna med kalkylblad är att de tillåter dig att skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan samarbeta för att använda, skapa och underhålla olika listor.

Aspose.Cells för Python via .NET stödjer skapande och hantering av Listor.

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

### **Användning av Aspose.Cells för Python via .NET API**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en samling som ger tillgång till varje arbetsblad i en Excel-fil.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att skapa en [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) i ett kalkylblad, använd [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects)-egenskapen i klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Varje [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) är i själva verket en objekt av klassen [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool), som dessutom tillhandahåller [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool)-metoden för att lägga till ett List-objekt och specificera en intervall av celler för listan.

Enligt det angivna cellområdet skapas List-objektet av Aspose.Cells för Python via .NET. Använd attribut (t.ex. [**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals), [**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns) osv.) för att kontrollera listan.

I exemplet nedan har vi skapat samma [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) med Aspose.Cells för Python via .NET API som vi skapade med Microsoft Excel i föregående avsnitt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **Formatera en tabell**

För att hantera och analysera en grupp relaterad data är det möjligt att förvandla ett cellområde till ett listobjekt (även känt som ett Excel-tabell). En tabell är en serie av rader och kolumner som innehåller relaterad data, som hanteras oberoende av annan data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverad i rubrikraden så att du snabbt kan filtrera eller sortera din listobjekts data. Du kan lägga till en totalsrad (en speciell rad i en lista som tillhandahåller ett urval av aggregeringsfunktioner som är användbara för att arbeta med numerisk data) till listobjektet som ger en rullgardinslista av aggregeringsfunktioner för varje totalsradscell. Aspose.Cells för Python via .NET erbjuder alternativ för att skapa och hantera listor (eller tabeller).

### **Formatera ett Listobjekt**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som ger tillgång till varje arbetsblad i en Excel-fil.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att skapa en [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) i ett kalkylblad, använd [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects)-egenskapen i klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Varje [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) är i själva verket en objekt av klassen [**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection), som dessutom tillhandahåller [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool)-metoden för att lägga till ett List-objekt och specificera det intervall av celler den ska omfatta. Enligt det angivna cellintervallet skapas en [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) i kalkylbladet av Aspose.Cells. Använd attribut (till exempel [**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)) för klassen [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) för att formatera tabellen enligt dina behov.

I exemplet nedan läggs provdata till ett kalkylblad, ett [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) läggs till och standardstilar tillämpas på det. [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)-stilar stöds av Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **Fortsatta ämnen**
- [Konvertera tabell till ODS](/cells/sv/python-net/convert-table-to-ods/)
- [Hitta frågetabeller och lista objekt relaterade till externa dataanslutningar](/cells/sv/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Läs och skriv tabell med datakälla för frågetabell](/cells/sv/python-net/read-and-write-table-with-query-table-data-source/)
- [Ange kommentaren för tabell eller listobjekt inne i kalkylbladet](/cells/sv/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabeller och områden](/cells/sv/python-net/tables-and-ranges/)


{{< app/cells/assistant language="python-net" >}}
