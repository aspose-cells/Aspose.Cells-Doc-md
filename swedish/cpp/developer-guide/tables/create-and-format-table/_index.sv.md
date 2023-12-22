---
title: Skapa och formatera tabell
type: docs
weight: 10
url: /sv/cpp/create-and-format-table/
---
##  **Skapa bord**
En av fördelarna med kalkylblad är att de låter dig skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan arbeta tillsammans för att använda, skapa och underhålla olika listor.

Aspose.Cells stöder att skapa och hantera listor.
###  **Fördelar med ett listobjekt**
Det finns en hel del fördelar när du konverterar en lista med data till ett faktiskt listobjekt

- Nya rader och kolumner inkluderas automatiskt.
- En total rad längst ner på din lista kan enkelt läggas till för att visa SUMMA, AVERAGE, COUNT, etc.
- Kolumner som läggs till till höger infogas automatiskt i List-objektet.
- Diagram baserade på rader och kolumner utökas automatiskt.
- Namngivna intervall som tilldelats rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig radering och radering.
###  **Skapa ett listobjekt med Microsoft Excel**

|**Väljer dataintervall för att skapa listobjekt**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Detta visar dialogrutan Skapa lista.

|**Dialogrutan Skapa lista**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Implementera List-objektet för data och ange total rad (Välj *Data**, sedan *Lista**, följt av *Total rad**).

|**Skapa ett listobjekt**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
###  **Använder Aspose.Cells API**
 Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass tillhandahåller ett brett utbud av metoder för att hantera ett kalkylblad. Att skapa en[ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) i ett kalkylblad använder du[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) insamlingsmetod för[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. Varje `[ListObject]` är i själva verket ett föremål för[ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) klass, som ytterligare ger[Lägg till](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)metod för att lägga till ett `[ListObject]`-objekt och ange ett cellintervall för listan.

 Enligt det specificerade cellintervallet skapas objektet `[ListObject]` av Aspose.Cells. Använd attribut (t.ex.[SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) och[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)etc.) av klassen `[ListObject]` för att kontrollera listan.

I exemplet nedan har vi skapat samma `[ListObject]` med Aspose.Cells API som vi skapade med Microsoft Excel i avsnittet ovan.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **Formatera en tabell**
För att hantera och analysera en grupp relaterade data är det möjligt att förvandla ett cellintervall till ett listobjekt (även känt som en Excel-tabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende av data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverad i rubrikraden så att du snabbt kan filtrera eller sortera dina listobjektdata. Du kan lägga till en totalrad (en speciell rad i en lista som tillhandahåller ett urval av aggregerade funktioner som är användbara för att arbeta med numerisk data) till listobjektet som tillhandahåller en rullgardinslista med aggregerade funktioner för varje totalradcell. Aspose.Cells ger alternativ för att skapa och hantera listor (eller tabeller).
###  **Formatera ett listobjekt**
 Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. Att skapa en*ListObject*i ett kalkylblad, använd `ListObjectCollection`. Varje `[ListObject]` är i själva verket ett objekt i klassen `ListObjectCollection`, vilket ytterligare tillhandahåller[Lägg till](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)metod för att lägga till ett `[ListObject]`-objekt och ange det cellintervall som det ska omfatta. Enligt det specificerade cellområdet, a*ListObject* skapas i kalkylbladet av Aspose.Cells. Använd attribut (t.ex.[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) av klassen `[ListObject]` för att formatera tabellen för dina krav.

Exemplet nedan lägger till exempeldata i ett kalkylblad, lägger till ett `[ListObject]` och tillämpar standardstilar på det. `[ListObject]`-stilar stöds av Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
