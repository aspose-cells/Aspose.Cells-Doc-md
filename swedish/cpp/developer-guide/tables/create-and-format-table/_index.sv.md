---
title: Skapa och formatera tabell
type: docs
weight: 10
url: /sv/cpp/create-and-format-table/
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

|**Välja dataintervall för att skapa List-objekt**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Detta visar skapa listdialogrutan.

|**Skapa lista dialog**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Implementera List-objektet för data och ange total rad (välj **Data**, sedan **List**, följt av **Total rad**).

|**Skapa ett listobjekt**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
### **Använda Aspose.Cells API**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som tillåter åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller ett brett utbud av metoder för att hantera ett kalkylblad. För att skapa ett [ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) i ett kalkylblad, används metoden [GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) i klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Varje `[ListObject]` är i själva verket ett objekt av klassen [ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/), som ytterligare tillhandahåller metoden [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) för att lägga till ett `[ListObject]` objekt och specificera en radie av celler för listan.

Enligt det angivna cellintervallen skapas `[ListObject]` objekt av Aspose.Cells. Använd attribut (t.ex. [SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) och [GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/) osv.) av klassen `[ListObject]` för att kontrollera listan.

I det angivna exemplet har vi skapat samma `[ListObject]` användande Aspose.Cells API som vi skapade med Microsoft Excel i avsnittet ovan.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
## **Formatera en tabell**
För att hantera och analysera en grupp relaterade data, är det möjligt att omvandla ett cellintervall till ett listobjekt (även känt som en Excel-tabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende av data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverad i raden för sidhuvud så att du snabbt kan filtrera eller sortera dina listobjektsdata. Du kan lägga till en totalrad (en speciell rad i en lista som ger ett urval av aggregeringsfunktioner som är användbara för att arbeta med numeriska data) till listobjektet som ger en nedrullningslista med aggregeringsfunktioner för varje cell i totalraden. Aspose.Cells tillhandahåller alternativ för att skapa och hantera listor (eller tabeller).
### **Formatera ett Listobjekt**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som tillåter åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att skapa ett *ListObject* i ett kalkylblad, används `ListObjectCollection`. Varje `[ListObject]` är i själva verket ett objekt av `ListObjectCollection` klassen, som ytterligare tillhandahåller [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) metoden för att lägga till ett `[ListObject]` objekt och ange intervallen av celler den bör omfatta. Enligt det angivna cellintervallen skapas en *ListObject* i kalkylbladet av Aspose.Cells. Använd attribut (t.ex. [SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) av klassen `[ListObject]` för att formatera tabellen för dina behov.

Exemplet nedan lägger till exempeldata på ett kalkylblad, lägger till ett `[ListObject]` och tillämpar standardstilar på det. `[ListObject]` stilar stöds av Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
