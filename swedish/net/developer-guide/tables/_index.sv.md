---
title: Skapa och hantera tabeller med Microsoft Excel-filer.
linktitle: Tabeller
type: docs
weight: 150
url: /sv/net/create-and-format-table/
description: Infoga, ändra storlek, redigera, ta bort, formatera tabell över Excel-filer med Aspose.Cells-biblioteket.
---
## **Skapa bord**

En av fördelarna med kalkylblad är att de låter dig skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan arbeta tillsammans för att använda, skapa och underhålla olika listor.

Aspose.Cells stöder att skapa och hantera listor.

### **Fördelar med ett listobjekt**

Det finns en hel del fördelar när du konverterar en lista med data till ett faktiskt listobjekt

- Nya rader och kolumner inkluderas automatiskt.
- En total rad längst ner på din lista kan enkelt läggas till för att visa SUMMA, AVERAGE, COUNT, etc.
- Kolumner som läggs till till höger infogas automatiskt i List-objektet.
- Diagram baserade på rader och kolumner utökas automatiskt.
- Namngivna intervall som tilldelats rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig radering och radering.

### **Skapa ett listobjekt med hjälp av Microsoft Excel**

- Välja dataintervall för att skapa ett listobjekt
- Detta visar dialogrutan Skapa lista.
-  Implementera List-objektet för data och ange total rad (Välj**Data** , då**Lista** , följd av**Total rad**).

### **Använder Aspose.Cells API**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Att skapa en[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) i ett kalkylblad använder du[**Listobjekt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) samling egendom av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. Varje[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) är i själva verket ett föremål för[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) klass, som ytterligare ger[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)metod för att lägga till ett List-objekt och ange ett cellintervall för listan.

Enligt det angivna cellintervallet skapas List-objektet av Aspose.Cells. Använd attribut (t.ex.[**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**Lista kolumner**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) , etc.) av[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)klass för att kontrollera listan.

 I exemplet nedan har vi skapat detsamma[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)använder Aspose.Cells API som vi skapade med Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Formatera en tabell**

För att hantera och analysera en grupp relaterade data är det möjligt att förvandla ett cellintervall till ett listobjekt (även känt som en Excel-tabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende av data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverad i rubrikraden så att du snabbt kan filtrera eller sortera dina listobjektdata. Du kan lägga till en totalrad (en speciell rad i en lista som ger ett urval av aggregerade funktioner som är användbara för att arbeta med numerisk data) till listobjektet som tillhandahåller en rullgardinslista med aggregerade funktioner för varje total radcell. Aspose.Cells ger alternativ för att skapa och hantera listor (eller tabeller).

### **Formatera ett listobjekt**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. Att skapa en[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) i ett kalkylblad, använd[**Listobjekt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) samling egendom av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. Varje[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) är i själva verket ett föremål för[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) klass, som ytterligare ger[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) metod för att lägga till ett List-objekt och ange det cellintervall som det ska omfatta. Enligt det specificerade cellområdet, a[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)skapas i kalkylbladet av Aspose.Cells. Använd attribut (t.ex.[**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) ) av[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)klass för att formatera tabellen för ditt krav.

 Exemplet nedan lägger till exempeldata till ett kalkylblad, lägger till en[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) och tillämpa standardstilar på den.[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)stilar stöds av Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Förhandsämnen**
- [Konvertera tabell till ODS](/cells/sv/net/convert-table-to-ods/)
- [Hitta frågetabeller och listobjekt relaterade till externa dataanslutningar](/cells/sv/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Läs och skriv tabell med datakälla för frågetabell](/cells/sv/net/read-and-write-table-with-query-table-data-source/)
- [Ställ in kommentaren för tabell eller listobjekt i kalkylbladet](/cells/sv/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabeller och intervall](/cells/sv/net/tables-and-ranges/)

